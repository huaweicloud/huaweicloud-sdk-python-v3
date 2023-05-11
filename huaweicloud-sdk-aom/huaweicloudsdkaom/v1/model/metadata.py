# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'configuration': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'configuration': 'configuration'
    }

    def __init__(self, type=None, configuration=None):
        """Metadata

        The model defined in huaweicloud sdk

        :param type: 节点类型。
        :type type: str
        :param configuration: 配置信息。
        :type configuration: dict(str, object)
        """
        
        

        self._type = None
        self._configuration = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if configuration is not None:
            self.configuration = configuration

    @property
    def type(self):
        """Gets the type of this Metadata.

        节点类型。

        :return: The type of this Metadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Metadata.

        节点类型。

        :param type: The type of this Metadata.
        :type type: str
        """
        self._type = type

    @property
    def configuration(self):
        """Gets the configuration of this Metadata.

        配置信息。

        :return: The configuration of this Metadata.
        :rtype: dict(str, object)
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this Metadata.

        配置信息。

        :param configuration: The configuration of this Metadata.
        :type configuration: dict(str, object)
        """
        self._configuration = configuration

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
