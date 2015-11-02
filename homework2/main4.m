%N = 1:10000;
N = linspace(1, 10000);
d = 50;
delta = 0.05;

%epsilon = sqrt( (8.0 ./ N) .* log( 4.0 * power(2 * N, d) ./ delta ) );

%epsilon = sqrt( (16.0 ./ N) .* log( 2.0 * power(N, d) ./ sqrt(delta) ) );

% epsilon = sqrt( (2.0 ./ N) .* log( 2.0 .* N .* power(N, d) ) );
% epsilon = epsilon + sqrt( (2.0 ./ N) * log( 1 ./ delta ) );
% epsilon = epsilon + (1 ./ N);

%a = N;
%b = -2;
%c = -log( 6.0 * power(2 * N, d) ./ delta );

% epsilon = (-b + sqrt( power(b, 2) - 4.0 .* N .* c) ) / (2.0 * a);

%N = 5000;

epsilon = (2 + sqrt( 4.0 - 4.0 .* N .* (-log( 6.0 * power(2 * N, 50) ./ 0.05 ))) ) / (2.0 * N);
%display(epsilon)

%epsilon = 0.5;

%figure;
%set (gcf,'Position',[500, 300, 900, 500], 'color','w')

%plot(N, epsilon, 'r-', 'LineWidth', 3);
plot(N, epsilon);
%axis([0, 10000, 0, 1])
%title('Original VC bound');
%title('Variant VC bound');
%title('Rademacher Penalty Bound')

xlabel('N');
ylabel('Epsilon');

N = 10000;
%display(sqrt( (8.0 ./ N) .* log( 4.0 * power(2 * N, d) ./ delta ) ));
%display(sqrt( (16.0 ./ N) .* log( 2.0 * power(N, d) ./ sqrt(delta) ) ));
%display(sqrt( (2.0 ./ N) .* log( 2.0 * N * power(N, d) ) ) + sqrt( (2.0 ./ N) .* log( 1 ./ delta ) ) + (1 ./ N));

% a = N;
% b = -2;
% c = -log( 6.0 * power(2 * N, d) ./ delta );
% 
% epsilon = (-b + sqrt( power(b, 2) - 4.0 * a * c )) / (2.0 * a);

a = 2 * N - 4;
b = -4;
c = -(log(4.0) + 100 * log(N) - log(delta));

epsilon = (-b + sqrt( power(b, 2) - 4.0 * a * c )) / (2.0 * a);

display(epsilon);
