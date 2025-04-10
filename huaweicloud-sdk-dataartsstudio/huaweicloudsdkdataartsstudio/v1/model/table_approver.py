# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableApprover:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'permission_set_id': 'str',
        'type': 'int',
        'workspace_id': 'str',
        'table_approver_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'permission_set_id': 'permission_set_id',
        'type': 'type',
        'workspace_id': 'workspace_id',
        'table_approver_type': 'table_approver_type'
    }

    def __init__(self, id=None, name=None, permission_set_id=None, type=None, workspace_id=None, table_approver_type=None):
        r"""TableApprover

        The model defined in huaweicloud sdk

        :param id: 审批人id
        :type id: str
        :param name: 审批人姓名
        :type name: str
        :param permission_set_id: 权限集id
        :type permission_set_id: str
        :param type: 审批人类型, 0 用户  1 用户组  2 角色（空间管理员）
        :type type: int
        :param workspace_id: 空间id
        :type workspace_id: str
        :param table_approver_type: 安全管理员：SECURITY_MANAGER，空间权限集管理员WORKSPACE_PERMISSION_SET_MANAGER，权限集管理员PERMISSION_SET_MANAGER
        :type table_approver_type: str
        """
        
        

        self._id = None
        self._name = None
        self._permission_set_id = None
        self._type = None
        self._workspace_id = None
        self._table_approver_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if type is not None:
            self.type = type
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if table_approver_type is not None:
            self.table_approver_type = table_approver_type

    @property
    def id(self):
        r"""Gets the id of this TableApprover.

        审批人id

        :return: The id of this TableApprover.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TableApprover.

        审批人id

        :param id: The id of this TableApprover.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TableApprover.

        审批人姓名

        :return: The name of this TableApprover.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TableApprover.

        审批人姓名

        :param name: The name of this TableApprover.
        :type name: str
        """
        self._name = name

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this TableApprover.

        权限集id

        :return: The permission_set_id of this TableApprover.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this TableApprover.

        权限集id

        :param permission_set_id: The permission_set_id of this TableApprover.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def type(self):
        r"""Gets the type of this TableApprover.

        审批人类型, 0 用户  1 用户组  2 角色（空间管理员）

        :return: The type of this TableApprover.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TableApprover.

        审批人类型, 0 用户  1 用户组  2 角色（空间管理员）

        :param type: The type of this TableApprover.
        :type type: int
        """
        self._type = type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this TableApprover.

        空间id

        :return: The workspace_id of this TableApprover.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this TableApprover.

        空间id

        :param workspace_id: The workspace_id of this TableApprover.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def table_approver_type(self):
        r"""Gets the table_approver_type of this TableApprover.

        安全管理员：SECURITY_MANAGER，空间权限集管理员WORKSPACE_PERMISSION_SET_MANAGER，权限集管理员PERMISSION_SET_MANAGER

        :return: The table_approver_type of this TableApprover.
        :rtype: str
        """
        return self._table_approver_type

    @table_approver_type.setter
    def table_approver_type(self, table_approver_type):
        r"""Sets the table_approver_type of this TableApprover.

        安全管理员：SECURITY_MANAGER，空间权限集管理员WORKSPACE_PERMISSION_SET_MANAGER，权限集管理员PERMISSION_SET_MANAGER

        :param table_approver_type: The table_approver_type of this TableApprover.
        :type table_approver_type: str
        """
        self._table_approver_type = table_approver_type

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
        if not isinstance(other, TableApprover):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
