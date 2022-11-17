# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutputWatermarkPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_duration': 'int'
    }

    attribute_map = {
        'time_duration': 'time_duration'
    }

    def __init__(self, time_duration=None):
        """OutputWatermarkPara

        The model defined in huaweicloud sdk

        :param time_duration: 水印时长 
        :type time_duration: int
        """
        
        

        self._time_duration = None
        self.discriminator = None

        if time_duration is not None:
            self.time_duration = time_duration

    @property
    def time_duration(self):
        """Gets the time_duration of this OutputWatermarkPara.

        水印时长 

        :return: The time_duration of this OutputWatermarkPara.
        :rtype: int
        """
        return self._time_duration

    @time_duration.setter
    def time_duration(self, time_duration):
        """Sets the time_duration of this OutputWatermarkPara.

        水印时长 

        :param time_duration: The time_duration of this OutputWatermarkPara.
        :type time_duration: int
        """
        self._time_duration = time_duration

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
        if not isinstance(other, OutputWatermarkPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
