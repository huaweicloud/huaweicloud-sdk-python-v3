# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerProcess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_window': 'int',
        'reply_mode': 'str',
        'reply_texts': 'list[str]',
        'reply_order': 'str'
    }

    attribute_map = {
        'time_window': 'time_window',
        'reply_mode': 'reply_mode',
        'reply_texts': 'reply_texts',
        'reply_order': 'reply_order'
    }

    def __init__(self, time_window=None, reply_mode=None, reply_texts=None, reply_order=None):
        """TriggerProcess

        The model defined in huaweicloud sdk

        :param time_window: 处理抑制时长。单位秒。  -1 表示整场直播 0 表示无抑制，每次都触发
        :type time_window: int
        :param reply_mode: 回复类型。 SYSTEM_REPLY：系统自动回复设置的话术
        :type reply_mode: str
        :param reply_texts: 回复话术集
        :type reply_texts: list[str]
        :param reply_order: 回复次序 - RANDOM：随机 - ORDER：顺序循环
        :type reply_order: str
        """
        
        

        self._time_window = None
        self._reply_mode = None
        self._reply_texts = None
        self._reply_order = None
        self.discriminator = None

        if time_window is not None:
            self.time_window = time_window
        if reply_mode is not None:
            self.reply_mode = reply_mode
        if reply_texts is not None:
            self.reply_texts = reply_texts
        if reply_order is not None:
            self.reply_order = reply_order

    @property
    def time_window(self):
        """Gets the time_window of this TriggerProcess.

        处理抑制时长。单位秒。  -1 表示整场直播 0 表示无抑制，每次都触发

        :return: The time_window of this TriggerProcess.
        :rtype: int
        """
        return self._time_window

    @time_window.setter
    def time_window(self, time_window):
        """Sets the time_window of this TriggerProcess.

        处理抑制时长。单位秒。  -1 表示整场直播 0 表示无抑制，每次都触发

        :param time_window: The time_window of this TriggerProcess.
        :type time_window: int
        """
        self._time_window = time_window

    @property
    def reply_mode(self):
        """Gets the reply_mode of this TriggerProcess.

        回复类型。 SYSTEM_REPLY：系统自动回复设置的话术

        :return: The reply_mode of this TriggerProcess.
        :rtype: str
        """
        return self._reply_mode

    @reply_mode.setter
    def reply_mode(self, reply_mode):
        """Sets the reply_mode of this TriggerProcess.

        回复类型。 SYSTEM_REPLY：系统自动回复设置的话术

        :param reply_mode: The reply_mode of this TriggerProcess.
        :type reply_mode: str
        """
        self._reply_mode = reply_mode

    @property
    def reply_texts(self):
        """Gets the reply_texts of this TriggerProcess.

        回复话术集

        :return: The reply_texts of this TriggerProcess.
        :rtype: list[str]
        """
        return self._reply_texts

    @reply_texts.setter
    def reply_texts(self, reply_texts):
        """Sets the reply_texts of this TriggerProcess.

        回复话术集

        :param reply_texts: The reply_texts of this TriggerProcess.
        :type reply_texts: list[str]
        """
        self._reply_texts = reply_texts

    @property
    def reply_order(self):
        """Gets the reply_order of this TriggerProcess.

        回复次序 - RANDOM：随机 - ORDER：顺序循环

        :return: The reply_order of this TriggerProcess.
        :rtype: str
        """
        return self._reply_order

    @reply_order.setter
    def reply_order(self, reply_order):
        """Sets the reply_order of this TriggerProcess.

        回复次序 - RANDOM：随机 - ORDER：顺序循环

        :param reply_order: The reply_order of this TriggerProcess.
        :type reply_order: str
        """
        self._reply_order = reply_order

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
        if not isinstance(other, TriggerProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
