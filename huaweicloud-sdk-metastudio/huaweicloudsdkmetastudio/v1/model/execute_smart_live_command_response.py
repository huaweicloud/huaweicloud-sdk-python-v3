# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteSmartLiveCommandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command_id': 'str',
        'command': 'str',
        'result': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'command_id': 'command_id',
        'command': 'command',
        'result': 'result',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, command_id=None, command=None, result=None, x_request_id=None):
        r"""ExecuteSmartLiveCommandResponse

        The model defined in huaweicloud sdk

        :param command_id: 控制命令ID
        :type command_id: str
        :param command: 命令名称。 - INSERT_PLAY_SCRIPT：插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：ShootScript。 - REWRITE_PLAY_SCRIPT：动态编辑未播放剧本。params结构定义：scene_scripts。 - INSERT_PLAY_AUDIO：插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：PlayAudioInfo。 - GET_CURRENT_PLAYING_SCRIPTS：查询本轮剧本列表。响应为LivePlayingScriptList结构。 - REFRESH_OUTPUT_URL：更新当前任务的rtmp推流信息。params结构定义： RefreshOutputUrlConfig。 - REWRITE_INTERACTION_RULES：动态修改互动规则。params结构定义：interaction_rules。 - GET_LIVE_JOB_CONFIG_INFO：获取任务中的房间信息。params结构定义：SmartLiveRoomInfo。 - CLEAN_UP_INSERT_COMMAND：清理未播放的插入命令。params结构定义：[CleanUpInsertCommand](metastudio_02_0014.xml) - RESET_EXIT_CONFIG: 重置退出参数。params结构定义：LiveExitConfig
        :type command: str
        :param result: 命令执行结果
        :type result: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ExecuteSmartLiveCommandResponse, self).__init__()

        self._command_id = None
        self._command = None
        self._result = None
        self._x_request_id = None
        self.discriminator = None

        if command_id is not None:
            self.command_id = command_id
        if command is not None:
            self.command = command
        if result is not None:
            self.result = result
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def command_id(self):
        r"""Gets the command_id of this ExecuteSmartLiveCommandResponse.

        控制命令ID

        :return: The command_id of this ExecuteSmartLiveCommandResponse.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        r"""Sets the command_id of this ExecuteSmartLiveCommandResponse.

        控制命令ID

        :param command_id: The command_id of this ExecuteSmartLiveCommandResponse.
        :type command_id: str
        """
        self._command_id = command_id

    @property
    def command(self):
        r"""Gets the command of this ExecuteSmartLiveCommandResponse.

        命令名称。 - INSERT_PLAY_SCRIPT：插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：ShootScript。 - REWRITE_PLAY_SCRIPT：动态编辑未播放剧本。params结构定义：scene_scripts。 - INSERT_PLAY_AUDIO：插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：PlayAudioInfo。 - GET_CURRENT_PLAYING_SCRIPTS：查询本轮剧本列表。响应为LivePlayingScriptList结构。 - REFRESH_OUTPUT_URL：更新当前任务的rtmp推流信息。params结构定义： RefreshOutputUrlConfig。 - REWRITE_INTERACTION_RULES：动态修改互动规则。params结构定义：interaction_rules。 - GET_LIVE_JOB_CONFIG_INFO：获取任务中的房间信息。params结构定义：SmartLiveRoomInfo。 - CLEAN_UP_INSERT_COMMAND：清理未播放的插入命令。params结构定义：[CleanUpInsertCommand](metastudio_02_0014.xml) - RESET_EXIT_CONFIG: 重置退出参数。params结构定义：LiveExitConfig

        :return: The command of this ExecuteSmartLiveCommandResponse.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this ExecuteSmartLiveCommandResponse.

        命令名称。 - INSERT_PLAY_SCRIPT：插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：ShootScript。 - REWRITE_PLAY_SCRIPT：动态编辑未播放剧本。params结构定义：scene_scripts。 - INSERT_PLAY_AUDIO：插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：PlayAudioInfo。 - GET_CURRENT_PLAYING_SCRIPTS：查询本轮剧本列表。响应为LivePlayingScriptList结构。 - REFRESH_OUTPUT_URL：更新当前任务的rtmp推流信息。params结构定义： RefreshOutputUrlConfig。 - REWRITE_INTERACTION_RULES：动态修改互动规则。params结构定义：interaction_rules。 - GET_LIVE_JOB_CONFIG_INFO：获取任务中的房间信息。params结构定义：SmartLiveRoomInfo。 - CLEAN_UP_INSERT_COMMAND：清理未播放的插入命令。params结构定义：[CleanUpInsertCommand](metastudio_02_0014.xml) - RESET_EXIT_CONFIG: 重置退出参数。params结构定义：LiveExitConfig

        :param command: The command of this ExecuteSmartLiveCommandResponse.
        :type command: str
        """
        self._command = command

    @property
    def result(self):
        r"""Gets the result of this ExecuteSmartLiveCommandResponse.

        命令执行结果

        :return: The result of this ExecuteSmartLiveCommandResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ExecuteSmartLiveCommandResponse.

        命令执行结果

        :param result: The result of this ExecuteSmartLiveCommandResponse.
        :type result: str
        """
        self._result = result

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ExecuteSmartLiveCommandResponse.

        :return: The x_request_id of this ExecuteSmartLiveCommandResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ExecuteSmartLiveCommandResponse.

        :param x_request_id: The x_request_id of this ExecuteSmartLiveCommandResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ExecuteSmartLiveCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
