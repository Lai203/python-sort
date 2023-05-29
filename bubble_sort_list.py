#Ahmad ingin mengurutkan daftar angka secara descending menggunakan
#Bubble sort. Berikut adalah daftar angka yang ingin diurutkan : 
#[42, 19, 33, 8, 55]. Bantulah Ahmad untuk mengurutkan daftar angka
#tersebut secara descending menggunakan bubble sort

def bubble_sort(arr) :
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr [j+1]:
                arr [j], arr[j+1] = arr[j+1], arr[j]

List_Ahmad = [42, 19, 33, 8, 55]
bubble_sort(List_Ahmad)
print ("Hasil Pengurutan : ", List_Ahmad)
