import json


def load_internships(path="internships.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def recommend(my_skills, internships, top_n=5):
    results = []

    for internship in internships:
        required = internship["skills"]
        matched = [s for s in required if s in my_skills]
        missing = [s for s in required if s not in my_skills]
        score = len(matched) / len(required)

        results.append({
            "title": internship["title"],
            "company": internship["company"],
            "score": score,
            "matched": matched,
            "missing": missing,
        })

    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_n]


if __name__ == "__main__":
    internships = load_internships()

    text = input("Type your skills, separated by commas like excel or sql: ")
    my_skills = [s.strip().lower() for s in text.split(",")]

    for r in recommend(my_skills, internships):
        print(f'{r["title"]} ({r["company"]}) - {round(r["score"] * 100)}%')
        print("  matched:", r["matched"])
        print("  missing:", r["missing"])