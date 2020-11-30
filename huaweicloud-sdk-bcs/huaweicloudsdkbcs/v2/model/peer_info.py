# coding: utf-8

import pprint
import re

import six





class PeerInfo:


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
        'node_cnt': 'int',
        'status': 'str',
        'status_detail': 'str',
        'pvc_name': 'str',
        'address': 'list[PeerAddress]'
    }

    attribute_map = {
        'name': 'name',
        'node_cnt': 'node_cnt',
        'status': 'status',
        'status_detail': 'status_detail',
        'pvc_name': 'pvc_name',
        'address': 'address'
    }

    def __init__(self, name=None, node_cnt=None, status=None, status_detail=None, pvc_name=None, address=None):
        """PeerInfo - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._node_cnt = None
        self._status = None
        self._status_detail = None
        self._pvc_name = None
        self._address = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if node_cnt is not None:
            self.node_cnt = node_cnt
        if status is not None:
            self.status = status
        if status_detail is not None:
            self.status_detail = status_detail
        if pvc_name is not None:
            self.pvc_name = pvc_name
        if address is not None:
            self.address = address

    @property
    def name(self):
        """Gets the name of this PeerInfo.

        组织名称

        :return: The name of this PeerInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PeerInfo.

        组织名称

        :param name: The name of this PeerInfo.
        :type: str
        """
        self._name = name

    @property
    def node_cnt(self):
        """Gets the node_cnt of this PeerInfo.

        节点数量

        :return: The node_cnt of this PeerInfo.
        :rtype: int
        """
        return self._node_cnt

    @node_cnt.setter
    def node_cnt(self, node_cnt):
        """Sets the node_cnt of this PeerInfo.

        节点数量

        :param node_cnt: The node_cnt of this PeerInfo.
        :type: int
        """
        self._node_cnt = node_cnt

    @property
    def status(self):
        """Gets the status of this PeerInfo.

        节点状态，分为创建中（IsCreating），升级中（IsUpgrading），扩缩容中（Adding/IsScaling），删除中（Isdeleting），正常（Normal），异常（AbNormal），未知（其余值）

        :return: The status of this PeerInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PeerInfo.

        节点状态，分为创建中（IsCreating），升级中（IsUpgrading），扩缩容中（Adding/IsScaling），删除中（Isdeleting），正常（Normal），异常（AbNormal），未知（其余值）

        :param status: The status of this PeerInfo.
        :type: str
        """
        self._status = status

    @property
    def status_detail(self):
        """Gets the status_detail of this PeerInfo.

        节点状态，形式如：1/1，分母是该组织下节点总数，分子是正常节点个数

        :return: The status_detail of this PeerInfo.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this PeerInfo.

        节点状态，形式如：1/1，分母是该组织下节点总数，分子是正常节点个数

        :param status_detail: The status_detail of this PeerInfo.
        :type: str
        """
        self._status_detail = status_detail

    @property
    def pvc_name(self):
        """Gets the pvc_name of this PeerInfo.

        节点对应pvc名称

        :return: The pvc_name of this PeerInfo.
        :rtype: str
        """
        return self._pvc_name

    @pvc_name.setter
    def pvc_name(self, pvc_name):
        """Sets the pvc_name of this PeerInfo.

        节点对应pvc名称

        :param pvc_name: The pvc_name of this PeerInfo.
        :type: str
        """
        self._pvc_name = pvc_name

    @property
    def address(self):
        """Gets the address of this PeerInfo.

        Peer节点域名/IP地址

        :return: The address of this PeerInfo.
        :rtype: list[PeerAddress]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PeerInfo.

        Peer节点域名/IP地址

        :param address: The address of this PeerInfo.
        :type: list[PeerAddress]
        """
        self._address = address

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PeerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
