# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchGaussMySqlProxyBinlogPullRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'support_binlog_pull': 'bool',
        'binlog_route_master': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'support_binlog_pull': 'support_binlog_pull',
        'binlog_route_master': 'binlog_route_master'
    }

    def __init__(self, type=None, support_binlog_pull=None, binlog_route_master=None):
        r"""SwitchGaussMySqlProxyBinlogPullRequestBody

        The model defined in huaweicloud sdk

        :param type: **参数解释**：  数据库代理模式。  **约束限制**：  不涉及。  **取值范围**： - readwrite：读写模式。 - readonly：TP只读模式。  **默认取值**：  不涉及。
        :type type: str
        :param support_binlog_pull: **参数解释**：  数据库代理拉取Binlog开关。  **约束限制**：  不涉及。  **取值范围**： - true：开启。 - false：关闭。  **默认取值**：  不涉及。
        :type support_binlog_pull: bool
        :param binlog_route_master: **参数解释**： 数据库代理是否从数据库主节点拉取Binlog。  **约束限制**：  - 读写代理可以设置从数据库主节点或者只读节点拉取Binlog，TP只读代理只支持从只读节点拉取Binlog。 - binlog_route_master参数仅在support_binlog_pull为true时生效。  **取值范围**： - true：从主节点拉取。 - false：从只读节点拉取。  **默认取值**：  false。
        :type binlog_route_master: bool
        """
        
        

        self._type = None
        self._support_binlog_pull = None
        self._binlog_route_master = None
        self.discriminator = None

        self.type = type
        self.support_binlog_pull = support_binlog_pull
        if binlog_route_master is not None:
            self.binlog_route_master = binlog_route_master

    @property
    def type(self):
        r"""Gets the type of this SwitchGaussMySqlProxyBinlogPullRequestBody.

        **参数解释**：  数据库代理模式。  **约束限制**：  不涉及。  **取值范围**： - readwrite：读写模式。 - readonly：TP只读模式。  **默认取值**：  不涉及。

        :return: The type of this SwitchGaussMySqlProxyBinlogPullRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SwitchGaussMySqlProxyBinlogPullRequestBody.

        **参数解释**：  数据库代理模式。  **约束限制**：  不涉及。  **取值范围**： - readwrite：读写模式。 - readonly：TP只读模式。  **默认取值**：  不涉及。

        :param type: The type of this SwitchGaussMySqlProxyBinlogPullRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def support_binlog_pull(self):
        r"""Gets the support_binlog_pull of this SwitchGaussMySqlProxyBinlogPullRequestBody.

        **参数解释**：  数据库代理拉取Binlog开关。  **约束限制**：  不涉及。  **取值范围**： - true：开启。 - false：关闭。  **默认取值**：  不涉及。

        :return: The support_binlog_pull of this SwitchGaussMySqlProxyBinlogPullRequestBody.
        :rtype: bool
        """
        return self._support_binlog_pull

    @support_binlog_pull.setter
    def support_binlog_pull(self, support_binlog_pull):
        r"""Sets the support_binlog_pull of this SwitchGaussMySqlProxyBinlogPullRequestBody.

        **参数解释**：  数据库代理拉取Binlog开关。  **约束限制**：  不涉及。  **取值范围**： - true：开启。 - false：关闭。  **默认取值**：  不涉及。

        :param support_binlog_pull: The support_binlog_pull of this SwitchGaussMySqlProxyBinlogPullRequestBody.
        :type support_binlog_pull: bool
        """
        self._support_binlog_pull = support_binlog_pull

    @property
    def binlog_route_master(self):
        r"""Gets the binlog_route_master of this SwitchGaussMySqlProxyBinlogPullRequestBody.

        **参数解释**： 数据库代理是否从数据库主节点拉取Binlog。  **约束限制**：  - 读写代理可以设置从数据库主节点或者只读节点拉取Binlog，TP只读代理只支持从只读节点拉取Binlog。 - binlog_route_master参数仅在support_binlog_pull为true时生效。  **取值范围**： - true：从主节点拉取。 - false：从只读节点拉取。  **默认取值**：  false。

        :return: The binlog_route_master of this SwitchGaussMySqlProxyBinlogPullRequestBody.
        :rtype: bool
        """
        return self._binlog_route_master

    @binlog_route_master.setter
    def binlog_route_master(self, binlog_route_master):
        r"""Sets the binlog_route_master of this SwitchGaussMySqlProxyBinlogPullRequestBody.

        **参数解释**： 数据库代理是否从数据库主节点拉取Binlog。  **约束限制**：  - 读写代理可以设置从数据库主节点或者只读节点拉取Binlog，TP只读代理只支持从只读节点拉取Binlog。 - binlog_route_master参数仅在support_binlog_pull为true时生效。  **取值范围**： - true：从主节点拉取。 - false：从只读节点拉取。  **默认取值**：  false。

        :param binlog_route_master: The binlog_route_master of this SwitchGaussMySqlProxyBinlogPullRequestBody.
        :type binlog_route_master: bool
        """
        self._binlog_route_master = binlog_route_master

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
        if not isinstance(other, SwitchGaussMySqlProxyBinlogPullRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
