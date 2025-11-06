# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAuthorizeTxtRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_name': 'str'
    }

    attribute_map = {
        'zone_name': 'zone_name'
    }

    def __init__(self, zone_name=None):
        r"""ShowAuthorizeTxtRecordRequest

        The model defined in huaweicloud sdk

        :param zone_name: 待创建的子域名。
        :type zone_name: str
        """
        
        

        self._zone_name = None
        self.discriminator = None

        self.zone_name = zone_name

    @property
    def zone_name(self):
        r"""Gets the zone_name of this ShowAuthorizeTxtRecordRequest.

        待创建的子域名。

        :return: The zone_name of this ShowAuthorizeTxtRecordRequest.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this ShowAuthorizeTxtRecordRequest.

        待创建的子域名。

        :param zone_name: The zone_name of this ShowAuthorizeTxtRecordRequest.
        :type zone_name: str
        """
        self._zone_name = zone_name

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
        if not isinstance(other, ShowAuthorizeTxtRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
