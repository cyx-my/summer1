def emaild(line):
    if line.startswith("From"):
        parts = line.split()
        if len(parts) >= 2:
            email = parts[1]
            return email
    return None

# Path
file_path = r"C:\Users\陈禹炫\Desktop\mbox.txt"

# Dictionary
email_counts = {}

with open(file_path, "r") as file:
    for line in file:
        email = emaild(line)
        if email:
            email_counts[email] = email_counts.get(email, 0) + 1

max_count = 0
max_email = ""

for email, count in email_counts.items():
    if count > max_count:
        max_count = count
        max_email = email

print("Email address with the highest message count:")
print("Email: ", max_email)
print("Message Count: ", max_count)


