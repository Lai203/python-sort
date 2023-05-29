#Berdasarkan statistik sepak bola musim 2022/2023, terdapat
#daftar pemain yang perlu diurutkan berdasarkan jumlah gol
#yang dicetak secara descending menggunakan selection sort
#Setiap pemain memiliki informasi berikut : Nama Pemain, Klub
#Pemain, dan jumlah gol yang dicetak. Buatlah untuk mengurutkan
#daftar pemain berdasarkan jumlah gol yang dicetak secara descending
#menggunakan selection sort.

def selection_sort(arr) :
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j][2] > arr [min_index][2]:
                min_index = j
        arr [i], arr[min_index] = arr[min_index], arr[i]

list_bola = [ ["Kylian Mbappe", "Paris Saint Germain", 40], 
        ["Victor Osimhen", "Napoli", 28], 
        ["Robert Lewandowski", "Barcelona", 33], 
        ["Erling Haaland", "Manchester City", 52],
        ["Christopher Nkunku", "RB Leipzig", 22]]

selection_sort(list_bola)
print ("Hasil Pengurutan : ", list_bola)
