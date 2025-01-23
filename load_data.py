import csv
import os
from app import db, Roto, app

# Path to the CSV file
CSV_FILE_PATH = "libc.csv"

def load_data():
    with app.app_context():  # Ensure we are in the app context
        with open(CSV_FILE_PATH, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    print("Processing row:", row)  # Debugging: Print each row
                    team = Roto(
                        team=row["team"],
                        date=row["date"],  # Ensure this is in YYYY-MM-DD format
                        r=int(row["r"]),
                        hr=int(row["hr"]),
                        rbi=int(row["rbi"]),
                        sb=int(row["sb"]),
                        bb=int(row["bb"]),
                        avg=float(row["avg"]),
                        ops=float(row["ops"]),
                        w=int(row["w"]),
                        k=int(row["k"]),
                        era=float(row["era"]),
                        whip=float(row["whip"]),
                        qs=int(row["qs"]),
                        sv_h=int(row["sv+h"]),
                        total=int(row["total"]),
                        bat=int(row["bat"]),
                        pitch=int(row["pitch"]),
                        rank=int(row["rank"]),
                        b_rank=int(row["b_rank"]),
                        p_rank=int(row["p_rank"]),
                    )
                    db.session.add(team)  # Add the instance to the session
                except Exception as e:
                    print(f"Error processing row: {row}")
                    print(f"Error details: {e}")

            # Commit the session to write changes to the database
            try:
                db.session.commit()
                print("Data loaded successfully!")
            except Exception as commit_error:
                print(f"Error committing session: {commit_error}")

if __name__ == "__main__":
    load_data()