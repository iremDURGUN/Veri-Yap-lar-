# Bağlı liste olarak kullanılacak liste oluşturulur
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Eleman ekleme işlemi
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # Eleman çıkarma işlemi
    def dequeue(self):
        if not self.is_empty():
            popped_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return popped_item
        else:
            return None

    # stack'in boş olup olmadığını kontrol eder
    def is_empty(self):
        return self.front is None


# Queue'yu my_queue'ya atama yaparız çünkü queue iki parametrelidir.
# Atama sayesinde sadece bir parametre üstünde işlem yaparız.
my_queue = Queue()

# queue'ya veri ekler
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# queue'nun dequeue işlemini yaptığı veri değerini çıktı olarak verir.
print(my_queue.dequeue())  # 10

"""
Bir queue (kuyruk), verilerin eklenip çıkarıldığı, ilk eklenen elemanın ilk çıkarıldığı (FIFO - First In, First Out) 
ve dinamik bir veri yapısıdır. Queue, bir düzen içinde sıralı olarak gelen verileri işlemek için kullanılır. 
Queue, genellikle işlemlerin belirli bir sıra ile gerçekleştirilmesi gerektiği durumlarda kullanılır.
Kaç elemanlı olduğu bilinmez. 
Örneğin, işlem sırasını bekleyen verileri sırayla işlemek veya verilerin sırasıyla işlenmesi gereken 
bir işlem kuyruğu yönetmek için kullanılabilir. 
Queue, çeşitli uygulamalarda ve algoritmaların implementasyonunda yaygın olarak kullanılan önemli bir veri yapısıdır.

Metodlar;

Enqueue: Bu metod, kuyruğa bir eleman eklemek için kullanılır. Eklenen eleman kuyruğun sonuna yerleştirilir.
Queue'ya bir eleman eklemek O(1) karmaşıklığa sahiptir.

Dequeue: Bu metod, kuyruğun başındaki (yani ilk) elemanı çıkarmak için kullanılır. 
Kuyruk boşsa, bu işlem genellikle bir hata verir veya özel bir değer döndürür.
Queue'dan bir eleman silmek O(1) karmaşıklığa sahiptir.

Is_Empty: Bu metod, kuyruğun boş olup olmadığını kontrol etmek için kullanılır. 
Kuyruk boşsa True, değilse False döndürür.

Search(Arama): Queue'da bir elemanı aramak O(n) karmaşıklığa sahiptir çünkü en kötü durumda tüm kuyruk taranmalıdır.

FIFO - First In First Out:

Bu metodlar, Queue veri yapısının temel işlemleridir ve kuyrukların “İlk Giren İlk Çıkar” (FIFO - First In First Out) 
prensibine göre çalışmasını sağlar.

FIFO (First In, First Out) prensibi, bir veri yapısının elemanlarının nasıl eklenip çıkarılacağını belirler. 
FIFO prensibine göre, ilk eklenen eleman ilk çıkarılır. Bu prensip, bir kuyruk (queue) gibi veri yapılarında kullanılır.

Bir örnekle açıklamak gerekirse, bir süpermarket kuyruğunu düşünelim. 
Müşteriler kuyruğun sonuna eklenir (enqueue işlemi) ve kasadaki görevli, kuyruğun başındaki (yani ilk gelen) 
müşteriye hizmet eder (dequeue işlemi). Bu durumda, ilk gelen müşteri (yani ilk eklenen) ilk hizmet alır. 
İşte bu, FIFO prensibinin bir örneğidir.

Bu prensip, birçok algoritma ve veri yapısında kullanılır. Örneğin, bir işletim sisteminin iş planlama (scheduling)
algoritmaları, genellikle FIFO prensibini kullanır. İşler, işlemciye ilk gelen ilk işlenir prensibiyle sıraya alınır. 
Aynı şekilde, genişlik öncelikli arama (BFS - Breadth First Search) algoritması da FIFO prensibini kullanır. 
BFS, bir düğümü ziyaret ettiğinde, tüm komşularını bir kuyruğa ekler ve daha sonra kuyruğun başındaki 
(yani ilk eklenen) düğümü ziyaret eder. Bu, BFS’nin bir ağacın veya grafiğin genişliklerine öncelik vermesini sağlar.
Bu nedenle, hangi veri yapısının kullanılacağına karar verirken, uygulamanın gereksinimlerini dikkate almak önemlidir.
"""
