# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cert:

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
        'description': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, type=None):
        """Cert

        The model defined in huaweicloud sdk

        :param name: 证书名称
        :type name: str
        :param description: 证书描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param type: 证书类型，包含： - application：应用证书 - device：设备证书
        :type type: str
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type

    @property
    def name(self):
        """Gets the name of this Cert.

        证书名称

        :return: The name of this Cert.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cert.

        证书名称

        :param name: The name of this Cert.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Cert.

        证书描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this Cert.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Cert.

        证书描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this Cert.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this Cert.

        证书类型，包含： - application：应用证书 - device：设备证书

        :return: The type of this Cert.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Cert.

        证书类型，包含： - application：应用证书 - device：设备证书

        :param type: The type of this Cert.
        :type type: str
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
        if not isinstance(other, Cert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
