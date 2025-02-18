import unam.fc.concurrent.practica6.FifoReadWriteLock;
import java.util.concurrent.locks.Lock;


public class TestFifoReadWriteLock {
    public static void main(String[] args) {
        FifoReadWriteLock lock = new FifoReadWriteLock();
        Lock readLock = lock.readLock();
        Lock writeLock = lock.writeLock();

        // Simular múltiples lectores
        for (int i = 0; i < 3; i++) {
            int readerId = i;
            new Thread(() -> {
                readLock.lock();
                try {
                    System.out.println("Reader " + readerId + " is reading.");
                    Thread.sleep(2000); // Simula la lectura
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    System.out.println("Reader " + readerId + " finished reading.");
                    readLock.unlock();
                }
            }).start();
        }

        // Simular un escritor
        new Thread(() -> {
            writeLock.lock();
            try {
                System.out.println("Writer is writing.");
                Thread.sleep(3000); // Simula la escritura
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                System.out.println("Writer finished writing.");
                writeLock.unlock();
            }
        }).start();
    }
}
