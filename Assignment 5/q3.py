X = ord('A') + ord('D')
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])
print("Sales dataset:", sales)

tax_rate = ((X % 5) + 5) / 100
sales_after_tax = sales * (1 + tax_rate)
print("Sales after tax:", sales_after_tax)

discounted_sales=[]
for sale in sales:
    if sale < X + 100:
        discounted_sales.append(sale * 0.95)
    elif sale >= X + 100:
        discounted_sales.append(sale * 0.90) 
print("Sales after discounting:",discounted_sales)

weeks = 3
weekly_sales = np.vstack([sales] * weeks)
growth_factor = 1.02 ** np.arange(weeks)[:, None]
weekly_sales_adjusted = weekly_sales * growth_factor

print("Adjusted sales for 3 weeks:\n", weekly_sales_adjusted)