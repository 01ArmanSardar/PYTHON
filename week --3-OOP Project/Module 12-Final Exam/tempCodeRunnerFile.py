if self.loan_limit>0:
            self.balance+=amount
            self.loan_limit-=1
            # self.total_loan+=amount
        else:
            print('your loan limit exceeded')