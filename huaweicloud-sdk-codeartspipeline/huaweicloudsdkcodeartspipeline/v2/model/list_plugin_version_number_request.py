# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginVersionNumberRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'plugin_name': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'plugin_name': 'plugin_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, plugin_name=None, offset=None, limit=None):
        """ListPluginVersionNumberRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param plugin_name: 插件名
        :type plugin_name: str
        :param offset: 偏移
        :type offset: str
        :param limit: 大小
        :type limit: str
        """
        
        

        self._domain_id = None
        self._plugin_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        """Gets the domain_id of this ListPluginVersionNumberRequest.

        租户ID

        :return: The domain_id of this ListPluginVersionNumberRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListPluginVersionNumberRequest.

        租户ID

        :param domain_id: The domain_id of this ListPluginVersionNumberRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this ListPluginVersionNumberRequest.

        插件名

        :return: The plugin_name of this ListPluginVersionNumberRequest.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this ListPluginVersionNumberRequest.

        插件名

        :param plugin_name: The plugin_name of this ListPluginVersionNumberRequest.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def offset(self):
        """Gets the offset of this ListPluginVersionNumberRequest.

        偏移

        :return: The offset of this ListPluginVersionNumberRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPluginVersionNumberRequest.

        偏移

        :param offset: The offset of this ListPluginVersionNumberRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPluginVersionNumberRequest.

        大小

        :return: The limit of this ListPluginVersionNumberRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPluginVersionNumberRequest.

        大小

        :param limit: The limit of this ListPluginVersionNumberRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListPluginVersionNumberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
