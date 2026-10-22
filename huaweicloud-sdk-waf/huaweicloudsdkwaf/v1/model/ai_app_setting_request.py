# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiAppSettingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_sign': 'ApiSign'
    }

    attribute_map = {
        'api_sign': 'api_sign'
    }

    def __init__(self, api_sign=None):
        r"""AiAppSettingRequest

        The model defined in huaweicloud sdk

        :param api_sign: 
        :type api_sign: :class:`huaweicloudsdkwaf.v1.ApiSign`
        """
        
        

        self._api_sign = None
        self.discriminator = None

        if api_sign is not None:
            self.api_sign = api_sign

    @property
    def api_sign(self):
        r"""Gets the api_sign of this AiAppSettingRequest.

        :return: The api_sign of this AiAppSettingRequest.
        :rtype: :class:`huaweicloudsdkwaf.v1.ApiSign`
        """
        return self._api_sign

    @api_sign.setter
    def api_sign(self, api_sign):
        r"""Sets the api_sign of this AiAppSettingRequest.

        :param api_sign: The api_sign of this AiAppSettingRequest.
        :type api_sign: :class:`huaweicloudsdkwaf.v1.ApiSign`
        """
        self._api_sign = api_sign

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
        if not isinstance(other, AiAppSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
