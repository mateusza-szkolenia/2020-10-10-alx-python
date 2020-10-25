imiona_meskie_a = [ "Kuba", "Barnaba" ]
imiona_zenskie_bez_a = [ "Viki", "Margaret" ]
imiona = [ "Mateusz", "Magda", "Andrzej", "Dariusz", "Kuba", "Viki", "Jacek" ]

meskie = [ imie for imie in imiona if ( imie in imiona_meskie_a ) or ( imie[-1] != 'a' and imie not in imiona_zenskie_bez_a ) ]
zenskie = [ imie for imie in imiona if ( imie not in imiona_meskie_a ) and ( imie[-1] == 'a' or imie in imiona_zenskie_bez_a ) ]

print( f"Meskie: {meskie}")
print( f"Zenskie: {zenskie}")
