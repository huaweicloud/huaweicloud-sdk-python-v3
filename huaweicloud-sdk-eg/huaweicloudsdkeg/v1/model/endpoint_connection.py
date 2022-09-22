# coding: utf-8

import re
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
        'endpoint_service_id': 'str',
        'endpoint_service_name': 'str',
        'marker_id': 'str',
        'id': 'str',
        'ip': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'endpoint_service_id': 'endpoint_service_id',
        'endpoint_service_name': 'endpoint_service_name',
        'marker_id': 'marker_id',
        'id': 'id',
        'ip': 'ip',
        'created_time': 'created_time'
    }

    def __init__(self, endpoint_service_id=None, endpoint_service_name=None, marker_id=None, id=None, ip=None, created_time=None):
        """EndpointConnection

        The model defined in huaweicloud sdk

        :param endpoint_service_id: 访问端点的服务ID
        :type endpoint_service_id: str
        :param endpoint_service_name: 访问端点的服务名称
        :type endpoint_service_name: str
        :param marker_id: 访问端点的终端节点的报文ID
        :type marker_id: str
        :param id: 访问端点的终端节点ID
        :type id: str
        :param ip: 访问端点的终端节点IP
        :type ip: str
        :param created_time: 访问端点的终端节点创建时间
        :type created_time: str
        """
        
        

        self._endpoint_service_id = None
        self._endpoint_service_name = None
        self._marker_id = None
        self._id = None
        self._ip = None
        self._created_time = None
        self.discriminator = None

        if endpoint_service_id is not None:
            self.endpoint_service_id = endpoint_service_id
        if endpoint_service_name is not None:
            self.endpoint_service_name = endpoint_service_name
        if marker_id is not None:
            self.marker_id = marker_id
        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if created_time is not None:
            self.created_time = created_time

    @property
    def endpoint_service_id(self):
        """Gets the endpoint_service_id of this EndpointConnection.

        访问端点的服务ID

        :return: The endpoint_service_id of this EndpointConnection.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        """Sets the endpoint_service_id of this EndpointConnection.

        访问端点的服务ID

        :param endpoint_service_id: The endpoint_service_id of this EndpointConnection.
        :type endpoint_service_id: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def endpoint_service_name(self):
        """Gets the endpoint_service_name of this EndpointConnection.

        访问端点的服务名称

        :return: The endpoint_service_name of this EndpointConnection.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        """Sets the endpoint_service_name of this EndpointConnection.

        访问端点的服务名称

        :param endpoint_service_name: The endpoint_service_name of this EndpointConnection.
        :type endpoint_service_name: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def marker_id(self):
        """Gets the marker_id of this EndpointConnection.

        访问端点的终端节点的报文ID

        :return: The marker_id of this EndpointConnection.
        :rtype: str
        """
        return self._marker_id

    @marker_id.setter
    def marker_id(self, marker_id):
        """Sets the marker_id of this EndpointConnection.

        访问端点的终端节点的报文ID

        :param marker_id: The marker_id of this EndpointConnection.
        :type marker_id: str
        """
        self._marker_id = marker_id

    @property
    def id(self):
        """Gets the id of this EndpointConnection.

        访问端点的终端节点ID

        :return: The id of this EndpointConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EndpointConnection.

        访问端点的终端节点ID

        :param id: The id of this EndpointConnection.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this EndpointConnection.

        访问端点的终端节点IP

        :return: The ip of this EndpointConnection.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this EndpointConnection.

        访问端点的终端节点IP

        :param ip: The ip of this EndpointConnection.
        :type ip: str
        """
        self._ip = ip

    @property
    def created_time(self):
        """Gets the created_time of this EndpointConnection.

        访问端点的终端节点创建时间

        :return: The created_time of this EndpointConnection.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EndpointConnection.

        访问端点的终端节点创建时间

        :param created_time: The created_time of this EndpointConnection.
        :type created_time: str
        """
        self._created_time = created_time

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
