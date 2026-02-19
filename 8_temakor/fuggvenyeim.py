def fizetes_szamolas(oraszam:int,oraber:float,tulora_szorzo:float = 1.5):
    fizetes = 0
    if oraszam<=40:
        fizetes = oraszam * oraber
    else:
        alap = 40 * oraber
        tulora = (oraszam-40)*(oraber*tulora_szorzo)
        fizetes = alap+tulora
    return fizetes