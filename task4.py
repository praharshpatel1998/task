
# the python program for sum of numbers using for loop in range
total_sum = 0
start = (int(input("enter the start number: ")))
end = (int(input("enter the end number: ")))
for num in range(start, end + 1):
    total_sum = total_sum + num
print(f"The sum of numbers from {start} to {end} is: {total_sum}")