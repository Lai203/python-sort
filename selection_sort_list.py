#Andi memiliki sebuah daftar angka yang ingin diurutkan secara 
#ascending menggunakan Selection Sort. Berikut adalah daftar
#angka yang dimiliki Andi: [9,5,3,8,2]. Bantulah Andi untuk
#mengurutkan daftar angka tersebut menggunakan selection sort

def selection_sort(arr) :
    n = len(arr)
    for i in range(n-1) :
        min_index = i
        for j in range (i+1, n) :
            if arr[j] < arr[min_index] :
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
list_Andi = [9, 5, 3, 8, 2]
selection_sort(list_Andi)
print("Hasil Pengurutan : ", list_Andi)