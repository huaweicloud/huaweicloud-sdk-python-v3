# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateChannelDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'description': 'str',
        'group_id': 'str',
        'input': 'list[CreateModuleVo]',
        'nodes': 'list[NodeVo]',
        'output': 'list[CreateModuleVo]',
        'parser_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'action': 'action',
        'description': 'description',
        'group_id': 'group_id',
        'input': 'input',
        'nodes': 'nodes',
        'output': 'output',
        'parser_id': 'parser_id',
        'title': 'title'
    }

    def __init__(self, action=None, description=None, group_id=None, input=None, nodes=None, output=None, parser_id=None, title=None):
        r"""CreateChannelDto

        The model defined in huaweicloud sdk

        :param action: **参数解释**: 节点运行状态的监控 - START 开始 - STOP 停止 - REMOVE 移除 - RESTART 重启 - REFRESH 刷新 - INSTALL 安装  **约束限制** 不涉及 **取值范围**: - START - STOP - REMOVE - RESTART - REFRESH - INSTALL  **默认值** 不涉及
        :type action: str
        :param description: 描述信息
        :type description: str
        :param group_id: UUID
        :type group_id: str
        :param input: 相关描述信息
        :type input: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        :param nodes: 相关描述信息
        :type nodes: list[:class:`huaweicloudsdksecmaster.v1.NodeVo`]
        :param output: 相关描述信息
        :type output: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        :param parser_id: UUID
        :type parser_id: str
        :param title: 相关标题
        :type title: str
        """
        
        

        self._action = None
        self._description = None
        self._group_id = None
        self._input = None
        self._nodes = None
        self._output = None
        self._parser_id = None
        self._title = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        self.group_id = group_id
        self.input = input
        self.nodes = nodes
        self.output = output
        self.parser_id = parser_id
        self.title = title

    @property
    def action(self):
        r"""Gets the action of this CreateChannelDto.

        **参数解释**: 节点运行状态的监控 - START 开始 - STOP 停止 - REMOVE 移除 - RESTART 重启 - REFRESH 刷新 - INSTALL 安装  **约束限制** 不涉及 **取值范围**: - START - STOP - REMOVE - RESTART - REFRESH - INSTALL  **默认值** 不涉及

        :return: The action of this CreateChannelDto.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateChannelDto.

        **参数解释**: 节点运行状态的监控 - START 开始 - STOP 停止 - REMOVE 移除 - RESTART 重启 - REFRESH 刷新 - INSTALL 安装  **约束限制** 不涉及 **取值范围**: - START - STOP - REMOVE - RESTART - REFRESH - INSTALL  **默认值** 不涉及

        :param action: The action of this CreateChannelDto.
        :type action: str
        """
        self._action = action

    @property
    def description(self):
        r"""Gets the description of this CreateChannelDto.

        描述信息

        :return: The description of this CreateChannelDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateChannelDto.

        描述信息

        :param description: The description of this CreateChannelDto.
        :type description: str
        """
        self._description = description

    @property
    def group_id(self):
        r"""Gets the group_id of this CreateChannelDto.

        UUID

        :return: The group_id of this CreateChannelDto.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CreateChannelDto.

        UUID

        :param group_id: The group_id of this CreateChannelDto.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def input(self):
        r"""Gets the input of this CreateChannelDto.

        相关描述信息

        :return: The input of this CreateChannelDto.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this CreateChannelDto.

        相关描述信息

        :param input: The input of this CreateChannelDto.
        :type input: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        """
        self._input = input

    @property
    def nodes(self):
        r"""Gets the nodes of this CreateChannelDto.

        相关描述信息

        :return: The nodes of this CreateChannelDto.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.NodeVo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this CreateChannelDto.

        相关描述信息

        :param nodes: The nodes of this CreateChannelDto.
        :type nodes: list[:class:`huaweicloudsdksecmaster.v1.NodeVo`]
        """
        self._nodes = nodes

    @property
    def output(self):
        r"""Gets the output of this CreateChannelDto.

        相关描述信息

        :return: The output of this CreateChannelDto.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this CreateChannelDto.

        相关描述信息

        :param output: The output of this CreateChannelDto.
        :type output: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        """
        self._output = output

    @property
    def parser_id(self):
        r"""Gets the parser_id of this CreateChannelDto.

        UUID

        :return: The parser_id of this CreateChannelDto.
        :rtype: str
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        r"""Sets the parser_id of this CreateChannelDto.

        UUID

        :param parser_id: The parser_id of this CreateChannelDto.
        :type parser_id: str
        """
        self._parser_id = parser_id

    @property
    def title(self):
        r"""Gets the title of this CreateChannelDto.

        相关标题

        :return: The title of this CreateChannelDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateChannelDto.

        相关标题

        :param title: The title of this CreateChannelDto.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, CreateChannelDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
