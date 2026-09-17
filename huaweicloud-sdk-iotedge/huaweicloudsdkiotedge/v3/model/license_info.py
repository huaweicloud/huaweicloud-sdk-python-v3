# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LicenseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'esn': 'str',
        'expire_time': 'str',
        'grace_time': 'str'
    }

    attribute_map = {
        'esn': 'esn',
        'expire_time': 'expire_time',
        'grace_time': 'grace_time'
    }

    def __init__(self, esn=None, expire_time=None, grace_time=None):
        r"""LicenseInfo

        The model defined in huaweicloud sdk

        :param esn: esn码
        :type esn: str
        :param expire_time: 超期时间
        :type expire_time: str
        :param grace_time: 宽限期
        :type grace_time: str
        """
        
        

        self._esn = None
        self._expire_time = None
        self._grace_time = None
        self.discriminator = None

        self.esn = esn
        self.expire_time = expire_time
        if grace_time is not None:
            self.grace_time = grace_time

    @property
    def esn(self):
        r"""Gets the esn of this LicenseInfo.

        esn码

        :return: The esn of this LicenseInfo.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        r"""Sets the esn of this LicenseInfo.

        esn码

        :param esn: The esn of this LicenseInfo.
        :type esn: str
        """
        self._esn = esn

    @property
    def expire_time(self):
        r"""Gets the expire_time of this LicenseInfo.

        超期时间

        :return: The expire_time of this LicenseInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this LicenseInfo.

        超期时间

        :param expire_time: The expire_time of this LicenseInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def grace_time(self):
        r"""Gets the grace_time of this LicenseInfo.

        宽限期

        :return: The grace_time of this LicenseInfo.
        :rtype: str
        """
        return self._grace_time

    @grace_time.setter
    def grace_time(self, grace_time):
        r"""Sets the grace_time of this LicenseInfo.

        宽限期

        :param grace_time: The grace_time of this LicenseInfo.
        :type grace_time: str
        """
        self._grace_time = grace_time

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
        if not isinstance(other, LicenseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
