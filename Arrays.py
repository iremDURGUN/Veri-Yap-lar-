import array as arr

# Array'de veri arama
def search(x):
    # Array oluşturma
    numbers = arr.array('i', [10, 20, 30])

    # Sayaçları deklare ederiz.
    cCounter = 0  # # Dizide gezerken hangi index değerinde olduğumuzu tespit etmek için sayaç oluştururuz.

    #  Değeri verilmiş verinin index'ini arama
    for k in numbers:
        if k == x:
            print(f'Girdiginiz degerin index sayısı: {cCounter}')
            break
        else:
            cCounter += 1


# Fonksiyon çağrılarak çalıştırılır.
# search(1)

# Array'e veri ekleme
def append(x):
    # Sayaçları deklare ederiz.
    indexSize = 0
    counter = 0

    # İçerisinde 0 değereleri olan 5 elemanlı bir dizi oluşturduk
    newN = [0] * 5

    # Oluşturduğumuz boş dizinin içini yeni veriler ile doldurduk
    for k in newN:
        newN[indexSize] = indexSize * 6
        indexSize += 1
    print(newN)  # Dizinin elemanları girilmiş olarak çıktısı verilir

    # İçerisinde 0 değereleri olan 6 elemanlı yeni bir dizi oluşturduk
    num = [0] * 6

    # 5 elemanlı olan dizinin içersindeki elemanları 6 elemanlı olan yeni diziye kopyalarız
    for s in newN:
        num[counter] = s
        counter += 1

    # Diziye yeni eklemek istediğimiz elemanı ekleriz
    if indexSize <= counter:
        num[counter] = x
        print(num)  # Dizinin yeni elemanı girilmiş olarak çıktısı verilir


# Fonksiyon çağrılarak çalıştırılır.
# append(50)


def access(x):
    # Sayaçları deklare ederiz.
    indexSize = 0

    # İçerisinde 0 değereleri olan 5 elemanlı bir dizi oluşturduk
    num = [0] * 5

    # Oluşturduğumuz boş dizinin içini yeni veriler ile doldurduk
    for k in num:
        num[indexSize] = indexSize * 6
        indexSize += 1

    print(num[x])


# Fonksiyon çağrılarak çalıştırılır.
# access(2)

def delete(x):
    # Sayaçları deklare ederiz.
    indexSize = 0

    # İçerisinde 0 değereleri olan 5 elemanlı bir dizi oluşturduk
    num = [0] * 5

    # Oluşturduğumuz boş dizinin içini yeni veriler ile doldurduk
    for k in num:
        num[indexSize] = indexSize * 6
        indexSize += 1

    if x <= indexSize:
        for k in range(x, indexSize - 1):
            num[x] = num[x + 1]
            x = x + 1
    num[indexSize - 1] = 0
    print(num)


# Fonksiyon çağrılarak çalıştırılır.
# delete(2)


def deleteSecondWay(x):
    # Sayaçları deklare ederiz.
    indexSize = 0
    counter = 0

    # İçerisinde 0 değereleri olan 5 elemanlı bir dizi oluşturduk
    num = [0] * 5

    # Oluşturduğumuz boş dizinin içini yeni veriler ile doldurduk
    for k in num:
        num[indexSize] = indexSize * 6
        indexSize += 1

    # Bir index silindikten sonra değerlerin tekrar yazılması için bir dizi oluştururuz
    numN = [0] * 4

    # Girilen parametre dizi boyutundan büyükse uyarı döndürmesi için if yapısı kullanırız
    if x >= indexSize:
        print("Girdiğiniz index sayısı dizinin boyutundan büyüktür.")

    else:

        # Varolan dizinin üstünde silinmek istenen index değerini silerek bir üst index'deki değeri yazar üstüne
        for s in range(x, indexSize - 1):
            num[x] = num[x + 1]
            x = x + 1

        # Yukarıda dizinin değerlerini kaydırdık buradada index sayısı bir azaltılan yeni diziye değerler kaydedilir
        for k in range(0, indexSize - 1):
            numN[k] = num[counter]
            counter += 1
        print(numN)


# Fonksiyon çağrılarak çalıştırılır.
# deleteSecondWay(4)

"""
Array'ler statik yapıdadırlar. Verileri hafızada yan yana sıralı bir şekilde tutmamızı sağlar. 
Bu da veri aramada en hızlı şekilde cevap döndürülmesini sağlayacak yapıdır.
Ancak, dizilerin sabit boyutta olması ve veri ekleme işlemini zorlaştırması gibi bazı kısıtlamalara da sahiptirler. 
Bu nedenle, veri boyutunun bilinmedği durumlarda dinamik veri yapıları tercih edilebilir.

Veri Ekleme;
Yukarıda yaptığımız gibi veri ekleme işlemi yapabiliriz ama bunu yapabilmek için elimizdeki array'in boyutundan,
eklemek istediğimiz veri adeti kadar artırılmış boyutta başka bir dizi oluşturmalıyız.
Elimizdeki verileri ve eklenicek verileri de bu yeni diziye eklemeliyiz.
Veri ekleme işlemini bu şekilde yapabiliriz.

Veri Silme;
Silme metodunu iki farklı şekilde gerçekleştirdik ilk versiyonda veri silindiğinde var olan dizide istenen index'deki
veri silinir ve dizide elemanlar kaydırılarak en son eleman boşaltılır ve dizi boyutunun aynı kalması sağlanır.

İkinci yöntemde ise veriyi sileriz ve index sayısı var olan diziden eksik olan bir dizi oluştururuz.
Oluşturulan yeni diziye geriye kalan verileri atarız.

Bu iki yöntem arasında ki farklar;
İlk yöntemde dizi boyutu değişmez ve işlem ikinci yönteme göre hızlıdır.Fakat RAM' de fazladan yer tutmamıza sebep olur.
İkinci yöntemde ise yeni bir dizi oluştururuz. Bu da çalışma hızını etkiler.

Veri arama;
Bu işlemi yaparken sorgulanan verinin tutulduğu yeri(index'ini) ararken dizinin içinde gezerek istenen verinin hangi index'de tutulduğunu buluruz. 

Veriye erişim;
Bu işlemi yaparken array verilerin nerede olduğunu bildiği için index numarasıyla direkt olarak erişim sağlarız.

Metodlar;

Search (Arama): Bu metod, dizide belirli bir elemanı aramak için kullanılır.
Dizide bir elemanı aramak O(n) karmaşıklığa sahiptir çünkü en kötü durumda tüm dizi taranmalıdır. 

Append (Ekleme): Bu metod, dizinin sonuna bir eleman eklemek için kullanılır.
Sona ekleme işlemi genellikle O(1) karmaşıklığa sahiptir. 
Ancak, dizi doluysa ve yeni bir eleman eklenmek istenirse, yeni bir dizi oluşturulmalı 
ve tüm elemanlar yeni diziye kopyalanmalıdır. Bu durumda karmaşıklık O(n) olur.

Delete (Silme): Bu metod, diziden belirli bir elemanı silmek için kullanılır.
Diziden bir eleman silmek genellikle O(n) karmaşıklığa sahiptir 
çünkü silinen elemandan sonraki tüm elemanlar bir önceki indekse kaydırılmalıdır.

Access (Erişim): Bu metod, dizinin belirli bir indeksindeki elemana erişmek için kullanılır.
Bu işlem genellikle O(1) karmaşıklığa sahiptir çünkü diziler, indeksleme işlemini hızlı bir şekilde gerçekleştirir.

Bu metodlar, array veri yapısının temel işlemleridir ve array'lerin birçok algoritma ve problem çözümünde 
kullanılmasını sağlar.
"""
