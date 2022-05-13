# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthCodeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'time': 'str',
        'color': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'name': 'name',
        'time': 'time',
        'color': 'color',
        'confidence': 'confidence'
    }

    def __init__(self, name=None, time=None, color=None, confidence=None):
        """HealthCodeResult

        The model defined in huaweicloud sdk

        :param name: 姓名 
        :type name: str
        :param time: 健康码更新时间 
        :type time: str
        :param color: 健康码颜色，可选值包括： - \&quot;green\&quot; - \&quot;yellow\&quot; - \&quot;red\&quot; - \&quot;gray\&quot; 
        :type color: str
        :param confidence: 各个字段的置信度 
        :type confidence: object
        """
        
        

        self._name = None
        self._time = None
        self._color = None
        self._confidence = None
        self.discriminator = None

        self.name = name
        self.time = time
        self.color = color
        self.confidence = confidence

    @property
    def name(self):
        """Gets the name of this HealthCodeResult.

        姓名 

        :return: The name of this HealthCodeResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthCodeResult.

        姓名 

        :param name: The name of this HealthCodeResult.
        :type name: str
        """
        self._name = name

    @property
    def time(self):
        """Gets the time of this HealthCodeResult.

        健康码更新时间 

        :return: The time of this HealthCodeResult.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this HealthCodeResult.

        健康码更新时间 

        :param time: The time of this HealthCodeResult.
        :type time: str
        """
        self._time = time

    @property
    def color(self):
        """Gets the color of this HealthCodeResult.

        健康码颜色，可选值包括： - \"green\" - \"yellow\" - \"red\" - \"gray\" 

        :return: The color of this HealthCodeResult.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this HealthCodeResult.

        健康码颜色，可选值包括： - \"green\" - \"yellow\" - \"red\" - \"gray\" 

        :param color: The color of this HealthCodeResult.
        :type color: str
        """
        self._color = color

    @property
    def confidence(self):
        """Gets the confidence of this HealthCodeResult.

        各个字段的置信度 

        :return: The confidence of this HealthCodeResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this HealthCodeResult.

        各个字段的置信度 

        :param confidence: The confidence of this HealthCodeResult.
        :type confidence: object
        """
        self._confidence = confidence

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
        if not isinstance(other, HealthCodeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
