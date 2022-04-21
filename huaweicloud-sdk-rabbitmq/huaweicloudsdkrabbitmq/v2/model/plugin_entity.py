# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'running': 'bool',
        'enable': 'bool',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'running': 'running',
        'enable': 'enable',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, running=None, enable=None, name=None, version=None):
        """PluginEntity

        The model defined in huaweicloud sdk

        :param running: 是否运行。
        :type running: bool
        :param enable: 是否启用。
        :type enable: bool
        :param name: 插件名称。
        :type name: str
        :param version: 插件版本。
        :type version: str
        """
        
        

        self._running = None
        self._enable = None
        self._name = None
        self._version = None
        self.discriminator = None

        if running is not None:
            self.running = running
        if enable is not None:
            self.enable = enable
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def running(self):
        """Gets the running of this PluginEntity.

        是否运行。

        :return: The running of this PluginEntity.
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this PluginEntity.

        是否运行。

        :param running: The running of this PluginEntity.
        :type running: bool
        """
        self._running = running

    @property
    def enable(self):
        """Gets the enable of this PluginEntity.

        是否启用。

        :return: The enable of this PluginEntity.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this PluginEntity.

        是否启用。

        :param enable: The enable of this PluginEntity.
        :type enable: bool
        """
        self._enable = enable

    @property
    def name(self):
        """Gets the name of this PluginEntity.

        插件名称。

        :return: The name of this PluginEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PluginEntity.

        插件名称。

        :param name: The name of this PluginEntity.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this PluginEntity.

        插件版本。

        :return: The version of this PluginEntity.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PluginEntity.

        插件版本。

        :param version: The version of this PluginEntity.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, PluginEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
