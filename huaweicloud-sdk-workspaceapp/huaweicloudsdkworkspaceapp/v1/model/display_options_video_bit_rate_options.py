# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisplayOptionsVideoBitRateOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average_video_bit_rate': 'int'
    }

    attribute_map = {
        'average_video_bit_rate': 'average_video_bit_rate'
    }

    def __init__(self, average_video_bit_rate=None):
        """DisplayOptionsVideoBitRateOptions

        The model defined in huaweicloud sdk

        :param average_video_bit_rate: 视频平均码率（Kbps）。取值范围为[256-100000]。默认：18000。
        :type average_video_bit_rate: int
        """
        
        

        self._average_video_bit_rate = None
        self.discriminator = None

        if average_video_bit_rate is not None:
            self.average_video_bit_rate = average_video_bit_rate

    @property
    def average_video_bit_rate(self):
        """Gets the average_video_bit_rate of this DisplayOptionsVideoBitRateOptions.

        视频平均码率（Kbps）。取值范围为[256-100000]。默认：18000。

        :return: The average_video_bit_rate of this DisplayOptionsVideoBitRateOptions.
        :rtype: int
        """
        return self._average_video_bit_rate

    @average_video_bit_rate.setter
    def average_video_bit_rate(self, average_video_bit_rate):
        """Sets the average_video_bit_rate of this DisplayOptionsVideoBitRateOptions.

        视频平均码率（Kbps）。取值范围为[256-100000]。默认：18000。

        :param average_video_bit_rate: The average_video_bit_rate of this DisplayOptionsVideoBitRateOptions.
        :type average_video_bit_rate: int
        """
        self._average_video_bit_rate = average_video_bit_rate

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
        if not isinstance(other, DisplayOptionsVideoBitRateOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
