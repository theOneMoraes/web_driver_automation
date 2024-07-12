from multiprocessing import Process
import JustAnotherPanel
import TurboPainel
import GrammFama
import Measmm

def main():
    processes = []

    # Lista de scripts a serem executados
    scripts = [Measmm, TurboPainel, GrammFama, JustAnotherPanel]

    for script in scripts:
        p = Process(target=script.run_script)
        processes.append(p)
        p.start()

    # for p in processes:
    #     p.join()

if __name__ == '__main__':
    main()

