def silnia( n ):
    print(f"Uruchomiono silnia({n})")
    if n > 1:
        return n * silnia( n - 1 )
    else:
        return 1

print( silnia(5) )