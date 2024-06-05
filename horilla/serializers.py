from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Employee, Department, LeaveRequest, Payroll, JobPosting, JobApplication

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user', 'first_name', 'last_name', 'job_title', 'department', 'email', 'phone_number', 'address', 'salary', 'hire_date', 'date_of_birth']
        read_only_fields = ['id','salary', 'department', 'job_title','hire_date'] # Fields that employees cannot edit

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class LeaveRequestSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = LeaveRequest
        fields = ['id', 'employee', 'start_date', 'end_date', 'reason', 'status']

class PayrollSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Payroll
        fields = ['id', 'employee', 'pay_date', 'amount', 'tax_deductions', 'net_pay']

class JobPostingSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = JobPosting
        fields = ['id', 'title', 'description', 'department', 'posting_date', 'closing_date']

class JobApplicationSerializer(serializers.ModelSerializer):
    job_posting = JobPostingSerializer()

    class Meta:
        model = JobApplication
        fields = ['id', 'job_posting', 'first_name', 'last_name', 'email', 'resume', 'application_date', 'status']
