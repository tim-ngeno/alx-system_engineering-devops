# 0x05-Processes and Signals
# Process
A process is a running instance of a program. When a process is created, a unique identifier gets assigned to it.

These Identifiers are called `PID`s and `PPID`s.

PIDs and PPIDs can be used to manage processes running on your system

## 1.PID
A PID, 'process ID', is the identifier that gets attached to your program when it starts running. They can be useful for interacting with the process.

## 2.PPID
A PPID, 'parent process ID', is simply the parent ID of the process ID.

It is given to the process that 'created' the process you're currently checking.

# Finding the PID and PPID
## PID
1. `pidof`
If you know the exact name of a process, you can use the `pidof` command to get its PID

example: 

`pidof chrome`: retrieves the PID of running chrome process(es)

2. `psgrep`
A combination of `ps` and `grep` to retrieve the PID of specified process name

- `psgrep partial_or_exact_process_name`
This is a more useful tool if you don't know the exact name of the process.
You can use `psgrep` with the `-l` flag to add list names to PIDs(if there is more than one match with the command)

3. `$$`
This returns the PID of your current process. Use `echo "$$"` to display the PID.

## PPID
1. `${PPID}`
Use the above command to get the parent ID of your child process
`echo "${PPID}"`

2. `ps -o ppid= -p <PID>`
The above command can be used if you know the PID of the current process

# Signals
A signal is an event generated by the UNIX/Linux systems in response to some condition
## Types of Signals
- Maskable: signals which can be modified or ignored (e.g. Ctrl+C)
- Non-Maskable: cannot be modified or ignored by user.

The two signals that cannot be intercepted and handled by user are `SIGKILL` and `SIGSTOP`. They are handled by the kernel, they are used to kill unresponsive tasks(apps)