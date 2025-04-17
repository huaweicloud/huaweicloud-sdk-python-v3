# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarnConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'anti_d_do_s': 'bool',
        'back_doors': 'bool',
        'bruce_force': 'bool',
        'high_privilege': 'bool',
        'remote_login': 'bool',
        'send_frequency': 'int',
        'waf': 'bool',
        'weak_password': 'bool'
    }

    attribute_map = {
        'anti_d_do_s': 'antiDDoS',
        'back_doors': 'back_doors',
        'bruce_force': 'bruce_force',
        'high_privilege': 'high_privilege',
        'remote_login': 'remote_login',
        'send_frequency': 'send_frequency',
        'waf': 'waf',
        'weak_password': 'weak_password'
    }

    def __init__(self, anti_d_do_s=None, back_doors=None, bruce_force=None, high_privilege=None, remote_login=None, send_frequency=None, waf=None, weak_password=None):
        r"""WarnConfig

        The model defined in huaweicloud sdk

        :param anti_d_do_s: DDoS攻击
        :type anti_d_do_s: bool
        :param back_doors: 网页后门
        :type back_doors: bool
        :param bruce_force: 暴力破解（系统登录，FTP，DB）
        :type bruce_force: bool
        :param high_privilege: 数据库进程权限过高
        :type high_privilege: bool
        :param remote_login: 异地登录提醒
        :type remote_login: bool
        :param send_frequency: 取值范围： - 0：表示每天一次 - 1：表示半小时一次  对于HID必选。
        :type send_frequency: int
        :param waf: 保留字段
        :type waf: bool
        :param weak_password: 弱口令（系统，数据库）
        :type weak_password: bool
        """
        
        

        self._anti_d_do_s = None
        self._back_doors = None
        self._bruce_force = None
        self._high_privilege = None
        self._remote_login = None
        self._send_frequency = None
        self._waf = None
        self._weak_password = None
        self.discriminator = None

        self.anti_d_do_s = anti_d_do_s
        if back_doors is not None:
            self.back_doors = back_doors
        if bruce_force is not None:
            self.bruce_force = bruce_force
        if high_privilege is not None:
            self.high_privilege = high_privilege
        if remote_login is not None:
            self.remote_login = remote_login
        if send_frequency is not None:
            self.send_frequency = send_frequency
        if waf is not None:
            self.waf = waf
        if weak_password is not None:
            self.weak_password = weak_password

    @property
    def anti_d_do_s(self):
        r"""Gets the anti_d_do_s of this WarnConfig.

        DDoS攻击

        :return: The anti_d_do_s of this WarnConfig.
        :rtype: bool
        """
        return self._anti_d_do_s

    @anti_d_do_s.setter
    def anti_d_do_s(self, anti_d_do_s):
        r"""Sets the anti_d_do_s of this WarnConfig.

        DDoS攻击

        :param anti_d_do_s: The anti_d_do_s of this WarnConfig.
        :type anti_d_do_s: bool
        """
        self._anti_d_do_s = anti_d_do_s

    @property
    def back_doors(self):
        r"""Gets the back_doors of this WarnConfig.

        网页后门

        :return: The back_doors of this WarnConfig.
        :rtype: bool
        """
        return self._back_doors

    @back_doors.setter
    def back_doors(self, back_doors):
        r"""Sets the back_doors of this WarnConfig.

        网页后门

        :param back_doors: The back_doors of this WarnConfig.
        :type back_doors: bool
        """
        self._back_doors = back_doors

    @property
    def bruce_force(self):
        r"""Gets the bruce_force of this WarnConfig.

        暴力破解（系统登录，FTP，DB）

        :return: The bruce_force of this WarnConfig.
        :rtype: bool
        """
        return self._bruce_force

    @bruce_force.setter
    def bruce_force(self, bruce_force):
        r"""Sets the bruce_force of this WarnConfig.

        暴力破解（系统登录，FTP，DB）

        :param bruce_force: The bruce_force of this WarnConfig.
        :type bruce_force: bool
        """
        self._bruce_force = bruce_force

    @property
    def high_privilege(self):
        r"""Gets the high_privilege of this WarnConfig.

        数据库进程权限过高

        :return: The high_privilege of this WarnConfig.
        :rtype: bool
        """
        return self._high_privilege

    @high_privilege.setter
    def high_privilege(self, high_privilege):
        r"""Sets the high_privilege of this WarnConfig.

        数据库进程权限过高

        :param high_privilege: The high_privilege of this WarnConfig.
        :type high_privilege: bool
        """
        self._high_privilege = high_privilege

    @property
    def remote_login(self):
        r"""Gets the remote_login of this WarnConfig.

        异地登录提醒

        :return: The remote_login of this WarnConfig.
        :rtype: bool
        """
        return self._remote_login

    @remote_login.setter
    def remote_login(self, remote_login):
        r"""Sets the remote_login of this WarnConfig.

        异地登录提醒

        :param remote_login: The remote_login of this WarnConfig.
        :type remote_login: bool
        """
        self._remote_login = remote_login

    @property
    def send_frequency(self):
        r"""Gets the send_frequency of this WarnConfig.

        取值范围： - 0：表示每天一次 - 1：表示半小时一次  对于HID必选。

        :return: The send_frequency of this WarnConfig.
        :rtype: int
        """
        return self._send_frequency

    @send_frequency.setter
    def send_frequency(self, send_frequency):
        r"""Sets the send_frequency of this WarnConfig.

        取值范围： - 0：表示每天一次 - 1：表示半小时一次  对于HID必选。

        :param send_frequency: The send_frequency of this WarnConfig.
        :type send_frequency: int
        """
        self._send_frequency = send_frequency

    @property
    def waf(self):
        r"""Gets the waf of this WarnConfig.

        保留字段

        :return: The waf of this WarnConfig.
        :rtype: bool
        """
        return self._waf

    @waf.setter
    def waf(self, waf):
        r"""Sets the waf of this WarnConfig.

        保留字段

        :param waf: The waf of this WarnConfig.
        :type waf: bool
        """
        self._waf = waf

    @property
    def weak_password(self):
        r"""Gets the weak_password of this WarnConfig.

        弱口令（系统，数据库）

        :return: The weak_password of this WarnConfig.
        :rtype: bool
        """
        return self._weak_password

    @weak_password.setter
    def weak_password(self, weak_password):
        r"""Sets the weak_password of this WarnConfig.

        弱口令（系统，数据库）

        :param weak_password: The weak_password of this WarnConfig.
        :type weak_password: bool
        """
        self._weak_password = weak_password

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
        if not isinstance(other, WarnConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
