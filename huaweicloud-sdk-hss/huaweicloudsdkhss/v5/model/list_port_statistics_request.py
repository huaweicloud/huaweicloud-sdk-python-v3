# coding: utf-8

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
        'port_string': 'str',
        'type': 'str',
        'enterprise_project_id': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'limit': 'int',
        'offset': 'int',
        'category': 'str'
    }

    attribute_map = {
        'port': 'port',
        'port_string': 'port_string',
        'type': 'type',
        'enterprise_project_id': 'enterprise_project_id',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'limit': 'limit',
        'offset': 'offset',
        'category': 'category'
    }

    def __init__(self, port=None, port_string=None, type=None, enterprise_project_id=None, sort_key=None, sort_dir=None, limit=None, offset=None, category=None):
        """ListPortStatisticsRequest

        The model defined in huaweicloud sdk

        :param port: 端口号，精确匹配
        :type port: int
        :param port_string: 端口字符串，用来进行模糊匹配
        :type port_string: str
        :param type: 端口类型
        :type type: str
        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param sort_key: 排序的key值，目前支持按照端口号port排序
        :type sort_key: str
        :param sort_dir: 升序还是降序，默认升序，asc
        :type sort_dir: str
        :param limit: 每页显示数量
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param category: 类别，默认为host，包含如下： - host：主机 - container：容器
        :type category: str
        """
        
        

        self._port = None
        self._port_string = None
        self._type = None
        self._enterprise_project_id = None
        self._sort_key = None
        self._sort_dir = None
        self._limit = None
        self._offset = None
        self._category = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if port_string is not None:
            self.port_string = port_string
        if type is not None:
            self.type = type
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if category is not None:
            self.category = category

    @property
    def port(self):
        """Gets the port of this ListPortStatisticsRequest.

        端口号，精确匹配

        :return: The port of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ListPortStatisticsRequest.

        端口号，精确匹配

        :param port: The port of this ListPortStatisticsRequest.
        :type port: int
        """
        self._port = port

    @property
    def port_string(self):
        """Gets the port_string of this ListPortStatisticsRequest.

        端口字符串，用来进行模糊匹配

        :return: The port_string of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._port_string

    @port_string.setter
    def port_string(self, port_string):
        """Sets the port_string of this ListPortStatisticsRequest.

        端口字符串，用来进行模糊匹配

        :param port_string: The port_string of this ListPortStatisticsRequest.
        :type port_string: str
        """
        self._port_string = port_string

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

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPortStatisticsRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListPortStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sort_key(self):
        """Gets the sort_key of this ListPortStatisticsRequest.

        排序的key值，目前支持按照端口号port排序

        :return: The sort_key of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListPortStatisticsRequest.

        排序的key值，目前支持按照端口号port排序

        :param sort_key: The sort_key of this ListPortStatisticsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListPortStatisticsRequest.

        升序还是降序，默认升序，asc

        :return: The sort_dir of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListPortStatisticsRequest.

        升序还是降序，默认升序，asc

        :param sort_dir: The sort_dir of this ListPortStatisticsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def limit(self):
        """Gets the limit of this ListPortStatisticsRequest.

        每页显示数量

        :return: The limit of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPortStatisticsRequest.

        每页显示数量

        :param limit: The limit of this ListPortStatisticsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPortStatisticsRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListPortStatisticsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPortStatisticsRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListPortStatisticsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def category(self):
        """Gets the category of this ListPortStatisticsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :return: The category of this ListPortStatisticsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListPortStatisticsRequest.

        类别，默认为host，包含如下： - host：主机 - container：容器

        :param category: The category of this ListPortStatisticsRequest.
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
        if not isinstance(other, ListPortStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
