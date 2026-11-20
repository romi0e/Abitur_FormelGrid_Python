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

    return FormulaDAG, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Induktion
    """)
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
