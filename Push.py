from functools import partial
import multiprocessing as mp
import time
# import iplist.txt

class Switch:
  def __init__(self, user, password, version, status, ssh_token):
    self.user = 'admin'
    self.password = 'password'
    self.version = version
    self.status = status
    self.ssh_token = ssh_token

  def update(self, version_to_update):
    commands = pointer[version_to_update]
    execute(commands)
    self.version = version_to_update

class Task:
  def __init__(self, switch, operations):
    self.switch = switch
    self.operations = operations
  
  def run(self):
    while self.switch.version < expected_version:
      self.switch.update(self.switch.version + 1)

    print(task.switch.user)

def task_runner(task):
  task.run()
  time.sleep(5)

version = [1,2,3,4,5]
pointers = ['download software 192.111.111.1 /switches/usr/chance/firmware/2',
'download software 192.111.111.1 /switches/usr/chance/firmware/3',
'download software 192.111.111.1 /switches/usr/chance/firmware/4',
'download software 192.111.111.1 /switches/usr/chance/firmware/5',
]
switches = ["a","b","c","d","e", "f"]

commands = {
  0: ['ls', 'sudo rm -rf /']
}



tasks = [
  Task(Switch("root", "1234", "1.0.0", "", ""), []),
  Task(Switch("root", "1234", "1.0.0", "", ""), []),
  Task(Switch("root", "1234", "1.0.0", "", ""), []),
  Task(Switch("root", "1234", "1.0.0", "", ""), []),
  Task(Switch("root", "1234", "1.0.0", "", ""), []),
  Task(Switch("root", "1234", "1.0.0", "", ""), []),
  Task(Switch("root", "1234", "1.0.0", "", ""), [])
]

def something(host):
  print(host)
  time.sleep(5)

def main():
  number_of_workers = 3
  pool = mp.Pool(number_of_workers)
  results = pool.map(something, switches)
  pool.close()
  pool.join()
  
main()
