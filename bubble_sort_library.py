#Di suatu perpustakaan ,terdapat daftar buku yang perlu diurutkan 
#berdasarkan jumlah halaman secara ascending menggunakan Bubble Sort.
#Setiap buku memiliki informasi berikut : judul buku, penulis, dan jumlah halaman.
#Bantulah perpustakaan tersebut mengurutkan daftar buku berdasarkan jumlah
#halaman secara ascending menggunakan bubble sort

def bubble_sort(arr) :
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j][2] > arr [j+1][2]:
                arr [j], arr[j+1] = arr[j+1], arr[j]

buku_perpus = [ ["Harry Potter and the Sorcerer's Stone", "J.K Rowling", 320],
        ["To Kill a Mockingbird", "Harper Lee", 281],
        ["The Great Gatsby", "F. Scott Fitzgerald", 180],
        ["Pride and Prejudice", "Jane Austen", 432],
        ["1984", "George Orwell", 328]]

bubble_sort(buku_perpus)
print ("Hasil Pengurutan : ", buku_perpus)
