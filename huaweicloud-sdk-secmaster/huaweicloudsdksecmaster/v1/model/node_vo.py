# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'args': 'list[ArgsVo]',
        'node_id': 'str',
        'node_status': 'str'
    }

    attribute_map = {
        'args': 'args',
        'node_id': 'node_id',
        'node_status': 'node_status'
    }

    def __init__(self, args=None, node_id=None, node_status=None):
        r"""NodeVo

        The model defined in huaweicloud sdk

        :param args: 相关描述信息
        :type args: list[:class:`huaweicloudsdksecmaster.v1.ArgsVo`]
        :param node_id: UUID
        :type node_id: str
        :param node_status: **参数解释**: 节点状态 - RUN 运行 - STOP 停止  **约束限制** 不涉及 **取值范围**: - RUN - STOP  **默认值** 不涉及
        :type node_status: str
        """
        
        

        self._args = None
        self._node_id = None
        self._node_status = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if node_id is not None:
            self.node_id = node_id
        if node_status is not None:
            self.node_status = node_status

    @property
    def args(self):
        r"""Gets the args of this NodeVo.

        相关描述信息

        :return: The args of this NodeVo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ArgsVo`]
        """
        return self._args

    @args.setter
    def args(self, args):
        r"""Sets the args of this NodeVo.

        相关描述信息

        :param args: The args of this NodeVo.
        :type args: list[:class:`huaweicloudsdksecmaster.v1.ArgsVo`]
        """
        self._args = args

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeVo.

        UUID

        :return: The node_id of this NodeVo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeVo.

        UUID

        :param node_id: The node_id of this NodeVo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_status(self):
        r"""Gets the node_status of this NodeVo.

        **参数解释**: 节点状态 - RUN 运行 - STOP 停止  **约束限制** 不涉及 **取值范围**: - RUN - STOP  **默认值** 不涉及

        :return: The node_status of this NodeVo.
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        r"""Sets the node_status of this NodeVo.

        **参数解释**: 节点状态 - RUN 运行 - STOP 停止  **约束限制** 不涉及 **取值范围**: - RUN - STOP  **默认值** 不涉及

        :param node_status: The node_status of this NodeVo.
        :type node_status: str
        """
        self._node_status = node_status

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
        if not isinstance(other, NodeVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
