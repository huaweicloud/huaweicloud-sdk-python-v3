# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestarInstanceInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    def __init__(self, type=None):
        """RestarInstanceInfo - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self.discriminator = None

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this RestarInstanceInfo.

        重启的类型，soft或者hard。 - soft表示软重启（只重启进程）。 - hard表示强制重启（重启虚拟机）。

        :return: The type of this RestarInstanceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestarInstanceInfo.

        重启的类型，soft或者hard。 - soft表示软重启（只重启进程）。 - hard表示强制重启（重启虚拟机）。

        :param type: The type of this RestarInstanceInfo.
        :type: str
        """
        self._type = type

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RestarInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
