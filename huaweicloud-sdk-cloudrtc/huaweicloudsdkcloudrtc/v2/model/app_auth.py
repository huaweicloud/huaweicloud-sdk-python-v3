# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppAuth:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'expire': 'int',
        'app_key': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'expire': 'expire',
        'app_key': 'app_key',
        'update_time': 'update_time'
    }

    def __init__(self, enable=None, expire=None, app_key=None, update_time=None):
        r"""AppAuth

        The model defined in huaweicloud sdk

        :param enable: 开启或关闭URL鉴权
        :type enable: bool
        :param expire: 接入RTC建链认证时的signature的有效期。单位：秒。默认300秒。signature由app_key生成 
        :type expire: int
        :param app_key: app鉴权秘钥
        :type app_key: str
        :param update_time: app鉴权的更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC
        :type update_time: str
        """
        
        

        self._enable = None
        self._expire = None
        self._app_key = None
        self._update_time = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if expire is not None:
            self.expire = expire
        if app_key is not None:
            self.app_key = app_key
        if update_time is not None:
            self.update_time = update_time

    @property
    def enable(self):
        r"""Gets the enable of this AppAuth.

        开启或关闭URL鉴权

        :return: The enable of this AppAuth.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this AppAuth.

        开启或关闭URL鉴权

        :param enable: The enable of this AppAuth.
        :type enable: bool
        """
        self._enable = enable

    @property
    def expire(self):
        r"""Gets the expire of this AppAuth.

        接入RTC建链认证时的signature的有效期。单位：秒。默认300秒。signature由app_key生成 

        :return: The expire of this AppAuth.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        r"""Sets the expire of this AppAuth.

        接入RTC建链认证时的signature的有效期。单位：秒。默认300秒。signature由app_key生成 

        :param expire: The expire of this AppAuth.
        :type expire: int
        """
        self._expire = expire

    @property
    def app_key(self):
        r"""Gets the app_key of this AppAuth.

        app鉴权秘钥

        :return: The app_key of this AppAuth.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this AppAuth.

        app鉴权秘钥

        :param app_key: The app_key of this AppAuth.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def update_time(self):
        r"""Gets the update_time of this AppAuth.

        app鉴权的更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :return: The update_time of this AppAuth.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AppAuth.

        app鉴权的更新时间，形如“2006-01-02T15:04:05.075Z”，时区为：UTC

        :param update_time: The update_time of this AppAuth.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, AppAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
