import os
import shutil

def set_zone():
    # Command to get the list of zones using gcloud
    command = 'gcloud compute zones list | grep "^NAME" | cut -d" " -f2'
    output = os.popen(command).read()

    # Split the output into a list
    zones_list = output.splitlines()

    # Print the list joined with ","
    print(','.join(zones_list))

def create_bucket(bucket_name, location):
    print(bucket_name, location)
    print(f"gsutil mb -l {location} gs://{bucket_name} -b on")
    if location:
        print("localizacion")
        # Create a bucket with specified location using gsutil
        command = f"gsutil mb -l {location} gs://{bucket_name} -b on"
        os.system(command)
    else:
        # Create a bucket without specifying a location using gsutil
        command = f"gsutil mb gs://{bucket_name} -b on"
        os.system(command)

def copy_folder_to_bucket(source_folder, bucket_name):
    # Copy the contents of a folder to a bucket using gsutil
    os.system(f"gsutil -m cp -r {source_folder} gs://{bucket_name}")

def import_vm(vm_name, source_uri, location):
    # Import a virtual machine instance using gcloud
    os.system(f"gcloud compute instances import {vm_name} --source-uri={source_uri} -zone {location}")

def main():
    # Prompt the user for bucket and location information
    bucket_name = input("Enter bucket name: ")
    location_choice = input("Choose bucket location (m for multiregional, z for zonal): ")
    if location_choice.lower() == 'm':
        print("Selected multiregional location") 
        location = False
    elif location_choice.lower() == 'z':
        set_zone()
        location = input("Enter zonal location: ")
    else:
        print("Selected none zone")
        location = False

    # Create the bucket and copy the "vm" folder to it
    create_bucket(bucket_name, location)
    copy_folder_to_bucket("vm", bucket_name)

    # Prompt the user for VM and import information
    vm_name = input("Enter VM name: ")
    file_extension = input("Enter the file extension to import (e.g., .ovf, .ova): ")
    source_uri = f"gs://{bucket_name}/vm/*.{file_extension}"
    location_vm = input("Choose the location of the VM: ")
    import_vm(vm_name, source_uri, location_vm)

if __name__ == "__main__":
    main()

