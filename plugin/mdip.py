fig_template = r'''\begin{figure}[htpb]
    \centering
    \includegraphics[width=0.8\textwidth]{%s}
    \caption{%s}
\end{figure}
'''

def get_latex_fig(var_name, img_path, caption):
    vim.vars[var_name] = fig_template % (img_path, caption)  

def insert_latex_fig(var_name, img_path, caption):
    vim.command('normal! i ' + fig_template % (img_path, caption))


