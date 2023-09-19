

Para clonar un repo 
Ej:
https://github.com/clear-code-projects/UltimatePygameIntro.git


git clone https://github.com/clear-code-projects/UltimatePygameIntro.git

Nota: git clone añadie tambien el .git folder 
si trabajas en otro git dara conflicto, hay que eliminarlo 

git clone --separate-git-dir=$(mktemp -u) --depth=1 <repo> <dir> && rm <dir>/.git

o con 

npx degit https://github.com/clear-code-projects/UltimatePygameIntro.git

pero npx necesita un directorio vacio 