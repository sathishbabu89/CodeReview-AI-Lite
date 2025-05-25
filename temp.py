def is_spam(email_text):
    spam_keywords = ["win", "free", "prize", "click", "subscribe now"]
    for word in spam_keywords:
        if word in email_text.lower():
            return True
    return False

# Example usage
email = "Congratulations! You have won a free prize. Click here to claim."
if is_spam(email):
    print("This email is spam!")
else:
    print("This email is not spam.")
