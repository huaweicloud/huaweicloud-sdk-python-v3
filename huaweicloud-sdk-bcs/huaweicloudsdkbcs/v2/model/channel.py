# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Channel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'create_time': 'str',
        'consensus': 'str',
        'peers': 'dict(str, list[str])',
        'consensus_nodes': 'dict(str, list[str])'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'consensus': 'consensus',
        'peers': 'peers',
        'consensus_nodes': 'consensusNodes'
    }

    def __init__(self, name=None, description=None, create_time=None, consensus=None, peers=None, consensus_nodes=None):
        r"""Channel

        The model defined in huaweicloud sdk

        :param name: 通道名
        :type name: str
        :param description: 通道细节描述
        :type description: str
        :param create_time: 通道创建时间
        :type create_time: str
        :param consensus: 共识策略
        :type consensus: str
        :param peers: key:组织名，value:节点名称列表
        :type peers: dict(str, list[str])
        :param consensus_nodes: key:组织名，value:节点名称列表
        :type consensus_nodes: dict(str, list[str])
        """
        
        

        self._name = None
        self._description = None
        self._create_time = None
        self._consensus = None
        self._peers = None
        self._consensus_nodes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if consensus is not None:
            self.consensus = consensus
        if peers is not None:
            self.peers = peers
        if consensus_nodes is not None:
            self.consensus_nodes = consensus_nodes

    @property
    def name(self):
        r"""Gets the name of this Channel.

        通道名

        :return: The name of this Channel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Channel.

        通道名

        :param name: The name of this Channel.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Channel.

        通道细节描述

        :return: The description of this Channel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Channel.

        通道细节描述

        :param description: The description of this Channel.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this Channel.

        通道创建时间

        :return: The create_time of this Channel.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Channel.

        通道创建时间

        :param create_time: The create_time of this Channel.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def consensus(self):
        r"""Gets the consensus of this Channel.

        共识策略

        :return: The consensus of this Channel.
        :rtype: str
        """
        return self._consensus

    @consensus.setter
    def consensus(self, consensus):
        r"""Sets the consensus of this Channel.

        共识策略

        :param consensus: The consensus of this Channel.
        :type consensus: str
        """
        self._consensus = consensus

    @property
    def peers(self):
        r"""Gets the peers of this Channel.

        key:组织名，value:节点名称列表

        :return: The peers of this Channel.
        :rtype: dict(str, list[str])
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        r"""Sets the peers of this Channel.

        key:组织名，value:节点名称列表

        :param peers: The peers of this Channel.
        :type peers: dict(str, list[str])
        """
        self._peers = peers

    @property
    def consensus_nodes(self):
        r"""Gets the consensus_nodes of this Channel.

        key:组织名，value:节点名称列表

        :return: The consensus_nodes of this Channel.
        :rtype: dict(str, list[str])
        """
        return self._consensus_nodes

    @consensus_nodes.setter
    def consensus_nodes(self, consensus_nodes):
        r"""Sets the consensus_nodes of this Channel.

        key:组织名，value:节点名称列表

        :param consensus_nodes: The consensus_nodes of this Channel.
        :type consensus_nodes: dict(str, list[str])
        """
        self._consensus_nodes = consensus_nodes

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
        if not isinstance(other, Channel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
