X(:,1) = [1;0];
X(:,2) = [0;1];
X(:,3) = [0;-1];
X(:,4) = [-1;0];
X(:,5) = [0;2];
X(:,6) = [0;-2];
X(:,7) = [-2;0];
y = [-1, -1, -1, 1, 1, 1, 1];
disp(y(1));
Q(1:7, 1:7) = 0;
for i = 1:7,
   for j = 1:7,
       Q(i, j) = y(i) * y(j) * ((1 + X(:, i).' * X(:, j)).^2);
   end
end
% disp(Q)
p(1:7) = -1;
b = 0;
A = eye(7);
c(1:7) = 0;

alpha = quadprog (Q, p, [], [], y, b, c);
disp(alpha);

w = [0;0];
for i = 1:7,
    w = w + alpha(i) * y(i) * X(:, i);
end

disp(w);

b=y(2);
for i = 2:6,
    b = b - alpha(i) * y(i) * (( 1 + X(:, i).' * X(:, 2) ).^2);
end
disp(b);