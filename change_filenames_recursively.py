import os
import sys
import traceback

# Print characters with UTF-8 encoding
sys.stdout.reconfigure(encoding="utf-8")

def replace(folder_path, old, new):
    print('path: "{0}", current name: "{1}" and new name is: "{2}"'.format(folder_path, old, new))
    for path, subdirs, files in os.walk(folder_path):
        
        for name in files:

            is_contained = (old.lower() in name.lower())
            print('name: {0} is contained in: {1}? = {2}'.format(old.lower(), name.lower(), is_contained))
            
            # Si el nombre del archivo contiene la cadena de texto 'old'
            if(is_contained):
                
                # Get la ruta completa del archivo (incluido su nombre y extension)
                file_path = os.path.join(path,name)
                print('file_path: {0} for name: {1}'.format(file_path, name))
                
                # Genero el nuevo nombre para el archivo. Uso la nueva cadena para reemplazar el substring coincidente
                new_name = os.path.join(path, name.lower().replace(old.lower(), new))
                print('new name: {0}'.format(new_name))
                
                # Renombro el archivo
                os.rename(file_path, new_name)
                

if __name__ == '__main__': 
    
    try:        
        # Calling main() function 
        replace('D:\Teología\Josef Urban\Serie Romanos', ' - ', '')
    except BaseException as e:
        # Get current system exception
        ex_type, ex_value, ex_traceback = sys.exc_info()

        # Extract unformatter stack traces as tuples
        trace_back = traceback.extract_tb(ex_traceback)

        # Format stacktrace
        stack_trace = list()

        # Message
        message_all = "";

        for trace in trace_back:
            message_all = message_all + trace[3]
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

        if len(str(ex_value)) == 0:
            ex_value = message_all

        print("Exception type : %s " % ex_type.__name__)
        print("Exception message : %s" %ex_value)
        print("Stack trace : %s" %stack_trace)