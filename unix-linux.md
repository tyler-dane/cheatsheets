# Unix/Linux Cheatsheet
A list of Unix/Linux commands that I find useful
- I develop primarily on OSX and RedHat 7 systems, so a number of these commands will be specific to those environments
- some  commands rely on non-default packages
- command syntax assumes user has root access
- commands listed in alphabetical order
- @author Ty Hitzeman

`awk`
- language for manipulation of files
    - `awk '{i=0;while(i++<2){gsub(/,,/,",0,");gsub(/ /, "")}}1' input-test.csv > new-input.csv`
        - takes empty fields from input-test.csv and saves as new-input.csv

`blkid -o list`
-  complete list of the partition's UUIDs

`cat /proc/meminfo`
- show memory info

`curl ifconfig.me`
- get public IP address

`df -khTi`
- shows block size, files system, human format, inode usage

`dig`
- DNS lookup utility
- `dig -x <address>`
    - maps addresses to names (reverse lookups)

`du -hs * | sort -rh | head -5`
- show 5 biggest files

`echo $?`
- get status code (0/1) of previous command
- 0 = no errors, 1 = error

`firewall-cmd`
- `firewall-cmd --list-ports`
    - lists port information
- `firewall-cmd --list-services`
    - lists firewall services information
- `firewall-cmd --permanent --add-service=https`
    - open the https service
- `firewall-cmd --zone=public --add-port=<port #>/tcp --permanent`
    - open single port and reload firewall
    - run `firewall-cmd --reload` after to apply change
- `firewall-cmd --zone=public --add-port=<beginning port #>-<end port #>/<tcp/udp>`
    - sequentially open ports
    - run `firewall-cmd --reload` after to apply change

`find`
- `find / -type d -name <dirname>`
    - find directories
- `find ./ -name *.egg-info -exec sudo rm -r {} \;`
    - find and delete files

`grep -rnw '/path/to/somewhere/' -e 'keywords-to-search-for'`
- find files with specific string / character matches (within the file)

`head`
- output the first part of files

```
head -1 file1.csv > final.csv
for filename in $(ls file*.csv); do sed 1d $filename >> final.csv; done
```
- combine CSVs:

`for filename in $(ls *.csv); do sed 1d $filename >> newfile.csv; done`
`head -1 file.csv | sed 's/[^,]//g' | wc -c`
- get number of columns in CSV: 
    
`hostnamectl`
- control the system hostname
    - `hostnamectl status`
        - shows currenty system hostname and related information
    - `hostnamectl set-hostname <hostname>`
        - sets hostname for all three classes of hostnames

`locate <path to file>`
- find files (much faster than `find`)

`ldd <path/to/binary`
- lists shared object dependencies required for a binary

`ln`
- make links between files
    - `ln -sf <TARGET> <CURRENT>`
        - creates soft link from current to target
        - EX: `ln -sf /opt/bacula/bin/bconsole /usr/sbin/bconsole`
            - points /usr/sbin/bconsole to /opt/bacula/bin/bconsole

`ls`
- `ls /sys/firmware`
    - Check if your system uses UEFI or BIOS. If `/efi` isn’t there, it uses BIOS
- `ls -l [Vv]*`
    - search for directories starting with 'V' or 'v'
- `ls -t`
    - orders list by most recently modified at top

`mount`
- mount a file system
    - mount -t ntfs-3g /dev/sdb1 /mnt/drive/
        - mounts a NTFS device (`/dev/sdb`) to `/mnt/drive`

`nmap <domain>.*`
- lists active ports
- Ex: `nmap 192.168.30.*` 

`nmcli`
- CLI for network manager
- `nmcli dev`
    - Check status of network devices
- `nmcli n <on/off>`
    - turn network on/off

`nslookup <ip address>`
- reverse DNS lookup

`pssh`
- execute commands  on multiple systems via SSH
    - `pssh -vAi -h ~/.pssh_host_files <command>`
        - runs <command>, prompting for password
        - be sure to create host file with system addresses and usernames

`rsync`
- a remote (and local) file-copying tool

`runuser`
- run a command with substitute user and group ID
    - Ex: `runuser -l tyler -c 'whoami'`

`sed`
- stream editor for filtering and transforming text
    - ex 1 - change https to http in file:
        - `sed -i 's/https/http/g' /etc/yum.repos.d/epel.repo`
    - ex 2 - change ‘log_level: info’ to ‘log_level: debug’
        - `sed -i -e 's/log_level: error/log_level: debug/ /etc/swoop/common/swoop/configuration/swoop.yaml`
    - ex 3 - change line 565 and print out the line after
        - `sed -i -e '565s/active: false/active: true/' sed.yaml &&  sed -n 565p sed.yaml`

`screen`
- screen manager with VT100/ANSI terminal emulation
    - `screen -r` to reattach

`sar`
- The system activity data collector, sadc, collects and stores performance information over time.
- The data collection may not be enabled by default. Creating a file /etc/cron.d/sysstat allows crontab to manage the collection of this data.
```
# Run system activity accounting tool every 10 minutes 
*/10 * * * * root /usr/lib64/sa/sa1 -S DISK 1 1 
# 0 * * * * root /usr/lib64/sa/sa1 -S DISK 600 6 & 
# Generate a daily summary of process accounting at 23:53 
53 23 * * * root /usr/lib64/sa/sa2 -A 
```

`systemctl`
 - `systemctl list-unit-files`
    - list systemd services

`telnet <address> <port>`
- communicate with another host using the TELNET protocol

`who is`
- show who is logged in
- `who is <ip address>`
    - get hostname/domain