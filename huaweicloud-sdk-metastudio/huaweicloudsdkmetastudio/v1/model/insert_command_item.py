# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsertCommandItem:

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
        'params': 'object',
        'source': 'str'
    }

    attribute_map = {
        'command_id': 'command_id',
        'command': 'command',
        'params': 'params',
        'source': 'source'
    }

    def __init__(self, command_id=None, command=None, params=None, source=None):
        r"""InsertCommandItem

        The model defined in huaweicloud sdk

        :param command_id: 控制命令ID
        :type command_id: str
        :param command: 命令名称。 - INSERT_PLAY_SCRIPT: 插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：[PlayTextInfo](metastudio_02_0014.xml) - INSERT_PLAY_AUDIO:插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：[PlayAudioInfo](metastudio_02_0014.xml) - REWRITE_INTERACTION_RULES: 修改互动规则。params结构定义：[PlayAudioInfo](metastudio_02_0014.xml)
        :type command: str
        :param params: 命令参数。
        :type params: object
        :param source: 命令来源。 * EXTERNAL： 外部命令 * AUTO: 系统自动触发
        :type source: str
        """
        
        

        self._command_id = None
        self._command = None
        self._params = None
        self._source = None
        self.discriminator = None

        if command_id is not None:
            self.command_id = command_id
        if command is not None:
            self.command = command
        if params is not None:
            self.params = params
        if source is not None:
            self.source = source

    @property
    def command_id(self):
        r"""Gets the command_id of this InsertCommandItem.

        控制命令ID

        :return: The command_id of this InsertCommandItem.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        r"""Sets the command_id of this InsertCommandItem.

        控制命令ID

        :param command_id: The command_id of this InsertCommandItem.
        :type command_id: str
        """
        self._command_id = command_id

    @property
    def command(self):
        r"""Gets the command of this InsertCommandItem.

        命令名称。 - INSERT_PLAY_SCRIPT: 插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：[PlayTextInfo](metastudio_02_0014.xml) - INSERT_PLAY_AUDIO:插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：[PlayAudioInfo](metastudio_02_0014.xml) - REWRITE_INTERACTION_RULES: 修改互动规则。params结构定义：[PlayAudioInfo](metastudio_02_0014.xml)

        :return: The command of this InsertCommandItem.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this InsertCommandItem.

        命令名称。 - INSERT_PLAY_SCRIPT: 插入表演脚本。用于互动回复。数字人不变，背景不变。params结构定义：[PlayTextInfo](metastudio_02_0014.xml) - INSERT_PLAY_AUDIO:插入驱动音频。用于音频直接驱动。数字人不变，背景不变。params结构定义：[PlayAudioInfo](metastudio_02_0014.xml) - REWRITE_INTERACTION_RULES: 修改互动规则。params结构定义：[PlayAudioInfo](metastudio_02_0014.xml)

        :param command: The command of this InsertCommandItem.
        :type command: str
        """
        self._command = command

    @property
    def params(self):
        r"""Gets the params of this InsertCommandItem.

        命令参数。

        :return: The params of this InsertCommandItem.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this InsertCommandItem.

        命令参数。

        :param params: The params of this InsertCommandItem.
        :type params: object
        """
        self._params = params

    @property
    def source(self):
        r"""Gets the source of this InsertCommandItem.

        命令来源。 * EXTERNAL： 外部命令 * AUTO: 系统自动触发

        :return: The source of this InsertCommandItem.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this InsertCommandItem.

        命令来源。 * EXTERNAL： 外部命令 * AUTO: 系统自动触发

        :param source: The source of this InsertCommandItem.
        :type source: str
        """
        self._source = source

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InsertCommandItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
