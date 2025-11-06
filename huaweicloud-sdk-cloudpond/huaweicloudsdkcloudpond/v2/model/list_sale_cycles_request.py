# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSaleCyclesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_code': 'str'
    }

    attribute_map = {
        'zone_code': 'zone_code'
    }

    def __init__(self, zone_code=None):
        r"""ListSaleCyclesRequest

        The model defined in huaweicloud sdk

        :param zone_code: 地区编码
        :type zone_code: str
        """
        
        

        self._zone_code = None
        self.discriminator = None

        if zone_code is not None:
            self.zone_code = zone_code

    @property
    def zone_code(self):
        r"""Gets the zone_code of this ListSaleCyclesRequest.

        地区编码

        :return: The zone_code of this ListSaleCyclesRequest.
        :rtype: str
        """
        return self._zone_code

    @zone_code.setter
    def zone_code(self, zone_code):
        r"""Sets the zone_code of this ListSaleCyclesRequest.

        地区编码

        :param zone_code: The zone_code of this ListSaleCyclesRequest.
        :type zone_code: str
        """
        self._zone_code = zone_code

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
        if not isinstance(other, ListSaleCyclesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
