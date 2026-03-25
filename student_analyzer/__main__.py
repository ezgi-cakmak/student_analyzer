import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Starting Student Analysis...\n")

    try:
        df = pd.read_csv("students.csv")
        print("Dataset loaded successfully!\n")
        print(df)

        df["average"] = (df["math_score"] + df["science_score"]) / 2
        print("\n--- With Averages ---")
        print(df)

        mean = df["average"].mean()
        if mean < 60:
            print("\nOverall performance is low.")
        elif mean < 80:
            print("\nPerformance is moderate.")
        else:
            print("\nPerformance is excellent.")

        top_student = df.loc[df["average"].idxmax()]
        print(f"\nTop student: {top_student['name']} ({top_student['average']:.2f})")

        low_perf = df[df["average"] < 60]
        print("\nLow performers:")
        print(low_perf[["name", "average"]])

        df.plot(x="name", y="average", kind="bar", legend=False)
        plt.title("Student Average Scores")
        plt.xlabel("Students")
        plt.ylabel("Average Score")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("Error: students.csv not found!")

if __name__ == "__main__":
    main()