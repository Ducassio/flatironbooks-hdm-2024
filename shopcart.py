# Save the form page HTML content to a file
with open("flatiron_books_licensing_request.html", "w") as file:
    file.write(form_page_html)

# Save the confirmation page HTML content to a file
with open("confirmation.html", "w") as file:
    file.write(confirmation_page_html)

print("HTML files 'flatiron_books_licensing_request.html' and 'confirmation.html' have been created.")