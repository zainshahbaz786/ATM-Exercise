import json
class x:
    def obj_to_json(self, dict,fname):
        self.dict = dict
        self.fname = fname

        #converting dict to json
        file_path = r'./Accounts/{}.json'.format(fname)
        with open(file_path, "w") as outfile:
            json.dump(dict, outfile, indent=4)


d={
    "name": "zeath",
    "cnic": "111",
    "age": 21,
    "address": "g11",
    "balance": 4928,
    "password": "1212"
}
obj=x()

obj.obj_to_json(d,"111")