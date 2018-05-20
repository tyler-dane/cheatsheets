# Unix/Linux Cheatsheet
A list of Unix/Linux commands that I find useful
- I develop primarily on OSX and RedHat 7 systems, so a number of these commands will be specific to those environments
- some  commands rely on non-default packages
- command syntax assumes user has root access
- commands listed in alphabetical order
- Author: [Ty Hitzeman](https://github.com/tyler-hitzeman)

`awk`
- language for manipulation of files
    - `awk '{i=0;while(i++<2){gsub(/,,/,",0,");gsub(/ /, "")}}1' input-test.csv > new-input.csv`
        - takes empty fields from input-test.csv and saves as new-input.csv

`blkid -o list`
-  complete list of the partition's UUIDs

`cat`
- concatenate and print files
    - `cat /etc/redhat-release` or `cat /etc/centos-release`
        - get version info
    - `cat /proc/meminfo`
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

`screen`
- screen manager with VT100/ANSI terminal emulation
    - `screen -r` to reattach

`sed`
- stream editor for filtering and transforming text
    - ex 1 - change https to http in file:
        - `sed -i 's/https/http/g' /etc/yum.repos.d/epel.repo`
    - ex 2 - change ‘log_level: info’ to ‘log_level: debug’
        - `sed -i -e 's/log_level: error/log_level: debug/ /etc/app/common/app/configuration/app.yaml`
    - ex 3 - change line 565 and print out the line after
        - `sed -i -e '565s/active: false/active: true/' sed.yaml &&  sed -n 565p sed.yaml`

`split`
- split a file into pieces
    - ex - split 1GB file in two 500MB files:
    ```
    wc -l 1GB.csv (output: 2212463)
    myvar=$(expr 2212463 / 2)
    echo $myvar
    split -l $myvar 1GB.csv
    ```

`ssh`
- log in to a remote machine and execute commands
    - ex 1 - simple login: `ssh ty@192.168.30.120`
    - ex 2 - login and execute a series of arbitrary commands:
        ```
        for HOSTNAME in ${HOSTS} ; do
        ssh -t -l ${USERNAME} ${HOSTS} '
        read -p "Enter Build URL: " BUILD_URL;
        sudo su << HERE
        curl -o app.rpm -k $BUILD_URL
        rpm -i app.rpm
        echo "done"
        HERE'

        done
        ```
    - ex 3 - add local SSH key to remote server
    ```
    cd /home/ty
    cat .ssh/id_rsa.pub | ssh root@192.168.30.120 'cat >> .ssh/authorized_keys'
    ```
`ssh-keygen`
- generate, manage and convert authentication keys for ssh

`strace`
- trace system calls and signals
- useful for debugging on Linux 

`subscription-manager`
- register machines and manage subscriptions to RedHat products.
- `subscription-manager register --username=user@company.com --password=annakai1 --force && subscription-manager attach --auto`
    - register machine and attach subscription

`systemctl`
- control the systemd system and service manager
    - `systemctl list-unit-files`
        - list systemd services
    - `systemctl list-dependencies --all <app>`
        - lists dependencies
    - `systemctl start <service>`
        - start a service
    - `systemctl status <service>`
        - check status of a service
    `systemctl reload <service>`
        - reload a service
    `systemctl enable <service>`
        - enable a service (make it run on boot):

`tar`
- create and manipulate streaming archive files
    - ` tar -xvzf /file/to/untar.tar`
        - untar a file

`tcpdump`
- prints out a description of the contents of packets on a network interface
- useful in conjunction with WireShark
- `tcpdump -n -ttt -i any -w /home/ty/server1-server2.pcap`

`telnet <address> <port>`
- communicate with another host using the TELNET protocol

`timedatectl`
- query and change the system clock and its settings
- `timedatectl set-timezone America/Chicago`
    - set timezone to America/Chicago

`touch`
- set the modification and access times of files
- `touch /home/ty/test.txt`
    - creates empty txt file
- `touch -mt 0711171533 tests`
    - Changes atime and mtime of a file to 2007, Nov, 17th, 15:33

`unzip`
- list, test and extract compressed files in a ZIP archiv
    - `unzip <path/to/zip> <destination>`

`wc`
- word, line, character, and byte count
    - `wc -l <file>`
        - prints the number of lines in a file

`wget`
- non-interactive download of files from the Web
    - `wget -O- https://sourceforge.net/projects/bacula/files/bacula/9.0.1/bacula-regress-9.0.1.tar.gz/download | tar -xzvf - -C /usr/src` 
        - download a .tar and unzip to to the `/usr/src` directory
        - ‘O’ flag specifies that its a file to download
`who is`
- show who is logged in
- `who is <ip address>`
    - get hostname/domain

`xbindkeys`
- grab keys and mouse button events in X and starts associated shell command.

- `xbindkeys -f ~/.xbindkeysrc`
    - start xbindkeys daemon

    ```
    killall -s1 xbindkeys
    killall xbindkeys; xbindkeys
    killall -HUP xbindkeys
    ```

- restart xbindkeys
- references
    - https://www.linux.com/news/start-programs-pro-xbindkeys
    - http://butlerpc.net/blog/2011/01/using-xbindkeys-on-ubuntu-linux-to-remap-key-commands/
    - http://xahlee.info/linux/linux_xbindkeys_tutorial.html
    - http://dev-random.net/make-your-own-keybindings-in-linux-using-xbindkeys/


`yum`
- an interactive, rpm based, package manager
    - `yum history | yum history undo {#}`
        - undo a yum operation 
    - `yum update --exclude=pam* --skip-broken`
        - excludes any pam packages and skips any other broken dependencies (e.g. ipa)
    - `yum repolist`
    - `yum check-update`
        - shows updates without going into interactive mode
    - `yum provides`
        - shows which package provides some feature or file. Just use a specific name or a file-glob-syntax wildcare to list packages. Ex:
        - `yum provides /usr/sbin/semanage`
        - lists the package you’ll need to get semanage: policycoreutils-python-2.5-8.el7.x86_64

`zip`
- zip the logs.log file as a .zip
    - `zip heapdump1.zip biglogfile.log`

