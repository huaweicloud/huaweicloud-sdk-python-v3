# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InheritConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'inherit_type': 'str',
        'inherit_time_type': 'str'
    }

    attribute_map = {
        'status': 'status',
        'inherit_type': 'inherit_type',
        'inherit_time_type': 'inherit_time_type'
    }

    def __init__(self, status=None, inherit_type=None, inherit_time_type=None):
        r"""InheritConfig

        The model defined in huaweicloud sdk

        :param status: 是否开启鉴权继承，on：开启,off：关闭。
        :type status: str
        :param inherit_type: 鉴权继承配置， m3u8：M3U8,mpd：MPD,输入多个时用“,”分开，例如“m3u8,mpd”  &gt; 开启鉴权继承时，该参数必填。
        :type inherit_type: str
        :param inherit_time_type: 鉴权继承的文件类型时间, sys_time：当前系统时间，parent_url_time：与m3u8和mpd访问链接保持一致。  &gt; 开启鉴权继承时，该参数必填。
        :type inherit_time_type: str
        """
        
        

        self._status = None
        self._inherit_type = None
        self._inherit_time_type = None
        self.discriminator = None

        self.status = status
        if inherit_type is not None:
            self.inherit_type = inherit_type
        if inherit_time_type is not None:
            self.inherit_time_type = inherit_time_type

    @property
    def status(self):
        r"""Gets the status of this InheritConfig.

        是否开启鉴权继承，on：开启,off：关闭。

        :return: The status of this InheritConfig.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InheritConfig.

        是否开启鉴权继承，on：开启,off：关闭。

        :param status: The status of this InheritConfig.
        :type status: str
        """
        self._status = status

    @property
    def inherit_type(self):
        r"""Gets the inherit_type of this InheritConfig.

        鉴权继承配置， m3u8：M3U8,mpd：MPD,输入多个时用“,”分开，例如“m3u8,mpd”  > 开启鉴权继承时，该参数必填。

        :return: The inherit_type of this InheritConfig.
        :rtype: str
        """
        return self._inherit_type

    @inherit_type.setter
    def inherit_type(self, inherit_type):
        r"""Sets the inherit_type of this InheritConfig.

        鉴权继承配置， m3u8：M3U8,mpd：MPD,输入多个时用“,”分开，例如“m3u8,mpd”  > 开启鉴权继承时，该参数必填。

        :param inherit_type: The inherit_type of this InheritConfig.
        :type inherit_type: str
        """
        self._inherit_type = inherit_type

    @property
    def inherit_time_type(self):
        r"""Gets the inherit_time_type of this InheritConfig.

        鉴权继承的文件类型时间, sys_time：当前系统时间，parent_url_time：与m3u8和mpd访问链接保持一致。  > 开启鉴权继承时，该参数必填。

        :return: The inherit_time_type of this InheritConfig.
        :rtype: str
        """
        return self._inherit_time_type

    @inherit_time_type.setter
    def inherit_time_type(self, inherit_time_type):
        r"""Sets the inherit_time_type of this InheritConfig.

        鉴权继承的文件类型时间, sys_time：当前系统时间，parent_url_time：与m3u8和mpd访问链接保持一致。  > 开启鉴权继承时，该参数必填。

        :param inherit_time_type: The inherit_time_type of this InheritConfig.
        :type inherit_time_type: str
        """
        self._inherit_time_type = inherit_time_type

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
        if not isinstance(other, InheritConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
