#coding:utf-8
import sys
sys.path.append("/var/root/PycharmProjects/firewallanalysis/")


from config.firewallconfig import firewall_object_name,firewall_rule_file_names,firewall_service_name
import xlrd




class firewallConfig(object):
    def __init__(self,path,firewall_name=None,firewall_config_all=None,firewall_rule=[],firewall_object=[],firewall_service=[]):
        self.path=path

    def xlsx2config(self):
        rules_list=[]
        object_list=[]
        service_list=[]
        workbooks=xlrd.open_workbook(self.path)
        for firewall in firewall_rule_file_names:
            table = workbooks.sheet_by_name(firewall)
            rules_list.append({
                'firewall_name':firewall,
                'data':table
            })
        for firewall in firewall_object_name:
            table = workbooks.sheet_by_name(firewall)
            object_list.append({
                'firewall_name': firewall,
                'data': table
            })

        for firewall in firewall_service_name:
            table = workbooks.sheet_by_name(firewall)
            service_list.append({
                'firewall_name': firewall,
                'data': table
            })

        self.firewall_rule =rules_list
        self.firewall_object=object_list
        self.firewall_service=service_list


#flag:用来标记有多少列

    def clean_rules(self,flag=0):
        list=[]
        rules=self.firewall_rule
        for rule in rules:
            table = rule['data']
            if table.nrows > 0:
                colnames = table.row_values(flag)
                for i in range(1, table.nrows):
                    # for i in range(1, 2):
                    row = table.row_values(i)
                    if row:
                        app = {}
                        for key in range(len(colnames)):
                            if colnames[key]=='rule.source':
                                rule_source_list=row[key].split(',')
                            if colnames[key]=='rule.service':
                                if isinstance(row[key],float):
                                    rule_service_list.append(row[key])
                                else:
                                    rule_service_list=row[key].split(',')
                            if colnames[key]=='rule.destination':

                                rule_destination_list=row[key].split(',')
                        print rule_destination_list
                        for key in range(len(colnames)):
                            for m in rule_source_list:
                                for n in rule_service_list:
                                    for p in rule_destination_list:


                                        """
                                        if colnames[key]=='rule.source':
                                            app[colnames[key]]=m
                                        if colnames[key] == 'rule.service':
                                            app[colnames[key]] = n
                                        if colnames[key] == 'rule.destination':
                                            app[colnames[key]] = p
                                        else:
                                            app[colnames[key]] = row[key]
                                        """

                        list.append(app)

        return list


    def clean_object(self,flag=0):
        pass
    def clean_service(self,flag=0):
        pass




if __name__ == '__main__':
    config=firewallConfig('/var/root/Documents/firewall0402.xlsx')
    config.xlsx2config()
    print config.clean_rules()




