import subprocess
import re

def run_code(js_code, inputs, outputs):
    tests_count = len(inputs)
    successful_tests = 0
    unsuccessful_tests = 0
    
    for i in range(tests_count):
        current_input = ', '.join([str(element) for element in inputs[i]])  # THIS NEEDS TO BE CHANGED (MAYBE)
        correct_output = str(outputs[i][0])  # THIS NEEDS TO BE CHANGED !!
        
        function_name = re.findall(r"(?<=function ).*(?=\()", js_code)
        current_js_code = js_code + '\n\n' + f'console.log({function_name[0]}({current_input}))'
        
        # Use subprocess to run JS code
        process = subprocess.Popen(['node', '-e', current_js_code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        # Decode output from bytes to string
        stdout_str = stdout.decode('utf-8').replace('\n', '')
        stdout_str = stdout_str.replace('undefined', '')
        stderr_str = stderr.decode('utf-8')
        
        if correct_output == stdout_str:
            successful_tests += 1
        else:
            unsuccessful_tests += 1
        
        if unsuccessful_tests == 0:
            message = 'Congratulations! Your solution is correct!'
        elif successful_tests > 0 and unsuccessful_tests > 0:
            message = 'Your solution is partially correct! Try again!'
        elif successful_tests == 0 and unsuccessful_tests > 0:
            message = 'Your solution is incorrect! Try again!'

    print(f'All tests: {tests_count}')
    print(f"You have {successful_tests} successful tests")
    print(f"You have {unsuccessful_tests} unsuccessful tests")
    print(f'The message is "{message}"')
    return successful_tests, unsuccessful_tests, message



# js_code = """
# console.log('Hello, world!');
# """

# Use for debuging porposes only
# run_code(js_code)