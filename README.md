# change_filenames_recursively
Cambia los nombres de archivos dentro de un directorio recursivamente.

La definición del método es: `def replace(folder_path, old, new):`

* Recorre recursivamente todos los subdirectorios de una carpeta (`folder_path`)
* Busca una cadena de texto (`old`) en la ruta completa del archivo, en caso de encontrarse una coincidencia genera un nuevo nombre concatenando una nueva cadena de texto (`new`) y renombra el archivo.

# Fuente: 
Se usó el código del artículo [How to rename multiple files recursively using Python?] (https://www.tutorialspoint.com/How-to-rename-multiple-files-recursively-using-Python)