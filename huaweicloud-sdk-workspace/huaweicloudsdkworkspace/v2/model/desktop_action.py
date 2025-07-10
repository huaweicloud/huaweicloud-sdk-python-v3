# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'message': 'str',
        'start_time': 'str',
        'finish_time': 'str',
        'result': 'str',
        'traceback': 'str'
    }

    attribute_map = {
        'action': 'action',
        'message': 'message',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'result': 'result',
        'traceback': 'traceback'
    }

    def __init__(self, action=None, message=None, start_time=None, finish_time=None, result=None, traceback=None):
        r"""DesktopAction

        The model defined in huaweicloud sdk

        :param action: 行为动作。
        :type action: str
        :param message: 行为完成状态信息。
        :type message: str
        :param start_time: 开始时间。
        :type start_time: str
        :param finish_time: 结束时间。
        :type finish_time: str
        :param result: 结果。
        :type result: str
        :param traceback: 异常信息。
        :type traceback: str
        """
        
        

        self._action = None
        self._message = None
        self._start_time = None
        self._finish_time = None
        self._result = None
        self._traceback = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if message is not None:
            self.message = message
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if result is not None:
            self.result = result
        if traceback is not None:
            self.traceback = traceback

    @property
    def action(self):
        r"""Gets the action of this DesktopAction.

        行为动作。

        :return: The action of this DesktopAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this DesktopAction.

        行为动作。

        :param action: The action of this DesktopAction.
        :type action: str
        """
        self._action = action

    @property
    def message(self):
        r"""Gets the message of this DesktopAction.

        行为完成状态信息。

        :return: The message of this DesktopAction.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this DesktopAction.

        行为完成状态信息。

        :param message: The message of this DesktopAction.
        :type message: str
        """
        self._message = message

    @property
    def start_time(self):
        r"""Gets the start_time of this DesktopAction.

        开始时间。

        :return: The start_time of this DesktopAction.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DesktopAction.

        开始时间。

        :param start_time: The start_time of this DesktopAction.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this DesktopAction.

        结束时间。

        :return: The finish_time of this DesktopAction.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this DesktopAction.

        结束时间。

        :param finish_time: The finish_time of this DesktopAction.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def result(self):
        r"""Gets the result of this DesktopAction.

        结果。

        :return: The result of this DesktopAction.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this DesktopAction.

        结果。

        :param result: The result of this DesktopAction.
        :type result: str
        """
        self._result = result

    @property
    def traceback(self):
        r"""Gets the traceback of this DesktopAction.

        异常信息。

        :return: The traceback of this DesktopAction.
        :rtype: str
        """
        return self._traceback

    @traceback.setter
    def traceback(self, traceback):
        r"""Sets the traceback of this DesktopAction.

        异常信息。

        :param traceback: The traceback of this DesktopAction.
        :type traceback: str
        """
        self._traceback = traceback

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
        if not isinstance(other, DesktopAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
