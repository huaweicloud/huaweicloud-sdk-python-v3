# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'port': 'int',
        'type': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'category': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'port': 'port',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'category': 'category'
    }

    def __init__(self, host_id=None, host_name=None, host_ip=None, port=None, type=None, enterprise_project_id=None, limit=None, offset=None, category=None):
        """ListPortsRequest

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param host_name: 主机名称
        :type host_name: str
        :param host_ip: 主机ip
        :type host_ip: str
        :param port: 端口号
        :type port: int
        :param type: 端口类型：目前包括TCP，UDP两种
        :type type: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param category: 类别，默认为host，包含如下： - host：主机 - container：容器
        :type category: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._port = None
        self._type = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._category = None
        self.discriminator = None

        self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
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
        if category is not None:
            self.category = category

    @property
    def host_id(self):
        """Gets the host_id of this ListPortsRequest.

        主机id

        :return: The host_id of this ListPortsRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListPortsRequest.

        主机id

        :param host_id: The host_id of this ListPortsRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this ListPortsRequest.

        主机名称

        :return: The host_name of this ListPortsRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListPortsRequest.

        主机名称

        :param host_name: The host_name of this ListPortsRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this ListPortsRequest.

        主机ip

        :return: The host_ip of this ListPortsRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListPortsRequest.

        主机ip

        :param host_ip: The host_ip of this ListPortsRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def port(self):
        """Gets the port of this ListPortsRequest.

        端口号

        :return: The port of this ListPortsRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListPortsRequest.

        端口号

        :param port: The port of this ListPortsRequest.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this ListPortsRequest.

        端口类型：目前包括TCP，UDP两种

        :return: The type of this ListPortsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPortsRequest.

        端口类型：目前包括TCP，UDP两种

        :param type: The type of this ListPortsRequest.
        :type type: str
        """
        self._type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPortsRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListPortsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPortsRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListPortsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        """Gets the limit of this ListPortsRequest.

        每页显示数量

        :return: The limit of this ListPortsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPortsRequest.

        每页显示数量

        :param limit: The limit of this ListPortsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPortsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListPortsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPortsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListPortsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def category(self):
        """Gets the category of this ListPortsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :return: The category of this ListPortsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListPortsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :param category: The category of this ListPortsRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
