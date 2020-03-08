Array=csvread('prime.csv');
col1 = Array(:, 1);
col2 = Array(:, 4);
col3 = Array(:, 5);
plot(col2,col3)