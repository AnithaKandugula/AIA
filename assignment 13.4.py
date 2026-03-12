#Refactor the following Python loop that doubles numbers into a more Pythonic version using list comprehension while keeping the same output: values=[2,4,6,8,10]; doubled=[]; for v in values: doubled.append(v*2); print(doubled)
'''values = [2, 4, 6, 8, 10]
doubled = [v * 2 for v in values]   
print(doubled)'''
#Task 2 – Refactor this Python code that builds a sentence using repeated string concatenation into a cleaner and more efficient approach while keeping the same output: words=["Refactoring","with","AI","improves","quality"]; message=""; for w in words: message+=w+" "; print(message.strip())
'''words = ["Refactoring", "with", "AI", "improves", "quality"]
message = " ".join(words)
print(message)
'''
#Rewrite this Python code using a safer dictionary access method like dict.get() while preserving the same behavior for missing keys: config={"host":"localhost","port":8080}; if "timeout" in config: print(config["timeout"]); else: print("Default timeout used")
'''config = {"host": "localhost", "port": 8080}
timeout = config.get("timeout", "Default timeout used")
print(timeout)'''
#Refactor this Python code that uses multiple if-elif statements for operations into a scalable mapping (dictionary of functions) approach while keeping the same behavior: action="divide"; x,y=10,2; if action=="add": result=x+y; elif action=="subtract": result=x-y; elif action=="multiply": result=x*y; elif action=="divide": result=x/y; else: result=None; print(result)
'''operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else None
}
action = "divide"
x, y = 10, 2
result = operations.get(action, lambda x, y: None)(x, y)
print(result)'''

#Refactor this Python code that manually searches for an item in a list using a loop into a more concise and readable approach while preserving the same output: inventory=["pen","notebook","eraser","marker"]; found=False; for item in inventory: if item=="eraser": found=True; break; print("Item Available" if found else "Item Not Available")
inventory = ["pen", "notebook", "eraser", "marker"]
found = "eraser" in inventory
print("Item Available" if found else "Item Not Available")
