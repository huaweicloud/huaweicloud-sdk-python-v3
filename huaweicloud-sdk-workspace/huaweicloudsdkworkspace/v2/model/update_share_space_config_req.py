# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateShareSpaceConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_name': 'str',
        'config_value': 'str'
    }

    attribute_map = {
        'config_name': 'config_name',
        'config_value': 'config_value'
    }

    def __init__(self, config_name=None, config_value=None):
        r"""UpdateShareSpaceConfigReq

        The model defined in huaweicloud sdk

        :param config_name: 配置名称。
        :type config_name: str
        :param config_value: 配置值，使用Json字符串,&#39;{\&quot;share_space_name\&quot;:“协同空间”, \&quot;use_share_password\&quot;:是否使用协同密码：true/false, \&quot;allow_anonymous\&quot;:是否匿名加入协同:true/false, \&quot;audio_and_video\&quot;:是否使用音频,\&quot;AUDIO\&quot;/\&quot;NONE\&quot;/\&quot;AUDIO_AND_VIDEO\&quot;,\&quot;keyboard_mouse_ctl\&quot;:云桌面是否可用键鼠true/false,\&quot;anonymous_input_ctrl\&quot;:是否开启匿名用户键鼠输入权限true/false, \&quot;is_user_confirm_enabled\&quot;:是否需要用户应答true/false,\&quot;wait_confirm_time\&quot;:等待时间30-180s}。&#39;
        :type config_value: str
        """
        
        

        self._config_name = None
        self._config_value = None
        self.discriminator = None

        if config_name is not None:
            self.config_name = config_name
        if config_value is not None:
            self.config_value = config_value

    @property
    def config_name(self):
        r"""Gets the config_name of this UpdateShareSpaceConfigReq.

        配置名称。

        :return: The config_name of this UpdateShareSpaceConfigReq.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this UpdateShareSpaceConfigReq.

        配置名称。

        :param config_name: The config_name of this UpdateShareSpaceConfigReq.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def config_value(self):
        r"""Gets the config_value of this UpdateShareSpaceConfigReq.

        配置值，使用Json字符串,'{\"share_space_name\":“协同空间”, \"use_share_password\":是否使用协同密码：true/false, \"allow_anonymous\":是否匿名加入协同:true/false, \"audio_and_video\":是否使用音频,\"AUDIO\"/\"NONE\"/\"AUDIO_AND_VIDEO\",\"keyboard_mouse_ctl\":云桌面是否可用键鼠true/false,\"anonymous_input_ctrl\":是否开启匿名用户键鼠输入权限true/false, \"is_user_confirm_enabled\":是否需要用户应答true/false,\"wait_confirm_time\":等待时间30-180s}。'

        :return: The config_value of this UpdateShareSpaceConfigReq.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this UpdateShareSpaceConfigReq.

        配置值，使用Json字符串,'{\"share_space_name\":“协同空间”, \"use_share_password\":是否使用协同密码：true/false, \"allow_anonymous\":是否匿名加入协同:true/false, \"audio_and_video\":是否使用音频,\"AUDIO\"/\"NONE\"/\"AUDIO_AND_VIDEO\",\"keyboard_mouse_ctl\":云桌面是否可用键鼠true/false,\"anonymous_input_ctrl\":是否开启匿名用户键鼠输入权限true/false, \"is_user_confirm_enabled\":是否需要用户应答true/false,\"wait_confirm_time\":等待时间30-180s}。'

        :param config_value: The config_value of this UpdateShareSpaceConfigReq.
        :type config_value: str
        """
        self._config_value = config_value

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
        if not isinstance(other, UpdateShareSpaceConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
