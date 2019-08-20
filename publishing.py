import publishers
import matplotlib.pyplot as plt
import numpy as np

#What is the difference between the average daily income of a pubisher versus an author?
#On average, how much of a books sales come from amazon?


#call a part of the list(0 or 1)("author revenue")
list_of_book = publishers.get_books()

#for row in list_of_book:
    #print(row["daily average"]["author revenue"])

author_revenue = []
publisher_revenue = []

for w in list_of_book:
    author = w["daily average"]["author revenue"]
    author_revenue.append(author)
    publisher = w["daily average"]["publisher revenue"]
    publisher_revenue.append(publisher)

#print(author_revenue)
#print(publisher_revenue)

total1 = sum(author_revenue)
length1 = len(author_revenue) + 1
avg1 = total1 / length1
print(avg1)
#print(list_of_book)
total2 = sum(publisher_revenue)
length2 = len(publisher_revenue) + 1
avg2 = total2 / length2
print(avg2)

amazon_revenue = []
sales = []


for s in list_of_book:
    amazon = s["daily average"]["amazon revenue"]
    amazon_revenue.append(amazon)
    gross = s["daily average"]["gross sales"]
    sales.append(gross)

#revenue = "author revenue"
total3 = sum(amazon_revenue)
length3 = len(amazon_revenue) + 1
avg3 = total3 / length3
print(avg3)
#print(list_of_book)
total4 = sum(sales)
length4 = len(sales) + 1
avg4 = total4 / length4
print(avg4)

total5 = avg3 / avg4
total6 = total5 * 100
print(total6)

#for books_sold in revenue:
#    writer = ["author revenue"]
#    author.append(list_of_book)
#    publisher.append(list_of_book)
#print(author)

objects = ('Author Revenue', 'Publisher Revenue')
y_axis = np.arange(len(objects))
performance = [avg1, avg2]

plt.bar(y_axis, performance, align='center', alpha=0.5, color = 'r')
plt.xticks(y_axis, objects)
plt.ylabel('Daily Income($)')
plt.title('Author Revenue v. Publisher Revenue')
plt.show()



objects = ('Amazon Revenue', 'Gross Sales')
y_axis = np.arange(len(objects))
performance = [avg3, avg4]

plt.bar(y_axis, performance, align='center', alpha=0.5, color = 'b')
plt.xticks(y_axis, objects)
plt.ylabel('Dollars($)')
plt.title('Amazon Revenue v. Gross Sales')
plt.show()
