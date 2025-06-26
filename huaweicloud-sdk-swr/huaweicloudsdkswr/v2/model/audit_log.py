# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'operation': 'str',
        'resource_type': 'str',
        'resource': 'str',
        'username': 'str',
        'op_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'operation': 'operation',
        'resource_type': 'resource_type',
        'resource': 'resource',
        'username': 'username',
        'op_time': 'op_time'
    }

    def __init__(self, id=None, operation=None, resource_type=None, resource=None, username=None, op_time=None):
        r"""AuditLog

        The model defined in huaweicloud sdk

        :param id: audit log ID
        :type id: int
        :param operation: 操作(e.g., create, update, delete)
        :type operation: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource: 资源名称
        :type resource: str
        :param username: 用户ID
        :type username: str
        :param op_time: 操作时间
        :type op_time: datetime
        """
        
        

        self._id = None
        self._operation = None
        self._resource_type = None
        self._resource = None
        self._username = None
        self._op_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if operation is not None:
            self.operation = operation
        if resource_type is not None:
            self.resource_type = resource_type
        if resource is not None:
            self.resource = resource
        if username is not None:
            self.username = username
        if op_time is not None:
            self.op_time = op_time

    @property
    def id(self):
        r"""Gets the id of this AuditLog.

        audit log ID

        :return: The id of this AuditLog.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AuditLog.

        audit log ID

        :param id: The id of this AuditLog.
        :type id: int
        """
        self._id = id

    @property
    def operation(self):
        r"""Gets the operation of this AuditLog.

        操作(e.g., create, update, delete)

        :return: The operation of this AuditLog.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this AuditLog.

        操作(e.g., create, update, delete)

        :param operation: The operation of this AuditLog.
        :type operation: str
        """
        self._operation = operation

    @property
    def resource_type(self):
        r"""Gets the resource_type of this AuditLog.

        资源类型

        :return: The resource_type of this AuditLog.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this AuditLog.

        资源类型

        :param resource_type: The resource_type of this AuditLog.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource(self):
        r"""Gets the resource of this AuditLog.

        资源名称

        :return: The resource of this AuditLog.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this AuditLog.

        资源名称

        :param resource: The resource of this AuditLog.
        :type resource: str
        """
        self._resource = resource

    @property
    def username(self):
        r"""Gets the username of this AuditLog.

        用户ID

        :return: The username of this AuditLog.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this AuditLog.

        用户ID

        :param username: The username of this AuditLog.
        :type username: str
        """
        self._username = username

    @property
    def op_time(self):
        r"""Gets the op_time of this AuditLog.

        操作时间

        :return: The op_time of this AuditLog.
        :rtype: datetime
        """
        return self._op_time

    @op_time.setter
    def op_time(self, op_time):
        r"""Sets the op_time of this AuditLog.

        操作时间

        :param op_time: The op_time of this AuditLog.
        :type op_time: datetime
        """
        self._op_time = op_time

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
        if not isinstance(other, AuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
