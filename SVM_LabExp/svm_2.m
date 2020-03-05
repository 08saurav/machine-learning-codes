%%%% SVM Implementation: Question 2 %%%%

%% Train SVM
data=csvread('cancer dataset\Training data.csv',1,0);
data(:,1:end-1)=zscore(data(:,1:end-1));

x = 
y = 

%% obtaining support vectors and corresponding alpha and y values using SMO
[alpha,x,y] = smo(x,y);
    
%% Calculate weight vector W and bias
W = 
b =
% Support Vectors
fprintf('Number of support Vectors : %d',length(alpha))


%% Test the SVM and display Accuracy and F1 Score
data=csvread('cancer dataset\Testing data.csv',1,0);
data(:,1:end-1)=zscore(data(:,1:end-1));
x=
y=
y_p=    % y_p contains predicted values of output
% Accuracy and F-measure
[cm, Accuracy, F1_score ] = confusionMatrix( y,y_p )
