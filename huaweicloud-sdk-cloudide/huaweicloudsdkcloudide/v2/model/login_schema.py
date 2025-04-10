# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ide_type': 'str',
        'ide_version': 'str',
        'plugin_version': 'str'
    }

    attribute_map = {
        'ide_type': 'ide_type',
        'ide_version': 'ide_version',
        'plugin_version': 'plugin_version'
    }

    def __init__(self, ide_type=None, ide_version=None, plugin_version=None):
        r"""LoginSchema

        The model defined in huaweicloud sdk

        :param ide_type: ide_type
        :type ide_type: str
        :param ide_version: ide_version
        :type ide_version: str
        :param plugin_version: plugin_version
        :type plugin_version: str
        """
        
        

        self._ide_type = None
        self._ide_version = None
        self._plugin_version = None
        self.discriminator = None

        self.ide_type = ide_type
        self.ide_version = ide_version
        self.plugin_version = plugin_version

    @property
    def ide_type(self):
        r"""Gets the ide_type of this LoginSchema.

        ide_type

        :return: The ide_type of this LoginSchema.
        :rtype: str
        """
        return self._ide_type

    @ide_type.setter
    def ide_type(self, ide_type):
        r"""Sets the ide_type of this LoginSchema.

        ide_type

        :param ide_type: The ide_type of this LoginSchema.
        :type ide_type: str
        """
        self._ide_type = ide_type

    @property
    def ide_version(self):
        r"""Gets the ide_version of this LoginSchema.

        ide_version

        :return: The ide_version of this LoginSchema.
        :rtype: str
        """
        return self._ide_version

    @ide_version.setter
    def ide_version(self, ide_version):
        r"""Sets the ide_version of this LoginSchema.

        ide_version

        :param ide_version: The ide_version of this LoginSchema.
        :type ide_version: str
        """
        self._ide_version = ide_version

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this LoginSchema.

        plugin_version

        :return: The plugin_version of this LoginSchema.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this LoginSchema.

        plugin_version

        :param plugin_version: The plugin_version of this LoginSchema.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

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
        if not isinstance(other, LoginSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
