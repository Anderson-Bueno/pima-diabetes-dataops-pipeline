import argparse
import sqlite3
from pathlib import Path

import pandas as pd


def run_sql(conn: sqlite3.Connection, sql_file: str) -> None:
    sql = Path(sql_file).read_text(encoding="utf-8")
    conn.executescript(sql)


def main(input_csv: str, output_csv: str, db_path: str) -> None:
    input_csv = Path(input_csv)
    output_csv = Path(output_csv)
    db_path = Path(db_path)

    output_csv.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_path)

    # 1) Schema
    run_sql(conn, "sql/01_schema.sql")

    # 2) Load
    df = pd.read_csv(input_csv)
    df.to_sql("diabetes", conn, if_exists="append", index=False)

    # 3) Transform (SQL rules)
    run_sql(conn, "sql/03_transform.sql")

    # 4) Export
    result = pd.read_sql_query("SELECT * FROM pacientes", conn)
    result.to_csv(output_csv, index=False)

    conn.close()
    print(f"OK -> {output_csv} ({len(result)} linhas)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline: IMC (BMI) + Filtro > 50 anos")
    parser.add_argument("--input_csv", required=True, help="Caminho do CSV original")
    parser.add_argument("--output_csv", default="data/processed/resultado.csv")
    parser.add_argument("--db_path", default="data/pipeline.db")
    args = parser.parse_args()

    main(args.input_csv, args.output_csv, args.db_path)
