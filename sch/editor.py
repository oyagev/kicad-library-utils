
class ComponentEditor(object):

    def __init__(self, component):
        self.field_map = {}
        self.component = component
        self.map_fields()

    def map_fields(self):

        for f in self.component.fields:
            id = int(f['id'])
            if id < 4:
                if id == 0:
                    self.field_map['Reference'] = f
                elif id == 1:
                    self.field_map['Value'] = f
                elif id == 2:
                    self.field_map['Footprint'] = f
                elif id == 3:
                    self.field_map['Datasheet'] = f
            else:
                self.field_map[f['name'].strip('"')] = f

    def set_field_value(self, field_name, value):
        try:
            field = self.field_map[field_name]
            field['ref'] = '"%s"' % value
        except KeyError:
            self.component.addField({
                'ref': '"%s"' % value,
                'name': '"%s"' % field_name
            })

    def set_footprint(self, value):
        self.set_field_value('Footprint', value)