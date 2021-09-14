import argparse
import json
import os
import tempfile


def storage():

    parser = argparse.ArgumentParser()
    parser.add_argument("--key")
    parser.add_argument("--val")
    args = parser.parse_args()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    if os.path.isfile(storage_path):
        if args.val:
            with open(str(storage_path), 'r') as f:
                py_obj = json.load(f)
                if args.key in py_obj:
                    py_obj[args.key] = py_obj[args.key] + [args.val]
                elif args.key not in py_obj:
                    py_obj.update({args.key: [args.val]})
            with open(storage_path, 'w') as f:
                json.dump(py_obj, f)
        else:
            try:
                with open(str(storage_path), 'r') as f:
                    py_obj = json.load(f)
                    if len(py_obj[args.key]) > 1:
                        print(', '.join(py_obj.get(args.key)))
                    else:
                        print(*py_obj.get(args.key))
            except:
                print(None)
    else:
        base = {}
        with open(str(storage_path), "w") as f:
            if args.val:
                base = {args.key: [args.val]}
                json.dump(base, f)
            else:
                base = {args.key: None}
                print(None)


storage()
