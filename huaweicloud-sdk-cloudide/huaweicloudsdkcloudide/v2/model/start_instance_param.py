# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartInstanceParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'plugin_enable_list': 'list[str]',
        'plugin_vars': 'dict(str, str)'
    }

    attribute_map = {
        'plugin_enable_list': 'plugin_enable_list',
        'plugin_vars': 'plugin_vars'
    }

    def __init__(self, plugin_enable_list=None, plugin_vars=None):
        """StartInstanceParam

        The model defined in huaweicloud sdk

        :param plugin_enable_list: 插件列表
        :type plugin_enable_list: list[str]
        :param plugin_vars: 插件参数
        :type plugin_vars: dict(str, str)
        """
        
        

        self._plugin_enable_list = None
        self._plugin_vars = None
        self.discriminator = None

        if plugin_enable_list is not None:
            self.plugin_enable_list = plugin_enable_list
        if plugin_vars is not None:
            self.plugin_vars = plugin_vars

    @property
    def plugin_enable_list(self):
        """Gets the plugin_enable_list of this StartInstanceParam.

        插件列表

        :return: The plugin_enable_list of this StartInstanceParam.
        :rtype: list[str]
        """
        return self._plugin_enable_list

    @plugin_enable_list.setter
    def plugin_enable_list(self, plugin_enable_list):
        """Sets the plugin_enable_list of this StartInstanceParam.

        插件列表

        :param plugin_enable_list: The plugin_enable_list of this StartInstanceParam.
        :type plugin_enable_list: list[str]
        """
        self._plugin_enable_list = plugin_enable_list

    @property
    def plugin_vars(self):
        """Gets the plugin_vars of this StartInstanceParam.

        插件参数

        :return: The plugin_vars of this StartInstanceParam.
        :rtype: dict(str, str)
        """
        return self._plugin_vars

    @plugin_vars.setter
    def plugin_vars(self, plugin_vars):
        """Sets the plugin_vars of this StartInstanceParam.

        插件参数

        :param plugin_vars: The plugin_vars of this StartInstanceParam.
        :type plugin_vars: dict(str, str)
        """
        self._plugin_vars = plugin_vars

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
        if not isinstance(other, StartInstanceParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
