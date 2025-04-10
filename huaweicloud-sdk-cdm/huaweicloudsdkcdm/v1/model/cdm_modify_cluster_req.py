# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdmModifyClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_off': 'bool',
        'schedule_boot_off': 'bool',
        'schedule_boot_time': 'str',
        'schedule_off_time': 'str',
        'auto_remind': 'bool',
        'phone_num': 'str',
        'email': 'str'
    }

    attribute_map = {
        'auto_off': 'autoOff',
        'schedule_boot_off': 'scheduleBootOff',
        'schedule_boot_time': 'scheduleBootTime',
        'schedule_off_time': 'scheduleOffTime',
        'auto_remind': 'autoRemind',
        'phone_num': 'phoneNum',
        'email': 'email'
    }

    def __init__(self, auto_off=None, schedule_boot_off=None, schedule_boot_time=None, schedule_off_time=None, auto_remind=None, phone_num=None, email=None):
        r"""CdmModifyClusterReq

        The model defined in huaweicloud sdk

        :param auto_off: 自动关机。
        :type auto_off: bool
        :param schedule_boot_off: 定时关机。
        :type schedule_boot_off: bool
        :param schedule_boot_time: 定时开机。
        :type schedule_boot_time: str
        :param schedule_off_time: 定时关机时间。
        :type schedule_off_time: str
        :param auto_remind: 消息通知。
        :type auto_remind: bool
        :param phone_num: 手机号码，最多填写20个，以英文逗号分隔。
        :type phone_num: str
        :param email: 邮箱地址，最多填写20个，以英文逗号分隔。
        :type email: str
        """
        
        

        self._auto_off = None
        self._schedule_boot_off = None
        self._schedule_boot_time = None
        self._schedule_off_time = None
        self._auto_remind = None
        self._phone_num = None
        self._email = None
        self.discriminator = None

        if auto_off is not None:
            self.auto_off = auto_off
        if schedule_boot_off is not None:
            self.schedule_boot_off = schedule_boot_off
        if schedule_boot_time is not None:
            self.schedule_boot_time = schedule_boot_time
        if schedule_off_time is not None:
            self.schedule_off_time = schedule_off_time
        if auto_remind is not None:
            self.auto_remind = auto_remind
        if phone_num is not None:
            self.phone_num = phone_num
        if email is not None:
            self.email = email

    @property
    def auto_off(self):
        r"""Gets the auto_off of this CdmModifyClusterReq.

        自动关机。

        :return: The auto_off of this CdmModifyClusterReq.
        :rtype: bool
        """
        return self._auto_off

    @auto_off.setter
    def auto_off(self, auto_off):
        r"""Sets the auto_off of this CdmModifyClusterReq.

        自动关机。

        :param auto_off: The auto_off of this CdmModifyClusterReq.
        :type auto_off: bool
        """
        self._auto_off = auto_off

    @property
    def schedule_boot_off(self):
        r"""Gets the schedule_boot_off of this CdmModifyClusterReq.

        定时关机。

        :return: The schedule_boot_off of this CdmModifyClusterReq.
        :rtype: bool
        """
        return self._schedule_boot_off

    @schedule_boot_off.setter
    def schedule_boot_off(self, schedule_boot_off):
        r"""Sets the schedule_boot_off of this CdmModifyClusterReq.

        定时关机。

        :param schedule_boot_off: The schedule_boot_off of this CdmModifyClusterReq.
        :type schedule_boot_off: bool
        """
        self._schedule_boot_off = schedule_boot_off

    @property
    def schedule_boot_time(self):
        r"""Gets the schedule_boot_time of this CdmModifyClusterReq.

        定时开机。

        :return: The schedule_boot_time of this CdmModifyClusterReq.
        :rtype: str
        """
        return self._schedule_boot_time

    @schedule_boot_time.setter
    def schedule_boot_time(self, schedule_boot_time):
        r"""Sets the schedule_boot_time of this CdmModifyClusterReq.

        定时开机。

        :param schedule_boot_time: The schedule_boot_time of this CdmModifyClusterReq.
        :type schedule_boot_time: str
        """
        self._schedule_boot_time = schedule_boot_time

    @property
    def schedule_off_time(self):
        r"""Gets the schedule_off_time of this CdmModifyClusterReq.

        定时关机时间。

        :return: The schedule_off_time of this CdmModifyClusterReq.
        :rtype: str
        """
        return self._schedule_off_time

    @schedule_off_time.setter
    def schedule_off_time(self, schedule_off_time):
        r"""Sets the schedule_off_time of this CdmModifyClusterReq.

        定时关机时间。

        :param schedule_off_time: The schedule_off_time of this CdmModifyClusterReq.
        :type schedule_off_time: str
        """
        self._schedule_off_time = schedule_off_time

    @property
    def auto_remind(self):
        r"""Gets the auto_remind of this CdmModifyClusterReq.

        消息通知。

        :return: The auto_remind of this CdmModifyClusterReq.
        :rtype: bool
        """
        return self._auto_remind

    @auto_remind.setter
    def auto_remind(self, auto_remind):
        r"""Sets the auto_remind of this CdmModifyClusterReq.

        消息通知。

        :param auto_remind: The auto_remind of this CdmModifyClusterReq.
        :type auto_remind: bool
        """
        self._auto_remind = auto_remind

    @property
    def phone_num(self):
        r"""Gets the phone_num of this CdmModifyClusterReq.

        手机号码，最多填写20个，以英文逗号分隔。

        :return: The phone_num of this CdmModifyClusterReq.
        :rtype: str
        """
        return self._phone_num

    @phone_num.setter
    def phone_num(self, phone_num):
        r"""Sets the phone_num of this CdmModifyClusterReq.

        手机号码，最多填写20个，以英文逗号分隔。

        :param phone_num: The phone_num of this CdmModifyClusterReq.
        :type phone_num: str
        """
        self._phone_num = phone_num

    @property
    def email(self):
        r"""Gets the email of this CdmModifyClusterReq.

        邮箱地址，最多填写20个，以英文逗号分隔。

        :return: The email of this CdmModifyClusterReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this CdmModifyClusterReq.

        邮箱地址，最多填写20个，以英文逗号分隔。

        :param email: The email of this CdmModifyClusterReq.
        :type email: str
        """
        self._email = email

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
        if not isinstance(other, CdmModifyClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
