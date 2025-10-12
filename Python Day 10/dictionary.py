import random

books = [
    ["The Alchemist", "Paulo Coelho", 15, 4.7],
    ["Jannat kay pattay", "Nemrah Ahmed", 10, 4.5],
    ["To Kill a Mockingbird", "Harper Lee", 20, 4.8],
    ["Atomic habits", "James Clear", 12, 4.3]
]

print("=== Book Finder ===")

book_choices = [random.randint(0, 3) for _ in range(4)]

# Run for 3 rounds
for round_num in range(5):
    print(f"\n--- Round {round_num + 1} ---")
    
    total_scores = []
    for choice in book_choices:
        title = books[choice][0]
        author = books[choice][1]
        price = books[choice][2]
        rating = books[choice][3]
        score = (100 - price) + (rating * 10)   
        total_scores.append(score)
        print(f"{title} by {author}: Score {score}")
    
    best_score = max(total_scores)
    best_index = total_scores.index(best_score)
    best_choice = book_choices[best_index]
    best_title = books[best_choice][0]
    best_author = books[best_choice][1]
    print(f"Best: {best_title} by {best_author}")
    
    book_choices = [best_choice, best_choice, best_choice, random.randint(0, 3)]

final_choice = book_choices[0]
final_title = books[final_choice][0]
final_author = books[final_choice][1]
final_price = books[final_choice][2]
final_rating = books[final_choice][3]
final_score = (100 - final_price) + (final_rating * 10)

print(f"\nFinal Choice: {final_title} by {final_author}")
print(f"Final Score: {final_score}")

