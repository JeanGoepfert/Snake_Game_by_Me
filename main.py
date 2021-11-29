import sys
from pathlib import Path
file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))


from Code.interface_graphique  import main

if __name__ == '__main__':
    main()