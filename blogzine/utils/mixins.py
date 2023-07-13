class NoLabelFormMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.label = ''


class DisableAutocompleteMixin:
    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['autocomplete'] = 'off'