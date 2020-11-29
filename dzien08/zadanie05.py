# Zaimplementuj klase CashMachine umozliwiajaca wpłacanie i
# wypłacanie pieniedzy. Zadbaj o to aby stan bankomatu
# przetrzymywany był w zmiennych prywatnych.
# Przykład uzycia:
# >>> cash_machine = CashMachine()
# >>> cash_machine.is_available()
# False
# >>> cash_machine.put_money([200, 100, 100, 50])
# >>> cash_machine.is_available()
# True
# >>> cash_machine.withdraw_money(150)
# [100, 50]