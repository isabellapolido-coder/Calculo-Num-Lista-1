clc;
clear;

% Dados
a = 0.401;
b = 42.7e-6;
N = 1000;
T = 300;
p = 3.5e7;
kb = 1.3806503e-23;

% Equacao:
% [p + a*(N/V)^2]*(V - N*b) = kb*N*T

f = @(V) (p + a*(N./V).^2).*(V - N*b) - kb*N*T;


%% 1 - METODO DA BISSECAO

V1 = N*b;
V2 = 0.05;
tol = 1e-12;

for i = 1:1000

    Vm = (V1 + V2)/2;

    if f(V1)*f(Vm) < 0
        V2 = Vm;
    else
        V1 = Vm;
    end

    if abs(V2 - V1) < tol
        break;
    end
end

V_bissecao = Vm;


%% 2 - METODO DA FALSA POSICAO

V1 = N*b;
V2 = 0.05;

for j = 1:1000

    V3 = (V1*f(V2) - V2*f(V1))/(f(V2)-f(V1));

    if f(V1)*f(V3) < 0
        V2 = V3;
    else
        V1 = V3;
    end

    if abs(f(V3)) < tol
        break;
    end
end

V_falsa = V3;


%% 3 - METODO DE NEWTON-RAPHSON

V = 0.05;

df = @(V) ...
    p + a*(N./V).^2 ...
    - 2*a*N^2.*(V-N*b)./V.^3;

for k = 1:1000

    V_novo = V - f(V)/df(V);

    if abs(V_novo - V) < tol
        break;
    end

    V = V_novo;
end

V_newton = V_novo;


%% RESULTADOS


fprintf('\nBissecao:\n');
fprintf('V = %.15e m^3\n', V_bissecao);
fprintf('Iteracoes = %d\n', i);

fprintf('\nFalsa Posicao:\n');
fprintf('V = %.15e m^3\n', V_falsa);
fprintf('Iteracoes = %d\n', j);

fprintf('\nNewton-Raphson:\n');
fprintf('V = %.15e m^3\n', V_newton);
fprintf('Iteracoes = %d\n', k);
