# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandShareRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extend': 'Extend'
    }

    attribute_map = {
        'extend': 'extend'
    }

    def __init__(self, extend=None):
        """ExpandShareRequestBody

        The model defined in huaweicloud sdk

        :param extend: 
        :type extend: :class:`huaweicloudsdksfsturbo.v1.Extend`
        """
        
        

        self._extend = None
        self.discriminator = None

        self.extend = extend

    @property
    def extend(self):
        """Gets the extend of this ExpandShareRequestBody.

        :return: The extend of this ExpandShareRequestBody.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.Extend`
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ExpandShareRequestBody.

        :param extend: The extend of this ExpandShareRequestBody.
        :type extend: :class:`huaweicloudsdksfsturbo.v1.Extend`
        """
        self._extend = extend

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
        if not isinstance(other, ExpandShareRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
