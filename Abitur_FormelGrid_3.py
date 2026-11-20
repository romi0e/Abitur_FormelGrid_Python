import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    from pathlib import Path
    import sys

    import marimo as mo

    # Prefer the local checkout so this demo tracks the in-repo FormulaDAG even
    # before it lands in a published wigglystuff release.
    repo_root = Path(__file__).resolve().parents[1]
    if (repo_root / "wigglystuff").exists():
        sys.path.insert(0, str(repo_root))

    from wigglystuff import EsmWidget, FormulaDAG
    from wigglystuff import ObservablePlot, TangleLatex

    return FormulaDAG, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Elektromagnetismus
    """)
    return


@app.cell
def _(FormulaDAG, mo):
    from tkinter import E
    firstStats = mo.ui.anywidget(
        widget=FormulaDAG(
            {
            "q": r" q = 1 \ Coulomb(Ladungsanhäufung)",
            "r": r" r = 1 \ m(Abstand)",
            "E": r" E = 1 \ J(Energie)",
            "U": r" U = 1 \ V(Spannung)",

            "I_t": r" I(t) = \use{q}'(t)",
            "U_q": r" U(q) = \use{E_f}'(\use{q})",

            "F": r" F = \use{E_f} \cdot \use{q} ",
            "E_f": r" \note{E} E = \frac{1}{4 \pi \epsilon_0} \cdot \frac{\use{q}}{\use{r}^2} \vec{r}",
            "F_c": r" \note{Fc} F_e = \frac{1}{4 \pi \epsilon_0} \cdot \frac{|\use{q}_1 \cdot q_2|}{\use{r}^2}",
            "phi": r" \note{phi} \phi = \frac{\use{W}}{\use{q}}",
            "W": r" W = \use{E} = \int \use{F_c} dr",

            "W_c": r" \note{HF} U = \use{W} \cdot d",
            "U_p": r" U = \Delta \use{phi}",

            "U_c": r" \note{U_c} U_c = 1 \ V",
            "Q": r" Q = 1 \ Coulomb(Kondensatorladung)",
            "C": r" \note{C} C = \frac{\use{Q}}{\use{U_c}}",
            "C_p": r" \note{C_p} C_p = \use{C} = \epsilon_0 \epsilon_r \frac{A}{d}",
            "C_s": r" \note{C_s} C_s = \use{C} = \epsilon_0 \epsilon_r 4 \pi r",

            "C_gesp": r" \note{C_para} C_{ges} = \sum \use{C} \ , \ Q_{ges} = \sum \use{Q}",
            "C_gesr": r" \note{C_reih} C_{ges} = [ \sum \use{C}^{-1} ]^{-1} \ , Q_1 = \use{Q}_n",

            "E_c": r" E = \frac{1}{2} \use{U_c} \use{Q} = \frac{1}{2} \use{C} \use{U_c}^2 = \frac{1}{2} \frac{\use{Q}^2}{\use{C}}",




            },
            notes={"E": "Elektrisches Feld(Punktladung):",
                    "Fc": "Coulomb Kraft:",

                    "phi": "Elektrisches Potential:",
                    "HF": "Potential im homologen Feld:",

                    "U_c": "Spannung am Kondensator",
                    "C": "Kapazität eines Kondensators",
                    "C_p": "Plattenkondensator",
                    "C_s": "Kugelkondensator",

                    "C_para": "Kondensator - Parallelschaltung",
                    "C_reih": "Kondensator - Reihenschaltung",

                    "E_c": "Energie am Kondensator",
                },



        

        )
    )
    firstStats
    return


@app.cell
def _(FormulaDAG, mo):
    stats = mo.ui.anywidget(
        FormulaDAG(
            {
                "B": r"B = \note{B}",
                "A": r"A = \note{A}",
                "n": r"n = \note{n}",
                "Phi": r"\Phi = \vec{\use{B}} \cdot \vec{\use{A}} \note{flux}",
                "Induktionsgesetz": r"U_{ind} = -\use{n} \frac{d \use{Phi}}{dt} \note{law}",
                "Vereinfacht":{
                    "tex": r"U_{ind} = -n \use{B}(t) \cdot \use{A}'(t)",
                    "tex": r"U_{ind} = -n \use{B}'(t) \cdot \use{A}(t)",
                },
            },
            notes={"flux": "(Skalarprodukt)",
                    "law": "- wegen Lenz'scher Regel",
                    "A": "Durchsetze Fläche",
                    "B": "Magnetfeldstärke",
                    "n": "Windungszahl"},
        )
    )
    stats
    return


if __name__ == "__main__":
    app.run()
