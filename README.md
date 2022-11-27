# Floyd-Warshall algorithm rewritten using recursion
This project uses the Floyd-Warshall Algorithm and converts an imperative Python solution using iterative looping to use a recursion.

# Install
To install, type the below into your command line
git clone https://github.com/kzaiets/floyd.git
This will save the folder containing all the files within the repository.
Ensure you install the necessary packages that can be found in requirements.txt
To install the requirements file, run the following command in your shell: pip install -r requirements.txt

# Usage
To run the code, change directory to src on your shell terminal and execute the following:
python ./floyd_recursive.py
The output will print in your terminal and should look like the following:
[[0, 5, 8, 9], [500, 0, 3, 4], [500, 500, 0, 1], [500, 500, 500, 0]]

# Running Unit Tests
To run the unit tests use the following in the terminal for the test.py file
python -m unittest test.test 

# Running Performance Tests
To run the performance tests use the following in the terminal for the test_performance.py file
python -m test.test_performance

# Contributing 
Pull requests accepted.

# License
MIT © Karina Zaiets