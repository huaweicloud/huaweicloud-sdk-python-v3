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
        'external_cursor_feedback': 'bool',
        'selfhelp_console_enable': 'bool',
        'client_mouse_send_interval': 'int',
        'windows_client_keyboard_mode': 'str',
        'windows_client_mouse_mode': 'str',
        'linux_client_keyboard_mode': 'str',
        'linux_client_mouse_mode': 'str',
        'special_keyboard': 'bool',
        'joy_stick_flag': 'bool'
    }

    attribute_map = {
        'mouse_feedback': 'mouse_feedback',
        'mouse_simulation_mode': 'mouse_simulation_mode',
        'external_cursor_feedback': 'external_cursor_feedback',
        'selfhelp_console_enable': 'selfhelp_console_enable',
        'client_mouse_send_interval': 'client_mouse_send_interval',
        'windows_client_keyboard_mode': 'windows_client_keyboard_mode',
        'windows_client_mouse_mode': 'windows_client_mouse_mode',
        'linux_client_keyboard_mode': 'linux_client_keyboard_mode',
        'linux_client_mouse_mode': 'linux_client_mouse_mode',
        'special_keyboard': 'special_keyboard',
        'joy_stick_flag': 'joy_stick_flag'
    }

    def __init__(self, mouse_feedback=None, mouse_simulation_mode=None, external_cursor_feedback=None, selfhelp_console_enable=None, client_mouse_send_interval=None, windows_client_keyboard_mode=None, windows_client_mouse_mode=None, linux_client_keyboard_mode=None, linux_client_mouse_mode=None, special_keyboard=None, joy_stick_flag=None):
        r"""PoliciesKeyboardMouse

        The model defined in huaweicloud sdk

        :param mouse_feedback: 虚拟机鼠标回馈。取值为： SELFADAPTION：自适应鼠标回馈。 FORCE：强制鼠标回馈。 CLOSE：关闭鼠标回馈。
        :type mouse_feedback: str
        :param mouse_simulation_mode: 虚拟机鼠标模拟方式。取值为： ABSOLUTE_POSITION：绝对位置模拟。 RELATIVE_POSITION：相对位置模拟。
        :type mouse_simulation_mode: str
        :param external_cursor_feedback: 虚拟机外部光标反馈。取值为： false：表示关闭。 true：表示开启。
        :type external_cursor_feedback: bool
        :param selfhelp_console_enable: 自助维护台抢占登录。取值为： false：表示关闭。 true：表示开启。
        :type selfhelp_console_enable: bool
        :param client_mouse_send_interval: 客户端鼠标发送间隔。取值范围为[1-30]。默认：30。
        :type client_mouse_send_interval: int
        :param windows_client_keyboard_mode: Windows客户端键盘模式。取值为： GLOBAL：Windows客户端键盘全局模式。（默认） WINDOW：Windows客户端键盘窗口模式。
        :type windows_client_keyboard_mode: str
        :param windows_client_mouse_mode: Windows客户端鼠标模式。取值为： GLOBAL：Windows客户端鼠标全局模式。 WINDOW：Windows客户端鼠标窗口模式。（默认）
        :type windows_client_mouse_mode: str
        :param linux_client_keyboard_mode: Linux客户端键盘模式。取值为： EVENT：Linux客户端键盘事件模式。（默认） GRAPH：Linux客户端键盘图形模式。
        :type linux_client_keyboard_mode: str
        :param linux_client_mouse_mode: Linux客户端鼠标模式。取值为： EVENT：Linux客户端鼠标事件模式。（默认） GRAPH：Linux客户端鼠标窗口模式。
        :type linux_client_mouse_mode: str
        :param special_keyboard: 特殊键盘。取值为： false：表示关闭。 true：表示开启。
        :type special_keyboard: bool
        :param joy_stick_flag: 游戏操纵杆。取值为： false：表示关闭。 true：表示开启。
        :type joy_stick_flag: bool
        """
        
        

        self._mouse_feedback = None
        self._mouse_simulation_mode = None
        self._external_cursor_feedback = None
        self._selfhelp_console_enable = None
        self._client_mouse_send_interval = None
        self._windows_client_keyboard_mode = None
        self._windows_client_mouse_mode = None
        self._linux_client_keyboard_mode = None
        self._linux_client_mouse_mode = None
        self._special_keyboard = None
        self._joy_stick_flag = None
        self.discriminator = None

        if mouse_feedback is not None:
            self.mouse_feedback = mouse_feedback
        if mouse_simulation_mode is not None:
            self.mouse_simulation_mode = mouse_simulation_mode
        if external_cursor_feedback is not None:
            self.external_cursor_feedback = external_cursor_feedback
        if selfhelp_console_enable is not None:
            self.selfhelp_console_enable = selfhelp_console_enable
        if client_mouse_send_interval is not None:
            self.client_mouse_send_interval = client_mouse_send_interval
        if windows_client_keyboard_mode is not None:
            self.windows_client_keyboard_mode = windows_client_keyboard_mode
        if windows_client_mouse_mode is not None:
            self.windows_client_mouse_mode = windows_client_mouse_mode
        if linux_client_keyboard_mode is not None:
            self.linux_client_keyboard_mode = linux_client_keyboard_mode
        if linux_client_mouse_mode is not None:
            self.linux_client_mouse_mode = linux_client_mouse_mode
        if special_keyboard is not None:
            self.special_keyboard = special_keyboard
        if joy_stick_flag is not None:
            self.joy_stick_flag = joy_stick_flag

    @property
    def mouse_feedback(self):
        r"""Gets the mouse_feedback of this PoliciesKeyboardMouse.

        虚拟机鼠标回馈。取值为： SELFADAPTION：自适应鼠标回馈。 FORCE：强制鼠标回馈。 CLOSE：关闭鼠标回馈。

        :return: The mouse_feedback of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._mouse_feedback

    @mouse_feedback.setter
    def mouse_feedback(self, mouse_feedback):
        r"""Sets the mouse_feedback of this PoliciesKeyboardMouse.

        虚拟机鼠标回馈。取值为： SELFADAPTION：自适应鼠标回馈。 FORCE：强制鼠标回馈。 CLOSE：关闭鼠标回馈。

        :param mouse_feedback: The mouse_feedback of this PoliciesKeyboardMouse.
        :type mouse_feedback: str
        """
        self._mouse_feedback = mouse_feedback

    @property
    def mouse_simulation_mode(self):
        r"""Gets the mouse_simulation_mode of this PoliciesKeyboardMouse.

        虚拟机鼠标模拟方式。取值为： ABSOLUTE_POSITION：绝对位置模拟。 RELATIVE_POSITION：相对位置模拟。

        :return: The mouse_simulation_mode of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._mouse_simulation_mode

    @mouse_simulation_mode.setter
    def mouse_simulation_mode(self, mouse_simulation_mode):
        r"""Sets the mouse_simulation_mode of this PoliciesKeyboardMouse.

        虚拟机鼠标模拟方式。取值为： ABSOLUTE_POSITION：绝对位置模拟。 RELATIVE_POSITION：相对位置模拟。

        :param mouse_simulation_mode: The mouse_simulation_mode of this PoliciesKeyboardMouse.
        :type mouse_simulation_mode: str
        """
        self._mouse_simulation_mode = mouse_simulation_mode

    @property
    def external_cursor_feedback(self):
        r"""Gets the external_cursor_feedback of this PoliciesKeyboardMouse.

        虚拟机外部光标反馈。取值为： false：表示关闭。 true：表示开启。

        :return: The external_cursor_feedback of this PoliciesKeyboardMouse.
        :rtype: bool
        """
        return self._external_cursor_feedback

    @external_cursor_feedback.setter
    def external_cursor_feedback(self, external_cursor_feedback):
        r"""Sets the external_cursor_feedback of this PoliciesKeyboardMouse.

        虚拟机外部光标反馈。取值为： false：表示关闭。 true：表示开启。

        :param external_cursor_feedback: The external_cursor_feedback of this PoliciesKeyboardMouse.
        :type external_cursor_feedback: bool
        """
        self._external_cursor_feedback = external_cursor_feedback

    @property
    def selfhelp_console_enable(self):
        r"""Gets the selfhelp_console_enable of this PoliciesKeyboardMouse.

        自助维护台抢占登录。取值为： false：表示关闭。 true：表示开启。

        :return: The selfhelp_console_enable of this PoliciesKeyboardMouse.
        :rtype: bool
        """
        return self._selfhelp_console_enable

    @selfhelp_console_enable.setter
    def selfhelp_console_enable(self, selfhelp_console_enable):
        r"""Sets the selfhelp_console_enable of this PoliciesKeyboardMouse.

        自助维护台抢占登录。取值为： false：表示关闭。 true：表示开启。

        :param selfhelp_console_enable: The selfhelp_console_enable of this PoliciesKeyboardMouse.
        :type selfhelp_console_enable: bool
        """
        self._selfhelp_console_enable = selfhelp_console_enable

    @property
    def client_mouse_send_interval(self):
        r"""Gets the client_mouse_send_interval of this PoliciesKeyboardMouse.

        客户端鼠标发送间隔。取值范围为[1-30]。默认：30。

        :return: The client_mouse_send_interval of this PoliciesKeyboardMouse.
        :rtype: int
        """
        return self._client_mouse_send_interval

    @client_mouse_send_interval.setter
    def client_mouse_send_interval(self, client_mouse_send_interval):
        r"""Sets the client_mouse_send_interval of this PoliciesKeyboardMouse.

        客户端鼠标发送间隔。取值范围为[1-30]。默认：30。

        :param client_mouse_send_interval: The client_mouse_send_interval of this PoliciesKeyboardMouse.
        :type client_mouse_send_interval: int
        """
        self._client_mouse_send_interval = client_mouse_send_interval

    @property
    def windows_client_keyboard_mode(self):
        r"""Gets the windows_client_keyboard_mode of this PoliciesKeyboardMouse.

        Windows客户端键盘模式。取值为： GLOBAL：Windows客户端键盘全局模式。（默认） WINDOW：Windows客户端键盘窗口模式。

        :return: The windows_client_keyboard_mode of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._windows_client_keyboard_mode

    @windows_client_keyboard_mode.setter
    def windows_client_keyboard_mode(self, windows_client_keyboard_mode):
        r"""Sets the windows_client_keyboard_mode of this PoliciesKeyboardMouse.

        Windows客户端键盘模式。取值为： GLOBAL：Windows客户端键盘全局模式。（默认） WINDOW：Windows客户端键盘窗口模式。

        :param windows_client_keyboard_mode: The windows_client_keyboard_mode of this PoliciesKeyboardMouse.
        :type windows_client_keyboard_mode: str
        """
        self._windows_client_keyboard_mode = windows_client_keyboard_mode

    @property
    def windows_client_mouse_mode(self):
        r"""Gets the windows_client_mouse_mode of this PoliciesKeyboardMouse.

        Windows客户端鼠标模式。取值为： GLOBAL：Windows客户端鼠标全局模式。 WINDOW：Windows客户端鼠标窗口模式。（默认）

        :return: The windows_client_mouse_mode of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._windows_client_mouse_mode

    @windows_client_mouse_mode.setter
    def windows_client_mouse_mode(self, windows_client_mouse_mode):
        r"""Sets the windows_client_mouse_mode of this PoliciesKeyboardMouse.

        Windows客户端鼠标模式。取值为： GLOBAL：Windows客户端鼠标全局模式。 WINDOW：Windows客户端鼠标窗口模式。（默认）

        :param windows_client_mouse_mode: The windows_client_mouse_mode of this PoliciesKeyboardMouse.
        :type windows_client_mouse_mode: str
        """
        self._windows_client_mouse_mode = windows_client_mouse_mode

    @property
    def linux_client_keyboard_mode(self):
        r"""Gets the linux_client_keyboard_mode of this PoliciesKeyboardMouse.

        Linux客户端键盘模式。取值为： EVENT：Linux客户端键盘事件模式。（默认） GRAPH：Linux客户端键盘图形模式。

        :return: The linux_client_keyboard_mode of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._linux_client_keyboard_mode

    @linux_client_keyboard_mode.setter
    def linux_client_keyboard_mode(self, linux_client_keyboard_mode):
        r"""Sets the linux_client_keyboard_mode of this PoliciesKeyboardMouse.

        Linux客户端键盘模式。取值为： EVENT：Linux客户端键盘事件模式。（默认） GRAPH：Linux客户端键盘图形模式。

        :param linux_client_keyboard_mode: The linux_client_keyboard_mode of this PoliciesKeyboardMouse.
        :type linux_client_keyboard_mode: str
        """
        self._linux_client_keyboard_mode = linux_client_keyboard_mode

    @property
    def linux_client_mouse_mode(self):
        r"""Gets the linux_client_mouse_mode of this PoliciesKeyboardMouse.

        Linux客户端鼠标模式。取值为： EVENT：Linux客户端鼠标事件模式。（默认） GRAPH：Linux客户端鼠标窗口模式。

        :return: The linux_client_mouse_mode of this PoliciesKeyboardMouse.
        :rtype: str
        """
        return self._linux_client_mouse_mode

    @linux_client_mouse_mode.setter
    def linux_client_mouse_mode(self, linux_client_mouse_mode):
        r"""Sets the linux_client_mouse_mode of this PoliciesKeyboardMouse.

        Linux客户端鼠标模式。取值为： EVENT：Linux客户端鼠标事件模式。（默认） GRAPH：Linux客户端鼠标窗口模式。

        :param linux_client_mouse_mode: The linux_client_mouse_mode of this PoliciesKeyboardMouse.
        :type linux_client_mouse_mode: str
        """
        self._linux_client_mouse_mode = linux_client_mouse_mode

    @property
    def special_keyboard(self):
        r"""Gets the special_keyboard of this PoliciesKeyboardMouse.

        特殊键盘。取值为： false：表示关闭。 true：表示开启。

        :return: The special_keyboard of this PoliciesKeyboardMouse.
        :rtype: bool
        """
        return self._special_keyboard

    @special_keyboard.setter
    def special_keyboard(self, special_keyboard):
        r"""Sets the special_keyboard of this PoliciesKeyboardMouse.

        特殊键盘。取值为： false：表示关闭。 true：表示开启。

        :param special_keyboard: The special_keyboard of this PoliciesKeyboardMouse.
        :type special_keyboard: bool
        """
        self._special_keyboard = special_keyboard

    @property
    def joy_stick_flag(self):
        r"""Gets the joy_stick_flag of this PoliciesKeyboardMouse.

        游戏操纵杆。取值为： false：表示关闭。 true：表示开启。

        :return: The joy_stick_flag of this PoliciesKeyboardMouse.
        :rtype: bool
        """
        return self._joy_stick_flag

    @joy_stick_flag.setter
    def joy_stick_flag(self, joy_stick_flag):
        r"""Sets the joy_stick_flag of this PoliciesKeyboardMouse.

        游戏操纵杆。取值为： false：表示关闭。 true：表示开启。

        :param joy_stick_flag: The joy_stick_flag of this PoliciesKeyboardMouse.
        :type joy_stick_flag: bool
        """
        self._joy_stick_flag = joy_stick_flag

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
