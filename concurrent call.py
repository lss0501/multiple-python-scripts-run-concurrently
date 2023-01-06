import multiprocessing
import os

OutPutPath = os.getcwd()


def run_script(script_name):
    os.system('python "%s/%s"'%(OutPutPath,script_name))


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=run_script, args=('concurrent_run1.py',))
    p2 = multiprocessing.Process(target=run_script, args=('concurrent_run2.py',))
    p3 = multiprocessing.Process(target=run_script, args=('concurrent_run3.py',))
    p4 = multiprocessing.Process(target=run_script, args=('concurrent_run4.py',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

