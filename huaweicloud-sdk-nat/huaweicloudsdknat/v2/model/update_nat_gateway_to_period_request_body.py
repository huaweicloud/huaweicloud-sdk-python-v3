# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNatGatewayToPeriodRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prepaid_options': 'PrepaidOptions'
    }

    attribute_map = {
        'prepaid_options': 'prepaid_options'
    }

    def __init__(self, prepaid_options=None):
        r"""UpdateNatGatewayToPeriodRequestBody

        The model defined in huaweicloud sdk

        :param prepaid_options: 
        :type prepaid_options: :class:`huaweicloudsdknat.v2.PrepaidOptions`
        """
        
        

        self._prepaid_options = None
        self.discriminator = None

        if prepaid_options is not None:
            self.prepaid_options = prepaid_options

    @property
    def prepaid_options(self):
        r"""Gets the prepaid_options of this UpdateNatGatewayToPeriodRequestBody.

        :return: The prepaid_options of this UpdateNatGatewayToPeriodRequestBody.
        :rtype: :class:`huaweicloudsdknat.v2.PrepaidOptions`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        r"""Sets the prepaid_options of this UpdateNatGatewayToPeriodRequestBody.

        :param prepaid_options: The prepaid_options of this UpdateNatGatewayToPeriodRequestBody.
        :type prepaid_options: :class:`huaweicloudsdknat.v2.PrepaidOptions`
        """
        self._prepaid_options = prepaid_options

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
        if not isinstance(other, UpdateNatGatewayToPeriodRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
