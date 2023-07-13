# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesKeyboardMouse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mouse_feedback': 'str',
        'mouse_simulation_mode': 'str',
        'external_cursor_feedback': 'bool'
    }

    attribute_map = {
        'mouse_feedback': 'mouse_feedback',
        'mouse_simulation_mode': 'mouse_simulation_mode',
        'external_cursor_feedback': 'external_cursor_feedback'
    }

    def __init__(self, mouse_feedback=None, mouse_simulation_mode=None, external_cursor_feedback=None):
        """PoliciesKeyboardMouse

        The model defined in huaweicloud sdk

        :param mouse_feedback: 虚拟机鼠标回馈。取值为： SELFADAPTION：自适应鼠标回馈。 FORCE：强制鼠标回馈。 CLOSE：关闭鼠标回馈。
        :type mouse_feedback: str
        :param mouse_simulation_mode: 虚拟机鼠标模拟方式。取值为： ABSOLUTE_POSITION：绝对位置模拟。 RELATIVE_POSITION：相对位置模拟。
        :type mouse_simulation_mode: str
        :param external_cursor_feedback: 虚拟机外部光标反馈。取值为： false：表示关闭。 true：表示开启。
        :type external_cursor_feedback: bool
        """
        
        

        self._mouse_feedback = None
        self._mouse_simulation_mode = None
        self._external_cursor_feedback = None
        self.discriminator = None

        if mouse_feedback is not None:
            self.mouse_feedback = mouse_feedback
        if mouse_simulation_mode is not None:
            self.mouse_simulation_mode = mouse_simulation_mode
        if external_cursor_feedback is not None:
            self.external_cursor_feedback = external_cursor_feedback

    @property
    def mouse_feedback(self):
        """Gets the mouse_feedback of this PoliciesKeyboardMouse.

        虚拟机鼠标回馈。取值为： SELFADAPTION：自适应鼠标回馈。 FORCE：强制鼠标回馈。 CLOSE：关闭鼠标回馈。

        :return: The mouse_feedback of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._mouse_feedback

    @mouse_feedback.setter
    def mouse_feedback(self, mouse_feedback):
        """Sets the mouse_feedback of this PoliciesKeyboardMouse.

        虚拟机鼠标回馈。取值为： SELFADAPTION：自适应鼠标回馈。 FORCE：强制鼠标回馈。 CLOSE：关闭鼠标回馈。

        :param mouse_feedback: The mouse_feedback of this PoliciesKeyboardMouse.
        :type mouse_feedback: str
        """
        self._mouse_feedback = mouse_feedback

    @property
    def mouse_simulation_mode(self):
        """Gets the mouse_simulation_mode of this PoliciesKeyboardMouse.

        虚拟机鼠标模拟方式。取值为： ABSOLUTE_POSITION：绝对位置模拟。 RELATIVE_POSITION：相对位置模拟。

        :return: The mouse_simulation_mode of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._mouse_simulation_mode

    @mouse_simulation_mode.setter
    def mouse_simulation_mode(self, mouse_simulation_mode):
        """Sets the mouse_simulation_mode of this PoliciesKeyboardMouse.

        虚拟机鼠标模拟方式。取值为： ABSOLUTE_POSITION：绝对位置模拟。 RELATIVE_POSITION：相对位置模拟。

        :param mouse_simulation_mode: The mouse_simulation_mode of this PoliciesKeyboardMouse.
        :type mouse_simulation_mode: str
        """
        self._mouse_simulation_mode = mouse_simulation_mode

    @property
    def external_cursor_feedback(self):
        """Gets the external_cursor_feedback of this PoliciesKeyboardMouse.

        虚拟机外部光标反馈。取值为： false：表示关闭。 true：表示开启。

        :return: The external_cursor_feedback of this PoliciesKeyboardMouse.
        :rtype: bool
        """
        return self._external_cursor_feedback

    @external_cursor_feedback.setter
    def external_cursor_feedback(self, external_cursor_feedback):
        """Sets the external_cursor_feedback of this PoliciesKeyboardMouse.

        虚拟机外部光标反馈。取值为： false：表示关闭。 true：表示开启。

        :param external_cursor_feedback: The external_cursor_feedback of this PoliciesKeyboardMouse.
        :type external_cursor_feedback: bool
        """
        self._external_cursor_feedback = external_cursor_feedback

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
        if not isinstance(other, PoliciesKeyboardMouse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
