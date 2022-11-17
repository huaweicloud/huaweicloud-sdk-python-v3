# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputRequest:

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
        'property_reference': 'PropertyReferenceReq'
    }

    attribute_map = {
        'name': 'name',
        'property_reference': 'property_reference'
    }

    def __init__(self, name=None, property_reference=None):
        """InputRequest

        The model defined in huaweicloud sdk

        :param name: 参数名，正则： \&quot;^[A-Za-z][A-Za-z_]{0,31}$\&quot;
        :type name: str
        :param property_reference: 
        :type property_reference: :class:`huaweicloudsdkiotanalytics.v1.PropertyReferenceReq`
        """
        
        

        self._name = None
        self._property_reference = None
        self.discriminator = None

        self.name = name
        self.property_reference = property_reference

    @property
    def name(self):
        """Gets the name of this InputRequest.

        参数名，正则： \"^[A-Za-z][A-Za-z_]{0,31}$\"

        :return: The name of this InputRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputRequest.

        参数名，正则： \"^[A-Za-z][A-Za-z_]{0,31}$\"

        :param name: The name of this InputRequest.
        :type name: str
        """
        self._name = name

    @property
    def property_reference(self):
        """Gets the property_reference of this InputRequest.

        :return: The property_reference of this InputRequest.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.PropertyReferenceReq`
        """
        return self._property_reference

    @property_reference.setter
    def property_reference(self, property_reference):
        """Sets the property_reference of this InputRequest.

        :param property_reference: The property_reference of this InputRequest.
        :type property_reference: :class:`huaweicloudsdkiotanalytics.v1.PropertyReferenceReq`
        """
        self._property_reference = property_reference

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
        if not isinstance(other, InputRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
