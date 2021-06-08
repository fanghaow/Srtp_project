clear;clc;close all;
%% Combine data
% load('/Users/fanghao_w/Desktop/Srtp_project/Software_project/junior_gui/DATA_0518/grape_data_0518.mat');
% load('/Users/fanghao_w/Desktop/Srtp_project/Software_project/junior_gui/DATA_0519/grape_data_0519.mat');
load('../DATA_0518/grape_data_0518.mat');
load('../DATA_0519/grape_data_0519.mat');
com_data = [grape_0518, zeros(258, 1), grape_0519];
% data : [2:257, 1:end], Despite 60th col, because one of data is deprecated
[row, col] = size(com_data);

% Wavelength
A0 = 590.8939192;
B1 = 2.303196492;
B2 = -0.0004665871929;
B3 = -0.000007877923077;
B4 = 3.020550598E-08;
B5 = -4.876599743E-11;
wavelength = zeros(256, 1);
for j = 1:256
    wavelength(j) = A0 + B1 * j + B2 * j ^ 2 + B3 * j ^ 3 + B4 * j ^ 4 + B5 * j ^ 5;
end

%% Filter
j = 0;
eff_data0 = zeros(256+1, col);
for i = 1:col
    if(i==60 || i==37)
        continue;
    end
    if(mean(com_data(80:120, i)) > 703)
        continue;
    end
    j = j + 1;
    eff_data0(:, j) = com_data(2:258, i); % (257, 168)
%     eff_label(j) = com_data(258, i);
end
% 
%% PLS
pre_times = 1000;
Abs_error = zeros(pre_times, 1);
for i = 1:pre_times
    % Normlize
    eff_data_ori = eff_data0';
    mu = mean(eff_data_ori);
    sigma = std(eff_data_ori);
    eff_data = zscore(eff_data_ori); % Norm
    data = eff_data(:, 1:256); 
    label = eff_data(:, 257);
    % Random chioce
    num = size(data, 1);
    rand_order = randperm(num);
    train_set = data(rand_order(1: round(0.7*num)), :);
    train_label = label(1: round(0.7*num));
    test_set = data(rand_order(round(0.7*num)+1 : end), :);
    test_label = label(rand_order(round(0.7*num)+1 : end));

    % Pricipal component analysis
    ncomp = 21; % Number of main component
    [XL, YL, XS, YS, BETA, PCTVAR, MSE, stats] = plsregress(train_set, train_label, ncomp);
    n = size(train_set, 2); % independ variable number
    m = size(train_label, 2); % depend variable number

    % Caculate Residuals Example
%     labelfit = [ones(size(train_set, 1),1) train_set] * BETA;
%     residuals = train_label - labelfit;

    % VIPscore
    W0 = stats.W ./ sqrt(sum(stats.W.^2,1));
    p = size(XL,1);
    sumSq = sum(XS.^2,1).*sum(YL.^2,1);
    vipScore = sqrt(p* sum(sumSq.*(W0.^2),2) ./ sum(sumSq,2));
    indVIP = find(vipScore >= 1);

    % Predict
    data_ori = eff_data_ori(:, 1:256); 
    label_ori = eff_data_ori(:, 257);
    test_set_ori = data_ori(rand_order(round(0.7*num)+1 : end), :);
    test_label_ori = label_ori(rand_order(round(0.7*num)+1 : end));

    labelfit_test = [ones(size(test_set, 1),1) test_set] * BETA;
    labelfit_test_ori = labelfit_test * sigma(end) + mu(end);
    residuals = test_label_ori - labelfit_test_ori;
    Abs_error(i) = mean(abs(residuals));
    fprintf('No.%d iteration',i);
    fprintf('\n');
end
%% Plot
figure(1);
plot(Abs_error);
xlabel('Observations');
ylabel('Mean Absolute Error');
title('Model Estimation');
hold on;
mean_error = mean(Abs_error);
plot([1 pre_times], [mean_error mean_error], 'r');
legend('Error Curve', 'Mean of Error');
fprintf('The mean Error is %f', mean_error);
fprintf('\n');