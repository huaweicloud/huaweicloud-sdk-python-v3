# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpCodeSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'http_codes': 'list[HttpCode]',
        'time': 'str'
    }

    attribute_map = {
        'http_codes': 'http_codes',
        'time': 'time'
    }

    def __init__(self, http_codes=None, time=None):
        """HttpCodeSummary

        The model defined in huaweicloud sdk

        :param http_codes: 状态码信息
        :type http_codes: list[:class:`huaweicloudsdklive.v2.HttpCode`]
        :param time: 采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。
        :type time: str
        """
        
        

        self._http_codes = None
        self._time = None
        self.discriminator = None

        if http_codes is not None:
            self.http_codes = http_codes
        if time is not None:
            self.time = time

    @property
    def http_codes(self):
        """Gets the http_codes of this HttpCodeSummary.

        状态码信息

        :return: The http_codes of this HttpCodeSummary.
        :rtype: list[:class:`huaweicloudsdklive.v2.HttpCode`]
        """
        return self._http_codes

    @http_codes.setter
    def http_codes(self, http_codes):
        """Sets the http_codes of this HttpCodeSummary.

        状态码信息

        :param http_codes: The http_codes of this HttpCodeSummary.
        :type http_codes: list[:class:`huaweicloudsdklive.v2.HttpCode`]
        """
        self._http_codes = http_codes

    @property
    def time(self):
        """Gets the time of this HttpCodeSummary.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :return: The time of this HttpCodeSummary.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this HttpCodeSummary.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :param time: The time of this HttpCodeSummary.
        :type time: str
        """
        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpCodeSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
