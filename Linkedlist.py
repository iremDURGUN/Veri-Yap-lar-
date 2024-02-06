# Bağlı liste olarak kullanılacak liste oluşturulur
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Linked List'e veri ekleme işlemi gerçekleştirilir
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    # Linked List'den veri silme işlemi gerçekleştirilir
    def delete(self, data):
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
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # Linked List'de o anda bulunan verileri gösterir
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Linked List'i new_linkedlist'e atama yaparız çünkü linked list iki parametrelidir.
# Atama sayesinde sadece bir parametre üstünde işlem yaparız.
new_linkedlist = LinkedList()

# linked list'e veri ekler
new_linkedlist.insert('a')
new_linkedlist.insert('b')
new_linkedlist.insert('c')
new_linkedlist.insert('d')

# linked list'in o an ki haliyle çıktı verir
print('Linked Listin elemanlari;')
new_linkedlist.print_list()  # çıktı: 'a', 'b', 'c' , 'd'

# linked list'de bulunan veriyi siler
new_linkedlist.delete('c')

# linked list'in o an ki haliyle çıktı verir
print('Linked Listin son hali;')
new_linkedlist.print_list()  # çıktı: 'a', 'b', 'd'

# linked list'de veri arama işlemi
print(new_linkedlist.search('b'))  # çıktı: True
print(new_linkedlist.search('f'))  # çıktı: False

"""

Linked list (bağlı liste), verilerin düğümler adı verilen yapılar aracılığıyla bağlı olduğu bir veri yapısıdır. 
Her düğüm, bir veri elemanını (değer) ve bir sonraki düğümün referansını (link veya bağlantı) içerir. 
Linked list'ler, verilerin eklenmesi ve çıkarılması konusunda esneklik sağlar ve dinamik bir yapıya sahiptir.
Hafızada istediği kadar genişler.

Temelde üç tür linked list vardır;
Tek yönlü linked list (singly linked list) : Tek yönlü linked list yukardada anlatıldığı gibi temel linked list yapısıdır.
Çift yönlü linked list (doubly linked list) : Çift linked list'de her veri hem kendinden önceki hem de sonraki veri değerini tanır.
Dairesel linked list (circular linked list) : Dairesel linked list'de akış yine tek yönlüdür 
ama linked list'deki son veri ve baştaki veri birbirlerine bağlıdır.

Düğüm (Node): Veri elemanını (değer) ve bir sonraki düğümün referansını içerir.

Başlangıç Noktası (Head): Listenin başlangıç düğümünü gösterir.

Linked list'ler, belirli senaryolarda dizilere göre avantajlı olabilir.
Örneğin, veri ekleme ve çıkarma işlemlerinde daha hızlıdırlar. Ancak, belirli bir indekse doğrudan erişim sağlamak 
dizilere göre daha yavaş olabilir çünkü başlangıçtan itibaren elemanlar arasında gezilmelidir.

Metodlar;

Insert(Ekleme): Linked List'in başına veya sonuna bir eleman eklemek O(1) karmaşıklığa sahiptir. 
Ancak, listenin ortasına bir eleman eklemek O(n) karmaşıklığa sahiptir çünkü eklemek istediğimiz 
konuma kadar liste taranmalıdır.

Delete(Silme): Linked List'in başından veya sonundan bir eleman silmek O(1) karmaşıklığa sahiptir. 
Ancak, listenin ortasından bir eleman silmek O(n) karmaşıklığa sahiptir çünkü silmek istediğimiz 
konuma kadar liste taranmalıdır.

Search(Arama): Linked List'de bir elemanı aramak O(n) karmaşıklığa sahiptir çünkü en kötü durumda tüm liste taranmalıdır.
Veri aramaya head'den başlanır bü yüzden arama yapmak zordur.

"""
