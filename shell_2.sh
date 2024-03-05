# Try to list the contents of a directory
ls /nonexistentdirectory

# Again, check the exit status
if [ $? -eq 0 ]; then
    echo "The directory was found."
else
    echo "The directory was not found."
fi