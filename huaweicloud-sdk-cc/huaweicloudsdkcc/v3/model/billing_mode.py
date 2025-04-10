# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BillingMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing_mode': 'BillingModeEnum'
    }

    attribute_map = {
        'billing_mode': 'billing_mode'
    }

    def __init__(self, billing_mode=None):
        r"""BillingMode

        The model defined in huaweicloud sdk

        :param billing_mode: 
        :type billing_mode: :class:`huaweicloudsdkcc.v3.BillingModeEnum`
        """
        
        

        self._billing_mode = None
        self.discriminator = None

        self.billing_mode = billing_mode

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this BillingMode.

        :return: The billing_mode of this BillingMode.
        :rtype: :class:`huaweicloudsdkcc.v3.BillingModeEnum`
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this BillingMode.

        :param billing_mode: The billing_mode of this BillingMode.
        :type billing_mode: :class:`huaweicloudsdkcc.v3.BillingModeEnum`
        """
        self._billing_mode = billing_mode

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
        if not isinstance(other, BillingMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
