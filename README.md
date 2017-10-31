 # WriteUp jogo da soma(prog250) HACKAFLAG Salvador 10/06/2017
```
 +++    HACKAFLAG - Jogo da Soma   +++

 [+] ZAAL X é um computador criado para jogar um jogo muito interessante
    chamado Jogo da Soma.

 [+] Nesse jogo, cada um escolhe, sem repetir, um número de 1 a 9, de
    maneira alternada, e ganha o jogo aquele que primeiro escolher uma
    combinação de 3 dígitos que some o valor de quinze.

 [+] Segue um exemplo onde o computador começa jogando.

    Computador: 5   8   4   6    -> Computador ganha com: [4, 5, 6]
    Jogador   :  9   2   3   -

 [+] Seu objetivo é derrotar ZAAL X, que sempre começa jogando, em até 20
    jogadas.

 [+] Caso você sobreviva as 20 rodadas sem perder, será dada uma
    oportunidade de você começar jogando.
 
 [+] Para começar, digite start: 
```
## Ideia

> A grande sacada desse desafio é perceber que o jeito mais fácil de se resolver sem muito esforço é encaixando um jogo da velha no desafio da seguinte maneira:

![Screen shot](https://raw.github.com/lucasnathaniel/progSalvador/master/tictactoe.png "TicTacToe")

> Caso queira saber mais sobre essa ordenação, veja: <http://www.ms.uky.edu/~lee/ma310sp15/gameoffifteen.pdf>

> O Jogo é dividido em 2 etapas: uma que o computador começa(que sempre dará empate, e que você deve forçar isso), e uma última em que você começa(infelizmente só tem 1 etapa dessa :/), em amabas as etapas eu segui esse tutorial: <https://pt.wikihow.com/Ganhar-no-Jogo-da-Velha>, sempre buscando a casa 5 ou 6, de uma maneira defensiva para não deixar o inimigo fazer uma linha. Na segunda etapa é só fazer uma pequena série de ifs para a vitória, após isso, a flag aparece, veja o log registrado.

## Execução

```
$ python3 prog.py
```

By: Lucas ~K4L1~ Nathaniel