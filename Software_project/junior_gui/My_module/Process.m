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
for j = 1:256
    wavelength(j) = A0 + B1 * j + B2 * j ^ 2 + B3 * j ^ 3 + B4 * j ^ 4 + B5 * j ^ 5;
end
%% Visualize
figure(1);
subplot(2,2,[1 2]);
for i = 1:col
    if(i==60 || i==37)
        continue;
    end
    if(mean(com_data(80:120, i)) > 703)
        j = j + 1;
        continue;
    end
    plot(wavelength, com_data(2:257, i));
    hold on;
end
xlim([0.95 * min(wavelength) 1.04 * max(wavelength)]);
ylim([100 1.05 * max(max(com_data))]);
xlabel('Wavelength');
ylabel('Strength');
title('Combined data');
subplot(2,2,3);
j = 0;
for i = 1:60
    if(i==60 || i==37)
        continue;
    end
    if(mean(com_data(80:120, i)) > 703)
        j = j + 1;
        continue;
    end
    plot(wavelength, com_data(2:257, i));
    hold on;
end
fprintf('There are %d data been deprecated', j);
fprintf('\n');
xlim([550 1150]);
xlabel('Wavelength');
ylabel('Strength');
title('First Data');
subplot(2,2,4);
for i = 61:col
    plot(wavelength, com_data(2:257, i));
    hold on;
end
xlim([550 1150]);
xlabel('Wavelength');
ylabel('Strength');
title('Second Data');

%% Filter
figure(2);
j = 0;
for i = 1:col
    if(i==60 || i==37)
        continue;
    end
    if(mean(com_data(80:120, i)) > 703)
        continue;
    end
    j = j + 1;
    eff_data(:, j) = com_data(2:258, i); % (257, 168)
%     eff_label(j) = com_data(258, i);
end
plot(wavelength, eff_data(1:256, :));
xlim([550 1150]);
xlabel('Wavelength');
ylabel('Strength');
title('Wavelength-Strength');
% 
%% PLS
% Normlize
eff_data_ori = eff_data';
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
figure(3);
ncomp = 21; % Number of main component
[XL, YL, XS, YS, BETA, PCTVAR, MSE, stats] = plsregress(train_set, train_label, ncomp);
plot(1:ncomp,cumsum(100*PCTVAR(2,:)),'-bo');
xlabel('Number of PLS components');
ylabel('Percent Variance Explained in data');
title('Pricipal Component Analysis');
n = size(train_set, 2); % independ variable number
m = size(train_label, 2); % depend variable number

% Caculate residuals
figure(4);
labelfit = [ones(size(train_set, 1),1) train_set] * BETA;
residuals = train_label - labelfit;
stem(residuals)
xlabel('Observations');
ylabel('Residuals');
title('Error Analysis');

% VIPscore
figure(5);
W0 = stats.W ./ sqrt(sum(stats.W.^2,1));
p = size(XL,1);
sumSq = sum(XS.^2,1).*sum(YL.^2,1);
vipScore = sqrt(p* sum(sumSq.*(W0.^2),2) ./ sum(sumSq,2));
indVIP = find(vipScore >= 1);
scatter(1:length(vipScore),vipScore,'x');
hold on;
scatter(indVIP,vipScore(indVIP),'rx');
plot([1 length(vipScore)],[1 1],'--k');
hold off;
axis tight;
xlabel('Predictor Variables');
ylabel('VIP Scores');
title('Characteristic Peaks');

%% Predict
data_ori = eff_data_ori(:, 1:256); 
label_ori = eff_data_ori(:, 257);
test_set_ori = data_ori(rand_order(round(0.7*num)+1 : end), :);
test_label_ori = label_ori(rand_order(round(0.7*num)+1 : end));

figure(6);
subplot(2,2,[1,2]);
labelfit_test = [ones(size(test_set, 1),1) test_set] * BETA;
labelfit_test_ori = labelfit_test * sigma(end) + mu(end);
residuals = test_label_ori - labelfit_test_ori;
stem(residuals)
xlabel('Observations');
ylabel('Residuals');
title('Error Analysis');
subplot(2,2,3);
plot(test_label_ori);
hold on;
plot(labelfit_test_ori);
legend('Real value', 'Predicting value');
title('Prediction')
xlabel('Observations');
ylabel('Sweetness/[%]');
subplot(2,2,4);
x = 0.95*min(labelfit_test_ori) : 0.01 : 1.1*max(labelfit_test_ori);
y = x;
plot(x, y);
hold on;
scatter(test_label_ori, labelfit_test_ori);
xlabel('Real value');
ylabel('Predicted value');
title('Visualize Result');
