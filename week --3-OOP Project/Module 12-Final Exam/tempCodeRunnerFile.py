a = input("Savings Account or Current Account (svA/cuA) :")
            if a == "sv":
                currentUser = SavingsAccount(name, email, addrs)
            else:
                currentUser = CurrentAccount(name, email, addrs)