clear;clc;
%% Load data
load('../DATA_0518/grape_data_0518.mat'); % First_data : (261, 59)
Data = grape_0518';
% data = Data(:, 2:257); 
% label = Data(:, 258);
%% Normlize
mu = mean(Data);
sigma = std(Data);
Data = zscore(Data); % Norm
data = Data(:, 2:257); 
label = Data(:, 258);
%% PLS
ncomp = 20; % Number of main component
[XL, YL, XS, YS, BETA, PCTVAR, MSE, stats] = plsregress(data, label, ncomp);
plot(1:ncomp,cumsum(100*PCTVAR(2,:)),'-bo');
xlabel('Number of PLS components');
ylabel('Percent Variance Explained in y');
n = size(data, 2); % independ variable number
m = size(label,2); % depend variable number

% Caculate residuals
labelfit = [ones(size(data, 1),1) data] * BETA;
residuals = label - labelfit;
stem(residuals)
xlabel('Observations');
ylabel('Residuals');

% VIPscore
W0 = stats.W ./ sqrt(sum(stats.W.^2,1));
p = size(XL,1);
sumSq = sum(XS.^2,1).*sum(YL.^2,1);
vipScore = sqrt(p* sum(sumSq.*(W0.^2),2) ./ sum(sumSq,2));
indVIP = find(vipScore >= 1);
scatter(1:length(vipScore),vipScore,'x')
hold on
scatter(indVIP,vipScore(indVIP),'rx')
plot([1 length(vipScore)],[1 1],'--k')
hold off
axis tight
xlabel('Predictor Variables')
ylabel('VIP Scores')