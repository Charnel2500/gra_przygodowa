import random
import time

def cieniołak():
    print('''W końcu docierasz do najbardziej dziewiczej, najciemniejszej części lasu, gdzie czai
    się ogromny cieniołak. Walczysz z nim zażarcie, wiedząc, że masz potężny łuk od Aleny. W końcu
    zwyciężasz. Z drzewa, którego pilnował zrywasz jabłko dające nadludzkie siły. Dzięki niemu przez
    resztę swojego życia znany jesteś jako niezrównany i niepokonany łowca - pogromca legendarnych bestii.''')

def małyCieniołak():
    print('''Bez łuku Aleny postanawiasz walczyć z mniejszym cieniołakiem, żyjącym trochę na uboczu, walka jest ciężka,
    ale to ty jestes górą. Nieopodal zauważasz jaskinie cieniołaka ze skarbem. Dzięki niemu, mając ogromne oszczędności,
    dożywasz starości''')

def smok():
    print('''Ogromny, przerażający smok pojawia się przed twoimi oczami. Jego siła, szybkość i zwinność jest niebywała.
    Jego ogień pali twoją tarczę, którą odrzucasz. Chwytasz buławę w obie ręce i rzucasz się prosto w jego ogromny łeb.
    Wyprowadzone uderzenie powala smoka, a ty znajdujesz elksir siły, który sprawia, że jesteś przez resztę swojego życia
    niezrównanym wojownikiem, gladiatorem, który zgładził najsłynniejszych rycerzy tego świata,
    którego imię nigdy nie zostanie zapomniane. ''')

def wiwerna():
    print('''Widzisz sporą wiwernę przed sobą. Walczycie zażarcie, ale w końcu odnosisz sukces. Za znalezione skarby, które
    pilnowała żyjesz spokojnie do końca życia w bogactwie i szczęściu''')

def wyświetlIntro():
    print('''Witaj! Ostatniej nocy spędziłeś w karczmie długie godziny. Chyba
    ktoś dosypał ci coś do kufla, bo nic nie pamiętasz. Budzisz się pośrodku
    wielkiego, ciemnego lasu. Wygląda na bardzo stary.''')
    time.sleep(4)

def pierwszeKroki():
    print('''Powoli wstajesz. Jak na środek lata nie jest zbyt ciepło. Rozglądasz
    się dookoła. Widzisz stare drzewa, gdzieniegdzie paprocie. Słyszysz śpiew ptaków
    i zapach kwiatów. Kilkadziesiąt metrów dalej widzisz niewielkie wzniesienie, a
    na nim kilka drzew. Postanawiasz tam iść i wspiąć na jedno z nich, aby móc lepiej
    rozejrzeć się po okolicy. Zajmuje ci to trochę czasu...''')
    time.sleep(6)

def widokOkolicy():
    print('''Wspinasz się na najwyższe drzewo i widzisz okolicę. Widzisz niedaleko drogę,
    możesz nią dotrzeć na północ lub południe lasu. Od ciebie zależy, którą drogę wybierzesz.
    Na północy widzisz, że las robi się jeszcze gęstszy, a drzewa są większe. Na południu
    las się rozrzedza, a na końcu widoć góry. Którą drogę wybierzesz? (1 - północ, 2 -
    południe)''')

def krasnoludKról():
    print('''W końcu docierasz do podnóża góry. U wejścia do jaskini czeka na ciebie krasnolud. Witam cię podróżniku!
    W tej jaskini czekają na ciebie groźne bestie. Widzę, że twój miecz jest już stary i zużyty. Może chciałbyś kupić
    moją buławę? Kosztuje jedyne 10 złota. Co ty na to? 1 - tak 2 - nie''')
    buława = int(input())
    if buława == 1:
        print("No i kupiłes. Teraz czas zmierzyć się ze swoim przeciwnikiem")
        smok()
    elif buława == 2:
        print("Jak nie to nie. Teraz czas zmierzyć się ze swoim przeciwnikiem")
        wiwerna()
    else:
        print("Zła wartość! Giń!!!!")


def władcaElfów():
    print('''Witaj kolego. Przed tobą władczyni elfów Alena! W tamtej części lasu czekają na ciebie ogromne cieniołaki. Widzę, że
    twój stary łuk jest w kiepskim stanie. Może kupisz mój za jedyne 6 sztuk złota? 1 - kup 2 - nie kupuj''')
    łuk = int(input())
    if łuk == 1:
        print("No i kupiłeś. Teraz czas zmierzyć się ze swoim przeciwnikiem")
        cieniołak()
    elif łuk == 2:
        print("Jak nie to nie. Teraz czas zmierzyć się ze swoim przeciwnikiem")
        małyCieniołak()
    else:
        print("Zła wartość! Giń!!!!")



def krainaElfów():
    print('''Idziesz północną drogą. Nagle przy drodzę zauważasz niewielką stertę kamieni
    pod którą wystaje niewielki woreczek. Co robisz? (1 - sprawdzasz co jest w środku, 2 -
    ignorujesz i idziesz dalej)''')
    sakiewka = int(input())
    twojeZdrowie = 10
    twojeZłoto = 5
    if sakiewka == 1:
        print("Znajdujesz złoto! Niestety, przy okazji ugryzł cię pająk! Idziesz dalej.")
        twojeZłoto = twojeZłoto + 1
        twojeZdrowie = twojeZdrowie - 2
        print("Twoje złoto: ")
        print(twojeZłoto)
        print("Zdrowie: " )
        print(twojeZdrowie)
        władcaElfów()
    elif sakiewka == 2:
        print("Wolisz nie ryzykować, idziesz dalej")
        print("Twoje złoto: ")
        print(twojeZłoto)
        print("Zdrowie: " )
        print(twojeZdrowie)
        władcaElfów()
    else:
        print("Zła wartość! Giń!!!!")



def krainaKrasnoludów():
    print('''Przemierzasz szlak, kierując się na południe. Las nie jest już tak gęsty jak przedtem. W zasięgu wzroku widzisz
    góry. Nagle słyszysz głośny krzyk. Przybiegasz i widzisz kupca, który walczy ze złoczyńcą. "Pomóż mi!" - krzyczy kupiec.
    "Nie słuchaj go, to mi pomóż" - mówi złoczyńca. Co wybierzesz? (1 - pomóż kupcowi, 2 - pomóż złoczyńcy, 3 - zabij ich obu)
    ''')
    pomoc = int(input())
    twojeZdrowie = 10
    twojeZłoto = 5
    if pomoc == 1:
        print("Kupiec jest ci bardzo wdzięczny, niestety jest chciwy i daje ci tylko 1 złoto. Idziesz dalej.")
        twojeZłoto = twojeZłoto + 1
        twojeZdrowie = twojeZdrowie
        print("Twoje złoto: ")
        print(twojeZłoto)
        print("Zdrowie: " )
        print(twojeZdrowie)
        krasnoludKról()

    elif pomoc == 2:
        print('''Złoczyńca nie dotrzymuje umowy, ale zabijasz go odnosząc przy tym poważne rany. Za to
        plądrujesz całe złoto jakie ma kupiec. Otrzymujesz 5 złota, ale tracisz 5 punktów zdrowia. Idziesz dalej.''')
        twojeZłoto = twojeZłoto + 5
        twojeZdrowie = twojeZdrowie - 5
        print("Twoje złoto: ")
        print(twojeZłoto)
        print("Zdrowie: " )
        print(twojeZdrowie)
        krasnoludKról()
    elif pomoc == 3:
        print('''Przykro mi nie dałeś rady, następnym razem mierz siły na zamiary.''')
    else:
        print("Zła wartość! Giń!!!!")



zagrajPonownie = 'tak'
while zagrajPonownie == 'tak' or zagrajPonownie == 't':
    wyświetlIntro()
    pierwszeKroki()
    widokOkolicy()
    wybierzDroge = int(input())
    if wybierzDroge == 1:
        krainaElfów()
    elif wybierzDroge == 2:
        krainaKrasnoludów()
    else:
        print("Zła wartość! Giń!!!!")

    print('Chcesz ponownie rozpocząć swoją przygodę? (tak lub nie)')
    zagrajPonownie = input()
