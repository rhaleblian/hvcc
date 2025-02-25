# Copyright (C) 2014-2018 Enzien Audio, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import json

import interpreters.pd2hv.PdParser as PdParser

def main():
    parser = argparse.ArgumentParser(
        description="")
    parser.add_argument(
        "cmd",
        help="command")
    args = parser.parse_args()

    if args.cmd == "pdobjects":
        obj_list = PdParser.PdParser.get_supported_objects()
        print(json.dumps(obj_list))
    else:
        pass

if __name__ == "__main__":
    main()
