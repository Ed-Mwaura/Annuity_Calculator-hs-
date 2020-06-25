import math


class Calculator:

    def calculate_months(self):
        print("Enter credit principal:")
        credit_p = int(input())
        print("Enter monthly payment:")
        m_payment = float(input())
        print("Enter credit interest:")
        c_interest = float(input())

        nominal_interest = c_interest / 1200

        log_base = m_payment / (m_payment - nominal_interest * credit_p)

        n_months = math.ceil(math.log(log_base, (1 + nominal_interest)))

        if n_months % 12 == 0:
            n_years = n_months / 12

            if n_years == 1:
                print(f'You need {n_years} year to repay this credit')
            else:
                print(f'You need {n_years} years to repay this credit!')
        else:
            n_years = n_months // 12
            n_rem_months = n_months % 12

            if n_years == 0:
                print(f'You need {n_rem_months} months to repay this credit!')
            elif n_years == 1:
                print(f'You need {n_years} year and {n_rem_months} months to repay this credit!')
            else:
                print(f'You need {n_years} years and {n_rem_months} months to repay this credit!')

    def calculate_monthly_payments(self):
        print("Enter credit principal:")
        credit_p = int(input())
        print("Enter count of periods:")
        c_periods = int(input())
        print("Enter credit interest:")
        c_interest = float(input())

        nominal_interest = c_interest / 1200

        denominator = math.pow(1 + nominal_interest, c_periods) - 1
        numerator = nominal_interest * math.pow(1 + nominal_interest, c_periods)
        annuity_payment = math.ceil(credit_p * (numerator / denominator))

        print(f'Your annuity payment = {annuity_payment}!')

    def calculate_differential_payments(self):
        print("Enter credit principal:")
        credit_p = int(input())
        print("Enter count of periods:")
        c_periods = int(input())
        print("Enter credit interest:")
        c_interest = float(input())

        nominal_interest = c_interest / 1200

        # start with 1 and end with total + 1; calculations start after the month is over
        # but python is zero indexed
        for i in range(1, c_periods + 1):
            inner_fraction = (credit_p * (i - 1)) / c_periods
            bracket_data = credit_p - inner_fraction
            total_calc = math.ceil(credit_p / c_periods + nominal_interest * bracket_data)

            print(f'month {i}: paid out {total_calc}')

    def calculate_principal(self):
        print("Enter monthly payment:")
        m_payment = float(input())
        print("Enter count of periods:")
        c_periods = int(input())
        print("Enter credit interest:")
        c_interest = float(input())

        nominal_interest = c_interest / 1200

        denominator_min = math.pow(1 + nominal_interest, c_periods) - 1
        numerator_min = nominal_interest * math.pow(1 + nominal_interest, c_periods)
        denominator = numerator_min / denominator_min

        credit_principal = round(m_payment / denominator)

        print(f'Your credit principal = {credit_principal}!')

    def intro(self):
        print("What type of payment do you choose? 'annuity' or 'diff'")
        pay_type = input()

        if pay_type == 'annuity':
            print("What do you want to calculate?")
            print('type "n" - for count of months, ')
            print('type "a" - for annuity monthly payment,')
            print('type "p" - for credit principal: ')

            choice = input()

            if choice == 'n':
                self.calculate_months()
            elif choice == 'a':
                self.calculate_monthly_payments()
            elif choice == 'p':
                self.calculate_principal()
            else:
                print("Invalid input!!")
        elif pay_type == 'diff':
            self.calculate_differential_payments()
        else:
            print("Invalid input!!")


calc = Calculator()
calc.intro()
