# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ControlSmartLiveReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'str',
        'params': 'object'
    }

    attribute_map = {
        'command': 'command',
        'params': 'params'
    }

    def __init__(self, command=None, params=None):
        """ControlSmartLiveReq

        The model defined in huaweicloud sdk

        :param command: 命令名称。 - INSERT_PLAY_SCRIPT: 插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：ShootScript - REWRITE_PLAY_SCRIPT: 动态编辑未播放剧本。params结构定义：scence_scripts - INSERT_PLAY_ADUIO: 插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：PlayAudioInfo
        :type command: str
        :param params: 命令参数。
        :type params: object
        """
        
        

        self._command = None
        self._params = None
        self.discriminator = None

        self.command = command
        if params is not None:
            self.params = params

    @property
    def command(self):
        """Gets the command of this ControlSmartLiveReq.

        命令名称。 - INSERT_PLAY_SCRIPT: 插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：ShootScript - REWRITE_PLAY_SCRIPT: 动态编辑未播放剧本。params结构定义：scence_scripts - INSERT_PLAY_ADUIO: 插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：PlayAudioInfo

        :return: The command of this ControlSmartLiveReq.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ControlSmartLiveReq.

        命令名称。 - INSERT_PLAY_SCRIPT: 插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：ShootScript - REWRITE_PLAY_SCRIPT: 动态编辑未播放剧本。params结构定义：scence_scripts - INSERT_PLAY_ADUIO: 插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：PlayAudioInfo

        :param command: The command of this ControlSmartLiveReq.
        :type command: str
        """
        self._command = command

    @property
    def params(self):
        """Gets the params of this ControlSmartLiveReq.

        命令参数。

        :return: The params of this ControlSmartLiveReq.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ControlSmartLiveReq.

        命令参数。

        :param params: The params of this ControlSmartLiveReq.
        :type params: object
        """
        self._params = params

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
        if not isinstance(other, ControlSmartLiveReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
