# Font Awesome Migration
Use a script to automatically migrate Font Awesome v4 to v5 (including unicode).

This Font Awesome migration script was successfully used to update a large project. The script was created iteratively and still needs to be cleaned up for simplified re-use.

## Resources
- Upgrading from version 4: https://fontawesome.com/how-to-use/on-the-web/setup/upgrading-from-version-4
    - Includes list of all/most of the icon name changes from v4 to v5
- Font Awesome Cheatsheet (free version icons): https://fontawesome.com/cheatsheet/free/solid
- Font Awesome Cheatsheet v4.7.0: https://fontawesome.com/v4.7.0/cheatsheet/

## Changes
- Replace from 'fa ' to 'fas ' or 'far '
- Replace from 'font-family: FontAwesome;' to 'font-family: "Font Awesome 5 Free";'
- Replace from 'font-family: "FontAwesome";' to 'font-family: "Font Awesome 5 Free";'
- Replace from '\f046' to '\f14a' and more unicode changes
- Replace from 'fa-star-o' to 'fa-star' with 'font-weight: normal'

Also, double-check for the following, which may need to be updated:
- 'fa.'
- '.fa'
- '"fa'
- 'fa '

