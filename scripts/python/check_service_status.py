import subprocess

def check_service_status(service_name):
	try:
		status = subprocess.check_output(["systemctl", "is-active", service_name], text=True).strip()
		if status == "active":
			print(f"{service_name} is running.")
		else:
			print(f"{service_name} is NOT running!")
	except Exception as e:
		print(f"Error checking {service_name}: {e}")

check_service_status("nginx")
check_service_status("apache2")
check_service_status("mysql")
check_service_status("docker")