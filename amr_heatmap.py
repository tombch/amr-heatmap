import csv
import argparse
import plotly.express as px


def add_genes(map, row, index):
    if row[index] not in map:
        map[row[index]] = [int(value) for value in row[6:]]
    else:
        for i, value in enumerate(row[6:]):
            map[row[index]][i] += int(value)


def main():
    parser = argparse.ArgumentParser(description="Plot AMR heatmap")
    parser.add_argument("input", help="Input CSV file")
    args = parser.parse_args()

    genes = []
    bacteria_map = {}
    source_map = {}

    with open(args.input, "r") as f:
        reader = csv.reader(f)
        genes.extend(next(reader)[6:])

        for row in reader:
            add_genes(source_map, row, 3)
            add_genes(bacteria_map, row, 4)

    bacteria = px.imshow(
        list(bacteria_map.values()),
        x=genes,
        y=list(bacteria_map.keys()),
        title="AMR Heatmap (Bacteria)",
    )
    bacteria.write_image("bacteria_amr.png", width=1200, height=800, scale=2)
    bacteria.write_html("bacteria_amr.html")

    source = px.imshow(
        list(source_map.values()),
        x=genes,
        y=list(source_map.keys()),
        title="AMR Heatmap (Source)",
    )
    source.write_image("source_amr.png", width=1200, height=800, scale=2)
    source.write_html("source_amr.html")


if __name__ == "__main__":
    main()
