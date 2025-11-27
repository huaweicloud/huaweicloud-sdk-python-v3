# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssociatedZonesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dns_suffix': 'list[str]'
    }

    attribute_map = {
        'dns_suffix': 'dnsSuffix'
    }

    def __init__(self, dns_suffix=None):
        r"""UpdateAssociatedZonesRequest

        The model defined in huaweicloud sdk

        :param dns_suffix: 在联邦管理的域名访问功能中，用于更改根域名
        :type dns_suffix: list[str]
        """
        
        

        self._dns_suffix = None
        self.discriminator = None

        if dns_suffix is not None:
            self.dns_suffix = dns_suffix

    @property
    def dns_suffix(self):
        r"""Gets the dns_suffix of this UpdateAssociatedZonesRequest.

        在联邦管理的域名访问功能中，用于更改根域名

        :return: The dns_suffix of this UpdateAssociatedZonesRequest.
        :rtype: list[str]
        """
        return self._dns_suffix

    @dns_suffix.setter
    def dns_suffix(self, dns_suffix):
        r"""Sets the dns_suffix of this UpdateAssociatedZonesRequest.

        在联邦管理的域名访问功能中，用于更改根域名

        :param dns_suffix: The dns_suffix of this UpdateAssociatedZonesRequest.
        :type dns_suffix: list[str]
        """
        self._dns_suffix = dns_suffix

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
        if not isinstance(other, UpdateAssociatedZonesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
