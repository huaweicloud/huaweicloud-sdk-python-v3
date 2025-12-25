# coding: utf-8

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
        'billing_mode': 'int'
    }

    attribute_map = {
        'billing_mode': 'billing_mode'
    }

    def __init__(self, billing_mode=None):
        r"""BillingMode

        The model defined in huaweicloud sdk

        :param billing_mode: 带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期。 2：国际站包周期。 3：大陆站按需计费。 4：国际站按需计费。 5：大陆站按95方式计费。 6：国际站按95方式计费。 7：大陆站按日95方式计费。 8：国际站按日95方式计费。
        :type billing_mode: int
        """
        
        

        self._billing_mode = None
        self.discriminator = None

        self.billing_mode = billing_mode

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this BillingMode.

        带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期。 2：国际站包周期。 3：大陆站按需计费。 4：国际站按需计费。 5：大陆站按95方式计费。 6：国际站按95方式计费。 7：大陆站按日95方式计费。 8：国际站按日95方式计费。

        :return: The billing_mode of this BillingMode.
        :rtype: int
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this BillingMode.

        带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期。 2：国际站包周期。 3：大陆站按需计费。 4：国际站按需计费。 5：大陆站按95方式计费。 6：国际站按95方式计费。 7：大陆站按日95方式计费。 8：国际站按日95方式计费。

        :param billing_mode: The billing_mode of this BillingMode.
        :type billing_mode: int
        """
        self._billing_mode = billing_mode

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
        if not isinstance(other, BillingMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
