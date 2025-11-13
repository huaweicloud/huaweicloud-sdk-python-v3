# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOcspSwitchRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ocsp_switch': 'bool'
    }

    attribute_map = {
        'ocsp_switch': 'ocsp_switch'
    }

    def __init__(self, ocsp_switch=None):
        r"""UpdateOcspSwitchRequestBody

        The model defined in huaweicloud sdk

        :param ocsp_switch: 启用或禁用OCSP。
        :type ocsp_switch: bool
        """
        
        

        self._ocsp_switch = None
        self.discriminator = None

        self.ocsp_switch = ocsp_switch

    @property
    def ocsp_switch(self):
        r"""Gets the ocsp_switch of this UpdateOcspSwitchRequestBody.

        启用或禁用OCSP。

        :return: The ocsp_switch of this UpdateOcspSwitchRequestBody.
        :rtype: bool
        """
        return self._ocsp_switch

    @ocsp_switch.setter
    def ocsp_switch(self, ocsp_switch):
        r"""Sets the ocsp_switch of this UpdateOcspSwitchRequestBody.

        启用或禁用OCSP。

        :param ocsp_switch: The ocsp_switch of this UpdateOcspSwitchRequestBody.
        :type ocsp_switch: bool
        """
        self._ocsp_switch = ocsp_switch

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
        if not isinstance(other, UpdateOcspSwitchRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
