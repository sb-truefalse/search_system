def search4symbols(phrase:str) -> set:
    """Возврощает уникальные символы"""
    return sorted(''.join(set(phrase)))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Возврощает множество букв из `letters`, в указаннй фразе"""
    return set(letters).intersection(set(phrase))
