# Array, Stack, Queue, Linked List, Dictionary (MAP - HASHMAP) yapılarını oluştururuz.


lib = ['Zeynep Yılmaz 100', 'Ezgi Altay 101', 'Merve Duman 102', 'Kadir Aydın 103',
       'Akif Ay 104']

dictionary = {
    'Zeynep Yılmaz': 100,
    'Ezgi Altay': 200,
    'Merve Duman': 300
}


# Array

# Array' e eleman ekleme işlemi
def appendArray(x):
    # Sayaçları deklare ederiz.
    counter = 0
    indexSize = 0

    # Varolan dizinin eleman sayısını hesaplarız.
    for k in lib:
        counter += 1

    # Yeni bir dizi oluştururuz.
    libNew = ["" for _ in range(counter + 1)]

    # Yeni diziye var olan dizinin elemanlarını yazdırırız.
    for s in lib:
        libNew[indexSize] = s
        indexSize += 1

    # Diziye yeni eklemek istediğimiz elemanı ekleriz
    if counter <= indexSize:
        libNew[indexSize] = x
    print(libNew)  # Dizinin yeni elemanı girilmiş olarak çıktısı verilir


# Eleman eklemek için fonksiyon çağrılarak çalıştırılır.
# appendArray('Ela Gök 105')


# Array' de değer silme işlemi
def deleteArray(x):
    # Sayaçları deklare ederiz.
    counter = 0
    indexSize = 0

    for n in lib:
        indexSize += 1

    # Elimizdeki dizinin bir fazla boyutunda yeni bir dizi oluştururuz.
    libNew = ["" for _ in range(indexSize)]

    # Silinmek istenen boyutda dizinin elemanı olup olmadığının kontrolü.
    if x >= indexSize:
        print("Girdiğiniz index sayısı dizinin boyutundan büyüktür.")

    else:
        # Varolan dizinin üstünde silinmek istenen index değerini silerek bir üst index'deki değeri yazar üstüne
        for s in range(x, indexSize - 1):
            lib[x] = lib[x + 1]
            x += 1

        # Yukarıda dizinin değerlerini kaydırdık buradada index sayısı bir azaltılan yeni diziye değerler kaydedilir
        for k in lib:
            if counter < indexSize - 1:
                libNew[counter] = k
                counter += 1
            else:
                print(libNew)


# Eleman silmek için fonksiyon çağrılarak çalıştırılır.
# deleteArray(0)


# Array' de değer arama işlemi yaparız.
def searchArray(x):
    print(f'Girdiğiniz değerde ki kişi:', lib[x])


# # Eleman aramak için fonksiyon çağrılarak çalıştırılır.
# searchArray(4)


# Array' de index' e göre eleman arama.
def searchIndexArray(x):
    print(lib[x])


# Elemanı Index numarasıyla aramak için fonksiyon çağrılarak çalıştırılır.
# searchIndexArray(3)


# QUEUE


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Queue' ya eleman ekleme işlemi
    def appendQueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Queue' ya eleman çıkarma işlemi
    def deleteQueue(self):
        if not self.is_empty():
            popped_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return popped_item
        else:
            return None

    # Queue' nun boş olup olmadığını kontrol eder
    def is_empty(self):
        return self.front is None

    # Queue' da arama işlemi
    def searchQueue(self, item):
        qs = Queue()
        count = 0
        # Queue' nun boş olup olmadığını kontrol ederek
        # elemanları teker teker çekip aradığımız eleman olup olmadığını kontrol ederiz.
        while not self.is_empty():
            k = self.deleteQueue()
            if k == item:
                print(f'{k} değeri Queue da {count} indexinde bulunmuştur.')
                qs.appendQueue(k)
                break
            else:
                qs.appendQueue(k)
            count += 1
        # Queue tekrardan doldurulur
        while not qs.is_empty():
            self.appendQueue(qs.deleteQueue())

            if self.is_empty():
                print(f'{self} değeri Queue da bulunamadı.')


# Eleman eklemek için fonksiyon çağrılarak çalıştırılır.
q = Queue()
q.appendQueue('Ayşe')
q.appendQueue('Zeynep')
q.appendQueue('Merve')


# Eleman silmek için fonksiyon çağrılarak çalıştırılır.
# print(q.deleteQueue())

# Eleman aramak için fonksiyon çağrılarak çalıştırılır.
# q.searchQueue('Merve')


# STACK

class stack:
    def __init__(self):
        self.stack = []  # Bağlı liste olarak kullanılacak liste oluşturulur

    # Eleman ekleme işlemi
    def appendStack(self, item):
        self.stack.append(item)

    # Eleman çıkarma işlemi
    def deleteStack(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    # Eleman arama işlemi sadece son elemanı döndürür
    def peek(self):
        return self.stack[-1]

    # stack'in boş olup olmadığını kontrol eder
    def is_empty(self):
        return len(self.stack) == 0

    # Stack' te eleman arama işlemi yapılır
    def searchStack(self, item):
        count = 0
        emptyStack = []
        found = True

        # Stack' ten elemanları teker teker çekerek aradığımız eleman olup olmadığını kontrol ederiz.
        while stack:
            k = self.deleteStack()
            if k == item:
                print(f'{k} değeri Stack de {count} indexinde bulunmuştur.')
                emptyStack.append(k)
                break
            else:
                emptyStack.append(k)
            count += 1

        # Stack' i tekrardan doldurulur.
        while emptyStack:
            self.appendStack(emptyStack.pop())
            if not found:
                print(f'{item} değeri Stack de bulunamamıştır.')


my_stack = stack()
# Stack' e eleman eklemek için fonksiyon çağrılarak çalıştırılır.
my_stack.appendStack('Ayşe')
my_stack.appendStack('Merve')
my_stack.appendStack('Kadir')
my_stack.appendStack('Ezgi')
my_stack.appendStack('Mirza')


# stack'ten aleman silmek için fonksiyon çağrılarak çalıştırılır.
# print(my_stack.deleteStack())

# stack'in en üstünde bulunan veri değerini çıktı olarak verir.
# print(my_stack.peek())

# Eleman aramak için fonksiyon çağrılarak çalıştırılır.
# my_stack.searchStack('Ezgi')


# Linked List

class NodeForLinkedList:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Linked List'e veri ekleme işlemi gerçekleştirilir
    def appendLinkedList(self, data):
        new_node = NodeForLinkedList(data)
        if not self.head:
            self.head = new_node
            self.current = self.head
        else:
            self.current.next = new_node
            self.current = self.current.next

    # Linked List'den veri silme işlemi gerçekleştirilir
    def deleteLinkedList(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # Linked List'de veri arama işlemi gerçekleştirilir
    def searchLinkedList(self, item):
        current = self.head
        count = 0
        while current:
            if current.data == item:
                return print(f'Aradığınız değer {item} {count} index de bulunmaktadır.')
            current = current.next
            count += 1
        return print(f'Aradığınız değer List de bulunmamaktadır')

    # Linked List'de o anda bulunan verileri gösterir
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


new_linkedlist = LinkedList()

# Eleman eklemek için fonksiyon çağrılarak çalıştırılır.
new_linkedlist.appendLinkedList('Ayşe')
new_linkedlist.appendLinkedList('Merve')
new_linkedlist.appendLinkedList('Kadir')
new_linkedlist.appendLinkedList('Zeynep')
new_linkedlist.appendLinkedList('Mirza')


# Eleman silmek için fonksiyon çağrılarak çalıştırılır.
# new_linkedlist.deleteLinkedList('Merve')

# linked list'in o an ki son verinin çıktısını verir
# new_linkedlist.print_list()

# Eleman aramak için fonksiyon çağrılarak çalıştırılır.
new_linkedlist.searchLinkedList('Zeynep')


# DICTIONARY (MAP - HASHMAP)

# Dictionary oluşturulur
def appendDictionary(key, value):
    # Dictionary'e yeni eleman ekleme işlemi
    print(dictionary)
    dictionary[key] = value
    print(dictionary)


# Eleman eklemek için fonksiyon çağrılarak çalıştırılır.
# appendDictionary('Ali Pek', 500)


def deleteDictionary(key):
    # Dictionary'den veri silme işlemi
    dictionaryNew = {}
    for k, v in dictionary.items():
        if k != key:
            dictionaryNew[k] = v
    print(dictionaryNew)


# Eleman silmek için fonksiyon çağrılarak çalıştırılır.
# deleteDictionary('Zeynep Yılmaz')


def searchDictionary(x):
    # Dictionary'de verinin var olup olmadığını tespit etmek.
    # Bunu in dictionary kalıbıylada __contains__ kalıbıylada yapabiliriz.
    if x in dictionary:
        print(f'Aradığınız değer {x} dictionary de vardır.')
        print(dictionary.__contains__(x))
    else:
        print('Girdiğiniz değer dictionary de yoktur.')


# Eleman aramak için fonksiyon çağrılarak çalıştırılır.
# searchDictionary('Zeynep Yılmaz')


"""

Big(O) Notation:
Big(O) notasyonu, bir algoritmanın performansını veya karmaşıklığını ifade etmek için kullanılan bir notasyondur.
Genellikle bir algoritmanın en kötü durum senaryosundaki (Worst Case) çalışma süresini ve
gereken bellek miktarını belirtmek için kullanılır.

Bir algoritmanın girdi boyutuna bağlı olarak nasıl artacağını gösterir. Genellikle n ile gösterilir.
Örneğin bir algoritmanın karmaşıklığı O(n) ise algoritmada çalışma süresi girdi boyutuyla doğru orantılıdır.
Yani girdi sayısı iki katına çıktığında çalışma süreside iki katına çıkar.

Bazı Big(o) Notasyonları;

O(1): Bu notasyon sabit zamanı gösterir. Girdi boyutu ne olursa olsun sabit zamanda çalışır.
O(n): Bu notasyon doğrusal zamanı gösterir. Girdi boyutu arttıkca çalışma süreside doğru orantılı olarak artar.
O(n^2): Bu notasyon karesel zamanı gösterir. Girdi boyutu arttıkça çalışma süresi girdinin karesi olarak artar.
O(logn): Bu notasyon logaritmik zamanı gösterir. Girdi boyutu arttıkça çalışma süresi logaritmik olarak artar.

Bu notasyonlar algoritmaların performansını karşılaştırmak ve problem için hangisinin 
daha uygun olduğunu karar vermemizi sağlar. Bir problemin birden fazla çözüm yolu yani algoritması olabilir.
Her algoritmanın da farklı karmaşıklığı olabilir. Bu da problem için birden çok çözüm bulunabileceğini ve
bu çözümler arasında karmaşıklığı en verimli olan algoritmayı seçerek hareket etmemiz gerektiğinin anlamına gelmektedir.

Bir algoritmanın Big O notasyonunu tespit etmek için ilk olarak işlem süresi analiz edilir. 
Örneğin algoritmadaki döngülerin ve iç içe döngülerin sayısına bakılır.

İkinci olarak algoritmanın işlem süresi matematiksel olarak ifade edilmelidir. 
Örneğin iki iç içe for döngüsünün matematiksel olarak ifadesi O(n^2)' dir.

Üçüncü olarak algoritmanın en kötü durumunu - en yavaş çalıştığı durum olarak düşünmek gerekmektedir.
Örneğin bir dizide eleman ararken aradığımız elemanın dizinin sonunda olması veya hiç olmaması
tüm diziyi gezerek tek tek arama yapmak zorunda kalmamız demektir.

Son olarak çalışma ve bellek süresini Big O notasyonu şeklinde (matematiksel olarak) ifade etmemiz gerekmektedir.


Aşağıdaki karmaşıklık ifadeleri yukarıda veri yapıları için yazdığımız method'lar için hesaplanmıştır.
Sırayla bakıcak olursak;

Array' de: Silme(Delete) İşlemi: O(n) , Arama(Search) İşlemi: O(1) , Ekleme(Append) İşlemi: O(n)

Oueue' da: Silme(Delete) İşlemi: O(n) , Arama(Search) İşlemi: O(n) , Ekleme(Append) İşlemi: O(1)

Stack' de: Silme(Delete) İşlemi: O(1) , Arama(Search) İşlemi: O(n) , Ekleme(Append) İşlemi: O(1)

Linked List' de: Silme(Delete) İşlemi: O(n) , Arama(Search) İşlemi: O(n) , Ekleme(Append) İşlemi: O(1)

Dictionary (MAP - HASHMAP)' de : Silme(Delete) İşlemi: O(n) , Arama(Search) İşlemi: O(1) , Ekleme(Append) İşlemi: O(1)


Bu karmaşıklık analizlerine bakarsak her method için farklı durumlar vardır. 
Bizim geliştirmek istediğimiz algoritma için kullanılacak yapıyı iyi analiz ederek seçmemiz gerekir.

Eğer Array seçersek arama işlemini çok hızlı şekilde çalıştıra biliriz.
Oueue' yu seçersek yapıdan çok hızlı eleman çıkartılır veya eklenir. Ama arama işlemi yavaş olur.
Stack' i seçersek yapıdan çok hızlı eleman çıkartılır veya eklenir. Ama arama işlemi yavaş olur.
Linked List' i seçersek tüm işlemleri veri girişine paralel olarak sabit zamanda yapabiliriz.
Dictionary' yi seçersek eleman ekleme ve arama işlemlerini çok hızlı yaparız ama eleman silme işlemi yavaş olur.







 
"""
