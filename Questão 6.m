clc;
clear;

% Dados
l2 = 10;
l1 = 8;
gamma = 3*pi/5;

% Função
f = @(alpha) ...
    l2*cos(pi-gamma-alpha)/sin(pi-gamma-alpha)^2 ...
    - l1*cos(alpha)/sin(alpha)^2;

% Intervalo inicial
a = 0.5;
b = 0.6;

% Tolerância
tol = 1e-12;

% Método da Bisseção
for k = 1:1000
    
    c = (a + b)/2;
    
    if abs(f(c)) < tol || abs(b-a)/2 < tol
        break;
    end
    
    if f(a)*f(c) < 0
        b = c;
    else
        a = c;
    end
end

% Valor encontrado
alpha = c;

% Comprimento da barra
L = l2/sin(pi-gamma-alpha) + l1/sin(alpha);

% Resultados
fprintf('Alpha = %.15f rad\n', alpha);
fprintf('Alpha = %.10f graus\n', rad2deg(alpha));
fprintf('Iteracoes = %d\n', k);
fprintf('f(alpha) = %.3e\n', f(alpha));
fprintf('Comprimento maximo L = %.15f\n', L);
