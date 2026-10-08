clc;
clear;

% Dados
a = 4.0;
x = 1.0;
tol = 1e-12;
max_iter = 100;

raiz_exata = sqrt(a);

% Método de Newton-Raphson
for k = 1:max_iter

    x_novo = 0.5 * (x + a/x);

    erro = abs(x_novo - x);

    if erro <= tol
        break;
    end

    x = x_novo;
end

raiz = x_novo;

fprintf('========== NEWTON-RAPHSON ==========\n');

fprintf('a = %.1f\n', a);
fprintf('x0 = %.1f\n', 1.0);

fprintf('\nRaiz exata:\n');
fprintf('sqrt(a) = %.15f\n', raiz_exata);

fprintf('\nAproximacao:\n');
fprintf('x = %.15f\n', raiz);

fprintf('\nNumero de iteracoes = %d\n', k);

fprintf('Erro = %.3e\n', abs(raiz - raiz_exata));
