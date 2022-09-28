# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessageClearRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message_retain_time': 'int',
        'message_retain_number': 'int'
    }

    attribute_map = {
        'message_retain_time': 'message_retain_time',
        'message_retain_number': 'message_retain_number'
    }

    def __init__(self, message_retain_time=None, message_retain_number=None):
        """ShowMessageClearRuleResponse

        The model defined in huaweicloud sdk

        :param message_retain_time: 保存时长，单位：天
        :type message_retain_time: int
        :param message_retain_number: 最多保留记录数
        :type message_retain_number: int
        """
        
        super(ShowMessageClearRuleResponse, self).__init__()

        self._message_retain_time = None
        self._message_retain_number = None
        self.discriminator = None

        if message_retain_time is not None:
            self.message_retain_time = message_retain_time
        if message_retain_number is not None:
            self.message_retain_number = message_retain_number

    @property
    def message_retain_time(self):
        """Gets the message_retain_time of this ShowMessageClearRuleResponse.

        保存时长，单位：天

        :return: The message_retain_time of this ShowMessageClearRuleResponse.
        :rtype: int
        """
        return self._message_retain_time

    @message_retain_time.setter
    def message_retain_time(self, message_retain_time):
        """Sets the message_retain_time of this ShowMessageClearRuleResponse.

        保存时长，单位：天

        :param message_retain_time: The message_retain_time of this ShowMessageClearRuleResponse.
        :type message_retain_time: int
        """
        self._message_retain_time = message_retain_time

    @property
    def message_retain_number(self):
        """Gets the message_retain_number of this ShowMessageClearRuleResponse.

        最多保留记录数

        :return: The message_retain_number of this ShowMessageClearRuleResponse.
        :rtype: int
        """
        return self._message_retain_number

    @message_retain_number.setter
    def message_retain_number(self, message_retain_number):
        """Sets the message_retain_number of this ShowMessageClearRuleResponse.

        最多保留记录数

        :param message_retain_number: The message_retain_number of this ShowMessageClearRuleResponse.
        :type message_retain_number: int
        """
        self._message_retain_number = message_retain_number

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
        if not isinstance(other, ShowMessageClearRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
