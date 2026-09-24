# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateExpirationTimeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expect_expiration_date': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'expect_expiration_date': 'expect_expiration_date',
        'time_zone': 'time_zone'
    }

    def __init__(self, expect_expiration_date=None, time_zone=None):
        r"""UpdateExpirationTimeReq

        The model defined in huaweicloud sdk

        :param expect_expiration_date: 预期过期日期，格式：YYYY-MM-DD。
        :type expect_expiration_date: str
        :param time_zone: 用户所在时区，格式形如 UTC+08:00
        :type time_zone: str
        """
        
        

        self._expect_expiration_date = None
        self._time_zone = None
        self.discriminator = None

        self.expect_expiration_date = expect_expiration_date
        self.time_zone = time_zone

    @property
    def expect_expiration_date(self):
        r"""Gets the expect_expiration_date of this UpdateExpirationTimeReq.

        预期过期日期，格式：YYYY-MM-DD。

        :return: The expect_expiration_date of this UpdateExpirationTimeReq.
        :rtype: str
        """
        return self._expect_expiration_date

    @expect_expiration_date.setter
    def expect_expiration_date(self, expect_expiration_date):
        r"""Sets the expect_expiration_date of this UpdateExpirationTimeReq.

        预期过期日期，格式：YYYY-MM-DD。

        :param expect_expiration_date: The expect_expiration_date of this UpdateExpirationTimeReq.
        :type expect_expiration_date: str
        """
        self._expect_expiration_date = expect_expiration_date

    @property
    def time_zone(self):
        r"""Gets the time_zone of this UpdateExpirationTimeReq.

        用户所在时区，格式形如 UTC+08:00

        :return: The time_zone of this UpdateExpirationTimeReq.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this UpdateExpirationTimeReq.

        用户所在时区，格式形如 UTC+08:00

        :param time_zone: The time_zone of this UpdateExpirationTimeReq.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, UpdateExpirationTimeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
