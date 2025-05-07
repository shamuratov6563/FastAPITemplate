from sqladmin import Admin, ModelView
from app.models import (
    User, Branch, Role, Activity, Group,
    UserBranch, UserRole, UserDescription,
    Attendance, WorkingDay
)

# ModelView'lar
class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.full_name, User.username, User.role]

class BranchAdmin(ModelView, model=Branch):
    column_list = [Branch.id, Branch.name]

class RoleAdmin(ModelView, model=Role):
    column_list = [Role.id, Role.name]

class ActivityAdmin(ModelView, model=Activity):
    column_list = [Activity.id, Activity.name, Activity.description]

class GroupAdmin(ModelView, model=Group):
    column_list = [Group.id, Group.name]

class UserBranchAdmin(ModelView, model=UserBranch):
    column_list = [UserBranch.id, UserBranch.user_id, UserBranch.branch_id]

class UserRoleAdmin(ModelView, model=UserRole):
    column_list = [UserRole.id, UserRole.user_id, UserRole.role_id]

class UserDescriptionAdmin(ModelView, model=UserDescription):
    column_list = [UserDescription.id, UserDescription.user_id, UserDescription.description]

class AttendanceAdmin(ModelView, model=Attendance):
    column_list = [Attendance.id, Attendance.date, Attendance.group_id]

class WorkingDayAdmin(ModelView, model=WorkingDay):
    column_list = [WorkingDay.id, WorkingDay.day_of_week, WorkingDay.group_id]



def setup_admin(admin: Admin):
    admin.add_view(UserAdmin)
    admin.add_view(BranchAdmin)
    admin.add_view(RoleAdmin)
    admin.add_view(ActivityAdmin)
    admin.add_view(GroupAdmin)
    admin.add_view(UserBranchAdmin)
    admin.add_view(UserRoleAdmin)
    admin.add_view(UserDescriptionAdmin)
    admin.add_view(AttendanceAdmin)
    admin.add_view(WorkingDayAdmin)