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
            "q": r" q = 1 \ Coulomb",
            "r": r" r = 1 \ m ",

            "I_t": r" I(t) = \use{q}'(t)",
            "U_q": r" U(q) = \use{E}'(\use{q})",

            "F": r" F = \use{E} \cdot \use{q} ",
            "E": r" \note{E} E = \frac{1}{4 \pi \epsilon_0} \cdot \frac{\use{q}}{\use{r}^2} \vec{r}",
            "F_c": r" \note{Fc} F_e = \frac{1}{4 \pi \epsilon_0} \cdot \frac{|\use{q}_1 \cdot q_2|}{\use{r}^2}",
            "phi": r" \note{phi} \phi = \frac{\use{W}}{\use{q}}",
            "W": r" W = \int \use{F_c} dr",

            "W_c": r" \note{HF} U = \use{W} \cdot d",
            "U": r" U = \Delta \use{phi}",

            "C": r" \note{C} C = \frac{\use{q}}{\use{U}}",
            "C_p": r" \note{C_p} C_p = \use{C} = \epsilon_0 \epsilon_r \frac{A}{d}",
            "C_s": r" \note{C_s} C_s = \use{C} = \epsilon_0 \epsilon_r 4 \pi r",


            },
            notes={"E": "Elektrisches Feld(Punktladung):",
                    "Fc": "Coulomb Kraft:",
                    "phi": "Elektrisches Potential:",
                    "HF": "Potential im homologen Feld:",
                    "C": "Kapazität eines Kondensators",
                    "C_p": "Plattenkondensator",
                    "C_s": "Kugelkondensator",
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
