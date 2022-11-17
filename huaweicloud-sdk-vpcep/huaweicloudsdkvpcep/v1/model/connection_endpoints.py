# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionEndpoints:

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
        'marker_id': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'domain_id': 'str',
        'error': 'list[QueryError]',
        'status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'marker_id': 'marker_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'error': 'error',
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, id=None, marker_id=None, created_at=None, updated_at=None, domain_id=None, error=None, status=None, description=None):
        """ConnectionEndpoints

        The model defined in huaweicloud sdk

        :param id: 终端节点的ID，唯一标识。
        :type id: str
        :param marker_id: 终端节点的报文标识。
        :type marker_id: int
        :param created_at: 终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ
        :type created_at: str
        :param updated_at: 终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ
        :type updated_at: str
        :param domain_id: 用户的Domain ID。
        :type domain_id: str
        :param error: 错误信息。  当终端节点服务状态异常，即“status”的值为“failed”时，会返回该字段。
        :type error: list[:class:`huaweicloudsdkvpcep.v1.QueryError`]
        :param status: 终端节点的连接状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败 ● deleting：删除中
        :type status: str
        :param description: 终端节点连接描述。
        :type description: str
        """
        
        

        self._id = None
        self._marker_id = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._error = None
        self._status = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if marker_id is not None:
            self.marker_id = marker_id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if domain_id is not None:
            self.domain_id = domain_id
        if error is not None:
            self.error = error
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ConnectionEndpoints.

        终端节点的ID，唯一标识。

        :return: The id of this ConnectionEndpoints.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectionEndpoints.

        终端节点的ID，唯一标识。

        :param id: The id of this ConnectionEndpoints.
        :type id: str
        """
        self._id = id

    @property
    def marker_id(self):
        """Gets the marker_id of this ConnectionEndpoints.

        终端节点的报文标识。

        :return: The marker_id of this ConnectionEndpoints.
        :rtype: int
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        """Sets the marker_id of this ConnectionEndpoints.

        终端节点的报文标识。

        :param marker_id: The marker_id of this ConnectionEndpoints.
        :type marker_id: int
        """
        self._marker_id = marker_id

    @property
    def created_at(self):
        """Gets the created_at of this ConnectionEndpoints.

        终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :return: The created_at of this ConnectionEndpoints.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConnectionEndpoints.

        终端节点的创建时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :param created_at: The created_at of this ConnectionEndpoints.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ConnectionEndpoints.

        终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :return: The updated_at of this ConnectionEndpoints.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ConnectionEndpoints.

        终端节点的更新时间。 采用UTC时间格式，格式为：YYYY-MMDDTHH:MM:SSZ

        :param updated_at: The updated_at of this ConnectionEndpoints.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        """Gets the domain_id of this ConnectionEndpoints.

        用户的Domain ID。

        :return: The domain_id of this ConnectionEndpoints.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ConnectionEndpoints.

        用户的Domain ID。

        :param domain_id: The domain_id of this ConnectionEndpoints.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def error(self):
        """Gets the error of this ConnectionEndpoints.

        错误信息。  当终端节点服务状态异常，即“status”的值为“failed”时，会返回该字段。

        :return: The error of this ConnectionEndpoints.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.QueryError`]
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ConnectionEndpoints.

        错误信息。  当终端节点服务状态异常，即“status”的值为“failed”时，会返回该字段。

        :param error: The error of this ConnectionEndpoints.
        :type error: list[:class:`huaweicloudsdkvpcep.v1.QueryError`]
        """
        self._error = error

    @property
    def status(self):
        """Gets the status of this ConnectionEndpoints.

        终端节点的连接状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败 ● deleting：删除中

        :return: The status of this ConnectionEndpoints.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectionEndpoints.

        终端节点的连接状态。 ● pendingAcceptance：待接受 ● creating：创建中 ● accepted：已接受 ● rejected：已拒绝 ● failed：失败 ● deleting：删除中

        :param status: The status of this ConnectionEndpoints.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this ConnectionEndpoints.

        终端节点连接描述。

        :return: The description of this ConnectionEndpoints.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectionEndpoints.

        终端节点连接描述。

        :param description: The description of this ConnectionEndpoints.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ConnectionEndpoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
