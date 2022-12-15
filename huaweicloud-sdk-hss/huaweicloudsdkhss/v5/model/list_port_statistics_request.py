# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'type': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'port': 'port',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, port=None, type=None, enterprise_project_id=None, limit=None, offset=None):
        """ListPortStatisticsRequest

        The model defined in huaweicloud sdk

        :param port: 端口号
        :type port: int
        :param type: 端口类型
        :type type: str
        :param enterprise_project_id: 企业项目
        :type enterprise_project_id: str
        :param limit: 默认10
        :type limit: int
        :param offset: 默认是0
        :type offset: int
        """
        
        

        self._port = None
        self._type = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def port(self):
        """Gets the port of this ListPortStatisticsRequest.

        端口号

        :return: The port of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListPortStatisticsRequest.

        端口号

        :param port: The port of this ListPortStatisticsRequest.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this ListPortStatisticsRequest.

        端口类型

        :return: The type of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPortStatisticsRequest.

        端口类型

        :param type: The type of this ListPortStatisticsRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPortStatisticsRequest.

        企业项目

        :return: The enterprise_project_id of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPortStatisticsRequest.

        企业项目

        :param enterprise_project_id: The enterprise_project_id of this ListPortStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListPortStatisticsRequest.

        默认10

        :return: The limit of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPortStatisticsRequest.

        默认10

        :param limit: The limit of this ListPortStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPortStatisticsRequest.

        默认是0

        :return: The offset of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPortStatisticsRequest.

        默认是0

        :param offset: The offset of this ListPortStatisticsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListPortStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
