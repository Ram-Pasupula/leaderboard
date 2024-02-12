import gradio as gr
import os

def sort_records(records):
    return records.sort("Quantity")

demo = gr.Interface(
    sort_records,
    gr.Dataframe(
        headers=["Item", "Quantity"],
        datatype=["str", "number"],
        row_count=3,
        col_count=(2, "fixed"),
        type="pandas"
    ),
    "dataframe",
    description="Sort by Quantity",
    examples=[
        [os.path.join(os.path.dirname(__file__), "polars_sort.csv")],
    ],
)

if __name__ == "__main__":
    demo.launch()
