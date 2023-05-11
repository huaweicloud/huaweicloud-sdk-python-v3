# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_type': 'str',
        'schema_name': 'str',
        'description': 'str',
        'status': 'str',
        'failed_reason': 'str',
        'failed_detail': 'str',
        'suggest_solution': 'list[str]'
    }

    attribute_map = {
        'permission_type': 'permission_type',
        'schema_name': 'schema_name',
        'description': 'description',
        'status': 'status',
        'failed_reason': 'failed_reason',
        'failed_detail': 'failed_detail',
        'suggest_solution': 'suggest_solution'
    }

    def __init__(self, permission_type=None, schema_name=None, description=None, status=None, failed_reason=None, failed_detail=None, suggest_solution=None):
        """PermissionItem

        The model defined in huaweicloud sdk

        :param permission_type: 权限类型。
        :type permission_type: str
        :param schema_name: schema名称。
        :type schema_name: str
        :param description: 权限描述。
        :type description: str
        :param status: 是否通过。
        :type status: str
        :param failed_reason: 失败原因。
        :type failed_reason: str
        :param failed_detail: 失败详情。
        :type failed_detail: str
        :param suggest_solution: 解决建议。
        :type suggest_solution: list[str]
        """
        
        

        self._permission_type = None
        self._schema_name = None
        self._description = None
        self._status = None
        self._failed_reason = None
        self._failed_detail = None
        self._suggest_solution = None
        self.discriminator = None

        if permission_type is not None:
            self.permission_type = permission_type
        if schema_name is not None:
            self.schema_name = schema_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_detail is not None:
            self.failed_detail = failed_detail
        if suggest_solution is not None:
            self.suggest_solution = suggest_solution

    @property
    def permission_type(self):
        """Gets the permission_type of this PermissionItem.

        权限类型。

        :return: The permission_type of this PermissionItem.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this PermissionItem.

        权限类型。

        :param permission_type: The permission_type of this PermissionItem.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def schema_name(self):
        """Gets the schema_name of this PermissionItem.

        schema名称。

        :return: The schema_name of this PermissionItem.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this PermissionItem.

        schema名称。

        :param schema_name: The schema_name of this PermissionItem.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def description(self):
        """Gets the description of this PermissionItem.

        权限描述。

        :return: The description of this PermissionItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PermissionItem.

        权限描述。

        :param description: The description of this PermissionItem.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this PermissionItem.

        是否通过。

        :return: The status of this PermissionItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PermissionItem.

        是否通过。

        :param status: The status of this PermissionItem.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        """Gets the failed_reason of this PermissionItem.

        失败原因。

        :return: The failed_reason of this PermissionItem.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this PermissionItem.

        失败原因。

        :param failed_reason: The failed_reason of this PermissionItem.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_detail(self):
        """Gets the failed_detail of this PermissionItem.

        失败详情。

        :return: The failed_detail of this PermissionItem.
        :rtype: str
        """
        return self._failed_detail

    @failed_detail.setter
    def failed_detail(self, failed_detail):
        """Sets the failed_detail of this PermissionItem.

        失败详情。

        :param failed_detail: The failed_detail of this PermissionItem.
        :type failed_detail: str
        """
        self._failed_detail = failed_detail

    @property
    def suggest_solution(self):
        """Gets the suggest_solution of this PermissionItem.

        解决建议。

        :return: The suggest_solution of this PermissionItem.
        :rtype: list[str]
        """
        return self._suggest_solution

    @suggest_solution.setter
    def suggest_solution(self, suggest_solution):
        """Sets the suggest_solution of this PermissionItem.

        解决建议。

        :param suggest_solution: The suggest_solution of this PermissionItem.
        :type suggest_solution: list[str]
        """
        self._suggest_solution = suggest_solution

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
        if not isinstance(other, PermissionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
