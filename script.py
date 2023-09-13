import json
import argparse
import sys

from mypackage import networkscan


def get_args():
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='This script scans a network, finds devices and services with default creds and saves results to a file')
    # Add arguments
    parser.add_argument(
        '-t', '--target', type=str, help='IP subnet range', required=False, default='192.168.0.0/24')
    parser.add_argument(
        '-c', '--config', type=str, help='Config file', required=False)
    parser.add_argument(
        '-p', '--ports', type=str, help='list of TCP ports, comma separated (Defaults: 22,23,80,8080,443)', required=False, default='22,23,80,8080,443')
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    ip_subnet_range = args.target
    config_file = args.config
    ports = args.ports
    # Return all variable values
    return ip_subnet_range, config_file, ports


def main():
    #
    # Scan the network and save the results to a list
    #
    ip_subnet_range, config_file, ports = get_args()

    ports = [int(port) for port in ports.split(',')]

    host_results = networkscan.network_scan(ip_subnet_range, ports)

    # Write the results to a file
    with open('scan_results.txt', 'w') as f:
        for host_entry in host_results:
            print(host_entry)  # Display the host_entry directly
            f.write(json.dumps(host_entry))
            f.write('\n')


if __name__ == "__main__":
    main()