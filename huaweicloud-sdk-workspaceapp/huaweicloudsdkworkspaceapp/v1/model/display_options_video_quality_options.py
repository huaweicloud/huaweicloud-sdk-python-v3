# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisplayOptionsVideoQualityOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average_video_quality': 'int',
        'lowest_video_quality': 'int',
        'highest_video_quality': 'int'
    }

    attribute_map = {
        'average_video_quality': 'average_video_quality',
        'lowest_video_quality': 'lowest_video_quality',
        'highest_video_quality': 'highest_video_quality'
    }

    def __init__(self, average_video_quality=None, lowest_video_quality=None, highest_video_quality=None):
        """DisplayOptionsVideoQualityOptions

        The model defined in huaweicloud sdk

        :param average_video_quality: 视频平均质量。取值范围为[5-59]。默认：15。
        :type average_video_quality: int
        :param lowest_video_quality: 视频最低质量。取值范围为[5-69]。默认：25。
        :type lowest_video_quality: int
        :param highest_video_quality: 视频最高质量。取值范围为[1-59]。默认：7。
        :type highest_video_quality: int
        """
        
        

        self._average_video_quality = None
        self._lowest_video_quality = None
        self._highest_video_quality = None
        self.discriminator = None

        if average_video_quality is not None:
            self.average_video_quality = average_video_quality
        if lowest_video_quality is not None:
            self.lowest_video_quality = lowest_video_quality
        if highest_video_quality is not None:
            self.highest_video_quality = highest_video_quality

    @property
    def average_video_quality(self):
        """Gets the average_video_quality of this DisplayOptionsVideoQualityOptions.

        视频平均质量。取值范围为[5-59]。默认：15。

        :return: The average_video_quality of this DisplayOptionsVideoQualityOptions.
        :rtype: int
        """
        return self._average_video_quality

    @average_video_quality.setter
    def average_video_quality(self, average_video_quality):
        """Sets the average_video_quality of this DisplayOptionsVideoQualityOptions.

        视频平均质量。取值范围为[5-59]。默认：15。

        :param average_video_quality: The average_video_quality of this DisplayOptionsVideoQualityOptions.
        :type average_video_quality: int
        """
        self._average_video_quality = average_video_quality

    @property
    def lowest_video_quality(self):
        """Gets the lowest_video_quality of this DisplayOptionsVideoQualityOptions.

        视频最低质量。取值范围为[5-69]。默认：25。

        :return: The lowest_video_quality of this DisplayOptionsVideoQualityOptions.
        :rtype: int
        """
        return self._lowest_video_quality

    @lowest_video_quality.setter
    def lowest_video_quality(self, lowest_video_quality):
        """Sets the lowest_video_quality of this DisplayOptionsVideoQualityOptions.

        视频最低质量。取值范围为[5-69]。默认：25。

        :param lowest_video_quality: The lowest_video_quality of this DisplayOptionsVideoQualityOptions.
        :type lowest_video_quality: int
        """
        self._lowest_video_quality = lowest_video_quality

    @property
    def highest_video_quality(self):
        """Gets the highest_video_quality of this DisplayOptionsVideoQualityOptions.

        视频最高质量。取值范围为[1-59]。默认：7。

        :return: The highest_video_quality of this DisplayOptionsVideoQualityOptions.
        :rtype: int
        """
        return self._highest_video_quality

    @highest_video_quality.setter
    def highest_video_quality(self, highest_video_quality):
        """Sets the highest_video_quality of this DisplayOptionsVideoQualityOptions.

        视频最高质量。取值范围为[1-59]。默认：7。

        :param highest_video_quality: The highest_video_quality of this DisplayOptionsVideoQualityOptions.
        :type highest_video_quality: int
        """
        self._highest_video_quality = highest_video_quality

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
        if not isinstance(other, DisplayOptionsVideoQualityOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
