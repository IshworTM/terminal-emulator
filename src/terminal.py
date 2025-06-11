import os
import shlex
import subprocess
from subprocess import CompletedProcess


class CustomTerminal:

    def __init__(self):
        self.ALLOWED_COMMANDS = {
            "ls": self.cmd_ls,
            "cd": self.cmd_cd,
            "pwd": self.cmd_pwd,
            "echo": self.cmd_echo,
            "cat": self.cmd_cat,
            "mkdir": self.cmd_mkdir,
            "rmdir": self.cmd_rmdir,
            "rm": self.cmd_rm,
            "touch": self.cmd_touch,
            "clear": self.cmd_clear,
            "ping": self.cmd_ping,
            "exit": self.cmd_exit,
            "nano": self.cmd_nano,
            "sl": self.cmd_sl,
        }

    def cmd_sl(self, args):
        """
        A fun command that simulates a train running across the terminal.
        """
        res = self.execute_subprocess_command(cmd="sl", args=args, check=True)
        return True if res else False

    def cmd_cd(self, args):
        if not args:
            print("[cd] -> missing operand")
            return
        try:
            os.chdir(args[0])
        except Exception as e:
            print(f"cd: {e}")

    def cmd_ls(self, args):
        subprocess.run(["ls", *args], check=True)

    def cmd_exit(self, args):
        print("Exiting...")
        exit(0)

    def cmd_pwd(self, args):
        try:
            print(f"Current Directory -> {os.getcwd()}")
        except Exception as e:
            print(f"[pwd] -> {e}")

    def cmd_echo(self, args):
        print(" ".join(args))

    def cmd_cat(self, args):
        subprocess.run(["cat", *args], check=True)

    def cmd_mkdir(self, args):
        os.makedirs(args[0], exist_ok=True)
        print(f"Directory '{args[0]}' created successfully.")

    def cmd_rmdir(self, args):
        if not args:
            print("[rmdir] -> missing directory name")
            return
        dir_path = os.path.join(os.getcwd(), args[0])
        if not os.path.isdir(dir_path):
            print(f"[rmdir] -> '{args[0]}' is not a valid directory or does not exist.")
            return
        try:
            if os.getcwd() == os.path.abspath(dir_path):
                os.chdir("..")
                print(f"Changed directory to parent before removing '{args[0]}'.")
            os.rmdir(dir_path)
            print(f"Directory '{args[0]}' removed successfully.")
        except OSError as e:
            print(f"[rmdir] -> {e.strerror}: '{args[0]}'")

    def cmd_rm(self, args):
        if not args:
            print("[rm] -> missing operand.")
            return False

        flags, parsed_args = self.parse_flags_and_args(args)

        if not parsed_args:
            print("[rm] -> missing target to remove.")
            return False

        res = self.execute_subprocess_command(
            cmd="rm",
            args=[*flags, *parsed_args],
            capture_output=True,
            text=True,
            check=True,
        )
        if not res:
            return False
        print(f"Removed: {', '.join(parsed_args)}")
        return True

    def cmd_touch(self, args):
        if not args:
            print("[touch] -> missing file name")
            return False

        flags, targets = self.parse_flags_and_args(args)

        if not targets:
            print("[touch] -> missing target file name")
            return False

        success = True

        for target in targets:
            try:
                if "-c" in flags:
                    if os.path.exists(target):
                        os.utime(target, None)
                    else:
                        print(f"[touch] -> '{target}' does not exist.")
                        success = False
                else:
                    with open(target, "a"):
                        os.utime(target, None)
            except Exception as e:
                print(f"[touch] -> error with target: '{target}': {e}")
                success = False
        return success

    def cmd_clear(self, args):
        os.system("clear" if os.name != "nt" else "cls")

    def cmd_ping(self, args):
        if not args:
            print("[ping] -> missing destination address")
            return False
        res = self.execute_subprocess_command(
            cmd="ping", args=args, capture_output=True, text=True, check=True
        )
        return True if res else False

    def cmd_nano(self, args):
        res = self.execute_subprocess_command(cmd="nano", args=args, check=True)
        return True if res else False

    @staticmethod
    def parse_flags_and_args(args):
        """
        Parses flags and arguments from a list of command line arguments.
        Returns a tuple of flags and args.
        """
        flags = []
        parsed_args = []
        for arg in args:
            if arg.startswith("-"):
                flags.append(arg)
            else:
                parsed_args.append(arg)
        return flags, parsed_args

    @staticmethod
    def execute_subprocess_command(
        cmd: str,
        args,
        capture_output: bool = False,
        text: bool = False,
        check: bool = False,
    ) -> subprocess.CompletedProcess[str] | bool:
        try:
            result = subprocess.run(
                [cmd, *args], capture_output=capture_output, text=text, check=check
            )
            return result
        except subprocess.CalledProcessError as e:
            print(f"[{cmd}] -> {e.stderr}")
            return False
        except FileNotFoundError:
            print("[{cmd}] -> command not found. Please ensure it's installed.")
            return False
        except Exception as e:
            print(f"[{cmd}] -> unexpected error: {e}")
            return False

    @staticmethod
    def extract_command(cmd):
        return shlex.split(cmd) if cmd else []

    def shell(self):
        """
        This function runs a shell command and returns the output.
        """
        while True:
            cwd = os.getcwd()
            uname = os.uname().nodename
            command = input(f"@{uname}:{cwd}$  ")
            if not command:
                continue

            parts = self.extract_command(command)

            if not parts:
                continue

            cmd, *cmd_args = parts

            if cmd not in self.ALLOWED_COMMANDS:
                print(
                    f"[Error] -> '{cmd}' either doesn't exist or is disallowed in this environment."
                )
                continue

            try:
                self.ALLOWED_COMMANDS[cmd](cmd_args)
            except Exception as e:
                print(f"Error while running the command {cmd}:\n>> {e}")
                continue


def main():
    CustomTerminal().shell()


if __name__ == "__main__":
    main()
