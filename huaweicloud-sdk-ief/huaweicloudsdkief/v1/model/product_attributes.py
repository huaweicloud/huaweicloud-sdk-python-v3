# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductAttributes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'str',
        'metadata': 'ProductMetadata'
    }

    attribute_map = {
        'value': 'value',
        'metadata': 'metadata'
    }

    def __init__(self, value=None, metadata=None):
        r"""ProductAttributes

        The model defined in huaweicloud sdk

        :param value: 产品属性值
        :type value: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkief.v1.ProductMetadata`
        """
        
        

        self._value = None
        self._metadata = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if metadata is not None:
            self.metadata = metadata

    @property
    def value(self):
        r"""Gets the value of this ProductAttributes.

        产品属性值

        :return: The value of this ProductAttributes.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ProductAttributes.

        产品属性值

        :param value: The value of this ProductAttributes.
        :type value: str
        """
        self._value = value

    @property
    def metadata(self):
        r"""Gets the metadata of this ProductAttributes.

        :return: The metadata of this ProductAttributes.
        :rtype: :class:`huaweicloudsdkief.v1.ProductMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ProductAttributes.

        :param metadata: The metadata of this ProductAttributes.
        :type metadata: :class:`huaweicloudsdkief.v1.ProductMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, ProductAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
