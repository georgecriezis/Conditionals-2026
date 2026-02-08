# a retail business offers discounts to customers based on a customer's membership status and purchase amount
purchase_amount = float(input("Enter the purchase amount: "))
membership_status = input("Are you a member? (yes/no): ").strip().lower()

if membership_status == "yes":
    if purchase_amount >= 100:
        discount = 0.15
    elif purchase_amount < 100:
        discount = 0.05
if membership_status == "no":
    if purchase_amount >= 150:
        discount = 0.10
    else:
        discount = 0.0
discount_amount = purchase_amount * discount
final_price = purchase_amount - discount_amount
print(f'Discount applied: {discount * 100:.0f}%')
print(f'Final price: ${final_price:.2f}')