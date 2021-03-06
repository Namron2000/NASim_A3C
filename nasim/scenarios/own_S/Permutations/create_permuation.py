from itertools import permutations

part_1= """
subnets: [4]
topology: [[1, 1],
           [1, 1]]
sensitive_hosts:
"""
part_2="""
os:
  - windows
services:
  - freeSSHd1.0.9
  - FTPShellClient6.70
  - postgreSQL9.3
  - phpFileManager0.9.8
  - https
processes:
  - none
exploits:
  e_freeSSHd1.0.9:
    service: freeSSHd1.0.9
    os: windows
    prob: 1
    cost: 3
    access: root
  e_FTPShellClient6.70:
    service: FTPShellClient6.70
    os: windows
    prob: 1
    cost: 3
    access: root
  e_postgreSQL9.3:
    service: postgreSQL9.3
    os: windows
    prob: 1
    cost: 3
    access: root
  e_phpFileManager0.9.8:
    service: phpFileManager0.9.8
    os: windows
    prob: 1
    cost: 3
    access: root
privilege_escalation:
  pe_none:
    process: none
    os: windows
    prob: 1.0
    cost: 1
    access: root
service_scan_cost: 1
os_scan_cost: 1
subnet_scan_cost: 1
process_scan_cost: 1
host_configurations:
"""
part_3 = """
firewall:
  (0, 1): [https, FTPShellClient6.70, postgreSQL9.3, phpFileManager0.9.8, freeSSHd1.0.9]
  (1, 0): [https, FTPShellClient6.70, postgreSQL9.3, phpFileManager0.9.8, freeSSHd1.0.9]
step_limit: 1000
"""

host_0 ="""
    os: windows
    services: [freeSSHd1.0.9]
    processes: []
"""

host_1 ="""
    os: windows
    services: [https]
    processes: []
"""

host_2 ="""
    os: windows
    services: [FTPShellClient6.70]
    processes: []
"""

host_3 ="""
    os: windows
    services: [postgreSQL9.3, phpFileManager0.9.8]
    processes: []
"""

switch = {
    0: host_0,
    1: host_1,
    2: host_2,
    3: host_3
}

if __name__ == "__main__":
    per = permutations([0, 1, 2, 3])
    for idx, elem in enumerate(per):
        with open("./nasim/scenarios/own_S/Permutations/Own_S_"+str(idx)+".yaml", "a") as file:
            file.write(part_1)
            for idx2, elem1 in enumerate(elem):
                if elem1 != 1:
                    file.write("  (1, " + str(idx2) + "): 100 \n")
            file.write(part_2)
            for idx2, elem1 in enumerate(elem):
                file.write("  (1, "+ str(idx2) +"):")
                file.write(switch.get(elem1))
            file.write(part_3)
