# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomQosLimit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l4': 'L4Limit',
        'l7': 'L7Limit'
    }

    attribute_map = {
        'l4': 'l4',
        'l7': 'l7'
    }

    def __init__(self, l4=None, l7=None):
        r"""CustomQosLimit

        The model defined in huaweicloud sdk

        :param l4: 
        :type l4: :class:`huaweicloudsdkelb.v3.L4Limit`
        :param l7: 
        :type l7: :class:`huaweicloudsdkelb.v3.L7Limit`
        """
        
        

        self._l4 = None
        self._l7 = None
        self.discriminator = None

        if l4 is not None:
            self.l4 = l4
        if l7 is not None:
            self.l7 = l7

    @property
    def l4(self):
        r"""Gets the l4 of this CustomQosLimit.

        :return: The l4 of this CustomQosLimit.
        :rtype: :class:`huaweicloudsdkelb.v3.L4Limit`
        """
        return self._l4

    @l4.setter
    def l4(self, l4):
        r"""Sets the l4 of this CustomQosLimit.

        :param l4: The l4 of this CustomQosLimit.
        :type l4: :class:`huaweicloudsdkelb.v3.L4Limit`
        """
        self._l4 = l4

    @property
    def l7(self):
        r"""Gets the l7 of this CustomQosLimit.

        :return: The l7 of this CustomQosLimit.
        :rtype: :class:`huaweicloudsdkelb.v3.L7Limit`
        """
        return self._l7

    @l7.setter
    def l7(self, l7):
        r"""Sets the l7 of this CustomQosLimit.

        :param l7: The l7 of this CustomQosLimit.
        :type l7: :class:`huaweicloudsdkelb.v3.L7Limit`
        """
        self._l7 = l7

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomQosLimit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
