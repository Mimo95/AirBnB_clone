#!/usr/bin/python3
"""
This script defines a HBNBCommand class .
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter for HBNB project.
    """
    
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    def precmd(self, line):
        """
        Preprocesses command before executing.

        Args:
            line (str): The command entered by the user.

        Returns:
            str: The processed command.
        """
        match_all = re.match(r'^([A-Za-z]+)\.all\(\)$', line)
        match_count = re.match(r'^([A-Za-z]+)\.count\(\)$', line)
        class_list = ["BaseModel", "User", "State", "City", 
                      "Place", "Review", "Amenity"]
    
        if match_all:
            classname = match_all.group(1)
            if classname in class_list:
                instances = storage.all()
                filtered_instances = [str(instance) for key, instance in 
                                      instances.items() if
                                      key.startswith(classname + ".")]

                print(filtered_instances)
                return ''  
            else:
                return ''  
        elif match_count:
            classname = match_count.group(1)
            if classname in class_list:
                count = sum(1 for key in 
                            storage._FileStorage__objects.keys() if
                            key.startswith(classname + "."))
                
                print(count)
                return ''  
            else:
                return ''  

        return line

    def do_create(self, classname):
        """
        Creates a new instance of the specified class.

        Args:
            classname (str): The name of the class.

        Returns:
            None
        """
        if not classname:
            print("** class name missing **")
        else:
            if classname == "BaseModel":
                instance = BaseModel()
                storage.save()
                print(instance.id)
            elif classname == "User":
                instance = User()
                storage.save()
                print(instance.id)
            elif classname == "State":
                instance = State()
                storage.save()
                print(instance.id)
            elif classname == "City":
                instance = City()
                storage.save()
                print(instance.id)
            elif classname == "Place":
                instance = Place()
                storage.save()
                print(instance.id)
            elif classname == "Review":
                instance = Review()
                storage.save()
                print(instance.id)
            elif classname == "Amenity":
                instance = Amenity()
                storage.save()
                print(instance.id)
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and ID.

        Args:
            args (str): The command arguments.

        Returns:
            None
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        else:
            if (args[0] != "BaseModel" and args[0] != "User" and 
                args[0] != "State" and args[0] != "City" and 
                args[0] != "Place" and args[0] != "Review" and
                    args[0] != "Amenity"):

                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                    if (not re.match(r, str(args[1])) or
                        args[0] + "." + args[1] not in 
                            storage._FileStorage__objects):
                        
                        print("** no instance found **")
                    else:
                        key = args[0] + "." + args[1]
                        del storage._FileStorage__objects[key]
                        storage.save()
    
    def do_show(self, args):
        """
        Displays the string representation of an instance.

        Args:
            args (str): The command arguments.

        Returns:
            None
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        else:
            if (args[0] != "BaseModel" and args[0] != "User" and 
                args[0] != "State" and args[0] != "City" and 
                args[0] != "Place" and args[0] != "Review" and 
                    args[0] != "Amenity"):
                
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                    if (not re.match(r, str(args[1])) or 
                        args[0] + "." + args[1] not in 
                            storage._FileStorage__objects):
                        
                        print("** no instance found **")
                    else:
                        key = args[0] + "." + args[1]
                        instance = storage._FileStorage__objects[key]
                        print(instance)

    def do_all(self, classname):
        """
        Displays all string representations of instances.

        Args:
            classname (str): The name of the class.

        Returns:
            None
        """
        if not classname:
            instances = storage.all()
            all_instances = [str(instance) for instance in instances.values()]
            print(all_instances)
        elif (classname == "BaseModel" or classname == "User"or
              classname == "State" or classname == "City" or
              classname == "Place" or classname == "Review" or
                classname == "Amenity"):
            
            instances = storage.all()
            filtered_instances = [str(instance) for key, instance in 
                                  instances.items() if 
                                  key.startswith(classname + ".")]
            
            print(filtered_instances)
        else:
            print("** class doesn't exist **")


    def do_update(self, args):
        """
        Updates an instance attribute value.

        Args:
            args (str): The command arguments.

        Returns:
            None
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        else:
            if (args[0] != "BaseModel" and args[0] != "User" and 
                args[0] != "State" and args[0] != "City" and 
                args[0] != "Place" and args[0] != "Review" and 
                    args[0] != "Amenity"):
                
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    if len(args) < 3:
                        r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                        if (not re.match(r, str(args[1])) or 
                            args[0] + "." + args[1] not in 
                                storage._FileStorage__objects):
                            
                            print("** no instance found **")
                        else:
                            print("** attribute name missing **")
                    else:
                        if len(args) < 4:
                            print("** value missing **")
                        else:
                            r = "^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$"
                            if (not re.match(r, str(args[1])) or 
                                args[0] + "." + args[1] not in 
                                    storage._FileStorage__objects):
                            
                                print("** no instance found **")
                            else:
                                key = args[0] + "." + args[1]
                                instance = storage._FileStorage__objects[key]
                                setattr(instance, args[2], args[3]) 
                                storage.save()
    
    def do_count(self, classname):
        """
        Counts the number of instances of a class.

        Args:
            classname (str): The name of the class.

        Returns:
            None
        """
        if not classname:
            print("** class name missing **")
        else:
            if classname in ["BaseModel", "User", "State", "City",
                             "Place", "Review", "Amenity"]:
                count = 0
                for key in storage._FileStorage__objects.keys():
                    if key.startswith(classname + "."):
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")

    def default(self, line):
        if not line.strip():
            return
        else:
            super().default(line)

    def emptyline(self):
        if sys.__stdin__.isatty():
            pass
        else:
            return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
