import pandas as pd
import matplotlib.pyplot as plt

# ---------- DATA ----------
df = pd.DataFrame({
    "Name": ["Aman","Riya","Karan","Neha","Rahul","Pooja","Vikas","Sneha","Arjun","Isha"],
    "Maths":   [78,92,45,88,60,95,38,81,70,55],
    "Science": [82,89,50,91,65,90,42,79,68,60],
    "English": [75,94,55,85,72,88,48,84,66,58],
    "Attendance": [85,95,60,92,70,98,55,88,80,65],
})

# ---------- ANALYSIS ----------
subjects = ["Maths", "Science", "English"]
df["Average"] = df[subjects].mean(axis=1).round(1)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print(df)
print("\nTopper:", df.loc[df["Average"].idxmax(), "Name"])
print("\nSubject averages:\n", df[subjects].mean().round(1))

# ---------- GRAPH 1: Subject-wise average ----------
df[subjects].mean().plot(kind="bar", color=["skyblue","orange","green"], rot=0)
plt.title("Subject-wise Average Marks")
plt.ylabel("Marks")
plt.savefig("graph1_subjects.png")
plt.show()

# ---------- GRAPH 2: Student-wise average ----------
plt.bar(df["Name"], df["Average"], color="teal")
plt.title("Student-wise Average Marks")
plt.xticks(rotation=45)
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("graph2_students.png")
plt.show()

# ---------- GRAPH 3: Attendance vs Marks ----------
plt.scatter(df["Attendance"], df["Average"], color="red")
plt.title("Attendance vs Marks")
plt.xlabel("Attendance %")
plt.ylabel("Average Marks")
plt.savefig("graph3_attendance.png")
plt.show()

# ---------- GRAPH 4: Pass / Fail ----------
df["Result"].value_counts().plot(kind="pie", autopct="%1.0f%%", colors=["lightgreen","salmon"])
plt.title("Pass vs Fail")
plt.ylabel("")
plt.savefig("graph4_result.png")
plt.show()
