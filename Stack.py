class stack:
    def __init__(self):
        self.stack = []  # Bağlı liste olarak kullanılacak liste oluşturulur

    # Eleman ekleme işlemi
    def push(self, item):
        self.stack.append(item)

    # Eleman çıkarma işlemi
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    # Eleman arama işlemi
    def peek(self):
        return self.stack[-1]

    # stack'in boş olup olmadığını kontrol eder
    def is_empty(self):
        return len(self.stack) == 0


# stack'i my_stack'e atama yaparız çünkü stack iki parametrelidir.
# Atama sayesinde sadece bir parametre üstünde işlem yaparız.
my_stack = stack()

# stack'e veri ekler
my_stack.push(10)
my_stack.push(20)

# stack'in en üstündeki veriyi siler ve çıktı olarak sildiği veri değerini verir.
print(my_stack.pop())  # 20

# stack'in en üstünde bulunan veri değerini çıktı olarak verir.
print(my_stack.peek())  # 10


"""
Stack, dinamik veri yapılarından biridir ve LIFO (Last In First Out - Son Giren İlk Çıkar) prensibine göre çalışır.
Bu, stack’e eklenen son öğenin, çıkarılan ilk öğe olacağı anlamına gelir.
Stack'te serbestçe gezilemez ve arama işlemi yapmak zordur. 
Stack’ler, bir dizi uygulamada kullanılır. Örneğin, bir programın fonksiyon çağrılarını takip etmek için kullanılır. 
Bir fonksiyon çağrıldığında, çağrının detayları bir stack’e “push” edilir ve fonksiyon tamamlandığında,
bu detaylar stack’ten “pop” edilir. Bu, programın hangi fonksiyonun sıradaki olduğunu bilmesini sağlar.
Stack, özellikle veri manipülasyonu sırasında kullanışlı bir veri yapısıdır ve pek çok algoritma 
ve problemin çözümünde temel bir rol oynar.

Metodlar;

Push: Bu metod, yığına bir eleman eklemek için kullanılır. Eklenen eleman yığının en üstüne (yani sonuna) yerleştirilir.
Stack'e bir eleman eklemek O(1) karmaşıklığa sahiptir. 

Pop: Bu metod, yığının en üstündeki (yani son) elemanı çıkarmak için kullanılır.
Yığın boşsa, bu işlem genellikle bir hata verir veya özel bir değer döndürür.
Stack'ten bir eleman silmek O(1) karmaşıklığa sahiptir.

Is_Empty: Bu metod, yığının boş olup olmadığını kontrol etmek için kullanılır. Yığın boşsa True, değilse False döndürür.

Search(Arama): Stack'te bir elemanı aramak O(n) karmaşıklığa sahiptir çünkü en kötü durumda tüm yığın taranmalıdır.

Bu metodlar, yığın veri yapısının temel işlemleridir ve yığınların “Son Giren İlk Çıkar” 
(LIFO - Last In First Out) prensibine göre çalışmasını sağlar.

LIFO (Last In, First Out);

LIFO (Last In, First Out) prensibi, bir veri yapısının elemanlarının nasıl eklenip çıkarılacağını belirler. 
LIFO prensibine göre, en son eklenen eleman ilk çıkarılır.
Bu prensip, stack gibi veri yapılarında kullanılır.

Bir örnekle açıklamak gerekirse, bir kitap yığını düşünelim. Kitapları yığının en üstüne ekliyoruz (push işlemi) 
ve bir kitap almak istediğimizde yığının en üstündeki kitabı alıyoruz (pop işlemi). Bu durumda, en son eklenen kitap 
(yani en üstteki kitap) ilk çıkarılan kitap olur. İşte bu, LIFO prensibinin bir örneğidir.

Bu prensip, birçok algoritma ve veri yapısında kullanılır. Örneğin, bir programın çağrı yığını (call stack), 
bir fonksiyon çağrıldığında yeni bir çerçeve (frame) ekler ve fonksiyon tamamlandığında bu çerçeveyi çıkarır. 
Bu, LIFO prensibine göre çalışır çünkü en son eklenen çerçeve (yani en son çağrılan fonksiyon) ilk çıkarılır. 
Aynı şekilde, derinlik öncelikli arama (DFS - Depth First Search) algoritması da LIFO prensibini kullanır. 
DFS, bir düğümü ziyaret ettiğinde, tüm komşularını bir yığına ekler ve daha sonra yığının en üstündeki 
(yani en son eklenen) düğümü ziyaret eder. Bu, DFS’nin bir ağacın veya grafiğin derinliklerine öncelik vermesini sağlar.


"""
