import subprocess

def start_mitm_proxy():
    subprocess.Popen(
        ["mitmweb", "-s", "lib/mitm/addons/log_requests.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        bufsize=1
    )
