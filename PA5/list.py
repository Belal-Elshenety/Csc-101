# list.py
# Here is where your list class will be held

class List:
    # These variables will be used in most classes. You may add more variables if needed
    # however, you will need to use and implement these variables in your solution
    list = []
    length = 0

    def __init__(self, length_of_list):
        # Your initialize (__init__) function will have more than one argument
        # This function should have arguments that decide the length of the list
        # and should extend the list variable above to the length the user has verified

        # Code your answer below
        self.list = [None]*length_of_list
        self.length = 0

    def add(self, value):
        # This function will add a value to your list at the specified index
        # This value should be placed at the end of the list
        # (meaning if you have a list of length 10 with five values inside, the
        #  new value should be placed at index 5)
        # The implementation of this function may require a helper function to
        # determine where this item should go

        # Code your answer below

        self.list[self.length] = value
        self.length += 1


    def remove(self, index):
        #  This function will remove the item at the index the user has typed
        #  The function should shift all values in the list that are at positions index + 1
        #  to length of list - 1 to the left once, overwriting the value previously contained
        #  at this index position.
        #  Consider writing a for loop to shift all values to the left once

        #  Code your answer below\
        for i in range(index, self.get_num_items()-1):
            self.list[i] = self.list[i + 1]
        self.list[self.get_num_items()-1] = None




    def get_length(self):
        # This function should return an int that calculates the entire length of the list
        # This would include both positions that are filled and positions that aren't filled
        # Consider using the length variable initialized in the class

        # Code your answer below
        count = 0
        for k in self.list:
            count +=1
        return count

    def get_num_items(self):
        # This function is similar to the get_length() function, however it will calculate
        # how many items are currently in the list (ignoring None spaces), and will return
        # an int on the number of items initialized

        # This function will be useful to use for other functions in this class

        # Code your answer below
        count = 0
        for k in self.list:
            if k is not None:
                count += 1
        return count

    # # Instructor will decide if insert is necessary
    def insert(self, index, value):
        # This function will insert a specified value into the list in the index that
        # was passed in
        # Every value at that index and beyond in the list before the insertion should
        # be shifted to the right to create space for the new value
        # Check to make sure the list has space for an insertion before shifting
        # consider using a loop or RecursionError
        # Check if the list has space for insertion

        # Code your answer below
        if self.length < len(self.list):
            # Shift elements to the right to create space for the new value
            for i in range(self.length - 1, index - 1, -1):
                self.list[i + 1] = self.list[i]
            # Insert the value at the specified index
            self.list[index] = value
            self.length += 1
        return self.list
        # pass

    def print_list(self):
        # This function will just output the list to use for testing purposes

        # Code your answer below (one return statement)
        return [k for k in self.list if k is not None]

    def second_dimension_ec(self, other):
        current_list = [item for item in self.list if item is not None]
        passed_list = list(other)
        result = [[0] * len(passed_list) for _ in range(len(current_list))]
        for i in range(len(current_list)):
            for j in range(len(passed_list)):
                result[i][j] = current_list[i] * passed_list[j]
        return result

    # # Consider creating your own helper functions in your solutions or creating
    # # functions that check if other functions can run (you can't run the add function
    # # on a list that is already full, etc)
