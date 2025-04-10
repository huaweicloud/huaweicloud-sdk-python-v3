# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vdi:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_lock_enable': 'bool',
        'auto_lock_options': 'AutoLockOptions',
        'disconnect_logout_enable': 'int',
        'disconnect_logout_options': 'DisconnectLogoutOptions',
        'disconnect_hibernate_enable': 'bool',
        'disconnect_hibernate_options': 'VdiDisconnectHibernateOptions',
        'no_operation_hibernate_enable': 'bool',
        'no_operation_hibernate_options': 'VdiNoOperationHibernateOptions'
    }

    attribute_map = {
        'auto_lock_enable': 'auto_lock_enable',
        'auto_lock_options': 'auto_lock_options',
        'disconnect_logout_enable': 'disconnect_logout_enable',
        'disconnect_logout_options': 'disconnect_logout_options',
        'disconnect_hibernate_enable': 'disconnect_hibernate_enable',
        'disconnect_hibernate_options': 'disconnect_hibernate_options',
        'no_operation_hibernate_enable': 'no_operation_hibernate_enable',
        'no_operation_hibernate_options': 'no_operation_hibernate_options'
    }

    def __init__(self, auto_lock_enable=None, auto_lock_options=None, disconnect_logout_enable=None, disconnect_logout_options=None, disconnect_hibernate_enable=None, disconnect_hibernate_options=None, no_operation_hibernate_enable=None, no_operation_hibernate_options=None):
        r"""Vdi

        The model defined in huaweicloud sdk

        :param auto_lock_enable: 是否开启自动锁屏。取值为：false：表示关闭。true：表示开启。
        :type auto_lock_enable: bool
        :param auto_lock_options: 
        :type auto_lock_options: :class:`huaweicloudsdkworkspace.v2.AutoLockOptions`
        :param disconnect_logout_enable: 是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。
        :type disconnect_logout_enable: int
        :param disconnect_logout_options: 
        :type disconnect_logout_options: :class:`huaweicloudsdkworkspace.v2.DisconnectLogoutOptions`
        :param disconnect_hibernate_enable: 是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。
        :type disconnect_hibernate_enable: bool
        :param disconnect_hibernate_options: 
        :type disconnect_hibernate_options: :class:`huaweicloudsdkworkspace.v2.VdiDisconnectHibernateOptions`
        :param no_operation_hibernate_enable: 是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。
        :type no_operation_hibernate_enable: bool
        :param no_operation_hibernate_options: 
        :type no_operation_hibernate_options: :class:`huaweicloudsdkworkspace.v2.VdiNoOperationHibernateOptions`
        """
        
        

        self._auto_lock_enable = None
        self._auto_lock_options = None
        self._disconnect_logout_enable = None
        self._disconnect_logout_options = None
        self._disconnect_hibernate_enable = None
        self._disconnect_hibernate_options = None
        self._no_operation_hibernate_enable = None
        self._no_operation_hibernate_options = None
        self.discriminator = None

        if auto_lock_enable is not None:
            self.auto_lock_enable = auto_lock_enable
        if auto_lock_options is not None:
            self.auto_lock_options = auto_lock_options
        if disconnect_logout_enable is not None:
            self.disconnect_logout_enable = disconnect_logout_enable
        if disconnect_logout_options is not None:
            self.disconnect_logout_options = disconnect_logout_options
        if disconnect_hibernate_enable is not None:
            self.disconnect_hibernate_enable = disconnect_hibernate_enable
        if disconnect_hibernate_options is not None:
            self.disconnect_hibernate_options = disconnect_hibernate_options
        if no_operation_hibernate_enable is not None:
            self.no_operation_hibernate_enable = no_operation_hibernate_enable
        if no_operation_hibernate_options is not None:
            self.no_operation_hibernate_options = no_operation_hibernate_options

    @property
    def auto_lock_enable(self):
        r"""Gets the auto_lock_enable of this Vdi.

        是否开启自动锁屏。取值为：false：表示关闭。true：表示开启。

        :return: The auto_lock_enable of this Vdi.
        :rtype: bool
        """
        return self._auto_lock_enable

    @auto_lock_enable.setter
    def auto_lock_enable(self, auto_lock_enable):
        r"""Sets the auto_lock_enable of this Vdi.

        是否开启自动锁屏。取值为：false：表示关闭。true：表示开启。

        :param auto_lock_enable: The auto_lock_enable of this Vdi.
        :type auto_lock_enable: bool
        """
        self._auto_lock_enable = auto_lock_enable

    @property
    def auto_lock_options(self):
        r"""Gets the auto_lock_options of this Vdi.

        :return: The auto_lock_options of this Vdi.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AutoLockOptions`
        """
        return self._auto_lock_options

    @auto_lock_options.setter
    def auto_lock_options(self, auto_lock_options):
        r"""Sets the auto_lock_options of this Vdi.

        :param auto_lock_options: The auto_lock_options of this Vdi.
        :type auto_lock_options: :class:`huaweicloudsdkworkspace.v2.AutoLockOptions`
        """
        self._auto_lock_options = auto_lock_options

    @property
    def disconnect_logout_enable(self):
        r"""Gets the disconnect_logout_enable of this Vdi.

        是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。

        :return: The disconnect_logout_enable of this Vdi.
        :rtype: int
        """
        return self._disconnect_logout_enable

    @disconnect_logout_enable.setter
    def disconnect_logout_enable(self, disconnect_logout_enable):
        r"""Sets the disconnect_logout_enable of this Vdi.

        是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。

        :param disconnect_logout_enable: The disconnect_logout_enable of this Vdi.
        :type disconnect_logout_enable: int
        """
        self._disconnect_logout_enable = disconnect_logout_enable

    @property
    def disconnect_logout_options(self):
        r"""Gets the disconnect_logout_options of this Vdi.

        :return: The disconnect_logout_options of this Vdi.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DisconnectLogoutOptions`
        """
        return self._disconnect_logout_options

    @disconnect_logout_options.setter
    def disconnect_logout_options(self, disconnect_logout_options):
        r"""Sets the disconnect_logout_options of this Vdi.

        :param disconnect_logout_options: The disconnect_logout_options of this Vdi.
        :type disconnect_logout_options: :class:`huaweicloudsdkworkspace.v2.DisconnectLogoutOptions`
        """
        self._disconnect_logout_options = disconnect_logout_options

    @property
    def disconnect_hibernate_enable(self):
        r"""Gets the disconnect_hibernate_enable of this Vdi.

        是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。

        :return: The disconnect_hibernate_enable of this Vdi.
        :rtype: bool
        """
        return self._disconnect_hibernate_enable

    @disconnect_hibernate_enable.setter
    def disconnect_hibernate_enable(self, disconnect_hibernate_enable):
        r"""Sets the disconnect_hibernate_enable of this Vdi.

        是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。

        :param disconnect_hibernate_enable: The disconnect_hibernate_enable of this Vdi.
        :type disconnect_hibernate_enable: bool
        """
        self._disconnect_hibernate_enable = disconnect_hibernate_enable

    @property
    def disconnect_hibernate_options(self):
        r"""Gets the disconnect_hibernate_options of this Vdi.

        :return: The disconnect_hibernate_options of this Vdi.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VdiDisconnectHibernateOptions`
        """
        return self._disconnect_hibernate_options

    @disconnect_hibernate_options.setter
    def disconnect_hibernate_options(self, disconnect_hibernate_options):
        r"""Sets the disconnect_hibernate_options of this Vdi.

        :param disconnect_hibernate_options: The disconnect_hibernate_options of this Vdi.
        :type disconnect_hibernate_options: :class:`huaweicloudsdkworkspace.v2.VdiDisconnectHibernateOptions`
        """
        self._disconnect_hibernate_options = disconnect_hibernate_options

    @property
    def no_operation_hibernate_enable(self):
        r"""Gets the no_operation_hibernate_enable of this Vdi.

        是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。

        :return: The no_operation_hibernate_enable of this Vdi.
        :rtype: bool
        """
        return self._no_operation_hibernate_enable

    @no_operation_hibernate_enable.setter
    def no_operation_hibernate_enable(self, no_operation_hibernate_enable):
        r"""Sets the no_operation_hibernate_enable of this Vdi.

        是否开启断开后自动注销。取值为：0：表示关闭。1：表示开启。

        :param no_operation_hibernate_enable: The no_operation_hibernate_enable of this Vdi.
        :type no_operation_hibernate_enable: bool
        """
        self._no_operation_hibernate_enable = no_operation_hibernate_enable

    @property
    def no_operation_hibernate_options(self):
        r"""Gets the no_operation_hibernate_options of this Vdi.

        :return: The no_operation_hibernate_options of this Vdi.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VdiNoOperationHibernateOptions`
        """
        return self._no_operation_hibernate_options

    @no_operation_hibernate_options.setter
    def no_operation_hibernate_options(self, no_operation_hibernate_options):
        r"""Sets the no_operation_hibernate_options of this Vdi.

        :param no_operation_hibernate_options: The no_operation_hibernate_options of this Vdi.
        :type no_operation_hibernate_options: :class:`huaweicloudsdkworkspace.v2.VdiNoOperationHibernateOptions`
        """
        self._no_operation_hibernate_options = no_operation_hibernate_options

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
        if not isinstance(other, Vdi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
