# Import-Socket
a Python program that scans for open ports on a hostname

ENG
This version of the script prompts the user to enter the hostname or IP address, and the starting and ending port numbers that they want to scan. It uses a try-except block to catch any errors that may occur during the connection attempt and instead of using connect_ex function. It uses the "sock.connect()" method to connect to the specified host and port, it check if the connection was successful. If it was successful, it means that the port is open, and it prints out the port number and hostname, then it closes the connection with shutdown method. It also saves the open ports on an empty list that defined as open_ports. After scanning all ports in the range, it prints out the list of open ports found on the host, or it prints a message saying that no open ports were found.

TR
Komut dosyasının bu sürümü, kullanıcıdan ana bilgisayar adını veya IP adresini ve taramak istedikleri başlangıç ve bitiş bağlantı noktası numaralarını girmesini ister. Bağlantı denemesi sırasında oluşabilecek hataları yakalamak için bir try-except bloğu kullanır ve connect_ex fonksiyonunu kullanmak yerine. Belirtilen ana bilgisayar ve porta bağlanmak için "sock.connect()" yöntemini kullanır, bağlantının başarılı olup olmadığını kontrol eder. Başarılı olduysa, portun açık olduğu anlamına gelir ve port numarasını ve ana bilgisayar adını yazdırır, ardından bağlantıyı shutdown yöntemiyle kapatır. Ayrıca açık portları open_ports olarak tanımlanmış boş bir listeye kaydeder. Aralıktaki tüm portları taradıktan sonra, ana bilgisayarda bulunan açık portların listesini yazdırır veya açık port bulunmadığını belirten bir mesaj yazdırır.
