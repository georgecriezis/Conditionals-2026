# A company awards annual bonuses based on an employee's performance score
annual = float(input("What's your annual salary? "))
performance_score = float(input("What's your performance score (0-100)? "))

if performance_score >=90:
    bonus = 0.20
elif performance_score >= 80:
    bonus = 0.10
elif performance_score >= 70:
    bonus = 0.05
else:
    bonus = 0.0

bonus_amount = annual * bonus
print(f'Performance bonus: {bonus * 100:.0f}%')
print(f'Bonus amount: ${bonus_amount:.2f}')