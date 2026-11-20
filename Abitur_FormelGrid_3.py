import wigglystuff


from wigglystuff import EsmWidget, FormulaDAG
from IPython.display import display

stats = FormulaDAG(
    {
        "Energy": r"E = q \cdot U",
        "U": r"U = R \cdot I \note{scale}",
    },
    notes={"scale": "distance measured in standard deviations"},
)

display(stats)