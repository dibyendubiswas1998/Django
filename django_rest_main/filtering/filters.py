import django_filters
from employee.models import Employee



class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name="emp_designation", lookup_expr='iexact')
    name = django_filters.CharFilter(field_name="emp_name", lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name="emp_id")
    
    # Advanced Filter, filter_by_id_range custom method
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='from_emp_id')
    id_max = django_filters.CharFilter(method='filter_by_id_range',label='to_emp_id')
    
    class Meta:
        model = Employee
        fields = ['designation', 'name', 'id_min', 'id_max']
        
    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)

        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        
        return queryset