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
    mo.md()
    """)
    return


@app.cell
def _(FormulaDAG, mo):
    stats = mo.ui.anywidget(
        FormulaDAG(
            {
                "mu": r"\mu = \frac{1}{n}\sum_{i=1}^{n} x_i",
                "var": r"\sigma^2 = \frac{1}{n}\sum_{i=1}^{n} (x_i - \use{mu})^2",
                "sigma": r"\sigma = \sqrt{\use{var}}",
                "z": {
                    "tex": r"z_i = \frac{x_i - \use{mu}}{\note{scale}{\use{sigma}}}",
                    "label": "z-score",
                },
            },
            notes={"scale": "distance measured in standard deviations"},
        )
    )
    stats
    return


if __name__ == "__main__":
    app.run()
