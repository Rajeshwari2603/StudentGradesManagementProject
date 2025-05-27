import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Step 1: Load Excel file
file_path = "data/student_grades.xlsx"
df = pd.read_excel(file_path)

# Step 2: Subject columns
subject_columns = ['Math', 'Physics', 'English', 'Chemistry']
df['Average'] = df[subject_columns].mean(axis=1)

# Step 3: Grade assignment logic
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average'].apply(get_grade)

# Step 4: Save processed data to SQLite DB
engine = create_engine('sqlite:///db/grades.db')
df.to_sql('students', con=engine, if_exists='replace', index=False)

print("✅ Processed Grades:")
print(df)

# Step 5: Modern Grade Distribution Chart
grade_counts = df['Grade'].value_counts().sort_index()

# Use clean ggplot style
plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(8, 5))

# Bar chart with style
bars = ax.bar(grade_counts.index, grade_counts.values,
              color='#1f77b4', edgecolor='black', linewidth=0.7)

# Label each bar with count
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1,
            f'{int(yval)}', ha='center', va='bottom',
            fontsize=10, fontweight='bold')

# Title and axis labels
ax.set_title("📊 Grade Distribution of Students", fontsize=14, fontweight='bold')
ax.set_xlabel("Grade", fontsize=12)
ax.set_ylabel("Number of Students", fontsize=12)
ax.set_ylim(0, max(grade_counts.values) + 10)

# Light gridlines
ax.yaxis.set_major_locator(mtick.MaxNLocator(integer=True))
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Layout and save
plt.tight_layout()
plt.savefig("grade_distribution.png", dpi=100)
plt.show()

print("✅ Data saved to database and chart generated successfully.")
