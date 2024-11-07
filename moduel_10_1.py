import threading
import time



def write_words(world_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for word in range(1, world_count + 1):
            f.write(f'Какое-то слово № {word}\n')
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")



thread1 = threading.Thread(target=write_words, args=(10, 'example1.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example2.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example3.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example4.txt'))
started_time = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time = time.time()
elapsed_time = round(end_time - started_time)
print(f'Работа потоков заняла: {elapsed_time} секунд')