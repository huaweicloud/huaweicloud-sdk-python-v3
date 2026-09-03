# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelConnectionProcessRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'process_ids': 'list[str]',
        'kill_all': 'bool',
        'node_id': 'str',
        'node_role': 'str'
    }

    attribute_map = {
        'process_ids': 'process_ids',
        'kill_all': 'kill_all',
        'node_id': 'node_id',
        'node_role': 'node_role'
    }

    def __init__(self, process_ids=None, kill_all=None, node_id=None, node_role=None):
        r"""CancelConnectionProcessRequestBody

        The model defined in huaweicloud sdk

        :param process_ids: 查杀会话的ID列表
        :type process_ids: list[str]
        :param kill_all: 是否查杀全部会话
        :type kill_all: bool
        :param node_id: 实例节点ID，实例节点的唯一标识
        :type node_id: str
        :param node_role: 实例节点类型（master：主节点，slave：副节点，readreplica：只读节点）
        :type node_role: str
        """
        
        

        self._process_ids = None
        self._kill_all = None
        self._node_id = None
        self._node_role = None
        self.discriminator = None

        self.process_ids = process_ids
        if kill_all is not None:
            self.kill_all = kill_all
        if node_id is not None:
            self.node_id = node_id
        if node_role is not None:
            self.node_role = node_role

    @property
    def process_ids(self):
        r"""Gets the process_ids of this CancelConnectionProcessRequestBody.

        查杀会话的ID列表

        :return: The process_ids of this CancelConnectionProcessRequestBody.
        :rtype: list[str]
        """
        return self._process_ids

    @process_ids.setter
    def process_ids(self, process_ids):
        r"""Sets the process_ids of this CancelConnectionProcessRequestBody.

        查杀会话的ID列表

        :param process_ids: The process_ids of this CancelConnectionProcessRequestBody.
        :type process_ids: list[str]
        """
        self._process_ids = process_ids

    @property
    def kill_all(self):
        r"""Gets the kill_all of this CancelConnectionProcessRequestBody.

        是否查杀全部会话

        :return: The kill_all of this CancelConnectionProcessRequestBody.
        :rtype: bool
        """
        return self._kill_all

    @kill_all.setter
    def kill_all(self, kill_all):
        r"""Sets the kill_all of this CancelConnectionProcessRequestBody.

        是否查杀全部会话

        :param kill_all: The kill_all of this CancelConnectionProcessRequestBody.
        :type kill_all: bool
        """
        self._kill_all = kill_all

    @property
    def node_id(self):
        r"""Gets the node_id of this CancelConnectionProcessRequestBody.

        实例节点ID，实例节点的唯一标识

        :return: The node_id of this CancelConnectionProcessRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CancelConnectionProcessRequestBody.

        实例节点ID，实例节点的唯一标识

        :param node_id: The node_id of this CancelConnectionProcessRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_role(self):
        r"""Gets the node_role of this CancelConnectionProcessRequestBody.

        实例节点类型（master：主节点，slave：副节点，readreplica：只读节点）

        :return: The node_role of this CancelConnectionProcessRequestBody.
        :rtype: str
        """
        return self._node_role

    @node_role.setter
    def node_role(self, node_role):
        r"""Sets the node_role of this CancelConnectionProcessRequestBody.

        实例节点类型（master：主节点，slave：副节点，readreplica：只读节点）

        :param node_role: The node_role of this CancelConnectionProcessRequestBody.
        :type node_role: str
        """
        self._node_role = node_role

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
        if not isinstance(other, CancelConnectionProcessRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
