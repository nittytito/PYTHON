has_account = True
email_verified = False
can_login = has_account and email_verified
print('has_account and email_verified',has_account and email_verified)
is_email_valid = "miya@gmail.com"
is_email_verified= "@" in is_email_valid
user_age = 17
is_age_valid= user_age >= 18
can_login_final = has_account and email_verified and is_email_valid and is_age_valid
print("Can Login: ", can_login)
print("Is email Valid: ",is_email_verified)
print("Is Age Valid: ",is_age_valid)
print("Login: ",can_login_final)
print("Has Account is True:",has_account is True)