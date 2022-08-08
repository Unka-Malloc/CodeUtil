import subprocess


def start(self, cmd, cwd):
    return subprocess.Popen(
        cmd,
        shell=True,
        cwd=cwd,
        text=True,
        encoding='utf-8',
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)


def read(process: subprocess):
    output = []

    line = process.stdout.readline().strip()
    while line:
        output.append(line)
        line = process.stdout.readline().strip()

    return output


def write(process: subprocess, cmd: str):
    process.stdin.write(f"{cmd}\n")
    process.stdin.flush()


def terminate(process: subprocess):
    process.stdin.close()
    process.terminate()
    process.kill()
    process.wait(timeout=0.2)
