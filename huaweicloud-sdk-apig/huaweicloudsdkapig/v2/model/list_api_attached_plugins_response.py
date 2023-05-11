# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiAttachedPluginsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'plugins': 'list[AttachedPluginInfo]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'plugins': 'plugins'
    }

    def __init__(self, size=None, total=None, plugins=None):
        """ListApiAttachedPluginsResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param plugins: 绑定API的插件列表。
        :type plugins: list[:class:`huaweicloudsdkapig.v2.AttachedPluginInfo`]
        """
        
        super(ListApiAttachedPluginsResponse, self).__init__()

        self._size = None
        self._total = None
        self._plugins = None
        self.discriminator = None

        self.size = size
        self.total = total
        if plugins is not None:
            self.plugins = plugins

    @property
    def size(self):
        """Gets the size of this ListApiAttachedPluginsResponse.

        本次返回的列表长度

        :return: The size of this ListApiAttachedPluginsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListApiAttachedPluginsResponse.

        本次返回的列表长度

        :param size: The size of this ListApiAttachedPluginsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        """Gets the total of this ListApiAttachedPluginsResponse.

        满足条件的记录数

        :return: The total of this ListApiAttachedPluginsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListApiAttachedPluginsResponse.

        满足条件的记录数

        :param total: The total of this ListApiAttachedPluginsResponse.
        :type total: int
        """
        self._total = total

    @property
    def plugins(self):
        """Gets the plugins of this ListApiAttachedPluginsResponse.

        绑定API的插件列表。

        :return: The plugins of this ListApiAttachedPluginsResponse.
        :rtype: list[:class:`huaweicloudsdkapig.v2.AttachedPluginInfo`]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this ListApiAttachedPluginsResponse.

        绑定API的插件列表。

        :param plugins: The plugins of this ListApiAttachedPluginsResponse.
        :type plugins: list[:class:`huaweicloudsdkapig.v2.AttachedPluginInfo`]
        """
        self._plugins = plugins

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
        if not isinstance(other, ListApiAttachedPluginsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
