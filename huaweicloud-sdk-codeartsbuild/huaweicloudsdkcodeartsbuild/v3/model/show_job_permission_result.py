# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobPermissionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'int',
        'job_id': 'str',
        'is_modify': 'bool',
        'is_delete': 'bool',
        'is_view': 'bool',
        'is_execute': 'bool',
        'is_copy': 'bool',
        'is_forbidden': 'bool',
        'is_manager': 'bool',
        'create_time': 'str',
        'last_update_time': 'str',
        'count': 'int'
    }

    attribute_map = {
        'role_id': 'role_id',
        'job_id': 'job_id',
        'is_modify': 'is_modify',
        'is_delete': 'is_delete',
        'is_view': 'is_view',
        'is_execute': 'is_execute',
        'is_copy': 'is_copy',
        'is_forbidden': 'is_forbidden',
        'is_manager': 'is_manager',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'count': 'count'
    }

    def __init__(self, role_id=None, job_id=None, is_modify=None, is_delete=None, is_view=None, is_execute=None, is_copy=None, is_forbidden=None, is_manager=None, create_time=None, last_update_time=None, count=None):
        r"""ShowJobPermissionResult

        The model defined in huaweicloud sdk

        :param role_id: 角色ID
        :type role_id: int
        :param job_id: 任务ID
        :type job_id: str
        :param is_modify: 是否有修改任务权限
        :type is_modify: bool
        :param is_delete: 是否有删除任务权限
        :type is_delete: bool
        :param is_view: 是否有查看任务权限
        :type is_view: bool
        :param is_execute: 是否有执行任务权限
        :type is_execute: bool
        :param is_copy: 是否有复制任务权限
        :type is_copy: bool
        :param is_forbidden: 是否有禁用任务权限
        :type is_forbidden: bool
        :param is_manager: 是否有管理任务权限
        :type is_manager: bool
        :param create_time: 任务创建时间
        :type create_time: str
        :param last_update_time: 任务最后修改时间
        :type last_update_time: str
        :param count: 次数
        :type count: int
        """
        
        

        self._role_id = None
        self._job_id = None
        self._is_modify = None
        self._is_delete = None
        self._is_view = None
        self._is_execute = None
        self._is_copy = None
        self._is_forbidden = None
        self._is_manager = None
        self._create_time = None
        self._last_update_time = None
        self._count = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if job_id is not None:
            self.job_id = job_id
        if is_modify is not None:
            self.is_modify = is_modify
        if is_delete is not None:
            self.is_delete = is_delete
        if is_view is not None:
            self.is_view = is_view
        if is_execute is not None:
            self.is_execute = is_execute
        if is_copy is not None:
            self.is_copy = is_copy
        if is_forbidden is not None:
            self.is_forbidden = is_forbidden
        if is_manager is not None:
            self.is_manager = is_manager
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if count is not None:
            self.count = count

    @property
    def role_id(self):
        r"""Gets the role_id of this ShowJobPermissionResult.

        角色ID

        :return: The role_id of this ShowJobPermissionResult.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ShowJobPermissionResult.

        角色ID

        :param role_id: The role_id of this ShowJobPermissionResult.
        :type role_id: int
        """
        self._role_id = role_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobPermissionResult.

        任务ID

        :return: The job_id of this ShowJobPermissionResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobPermissionResult.

        任务ID

        :param job_id: The job_id of this ShowJobPermissionResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def is_modify(self):
        r"""Gets the is_modify of this ShowJobPermissionResult.

        是否有修改任务权限

        :return: The is_modify of this ShowJobPermissionResult.
        :rtype: bool
        """
        return self._is_modify

    @is_modify.setter
    def is_modify(self, is_modify):
        r"""Sets the is_modify of this ShowJobPermissionResult.

        是否有修改任务权限

        :param is_modify: The is_modify of this ShowJobPermissionResult.
        :type is_modify: bool
        """
        self._is_modify = is_modify

    @property
    def is_delete(self):
        r"""Gets the is_delete of this ShowJobPermissionResult.

        是否有删除任务权限

        :return: The is_delete of this ShowJobPermissionResult.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        r"""Sets the is_delete of this ShowJobPermissionResult.

        是否有删除任务权限

        :param is_delete: The is_delete of this ShowJobPermissionResult.
        :type is_delete: bool
        """
        self._is_delete = is_delete

    @property
    def is_view(self):
        r"""Gets the is_view of this ShowJobPermissionResult.

        是否有查看任务权限

        :return: The is_view of this ShowJobPermissionResult.
        :rtype: bool
        """
        return self._is_view

    @is_view.setter
    def is_view(self, is_view):
        r"""Sets the is_view of this ShowJobPermissionResult.

        是否有查看任务权限

        :param is_view: The is_view of this ShowJobPermissionResult.
        :type is_view: bool
        """
        self._is_view = is_view

    @property
    def is_execute(self):
        r"""Gets the is_execute of this ShowJobPermissionResult.

        是否有执行任务权限

        :return: The is_execute of this ShowJobPermissionResult.
        :rtype: bool
        """
        return self._is_execute

    @is_execute.setter
    def is_execute(self, is_execute):
        r"""Sets the is_execute of this ShowJobPermissionResult.

        是否有执行任务权限

        :param is_execute: The is_execute of this ShowJobPermissionResult.
        :type is_execute: bool
        """
        self._is_execute = is_execute

    @property
    def is_copy(self):
        r"""Gets the is_copy of this ShowJobPermissionResult.

        是否有复制任务权限

        :return: The is_copy of this ShowJobPermissionResult.
        :rtype: bool
        """
        return self._is_copy

    @is_copy.setter
    def is_copy(self, is_copy):
        r"""Sets the is_copy of this ShowJobPermissionResult.

        是否有复制任务权限

        :param is_copy: The is_copy of this ShowJobPermissionResult.
        :type is_copy: bool
        """
        self._is_copy = is_copy

    @property
    def is_forbidden(self):
        r"""Gets the is_forbidden of this ShowJobPermissionResult.

        是否有禁用任务权限

        :return: The is_forbidden of this ShowJobPermissionResult.
        :rtype: bool
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        r"""Sets the is_forbidden of this ShowJobPermissionResult.

        是否有禁用任务权限

        :param is_forbidden: The is_forbidden of this ShowJobPermissionResult.
        :type is_forbidden: bool
        """
        self._is_forbidden = is_forbidden

    @property
    def is_manager(self):
        r"""Gets the is_manager of this ShowJobPermissionResult.

        是否有管理任务权限

        :return: The is_manager of this ShowJobPermissionResult.
        :rtype: bool
        """
        return self._is_manager

    @is_manager.setter
    def is_manager(self, is_manager):
        r"""Sets the is_manager of this ShowJobPermissionResult.

        是否有管理任务权限

        :param is_manager: The is_manager of this ShowJobPermissionResult.
        :type is_manager: bool
        """
        self._is_manager = is_manager

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowJobPermissionResult.

        任务创建时间

        :return: The create_time of this ShowJobPermissionResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowJobPermissionResult.

        任务创建时间

        :param create_time: The create_time of this ShowJobPermissionResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ShowJobPermissionResult.

        任务最后修改时间

        :return: The last_update_time of this ShowJobPermissionResult.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ShowJobPermissionResult.

        任务最后修改时间

        :param last_update_time: The last_update_time of this ShowJobPermissionResult.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def count(self):
        r"""Gets the count of this ShowJobPermissionResult.

        次数

        :return: The count of this ShowJobPermissionResult.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowJobPermissionResult.

        次数

        :param count: The count of this ShowJobPermissionResult.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowJobPermissionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
