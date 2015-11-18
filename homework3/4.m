N = linspace(-2, 2);
% err = max(0, 1-N);
% err = power(max(0, 1-N), 2);
err = max(0, -N);
%plot(N, epsilon, 'r-', 'LineWidth', 3);
plot(N, err);
%axis([0, 10000, 0, 1])
%title('Original VC bound');
%title('Variant VC bound');
%title('Rademacher Penalty Bound');

xlabel('N');
ylabel('err');