# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'plugin_provider': 'str',
        'plugin_type': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'offset': 'offset',
        'limit': 'limit',
        'plugin_provider': 'plugin_provider',
        'plugin_type': 'plugin_type'
    }

    def __init__(self, x_app_user_id=None, offset=None, limit=None, plugin_provider=None, plugin_type=None):
        r"""ListPluginConfigRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param plugin_provider: 插件供应商  * BOCHA:博查  * AMAP_WEATHER：高德天气
        :type plugin_provider: str
        :param plugin_type: 插件类型  * WEATHER_QUERY：天气查询  * WEB_SEARCH：网络搜索
        :type plugin_type: str
        """
        
        

        self._x_app_user_id = None
        self._offset = None
        self._limit = None
        self._plugin_provider = None
        self._plugin_type = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if plugin_provider is not None:
            self.plugin_provider = plugin_provider
        if plugin_type is not None:
            self.plugin_type = plugin_type

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ListPluginConfigRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ListPluginConfigRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ListPluginConfigRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ListPluginConfigRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def offset(self):
        r"""Gets the offset of this ListPluginConfigRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ListPluginConfigRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPluginConfigRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ListPluginConfigRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPluginConfigRequest.

        每页显示的条目数量。

        :return: The limit of this ListPluginConfigRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPluginConfigRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListPluginConfigRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def plugin_provider(self):
        r"""Gets the plugin_provider of this ListPluginConfigRequest.

        插件供应商  * BOCHA:博查  * AMAP_WEATHER：高德天气

        :return: The plugin_provider of this ListPluginConfigRequest.
        :rtype: str
        """
        return self._plugin_provider

    @plugin_provider.setter
    def plugin_provider(self, plugin_provider):
        r"""Sets the plugin_provider of this ListPluginConfigRequest.

        插件供应商  * BOCHA:博查  * AMAP_WEATHER：高德天气

        :param plugin_provider: The plugin_provider of this ListPluginConfigRequest.
        :type plugin_provider: str
        """
        self._plugin_provider = plugin_provider

    @property
    def plugin_type(self):
        r"""Gets the plugin_type of this ListPluginConfigRequest.

        插件类型  * WEATHER_QUERY：天气查询  * WEB_SEARCH：网络搜索

        :return: The plugin_type of this ListPluginConfigRequest.
        :rtype: str
        """
        return self._plugin_type

    @plugin_type.setter
    def plugin_type(self, plugin_type):
        r"""Sets the plugin_type of this ListPluginConfigRequest.

        插件类型  * WEATHER_QUERY：天气查询  * WEB_SEARCH：网络搜索

        :param plugin_type: The plugin_type of this ListPluginConfigRequest.
        :type plugin_type: str
        """
        self._plugin_type = plugin_type

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
        if not isinstance(other, ListPluginConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
