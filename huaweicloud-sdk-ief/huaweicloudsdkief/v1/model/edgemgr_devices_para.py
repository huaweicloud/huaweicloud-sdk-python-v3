# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgemgrDevicesPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'attributes': 'dict(str, ValueInAttributes)'
    }

    attribute_map = {
        'description': 'description',
        'attributes': 'attributes'
    }

    def __init__(self, description=None, attributes=None):
        r"""EdgemgrDevicesPara

        The model defined in huaweicloud sdk

        :param description: 终端设备描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param attributes: 终端设备静态属性
        :type attributes: dict(str, ValueInAttributes)
        """
        
        

        self._description = None
        self._attributes = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if attributes is not None:
            self.attributes = attributes

    @property
    def description(self):
        r"""Gets the description of this EdgemgrDevicesPara.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this EdgemgrDevicesPara.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EdgemgrDevicesPara.

        终端设备描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this EdgemgrDevicesPara.
        :type description: str
        """
        self._description = description

    @property
    def attributes(self):
        r"""Gets the attributes of this EdgemgrDevicesPara.

        终端设备静态属性

        :return: The attributes of this EdgemgrDevicesPara.
        :rtype: dict(str, ValueInAttributes)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this EdgemgrDevicesPara.

        终端设备静态属性

        :param attributes: The attributes of this EdgemgrDevicesPara.
        :type attributes: dict(str, ValueInAttributes)
        """
        self._attributes = attributes

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
        if not isinstance(other, EdgemgrDevicesPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
