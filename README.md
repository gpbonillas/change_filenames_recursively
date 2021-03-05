# change_filenames_recursively
Cambia el nombre de archivo dentro de un directorio recursivamente. 

The definition of method is: `def replace(folder_path, old, new):`

* Recorre recursivamente todos los subdirectorios de una carpeta (`folder_path`)
* Busca una cadena de texto (`old`) en la ruta completa del archivo, en caso de encontrarse una coincidencia genera un nuevo nombre concatenando una nueva cadena de texto (`new`) y renombra el archivo.
