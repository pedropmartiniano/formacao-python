from abc import ABC # Abstract Base Classes
from collections.abc import MutableSequence

class Playlist(MutableSequence):
    pass

# irá dar erro pois a classe pai "MutableSequence"(não só ela, como em várias outras classes abstratas) está esperando que todas suas classes filhas implementem alguns métodos obrigatórios(como se fosse uma interface)
filmes = Playlist()


#Para eu criar uma classe abstrata(classe que não deve ser instanciada e apenas herdada) e fazer que toda classe filha deve implementar um método, devo fazer o seguinte:
from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    @abstractmethod
    def __str__(self) -> str:
        pass