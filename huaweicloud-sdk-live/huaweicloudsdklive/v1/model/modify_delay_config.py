# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyDelayConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'app': 'str',
        'delay': 'int'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'app': 'app',
        'delay': 'delay'
    }

    def __init__(self, play_domain=None, app=None, delay=None):
        r"""ModifyDelayConfig

        The model defined in huaweicloud sdk

        :param play_domain: 播放域名
        :type play_domain: str
        :param app: 应用名称，默认为live
        :type app: str
        :param delay: 延时时间，单位：ms。  包含如下取值： - 2000（低）。 - 4000（中）。 - 6000（高）。
        :type delay: int
        """
        
        

        self._play_domain = None
        self._app = None
        self._delay = None
        self.discriminator = None

        self.play_domain = play_domain
        if app is not None:
            self.app = app
        self.delay = delay

    @property
    def play_domain(self):
        r"""Gets the play_domain of this ModifyDelayConfig.

        播放域名

        :return: The play_domain of this ModifyDelayConfig.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        r"""Sets the play_domain of this ModifyDelayConfig.

        播放域名

        :param play_domain: The play_domain of this ModifyDelayConfig.
        :type play_domain: str
        """
        self._play_domain = play_domain

    @property
    def app(self):
        r"""Gets the app of this ModifyDelayConfig.

        应用名称，默认为live

        :return: The app of this ModifyDelayConfig.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ModifyDelayConfig.

        应用名称，默认为live

        :param app: The app of this ModifyDelayConfig.
        :type app: str
        """
        self._app = app

    @property
    def delay(self):
        r"""Gets the delay of this ModifyDelayConfig.

        延时时间，单位：ms。  包含如下取值： - 2000（低）。 - 4000（中）。 - 6000（高）。

        :return: The delay of this ModifyDelayConfig.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this ModifyDelayConfig.

        延时时间，单位：ms。  包含如下取值： - 2000（低）。 - 4000（中）。 - 6000（高）。

        :param delay: The delay of this ModifyDelayConfig.
        :type delay: int
        """
        self._delay = delay

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
        if not isinstance(other, ModifyDelayConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
