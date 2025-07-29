import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports():
    target_ip = ip_entry.get()
    try:
        start = int(start_port.get())
        end = int(end_port.get())
    except ValueError:
        messagebox.showerror("Input Error", "Ports must be numbers")
        return

    open_ports = []
    output_text.delete("1.0", tk.END)  # Clear previous output

    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            msg = f"[OPEN] Port {port}\n"
            open_ports.append(msg)
            output_text.insert(tk.END, msg)
        sock.close()

    # Save to scan_report.txt
    if open_ports:
        with open("scan_report.txt", "w") as f:
            f.writelines(open_ports)
        messagebox.showinfo("Scan Complete", "Open ports saved to scan_report.txt")
    else:
        with open("scan_report.txt", "w") as f:
            f.write("No open ports found.")
        messagebox.showinfo("Scan Complete", "No open ports found.\nResult saved to scan_report.txt")

# GUI setup
root = tk.Tk()
root.title("Open Port Scanner")

tk.Label(root, text="Target IP:").grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1)

tk.Label(root, text="Start Port:").grid(row=1, column=0, padx=5, pady=5)
start_port = tk.Entry(root)
start_port.grid(row=1, column=1)

tk.Label(root, text="End Port:").grid(row=2, column=0, padx=5, pady=5)
end_port = tk.Entry(root)
end_port.grid(row=2, column=1)

scan_button = tk.Button(root, text="Start Scan", command=scan_ports)
scan_button.grid(row=3, column=0, columnspan=2, pady=10)

output_text = tk.Text(root, height=15, width=50)
output_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()