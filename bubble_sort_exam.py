#Hannah adalah seorang siswa yang ingin mengurutkan daftar nilai
#ujian siswa di kelasnya secara ascending menggunakan bubble sort.
#Berikut adalah daftar nilai ujian siswa di kelas Hannah : [78, 65]
#90, 82, 70]. Bantulah Hannah untuk mengurutkan daftar nilai tersebut
#Menggunakan bubble Sort.

def bubble_sort(arr) :
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr [j+1]:
                arr [j], arr[j+1] = arr[j+1], arr[j]

List_Hannah = [78, 65, 90, 82, 70]
bubble_sort(List_Hannah)
print ("Hasil Pengurutan : ", List_Hannah)
