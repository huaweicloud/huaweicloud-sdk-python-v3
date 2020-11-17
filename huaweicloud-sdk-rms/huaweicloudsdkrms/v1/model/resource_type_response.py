# coding: utf-8

import pprint
import re

import six





class ResourceTypeResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'display_name': 'str',
        '_global': 'bool',
        'regions': 'list[str]',
        'console_endpoint_id': 'str',
        'console_list_url': 'str',
        'console_detail_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        '_global': 'global',
        'regions': 'regions',
        'console_endpoint_id': 'console_endpoint_id',
        'console_list_url': 'console_list_url',
        'console_detail_url': 'console_detail_url'
    }

    def __init__(self, name=None, display_name=None, _global=None, regions=None, console_endpoint_id=None, console_list_url=None, console_detail_url=None):
        """ResourceTypeResponse - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._display_name = None
        self.__global = None
        self._regions = None
        self._console_endpoint_id = None
        self._console_list_url = None
        self._console_detail_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if _global is not None:
            self._global = _global
        if regions is not None:
            self.regions = regions
        if console_endpoint_id is not None:
            self.console_endpoint_id = console_endpoint_id
        if console_list_url is not None:
            self.console_list_url = console_list_url
        if console_detail_url is not None:
            self.console_detail_url = console_detail_url

    @property
    def name(self):
        """Gets the name of this ResourceTypeResponse.

        资源类型名称

        :return: The name of this ResourceTypeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceTypeResponse.

        资源类型名称

        :param name: The name of this ResourceTypeResponse.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this ResourceTypeResponse.

        资源类型显示名称，可以通过请求中 'X-Language'设置语言

        :return: The display_name of this ResourceTypeResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ResourceTypeResponse.

        资源类型显示名称，可以通过请求中 'X-Language'设置语言

        :param display_name: The display_name of this ResourceTypeResponse.
        :type: str
        """
        self._display_name = display_name

    @property
    def _global(self):
        """Gets the _global of this ResourceTypeResponse.

        是否是全局类型的资源

        :return: The _global of this ResourceTypeResponse.
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this ResourceTypeResponse.

        是否是全局类型的资源

        :param _global: The _global of this ResourceTypeResponse.
        :type: bool
        """
        self.__global = _global

    @property
    def regions(self):
        """Gets the regions of this ResourceTypeResponse.

        支持的region列表

        :return: The regions of this ResourceTypeResponse.
        :rtype: list[str]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ResourceTypeResponse.

        支持的region列表

        :param regions: The regions of this ResourceTypeResponse.
        :type: list[str]
        """
        self._regions = regions

    @property
    def console_endpoint_id(self):
        """Gets the console_endpoint_id of this ResourceTypeResponse.

        console对应的地址

        :return: The console_endpoint_id of this ResourceTypeResponse.
        :rtype: str
        """
        return self._console_endpoint_id

    @console_endpoint_id.setter
    def console_endpoint_id(self, console_endpoint_id):
        """Sets the console_endpoint_id of this ResourceTypeResponse.

        console对应的地址

        :param console_endpoint_id: The console_endpoint_id of this ResourceTypeResponse.
        :type: str
        """
        self._console_endpoint_id = console_endpoint_id

    @property
    def console_list_url(self):
        """Gets the console_list_url of this ResourceTypeResponse.

        console列表页地址

        :return: The console_list_url of this ResourceTypeResponse.
        :rtype: str
        """
        return self._console_list_url

    @console_list_url.setter
    def console_list_url(self, console_list_url):
        """Sets the console_list_url of this ResourceTypeResponse.

        console列表页地址

        :param console_list_url: The console_list_url of this ResourceTypeResponse.
        :type: str
        """
        self._console_list_url = console_list_url

    @property
    def console_detail_url(self):
        """Gets the console_detail_url of this ResourceTypeResponse.

        console详情页地址

        :return: The console_detail_url of this ResourceTypeResponse.
        :rtype: str
        """
        return self._console_detail_url

    @console_detail_url.setter
    def console_detail_url(self, console_detail_url):
        """Sets the console_detail_url of this ResourceTypeResponse.

        console详情页地址

        :param console_detail_url: The console_detail_url of this ResourceTypeResponse.
        :type: str
        """
        self._console_detail_url = console_detail_url

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
