clc;
clear;

% Valor de E (deve ser negativo)
E = -1;

% Funcao
f = @(x) -1./x.^3 - 1./x.^2 - E;

% Derivada
df = @(x) 3./x.^4 + 2./x.^3;

% Epsilon da maquina
tol = eps;


%% 1 - BISSECAO

% Intervalo para a raiz positiva
x1 = 1;
x2 = 2;

for i = 1:1000

    xm = (x1 + x2)/2;

    if i > 1
        if abs(xm - x_anterior) <= tol*max(1,abs(xm))
            break;
        end
    end

    if f(x1)*f(xm) < 0
        x2 = xm;
    else
        x1 = xm;
    end

    x_anterior = xm;
end

x_bissecao = xm;


%% 2 - FALSA POSICAO

x1 = 1;
x2 = 2;

for j = 1:1000

    x3 = (x1*f(x2) - x2*f(x1))/(f(x2)-f(x1));

    if j > 1
        if abs(x3 - x_anterior) <= tol*max(1,abs(x3))
            break;
        end
    end

    if f(x1)*f(x3) < 0
        x2 = x3;
    else
        x1 = x3;
    end

    x_anterior = x3;
end

x_falsa = x3;


%% 3 - NEWTON-RAPHSON

x = 1.5;

for k = 1:1000

    x_novo = x - f(x)/df(x);

    if abs(x_novo - x) <= tol*max(1,abs(x_novo))
        break;
    end

    x = x_novo;
end

x_newton = x_novo;


%% RESULTADOS


fprintf('\nBissecao:\n');
fprintf('x = %.15f\n', x_bissecao);
fprintf('Iteracoes = %d\n', i);

fprintf('\nFalsa Posicao:\n');
fprintf('x = %.15f\n', x_falsa);
fprintf('Iteracoes = %d\n', j);

fprintf('\nNewton-Raphson:\n');
fprintf('x = %.15f\n', x_newton);
fprintf('Iteracoes = %d\n', k);
