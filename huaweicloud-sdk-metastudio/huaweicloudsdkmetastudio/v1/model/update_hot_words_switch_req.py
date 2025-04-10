# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHotWordsSwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'enable_hot_words': 'bool'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'enable_hot_words': 'enable_hot_words'
    }

    def __init__(self, robot_id=None, enable_hot_words=None):
        r"""UpdateHotWordsSwitchReq

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param enable_hot_words: 热词功能开关。
        :type enable_hot_words: bool
        """
        
        

        self._robot_id = None
        self._enable_hot_words = None
        self.discriminator = None

        self.robot_id = robot_id
        self.enable_hot_words = enable_hot_words

    @property
    def robot_id(self):
        r"""Gets the robot_id of this UpdateHotWordsSwitchReq.

        应用ID。

        :return: The robot_id of this UpdateHotWordsSwitchReq.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this UpdateHotWordsSwitchReq.

        应用ID。

        :param robot_id: The robot_id of this UpdateHotWordsSwitchReq.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def enable_hot_words(self):
        r"""Gets the enable_hot_words of this UpdateHotWordsSwitchReq.

        热词功能开关。

        :return: The enable_hot_words of this UpdateHotWordsSwitchReq.
        :rtype: bool
        """
        return self._enable_hot_words

    @enable_hot_words.setter
    def enable_hot_words(self, enable_hot_words):
        r"""Sets the enable_hot_words of this UpdateHotWordsSwitchReq.

        热词功能开关。

        :param enable_hot_words: The enable_hot_words of this UpdateHotWordsSwitchReq.
        :type enable_hot_words: bool
        """
        self._enable_hot_words = enable_hot_words

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
        if not isinstance(other, UpdateHotWordsSwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
