#coding:utf-8

from storage.clean import firewallConfig
from config.firewallconfig import file_path
from storage.dbUtil import insert




if __name__ == '__main__':

    file_object=firewallConfig(file_path)
    rules,objects,services=file_object.xlsx2config()
    for rule in rules:
      #  firewall_name=rule.firewall_name
        table=rule['data']
        if table.nrows>0:
            colnames = table.row_values(0)
            for i in range(1,table.nrows):
            #for i in range(1, 2):
                row=table.row_values(i)
                if row:
                    app={}
                    for i in range(len(colnames)):
                        app[colnames[i]] = row[i]


                print row
              #  row.insert()



       # for item in rule_content:
        #    print




