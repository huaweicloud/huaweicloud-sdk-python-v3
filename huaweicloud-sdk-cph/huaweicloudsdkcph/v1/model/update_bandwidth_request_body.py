# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBandwidthRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'band_width_size': 'int'
    }

    attribute_map = {
        'band_width_size': 'band_width_size'
    }

    def __init__(self, band_width_size=None):
        """UpdateBandwidthRequestBody

        The model defined in huaweicloud sdk

        :param band_width_size: - 小于等于300Mbit/s：默认最小增长步长为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小增长步长为50Mbit/s。 - 大于1000Mbit/s：默认最小增长步长为500Mbit/s。
        :type band_width_size: int
        """
        
        

        self._band_width_size = None
        self.discriminator = None

        self.band_width_size = band_width_size

    @property
    def band_width_size(self):
        """Gets the band_width_size of this UpdateBandwidthRequestBody.

        - 小于等于300Mbit/s：默认最小增长步长为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小增长步长为50Mbit/s。 - 大于1000Mbit/s：默认最小增长步长为500Mbit/s。

        :return: The band_width_size of this UpdateBandwidthRequestBody.
        :rtype: int
        """
        return self._band_width_size

    @band_width_size.setter
    def band_width_size(self, band_width_size):
        """Sets the band_width_size of this UpdateBandwidthRequestBody.

        - 小于等于300Mbit/s：默认最小增长步长为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小增长步长为50Mbit/s。 - 大于1000Mbit/s：默认最小增长步长为500Mbit/s。

        :param band_width_size: The band_width_size of this UpdateBandwidthRequestBody.
        :type band_width_size: int
        """
        self._band_width_size = band_width_size

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
        if not isinstance(other, UpdateBandwidthRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
