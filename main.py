import sys

def main(group_name):
    print(f"Running script for group: {group_name}")
    # Add your script logic here

if __name__ == "__main__":
    # Default value for group_name
    group_name = None

    # Manually parse the '--group' argument
    for arg in sys.argv:
        if arg.startswith('--group='):
            group_name = arg.split('=')[1]
            break

    if group_name is None:
        print("Error: You must provide a group name using --group=<group_name>")
        sys.exit(1)

    main(group_name)
