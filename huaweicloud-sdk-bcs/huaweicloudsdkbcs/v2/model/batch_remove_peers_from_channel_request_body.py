# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRemovePeersFromChannelRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_name': 'str',
        'peers': 'int'
    }

    attribute_map = {
        'org_name': 'org_name',
        'peers': 'peers'
    }

    def __init__(self, org_name=None, peers=None):
        """BatchRemovePeersFromChannelRequestBody

        The model defined in huaweicloud sdk

        :param org_name: 组织名称。仅可输入一个组织名称
        :type org_name: str
        :param peers: 要退出的节点个数。取值范围(0, 组织中节点总数)
        :type peers: int
        """
        
        

        self._org_name = None
        self._peers = None
        self.discriminator = None

        self.org_name = org_name
        self.peers = peers

    @property
    def org_name(self):
        """Gets the org_name of this BatchRemovePeersFromChannelRequestBody.

        组织名称。仅可输入一个组织名称

        :return: The org_name of this BatchRemovePeersFromChannelRequestBody.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this BatchRemovePeersFromChannelRequestBody.

        组织名称。仅可输入一个组织名称

        :param org_name: The org_name of this BatchRemovePeersFromChannelRequestBody.
        :type org_name: str
        """
        self._org_name = org_name

    @property
    def peers(self):
        """Gets the peers of this BatchRemovePeersFromChannelRequestBody.

        要退出的节点个数。取值范围(0, 组织中节点总数)

        :return: The peers of this BatchRemovePeersFromChannelRequestBody.
        :rtype: int
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this BatchRemovePeersFromChannelRequestBody.

        要退出的节点个数。取值范围(0, 组织中节点总数)

        :param peers: The peers of this BatchRemovePeersFromChannelRequestBody.
        :type peers: int
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
        if not isinstance(other, BatchRemovePeersFromChannelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
