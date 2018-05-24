"# GitProyectFileUpload"

# # GitProyectFileUpload!

##Version sin vista, solo script.

Script para eliminar archivos de una ruta definida.
Para configurar la ruta y archivos a eliminar o excluir de eliminarse se debe editar el archivo filesList.json

## FilesList.json
Archivo de configuración para definir los parametros de: 
**files** string: contiene el listado de archivos(delimitados por " , " coma) que se deberán buscar en la ruta especificada para ser eliminados.

**excluded** string: contiene el listado de archivos(delimitados por " , " coma) que se deberá evitar sean eliminados.

**pathABS** boolean: Deberá contener el valor numerico 1, en caso que se requiera utilizar el path absoluto definido en la propiedad pathFiles de este archivo de configuración.¨ 
En caso que se requiera aliminar archivos alojados en la misma ruta que contenta estos scripts se podrá utilizar el pathRelativo, asignando el valor numerico 0 a esta propiedad.
**pathFiles** string: Define el path absoluto en caso que se requiera eliminar archivos de un ruta diferente a la del proyecto.
En caso de indicar error por el backslash, colocar doble backslash para solucionarlo.
Ej. "C:\\User\\proyectos\\fileTests"

*Los nombres de los archivos deben incluir la extensión