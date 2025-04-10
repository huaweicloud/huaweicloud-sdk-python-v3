# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelInfo:

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
        'org_names': 'list[str]',
        'org_name_hash': 'list[str]',
        'peers': 'dict(str, list[str])'
    }

    attribute_map = {
        'name': 'name',
        'org_names': 'org_names',
        'org_name_hash': 'org_name_hash',
        'peers': 'peers'
    }

    def __init__(self, name=None, org_names=None, org_name_hash=None, peers=None):
        r"""ChannelInfo

        The model defined in huaweicloud sdk

        :param name: 通道名
        :type name: str
        :param org_names: 通道中组织名
        :type org_names: list[str]
        :param org_name_hash: 通道中组织名的哈希值
        :type org_name_hash: list[str]
        :param peers: key:组织名，value:peer节点数组
        :type peers: dict(str, list[str])
        """
        
        

        self._name = None
        self._org_names = None
        self._org_name_hash = None
        self._peers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if org_names is not None:
            self.org_names = org_names
        if org_name_hash is not None:
            self.org_name_hash = org_name_hash
        if peers is not None:
            self.peers = peers

    @property
    def name(self):
        r"""Gets the name of this ChannelInfo.

        通道名

        :return: The name of this ChannelInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChannelInfo.

        通道名

        :param name: The name of this ChannelInfo.
        :type name: str
        """
        self._name = name

    @property
    def org_names(self):
        r"""Gets the org_names of this ChannelInfo.

        通道中组织名

        :return: The org_names of this ChannelInfo.
        :rtype: list[str]
        """
        return self._org_names

    @org_names.setter
    def org_names(self, org_names):
        r"""Sets the org_names of this ChannelInfo.

        通道中组织名

        :param org_names: The org_names of this ChannelInfo.
        :type org_names: list[str]
        """
        self._org_names = org_names

    @property
    def org_name_hash(self):
        r"""Gets the org_name_hash of this ChannelInfo.

        通道中组织名的哈希值

        :return: The org_name_hash of this ChannelInfo.
        :rtype: list[str]
        """
        return self._org_name_hash

    @org_name_hash.setter
    def org_name_hash(self, org_name_hash):
        r"""Sets the org_name_hash of this ChannelInfo.

        通道中组织名的哈希值

        :param org_name_hash: The org_name_hash of this ChannelInfo.
        :type org_name_hash: list[str]
        """
        self._org_name_hash = org_name_hash

    @property
    def peers(self):
        r"""Gets the peers of this ChannelInfo.

        key:组织名，value:peer节点数组

        :return: The peers of this ChannelInfo.
        :rtype: dict(str, list[str])
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        r"""Sets the peers of this ChannelInfo.

        key:组织名，value:peer节点数组

        :param peers: The peers of this ChannelInfo.
        :type peers: dict(str, list[str])
        """
        self._peers = peers

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
        if not isinstance(other, ChannelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
