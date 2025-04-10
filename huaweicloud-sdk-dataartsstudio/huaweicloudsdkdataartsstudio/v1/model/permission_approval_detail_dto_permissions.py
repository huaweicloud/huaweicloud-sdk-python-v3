# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionApprovalDetailDTOPermissions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'database_name': 'str',
        'permission_action': 'list[str]',
        'permission_set_id': 'str',
        'schema_name': 'str',
        'secrecy_level_id': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'database_name': 'database_name',
        'permission_action': 'permission_action',
        'permission_set_id': 'permission_set_id',
        'schema_name': 'schema_name',
        'secrecy_level_id': 'secrecy_level_id',
        'table_name': 'table_name'
    }

    def __init__(self, column_name=None, database_name=None, permission_action=None, permission_set_id=None, schema_name=None, secrecy_level_id=None, table_name=None):
        r"""PermissionApprovalDetailDTOPermissions

        The model defined in huaweicloud sdk

        :param column_name: 列名称
        :type column_name: str
        :param database_name: 库名称
        :type database_name: str
        :param permission_action: 权限
        :type permission_action: list[str]
        :param permission_set_id: 申请权限所在的空间权限集
        :type permission_set_id: str
        :param schema_name: schema名称
        :type schema_name: str
        :param secrecy_level_id: 密级
        :type secrecy_level_id: str
        :param table_name: 表名
        :type table_name: str
        """
        
        

        self._column_name = None
        self._database_name = None
        self._permission_action = None
        self._permission_set_id = None
        self._schema_name = None
        self._secrecy_level_id = None
        self._table_name = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if database_name is not None:
            self.database_name = database_name
        if permission_action is not None:
            self.permission_action = permission_action
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if schema_name is not None:
            self.schema_name = schema_name
        if secrecy_level_id is not None:
            self.secrecy_level_id = secrecy_level_id
        if table_name is not None:
            self.table_name = table_name

    @property
    def column_name(self):
        r"""Gets the column_name of this PermissionApprovalDetailDTOPermissions.

        列名称

        :return: The column_name of this PermissionApprovalDetailDTOPermissions.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        r"""Sets the column_name of this PermissionApprovalDetailDTOPermissions.

        列名称

        :param column_name: The column_name of this PermissionApprovalDetailDTOPermissions.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def database_name(self):
        r"""Gets the database_name of this PermissionApprovalDetailDTOPermissions.

        库名称

        :return: The database_name of this PermissionApprovalDetailDTOPermissions.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this PermissionApprovalDetailDTOPermissions.

        库名称

        :param database_name: The database_name of this PermissionApprovalDetailDTOPermissions.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def permission_action(self):
        r"""Gets the permission_action of this PermissionApprovalDetailDTOPermissions.

        权限

        :return: The permission_action of this PermissionApprovalDetailDTOPermissions.
        :rtype: list[str]
        """
        return self._permission_action

    @permission_action.setter
    def permission_action(self, permission_action):
        r"""Sets the permission_action of this PermissionApprovalDetailDTOPermissions.

        权限

        :param permission_action: The permission_action of this PermissionApprovalDetailDTOPermissions.
        :type permission_action: list[str]
        """
        self._permission_action = permission_action

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this PermissionApprovalDetailDTOPermissions.

        申请权限所在的空间权限集

        :return: The permission_set_id of this PermissionApprovalDetailDTOPermissions.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this PermissionApprovalDetailDTOPermissions.

        申请权限所在的空间权限集

        :param permission_set_id: The permission_set_id of this PermissionApprovalDetailDTOPermissions.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def schema_name(self):
        r"""Gets the schema_name of this PermissionApprovalDetailDTOPermissions.

        schema名称

        :return: The schema_name of this PermissionApprovalDetailDTOPermissions.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this PermissionApprovalDetailDTOPermissions.

        schema名称

        :param schema_name: The schema_name of this PermissionApprovalDetailDTOPermissions.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def secrecy_level_id(self):
        r"""Gets the secrecy_level_id of this PermissionApprovalDetailDTOPermissions.

        密级

        :return: The secrecy_level_id of this PermissionApprovalDetailDTOPermissions.
        :rtype: str
        """
        return self._secrecy_level_id

    @secrecy_level_id.setter
    def secrecy_level_id(self, secrecy_level_id):
        r"""Sets the secrecy_level_id of this PermissionApprovalDetailDTOPermissions.

        密级

        :param secrecy_level_id: The secrecy_level_id of this PermissionApprovalDetailDTOPermissions.
        :type secrecy_level_id: str
        """
        self._secrecy_level_id = secrecy_level_id

    @property
    def table_name(self):
        r"""Gets the table_name of this PermissionApprovalDetailDTOPermissions.

        表名

        :return: The table_name of this PermissionApprovalDetailDTOPermissions.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this PermissionApprovalDetailDTOPermissions.

        表名

        :param table_name: The table_name of this PermissionApprovalDetailDTOPermissions.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, PermissionApprovalDetailDTOPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
