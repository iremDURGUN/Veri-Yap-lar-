# Dictionary oluşturulur
dictionary = {
    'anahtar1': 'değer1',
    'anahtar2': 'değer2',
    'anahtar3': 'değer3'
}

# Dictionary'de anahtar1'in değerini çıktı olarak verir.
print(dictionary['anahtar1'])  # çıktı: 'değer1'

# Dictionary'e yeni eleman ekleme işlemi
dictionary['yeni_anahtar'] = 'yeni_değer'
print(dictionary)  # çıktı: {'yeni_anahtar': 'yeni_değer'}

# Dictionary'den veri silme işlemi
del dictionary['anahtar1']
print(dictionary)  # çıktı: {'anahtar2': 'değer2'}

# Dictionary'de verinin var olup olmadığını tespit etmek.
# Bunu in dictionary kalıbıylada __contains__ kalıbıylada yapabiliriz.
print('anahtar1' in dictionary)  # çıktı: False
print('anahtar3' in dictionary)  # çıktı: True
print(dictionary.__contains__("anahtar1"))  # çıktı: False

"""
Python’da, bir dictionary, anahtar-değer çiftlerini saklayan ve dinamik bir veri yapısıdır. Her anahtar benzersizdir 
ve bir değere karşılık gelir. Dictionary’ler, {} işaretleri arasında tanımlanır ve anahtar-değer çiftleri : ile ayrılır.
Python’daki dictionary’ler, hash tabloları olarak uygulanır. Bu, anahtar-değer çiftleri sayesinde anahtarlar üzerinden değerlere hızlıca erişebiliriz.
Ayrıca, dictionary’lerdeki öğeleri eklemek, silmek ve güncellemek de oldukça kolaydır.
Dictionary’lerdeki anahtarlar ve değerler her veri türünden olabilir. Anahtarlar genellikle string veya sayı tipinde olur.

Dictionary' e veri ekleme işlemi yapılırken anahtar(key)' ın benzersiz olması eklenme yapıldığında
eğer ki aynı anahtar değeri dictionary' de içeriyorsa size uyarı vermeksizin o veriyi eklemez. 
Çünkü anahtarın benzersiz yapıda olması veri tekrarının oluşmasını engeller.

Metodlar;

Veri Ekleme: Dictionary’ye yeni bir anahtar-değer çifti eklemek için, yeni anahtarı köşeli parantez içine alır 
ve değeri atarız. Bir anahtar-değer çiftini dictionary’ye eklemek genellikle O(1) zaman karmaşıklığına sahiptir. 
Yani, bu işlem çok hızlı gerçekleştirilir ve dictionary’nin boyutuna bağlı değildir.

Veri Silme: Dictionary’den bir anahtar-değer çifti silmek için del anahtar kelimesini kullanırız.
Bir anahtar-değer çiftini dictionary’den silmek genellikle O(1) zaman karmaşıklığına sahiptir. 
Yani, bu işlem çok hızlı gerçekleştirilir ve dictionary’nin boyutuna bağlı değildir.

Veri Arama: Dictionary’de bir anahtarın olup olmadığını kontrol etmek için in anahtar kelimesini kullanırız.
Bir anahtarı dictionary’de aramak da genellikle O(1) zaman karmaşıklığına sahiptir. 
Yani, bu işlem çok hızlı gerçekleştirilir ve dictionary’nin boyutuna bağlı değildir.

Ancak, bu karmaşıklıklar ideal durumları ifade eder ve bazı durumlarda (örneğin, hash çakışmaları durumunda) 
daha yüksek olabilir. Ayrıca, dictionary’nin boyutunu değiştirme işlemi O(n) zaman karmaşıklığına sahip olabilir, 
burada n dictionary’deki veri sayısıdır. Ancak bu genellikle ihmal edilir.
"""
