# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerAutoTerminateTimeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'auto_terminate_time': 'str'
    }

    attribute_map = {
        'auto_terminate_time': 'auto_terminate_time'
    }

    def __init__(self, auto_terminate_time=None):
        """UpdateServerAutoTerminateTimeRequestBody

        The model defined in huaweicloud sdk

        :param auto_terminate_time: 销毁时间
        :type auto_terminate_time: str
        """
        
        

        self._auto_terminate_time = None
        self.discriminator = None

        self.auto_terminate_time = auto_terminate_time

    @property
    def auto_terminate_time(self):
        """Gets the auto_terminate_time of this UpdateServerAutoTerminateTimeRequestBody.

        销毁时间

        :return: The auto_terminate_time of this UpdateServerAutoTerminateTimeRequestBody.
        :rtype: str
        """
        return self._auto_terminate_time

    @auto_terminate_time.setter
    def auto_terminate_time(self, auto_terminate_time):
        """Sets the auto_terminate_time of this UpdateServerAutoTerminateTimeRequestBody.

        销毁时间

        :param auto_terminate_time: The auto_terminate_time of this UpdateServerAutoTerminateTimeRequestBody.
        :type auto_terminate_time: str
        """
        self._auto_terminate_time = auto_terminate_time

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
        if not isinstance(other, UpdateServerAutoTerminateTimeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
