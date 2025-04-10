# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvironmentHostsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'environment_id': 'str',
        'key_field': 'str',
        'as_proxy': 'bool',
        'page_index': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'application_id': 'application_id',
        'environment_id': 'environment_id',
        'key_field': 'key_field',
        'as_proxy': 'as_proxy',
        'page_index': 'page_index',
        'page_size': 'page_size'
    }

    def __init__(self, application_id=None, environment_id=None, key_field=None, as_proxy=None, page_index=None, page_size=None):
        r"""ListEnvironmentHostsRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用id
        :type application_id: str
        :param environment_id: 环境id
        :type environment_id: str
        :param key_field: 主机名、ip关键字模糊搜索
        :type key_field: str
        :param as_proxy: 是否为代理机,true为代理机
        :type as_proxy: bool
        :param page_index: 分页页码
        :type page_index: int
        :param page_size: 分页查询每页条数
        :type page_size: int
        """
        
        

        self._application_id = None
        self._environment_id = None
        self._key_field = None
        self._as_proxy = None
        self._page_index = None
        self._page_size = None
        self.discriminator = None

        self.application_id = application_id
        self.environment_id = environment_id
        if key_field is not None:
            self.key_field = key_field
        if as_proxy is not None:
            self.as_proxy = as_proxy
        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size

    @property
    def application_id(self):
        r"""Gets the application_id of this ListEnvironmentHostsRequest.

        应用id

        :return: The application_id of this ListEnvironmentHostsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListEnvironmentHostsRequest.

        应用id

        :param application_id: The application_id of this ListEnvironmentHostsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def environment_id(self):
        r"""Gets the environment_id of this ListEnvironmentHostsRequest.

        环境id

        :return: The environment_id of this ListEnvironmentHostsRequest.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        r"""Sets the environment_id of this ListEnvironmentHostsRequest.

        环境id

        :param environment_id: The environment_id of this ListEnvironmentHostsRequest.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def key_field(self):
        r"""Gets the key_field of this ListEnvironmentHostsRequest.

        主机名、ip关键字模糊搜索

        :return: The key_field of this ListEnvironmentHostsRequest.
        :rtype: str
        """
        return self._key_field

    @key_field.setter
    def key_field(self, key_field):
        r"""Sets the key_field of this ListEnvironmentHostsRequest.

        主机名、ip关键字模糊搜索

        :param key_field: The key_field of this ListEnvironmentHostsRequest.
        :type key_field: str
        """
        self._key_field = key_field

    @property
    def as_proxy(self):
        r"""Gets the as_proxy of this ListEnvironmentHostsRequest.

        是否为代理机,true为代理机

        :return: The as_proxy of this ListEnvironmentHostsRequest.
        :rtype: bool
        """
        return self._as_proxy

    @as_proxy.setter
    def as_proxy(self, as_proxy):
        r"""Sets the as_proxy of this ListEnvironmentHostsRequest.

        是否为代理机,true为代理机

        :param as_proxy: The as_proxy of this ListEnvironmentHostsRequest.
        :type as_proxy: bool
        """
        self._as_proxy = as_proxy

    @property
    def page_index(self):
        r"""Gets the page_index of this ListEnvironmentHostsRequest.

        分页页码

        :return: The page_index of this ListEnvironmentHostsRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListEnvironmentHostsRequest.

        分页页码

        :param page_index: The page_index of this ListEnvironmentHostsRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListEnvironmentHostsRequest.

        分页查询每页条数

        :return: The page_size of this ListEnvironmentHostsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListEnvironmentHostsRequest.

        分页查询每页条数

        :param page_size: The page_size of this ListEnvironmentHostsRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListEnvironmentHostsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
