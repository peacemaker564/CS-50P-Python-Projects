def main():
    names = ["Mario",  "Luigi" , "Yoshi"]
    for name in names:
        print(invitation_letter(name , "Princess Peach"))



def invitation_letter(invitee, sender):
    return f"""

    ======================================

    Dear {invitee},

    You are cordially invited to ball at
    Peach's castle this evening at 7:00 pm.

    Sincerely,
    {sender}

    ======================================

    """



main()
