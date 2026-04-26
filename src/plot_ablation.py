import pandas as pd
import json
import plotly.graph_objects as go


def main():
    # ---------------------------------------------------------
    # 1. LOAD ALL 6 FILES
    # ---------------------------------------------------------

    # Load the 3 JSON files (Raw data from the AI)
    json_files = ['QwenT0.json', 'QwenT3.json', 'QwenT7.json']
    raw_data = [ ]
    for file in json_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                raw_data.extend(json.load(f))
        except FileNotFoundError:
            print(f"Warning: {file} not found.")

    print(f"✅ Loaded {len(raw_data)} raw extraction records from JSON files.")

    # Load the 3 CSV files (Aggregated Benchmarks for the graph)
    csv_files = ['QwenT0.csv', 'QwenT3.csv', 'QwenT7.csv']
    dfs = []
    for file in csv_files:
        try:
            dfs.append(pd.read_csv(file))
        except FileNotFoundError:
            print(f"Warning: {file} not found.")

    # Combine the CSVs into one master DataFrame
    df = pd.concat(dfs, ignore_index=True)

    # Convert temperature to string so it plots as distinct categories (0.0, 0.3, 0.7)
    df['temperature'] = df['temperature'].astype(str)

    print(f"✅ Loaded {len(df)} summary rows from CSV files.")

    # ---------------------------------------------------------
    # 2. BUILD THE INTERACTIVE PLOTLY GRAPH
    # ---------------------------------------------------------
    fig = go.Figure()

    prompts = ['Constrained_Prompt', 'Base_Prompt', 'Super_Prompt']

    # We add 3 sets of traces (one for F1, one for Precision, one for Recall).
    # We will use the dropdown menu to hide/show the relevant ones.

    # Trace Set 1: F1 Score (Visible by default)
    for p in prompts:
        d = df[df['prompt_type'] == p]
        fig.add_trace(go.Bar(x=d['temperature'], y=d['avg_f1'], name=p, visible=True))

    # Trace Set 2: Precision (Hidden by default)
    for p in prompts:
        d = df[df['prompt_type'] == p]
        fig.add_trace(go.Bar(x=d['temperature'], y=d['avg_precision'], name=p, visible=False))

    # Trace Set 3: Recall (Hidden by default)
    for p in prompts:
        d = df[df['prompt_type'] == p]
        fig.add_trace(go.Bar(x=d['temperature'], y=d['avg_recall'], name=p, visible=False))

    # ---------------------------------------------------------
    # 3. ADD DROPDOWN MENU
    # ---------------------------------------------------------
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=list([
                    dict(label="F1 Score",
                         method="update",
                         # Show first 3 traces, hide the rest
                         args=[{"visible": [True] * 3 + [False] * 3 + [False] * 3},
                               {"yaxis": {"title": "Average F1 Score"}}]),
                    dict(label="Precision",
                         method="update",
                         # Show middle 3 traces, hide the rest
                         args=[{"visible": [False] * 3 + [True] * 3 + [False] * 3},
                               {"yaxis": {"title": "Average Precision"}}]),
                    dict(label="Recall",
                         method="update",
                         # Show last 3 traces, hide the rest
                         args=[{"visible": [False] * 3 + [False] * 3 + [True] * 3},
                               {"yaxis": {"title": "Average Recall"}}]),
                ]),
                x=0.15,
                y=1.15
            )
        ],
        barmode='group',
        title=" Phi3 Ablation Study Results",
        xaxis_title="Temperature",
        yaxis_title="Average F1 Score",
        legend_title="Prompt Type",
        template="plotly_white"  # Gives it a clean, professional look
    )

    # ---------------------------------------------------------
    # 4. RENDER GRAPH
    # ---------------------------------------------------------
    # This will open a new tab in your default web browser
    fig.show()


if __name__ == "__main__":
    main()