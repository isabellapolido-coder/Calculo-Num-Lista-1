"""
Cálculo Numérico - Lista de exercícios (Questões 1 a 5)
Execute com:  python questoes_1_a_5.py
Dependências: numpy e matplotlib
    python -m pip install numpy matplotlib
"""
import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# Questão 1 - Aritmética de ponto flutuante, erros absolutos e relativos
# =============================================================================
def questao1():
    print("=" * 70)
    print("QUESTÃO 1")
    print("=" * 70)

    info = np.finfo(np.float64)
    realmax = info.max      # maior número flutuante
    realmin = info.tiny     # menor número flutuante normalizado positivo
    eps = info.eps          # diferença entre 1 e o próximo flutuante

    print(f"realmax = {realmax:.6e}")
    print(f"realmin = {realmin:.6e}")
    print(f"eps     = {eps:.6e}")
    print("\nSignificado:")
    print("  realmax: maior valor finito representável em double.")
    print("  realmin: menor valor positivo normalizado representável.")
    print("  eps:     menor distância entre 1 e o próximo número flutuante;")
    print("           limita o erro relativo de arredondamento (~eps/2).\n")

    valor_exato = 1.0  # ((1+x)-1)/x = 1 para qualquer x != 0
    for x in [1e-15, 1e15]:
        valor = ((1 + x) - 1) / x
        erro_abs = abs(valor - valor_exato)
        erro_rel = erro_abs / abs(valor_exato)
        print(f"x = {x:.0e}")
        print(f"   valor calculado = {valor:.16g}")
        print(f"   erro absoluto   = {erro_abs:.6e}")
        print(f"   erro relativo   = {erro_rel:.6e}\n")

    print("Discussão: para x = 1e-15, 1 + x perde os dígitos de x no")
    print("arredondamento (x < eps), gerando um resultado muito distante de 1")
    print("(cancelamento catastrófico). Para x = 1e15, 1 + x é representado")
    print("exatamente e o resultado é 1.\n")


# =============================================================================
# Questão 2 - Avaliação de f(x) próximo de x = 1
# =============================================================================
def f_expandida(x):
    return (x**7 - 7*x**6 + 21*x**5 - 35*x**4 +
            35*x**3 - 21*x**2 + 7*x - 1)


def f_fatorada(x):
    # A função é exatamente (x - 1)^7 (forma sem cancelamento)
    return (x - 1)**7


def questao2():
    print("=" * 70)
    print("QUESTÃO 2")
    print("=" * 70)

    x = np.linspace(1 - 2e-8, 1 + 2e-8, 401)
    y_exp = f_expandida(x)
    y_fat = f_fatorada(x)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    axes[0].plot(x, y_exp, "o-", ms=3)
    axes[0].set_title("f(x) - forma expandida (401 pontos)")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("f(x)")
    axes[0].ticklabel_format(axis="x", style="plain", useOffset=False)
    axes[0].grid(True)

    axes[1].plot(x, y_fat, "o-", ms=3, color="tab:orange")
    axes[1].set_title("f(x) = (x - 1)^7 (forma fatorada)")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("f(x)")
    axes[1].ticklabel_format(axis="x", style="plain", useOffset=False)
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig("questao2_grafico.png", dpi=120)
    print("Gráfico salvo em questao2_grafico.png")

    print(f"\nMáx |f_expandida| = {np.max(np.abs(y_exp)):.3e}")
    print(f"Máx |f_fatorada| = {np.max(np.abs(y_fat)):.3e}")
    print("\nDiscussão: na forma expandida ocorre cancelamento catastrófico,")
    print("pois os termos são da ordem de 1 e o resultado é da ordem de")
    print("(2e-8)^7 ~ 1e-53. O gráfico mostra apenas ruído de arredondamento,")
    print("enquanto a forma fatorada (x-1)^7 reproduz corretamente a função.\n")


# =============================================================================
# Questão 3 - Recorrência para I_n
# =============================================================================
def sucessao_recorrencia(N):
    """I_0 = (e-1)/e ;  I_{n+1} = 1 - (n+1) I_n"""
    I = np.zeros(N + 1)
    I[0] = (np.e - 1) / np.e
    for n in range(N):
        I[n + 1] = 1 - (n + 1) * I[n]
    return I


def I_exato(n, pontos=2_000_001):
    """
    Referência: I_n = integral de 0 a 1 de x^n e^(x-1) dx,
    calculada pela regra do trapézio com muitos pontos (só numpy).
    """
    x = np.linspace(0, 1, pontos)
    y = x**n * np.exp(x - 1)
    integrar = getattr(np, "trapezoid", None) or np.trapz
    return integrar(y, x)


def questao3(N=25):
    print("=" * 70)
    print("QUESTÃO 3")
    print("=" * 70)

    I_rec = sucessao_recorrencia(N)
    ns = np.arange(N + 1)
    I_ref = np.array([I_exato(n) for n in ns])
    erro = np.abs(I_rec - I_ref)

    print(f"{'n':>3} {'I_n (recorrência)':>22} {'I_n (exato)':>16} {'erro abs':>12}")
    for n in ns:
        print(f"{n:>3} {I_rec[n]:>22.10e} {I_ref[n]:>16.10e} {erro[n]:>12.3e}")

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5))
    ax[0].plot(ns, I_rec, "o-", label="recorrência")
    ax[0].plot(ns, I_ref, "s--", label="referência (integral)")
    ax[0].axhline(0, color="k", lw=0.8)
    ax[0].set_title("I_n em função de n")
    ax[0].set_xlabel("n")
    ax[0].legend()
    ax[0].grid(True)

    ax[1].semilogy(ns, erro, "o-", color="tab:red")
    ax[1].set_title("Erro absoluto da recorrência")
    ax[1].set_xlabel("n")
    ax[1].set_ylabel("|erro|")
    ax[1].grid(True)

    plt.tight_layout()
    plt.savefig("questao3_grafico.png", dpi=120)
    print("\nGráfico salvo em questao3_grafico.png")
    print("\nDiscussão: I_n -> 0 quando n -> infinito. A recorrência é instável:")
    print("o erro de arredondamento inicial é multiplicado por (n+1) a cada")
    print("passo, crescendo como n!. Por isso os valores perdem completamente")
    print("a precisão e saem do intervalo [0,1] após alguns termos.\n")


# =============================================================================
# Questão 4 - Estimativa de pi por Monte Carlo
# =============================================================================
def questao4(seed=42):
    print("=" * 70)
    print("QUESTÃO 4")
    print("=" * 70)

    rng = np.random.default_rng(seed)
    ns = np.unique(np.logspace(1, 7, 60).astype(int))
    N = ns[-1]

    x = rng.random(N)
    y = rng.random(N)
    dentro = (x**2 + y**2 <= 1.0)     # pontos dentro do quarto de círculo unitário
    m_acumulado = np.cumsum(dentro)   # m(n) para todos os n de uma vez

    pi_n = 4.0 * m_acumulado[ns - 1] / ns
    erro = np.abs(pi_n - np.pi)

    print(f"{'n':>10} {'pi_n':>12} {'erro':>12}")
    for i in range(0, len(ns), 6):
        print(f"{ns[i]:>10d} {pi_n[i]:>12.6f} {erro[i]:>12.3e}")
    print(f"{ns[-1]:>10d} {pi_n[-1]:>12.6f} {erro[-1]:>12.3e}")

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.loglog(ns, erro, "o-", ms=3, label="|pi_n - pi|")
    ax.loglog(ns, 1 / np.sqrt(ns), "--", color="gray",
              label="referência ~ 1/sqrt(n)")
    ax.set_title("Evolução do erro do método de Monte Carlo")
    ax.set_xlabel("n (número de pontos)")
    ax.set_ylabel("erro absoluto")
    ax.legend()
    ax.grid(True, which="both")
    plt.tight_layout()
    plt.savefig("questao4_grafico.png", dpi=120)
    print("\nGráfico salvo em questao4_grafico.png")
    print("\nDiscussão: o erro decai aproximadamente como 1/sqrt(n). Para")
    print("reduzir o erro por um fator 10 é preciso aumentar n por um fator 100.\n")


# =============================================================================
# Questão 5 - Série de Bailey-Borwein-Plouffe
# =============================================================================
def termo_m(m):
    return 16.0**(-m) * (4 / (8*m + 1)
                         - 2 / (8*m + 4)
                         - 1 / (8*m + 5)
                         - 1 / (8*m + 6))


def soma_parcial(n):
    """Soma dos n primeiros termos da série (m = 0, ..., n-1)."""
    return sum(termo_m(m) for m in range(n))


def questao5(pi_ref=3.141592, tol=1e-4):
    print("=" * 70)
    print("QUESTÃO 5")
    print("=" * 70)

    print(f"{'n':>3} {'S_n':>18} {'|S_n - pi|':>14}")
    S = 0.0
    n = 0
    n_encontrado = None
    while n < 50:
        S += termo_m(n)
        n += 1
        erro = abs(S - pi_ref)
        print(f"{n:>3} {S:>18.12f} {erro:>14.4e}")
        if erro < tol and n_encontrado is None:
            n_encontrado = n
        if n_encontrado is not None and n >= n_encontrado + 2:
            break

    print(f"\nPrimeiro n com erro < {tol:.0e}: n = {n_encontrado}")
    print(f"(soma dos termos m = 0 até m = {n_encontrado - 1})")
    print(f"Verificação: soma_parcial({n_encontrado}) = {soma_parcial(n_encontrado):.12f}\n")


# =============================================================================
if __name__ == "__main__":
    questao1()
    questao2()
    questao3()
    questao4()
    questao5()