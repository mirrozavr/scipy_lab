from scipy.integrate import solve_ivp
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

date = np.linspace(0, 10, 1000)

x = sy.symbols('x')
y = sy.symbols('y', cls=sy.Function)
sym_sol = sy.dsolve(sy.Eq(y(x).diff(x), - 2 * y(x)), y(x), ics={y(0): np.sqrt(2)})
sym_res = sy.lambdify(x, sym_sol.rhs, 'numpy')


def fun(x, y):
    return x
    return -2 * y


sci_res = solve_ivp(fun, [0, 10], [np.sqrt(2)], t_eval=date)

fig, (sci, sym, diff) = plt.subplots(ncols=3)
fig.set_figheight(5)
fig.set_figwidth(10)

sci.grid()
sci.set_title('SciPy', color='purple')
sci.plot(sci_res.t, sci_res.y[0], color='violet')

sym.grid()
sym.set_title('SymPy', color='purple')
sym.plot(date, sym_res(date), color='violet')

diff.grid()
diff.set_title('Differences', color='purple')
diff.plot(sci_res.t, sci_res.y[0] - sym_res(sci_res.t), color='violet')

plt.savefig('res.png')
plt.show()