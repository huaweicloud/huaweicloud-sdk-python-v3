# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointConnection:

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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'domain_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'marker_id': 'marker_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'domain_id': 'domain_id',
        'status': 'status'
    }

    def __init__(self, id=None, marker_id=None, created_at=None, updated_at=None, domain_id=None, status=None):
        r"""EndpointConnection

        The model defined in huaweicloud sdk

        :param id: 连接编号
        :type id: str
        :param marker_id: 连接报文标识
        :type marker_id: int
        :param created_at: 连接创建时间。UTC时间，格式：YYYY-MM-DDTHH:MM:SSZ
        :type created_at: datetime
        :param updated_at: 连接更新时间。UTC时间，格式：YYYY-MM-DDTHH:MM:SSZ
        :type updated_at: datetime
        :param domain_id: 用户的Domain ID
        :type domain_id: str
        :param status: 连接状态 - pendingAcceptance 待接受 - creating 创建中 - accepted 已接受 - rejected 已拒绝 - failed 失败 - deleting 删除中
        :type status: str
        """
        
        

        self._id = None
        self._marker_id = None
        self._created_at = None
        self._updated_at = None
        self._domain_id = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.marker_id = marker_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.domain_id = domain_id
        self.status = status

    @property
    def id(self):
        r"""Gets the id of this EndpointConnection.

        连接编号

        :return: The id of this EndpointConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EndpointConnection.

        连接编号

        :param id: The id of this EndpointConnection.
        :type id: str
        """
        self._id = id

    @property
    def marker_id(self):
        r"""Gets the marker_id of this EndpointConnection.

        连接报文标识

        :return: The marker_id of this EndpointConnection.
        :rtype: int
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        r"""Sets the marker_id of this EndpointConnection.

        连接报文标识

        :param marker_id: The marker_id of this EndpointConnection.
        :type marker_id: int
        """
        self._marker_id = marker_id

    @property
    def created_at(self):
        r"""Gets the created_at of this EndpointConnection.

        连接创建时间。UTC时间，格式：YYYY-MM-DDTHH:MM:SSZ

        :return: The created_at of this EndpointConnection.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EndpointConnection.

        连接创建时间。UTC时间，格式：YYYY-MM-DDTHH:MM:SSZ

        :param created_at: The created_at of this EndpointConnection.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this EndpointConnection.

        连接更新时间。UTC时间，格式：YYYY-MM-DDTHH:MM:SSZ

        :return: The updated_at of this EndpointConnection.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this EndpointConnection.

        连接更新时间。UTC时间，格式：YYYY-MM-DDTHH:MM:SSZ

        :param updated_at: The updated_at of this EndpointConnection.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def domain_id(self):
        r"""Gets the domain_id of this EndpointConnection.

        用户的Domain ID

        :return: The domain_id of this EndpointConnection.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this EndpointConnection.

        用户的Domain ID

        :param domain_id: The domain_id of this EndpointConnection.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def status(self):
        r"""Gets the status of this EndpointConnection.

        连接状态 - pendingAcceptance 待接受 - creating 创建中 - accepted 已接受 - rejected 已拒绝 - failed 失败 - deleting 删除中

        :return: The status of this EndpointConnection.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EndpointConnection.

        连接状态 - pendingAcceptance 待接受 - creating 创建中 - accepted 已接受 - rejected 已拒绝 - failed 失败 - deleting 删除中

        :param status: The status of this EndpointConnection.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, EndpointConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
