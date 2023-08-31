# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNewHostsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'key_field': 'str',
        'environment_id': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'sort_key': 'str',
        'sort_dir': 'str',
        'as_proxy': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'key_field': 'key_field',
        'environment_id': 'environment_id',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'as_proxy': 'as_proxy'
    }

    def __init__(self, group_id=None, key_field=None, environment_id=None, page_index=None, page_size=None, sort_key=None, sort_dir=None, as_proxy=None):
        """ListNewHostsRequest

        The model defined in huaweicloud sdk

        :param group_id: 项目ID
        :type group_id: str
        :param key_field: 主机名模糊查询信息
        :type key_field: str
        :param environment_id: 环境id
        :type environment_id: str
        :param page_index: 页码数
        :type page_index: int
        :param page_size: 每页显示的条目数量，默认为10
        :type page_size: int
        :param sort_key: 排序字段：as_proxy|host_name|owner_name，不传使用默认排序
        :type sort_key: str
        :param sort_dir: 排序方式：DESC、ASC，默认为DESC
        :type sort_dir: str
        :param as_proxy: 是否为代理机
        :type as_proxy: bool
        """
        
        

        self._group_id = None
        self._key_field = None
        self._environment_id = None
        self._page_index = None
        self._page_size = None
        self._sort_key = None
        self._sort_dir = None
        self._as_proxy = None
        self.discriminator = None

        self.group_id = group_id
        if key_field is not None:
            self.key_field = key_field
        if environment_id is not None:
            self.environment_id = environment_id
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if as_proxy is not None:
            self.as_proxy = as_proxy

    @property
    def group_id(self):
        """Gets the group_id of this ListNewHostsRequest.

        项目ID

        :return: The group_id of this ListNewHostsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListNewHostsRequest.

        项目ID

        :param group_id: The group_id of this ListNewHostsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def key_field(self):
        """Gets the key_field of this ListNewHostsRequest.

        主机名模糊查询信息

        :return: The key_field of this ListNewHostsRequest.
        :rtype: str
        """
        return self._key_field

    @key_field.setter
    def key_field(self, key_field):
        """Sets the key_field of this ListNewHostsRequest.

        主机名模糊查询信息

        :param key_field: The key_field of this ListNewHostsRequest.
        :type key_field: str
        """
        self._key_field = key_field

    @property
    def environment_id(self):
        """Gets the environment_id of this ListNewHostsRequest.

        环境id

        :return: The environment_id of this ListNewHostsRequest.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ListNewHostsRequest.

        环境id

        :param environment_id: The environment_id of this ListNewHostsRequest.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def page_index(self):
        """Gets the page_index of this ListNewHostsRequest.

        页码数

        :return: The page_index of this ListNewHostsRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        """Sets the page_index of this ListNewHostsRequest.

        页码数

        :param page_index: The page_index of this ListNewHostsRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        """Gets the page_size of this ListNewHostsRequest.

        每页显示的条目数量，默认为10

        :return: The page_size of this ListNewHostsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListNewHostsRequest.

        每页显示的条目数量，默认为10

        :param page_size: The page_size of this ListNewHostsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def sort_key(self):
        """Gets the sort_key of this ListNewHostsRequest.

        排序字段：as_proxy|host_name|owner_name，不传使用默认排序

        :return: The sort_key of this ListNewHostsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListNewHostsRequest.

        排序字段：as_proxy|host_name|owner_name，不传使用默认排序

        :param sort_key: The sort_key of this ListNewHostsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListNewHostsRequest.

        排序方式：DESC、ASC，默认为DESC

        :return: The sort_dir of this ListNewHostsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListNewHostsRequest.

        排序方式：DESC、ASC，默认为DESC

        :param sort_dir: The sort_dir of this ListNewHostsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def as_proxy(self):
        """Gets the as_proxy of this ListNewHostsRequest.

        是否为代理机

        :return: The as_proxy of this ListNewHostsRequest.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        """Sets the as_proxy of this ListNewHostsRequest.

        是否为代理机

        :param as_proxy: The as_proxy of this ListNewHostsRequest.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

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
        if not isinstance(other, ListNewHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
