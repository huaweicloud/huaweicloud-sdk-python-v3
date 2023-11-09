# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicsAgentDeployBcs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'bcs_ip': 'str',
        'block_chain_id': 'str',
        'block_chain_name': 'str',
        'channel_name': 'str',
        'org_name': 'str',
        'org_name_hash': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'bcs_ip': 'bcs_ip',
        'block_chain_id': 'block_chain_id',
        'block_chain_name': 'block_chain_name',
        'channel_name': 'channel_name',
        'org_name': 'org_name',
        'org_name_hash': 'org_name_hash'
    }

    def __init__(self, agent_id=None, bcs_ip=None, block_chain_id=None, block_chain_name=None, channel_name=None, org_name=None, org_name_hash=None):
        """TicsAgentDeployBcs

        The model defined in huaweicloud sdk

        :param agent_id: 可信节点Id
        :type agent_id: str
        :param bcs_ip: 区块链ip
        :type bcs_ip: str
        :param block_chain_id: 区块链Id
        :type block_chain_id: str
        :param block_chain_name: 区块链名称
        :type block_chain_name: str
        :param channel_name: 通道名称
        :type channel_name: str
        :param org_name: 组织名称
        :type org_name: str
        :param org_name_hash: 组织名称的hash
        :type org_name_hash: str
        """
        
        

        self._agent_id = None
        self._bcs_ip = None
        self._block_chain_id = None
        self._block_chain_name = None
        self._channel_name = None
        self._org_name = None
        self._org_name_hash = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if bcs_ip is not None:
            self.bcs_ip = bcs_ip
        if block_chain_id is not None:
            self.block_chain_id = block_chain_id
        if block_chain_name is not None:
            self.block_chain_name = block_chain_name
        if channel_name is not None:
            self.channel_name = channel_name
        if org_name is not None:
            self.org_name = org_name
        if org_name_hash is not None:
            self.org_name_hash = org_name_hash

    @property
    def agent_id(self):
        """Gets the agent_id of this TicsAgentDeployBcs.

        可信节点Id

        :return: The agent_id of this TicsAgentDeployBcs.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this TicsAgentDeployBcs.

        可信节点Id

        :param agent_id: The agent_id of this TicsAgentDeployBcs.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def bcs_ip(self):
        """Gets the bcs_ip of this TicsAgentDeployBcs.

        区块链ip

        :return: The bcs_ip of this TicsAgentDeployBcs.
        :rtype: str
        """
        return self._bcs_ip

    @bcs_ip.setter
    def bcs_ip(self, bcs_ip):
        """Sets the bcs_ip of this TicsAgentDeployBcs.

        区块链ip

        :param bcs_ip: The bcs_ip of this TicsAgentDeployBcs.
        :type bcs_ip: str
        """
        self._bcs_ip = bcs_ip

    @property
    def block_chain_id(self):
        """Gets the block_chain_id of this TicsAgentDeployBcs.

        区块链Id

        :return: The block_chain_id of this TicsAgentDeployBcs.
        :rtype: str
        """
        return self._block_chain_id

    @block_chain_id.setter
    def block_chain_id(self, block_chain_id):
        """Sets the block_chain_id of this TicsAgentDeployBcs.

        区块链Id

        :param block_chain_id: The block_chain_id of this TicsAgentDeployBcs.
        :type block_chain_id: str
        """
        self._block_chain_id = block_chain_id

    @property
    def block_chain_name(self):
        """Gets the block_chain_name of this TicsAgentDeployBcs.

        区块链名称

        :return: The block_chain_name of this TicsAgentDeployBcs.
        :rtype: str
        """
        return self._block_chain_name

    @block_chain_name.setter
    def block_chain_name(self, block_chain_name):
        """Sets the block_chain_name of this TicsAgentDeployBcs.

        区块链名称

        :param block_chain_name: The block_chain_name of this TicsAgentDeployBcs.
        :type block_chain_name: str
        """
        self._block_chain_name = block_chain_name

    @property
    def channel_name(self):
        """Gets the channel_name of this TicsAgentDeployBcs.

        通道名称

        :return: The channel_name of this TicsAgentDeployBcs.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this TicsAgentDeployBcs.

        通道名称

        :param channel_name: The channel_name of this TicsAgentDeployBcs.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def org_name(self):
        """Gets the org_name of this TicsAgentDeployBcs.

        组织名称

        :return: The org_name of this TicsAgentDeployBcs.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this TicsAgentDeployBcs.

        组织名称

        :param org_name: The org_name of this TicsAgentDeployBcs.
        :type org_name: str
        """
        self._org_name = org_name

    @property
    def org_name_hash(self):
        """Gets the org_name_hash of this TicsAgentDeployBcs.

        组织名称的hash

        :return: The org_name_hash of this TicsAgentDeployBcs.
        :rtype: str
        """
        return self._org_name_hash

    @org_name_hash.setter
    def org_name_hash(self, org_name_hash):
        """Sets the org_name_hash of this TicsAgentDeployBcs.

        组织名称的hash

        :param org_name_hash: The org_name_hash of this TicsAgentDeployBcs.
        :type org_name_hash: str
        """
        self._org_name_hash = org_name_hash

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
        if not isinstance(other, TicsAgentDeployBcs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
