# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScreenRecordsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_limit_type': 'str'
    }

    attribute_map = {
        'traffic_limit_type': 'traffic_limit_type'
    }

    def __init__(self, traffic_limit_type=None):
        r"""UpdateScreenRecordsRequestBody

        The model defined in huaweicloud sdk

        :param traffic_limit_type: 录屏限速类型
        :type traffic_limit_type: str
        """
        
        

        self._traffic_limit_type = None
        self.discriminator = None

        self.traffic_limit_type = traffic_limit_type

    @property
    def traffic_limit_type(self):
        r"""Gets the traffic_limit_type of this UpdateScreenRecordsRequestBody.

        录屏限速类型

        :return: The traffic_limit_type of this UpdateScreenRecordsRequestBody.
        :rtype: str
        """
        return self._traffic_limit_type

    @traffic_limit_type.setter
    def traffic_limit_type(self, traffic_limit_type):
        r"""Sets the traffic_limit_type of this UpdateScreenRecordsRequestBody.

        录屏限速类型

        :param traffic_limit_type: The traffic_limit_type of this UpdateScreenRecordsRequestBody.
        :type traffic_limit_type: str
        """
        self._traffic_limit_type = traffic_limit_type

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
        if not isinstance(other, UpdateScreenRecordsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
