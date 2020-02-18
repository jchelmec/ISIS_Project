from pathlib import Path

class fileDir:
    """Klasa odczytująca wszystkie pliki w katalogu"""

    def __init__(self, ext):
        """Konstruktor"""
        self.ext = ext

    def __iter__(self):
        '''Iteracja po pilkach w katalogu'''
        p = Path('.').glob(self.ext)
        return p

if __name__ == '__main__':
    file = fileDir('*.txt')

    for x in file:

        print( x)

