# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestProlongDurReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auto': 'int',
        'duration': 'int'
    }

    attribute_map = {
        'auto': 'auto',
        'duration': 'duration'
    }

    def __init__(self, auto=None, duration=None):
        """RestProlongDurReqBody

        The model defined in huaweicloud sdk

        :param auto: - 0: 手动延长 - 1: 自动延长（未携带延长时间时，默认每次延长15分钟）
        :type auto: int
        :param duration: 延长时间，单位为分钟。 默认值：15
        :type duration: int
        """
        
        

        self._auto = None
        self._duration = None
        self.discriminator = None

        self.auto = auto
        if duration is not None:
            self.duration = duration

    @property
    def auto(self):
        """Gets the auto of this RestProlongDurReqBody.

        - 0: 手动延长 - 1: 自动延长（未携带延长时间时，默认每次延长15分钟）

        :return: The auto of this RestProlongDurReqBody.
        :rtype: int
        """
        return self._auto

    @auto.setter
    def auto(self, auto):
        """Sets the auto of this RestProlongDurReqBody.

        - 0: 手动延长 - 1: 自动延长（未携带延长时间时，默认每次延长15分钟）

        :param auto: The auto of this RestProlongDurReqBody.
        :type auto: int
        """
        self._auto = auto

    @property
    def duration(self):
        """Gets the duration of this RestProlongDurReqBody.

        延长时间，单位为分钟。 默认值：15

        :return: The duration of this RestProlongDurReqBody.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RestProlongDurReqBody.

        延长时间，单位为分钟。 默认值：15

        :param duration: The duration of this RestProlongDurReqBody.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, RestProlongDurReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
