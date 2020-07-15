# coding: utf-8

import pprint
import re

import six





class InstanceReplicationListInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'replication_role': 'str',
        'replication_ip': 'str',
        'is_replication': 'bool',
        'replication_id': 'str',
        'node_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'replication_role': 'replication_role',
        'replication_ip': 'replication_ip',
        'is_replication': 'is_replication',
        'replication_id': 'replication_id',
        'node_id': 'node_id',
        'status': 'status'
    }

    def __init__(self, replication_role=None, replication_ip=None, is_replication=None, replication_id=None, node_id=None, status=None):
        """InstanceReplicationListInfo - a model defined in huaweicloud sdk"""
        
        

        self._replication_role = None
        self._replication_ip = None
        self._is_replication = None
        self._replication_id = None
        self._node_id = None
        self._status = None
        self.discriminator = None

        if replication_role is not None:
            self.replication_role = replication_role
        if replication_ip is not None:
            self.replication_ip = replication_ip
        if is_replication is not None:
            self.is_replication = is_replication
        if replication_id is not None:
            self.replication_id = replication_id
        if node_id is not None:
            self.node_id = node_id
        if status is not None:
            self.status = status

    @property
    def replication_role(self):
        """Gets the replication_role of this InstanceReplicationListInfo.

        副本角色，取值有： - master：表示主节点。 - slave：表示从节点。 

        :return: The replication_role of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._replication_role

    @replication_role.setter
    def replication_role(self, replication_role):
        """Sets the replication_role of this InstanceReplicationListInfo.

        副本角色，取值有： - master：表示主节点。 - slave：表示从节点。 

        :param replication_role: The replication_role of this InstanceReplicationListInfo.
        :type: str
        """
        self._replication_role = replication_role

    @property
    def replication_ip(self):
        """Gets the replication_ip of this InstanceReplicationListInfo.

        副本IP。

        :return: The replication_ip of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._replication_ip

    @replication_ip.setter
    def replication_ip(self, replication_ip):
        """Sets the replication_ip of this InstanceReplicationListInfo.

        副本IP。

        :param replication_ip: The replication_ip of this InstanceReplicationListInfo.
        :type: str
        """
        self._replication_ip = replication_ip

    @property
    def is_replication(self):
        """Gets the is_replication of this InstanceReplicationListInfo.

        是否是新加副本。

        :return: The is_replication of this InstanceReplicationListInfo.
        :rtype: bool
        """
        return self._is_replication

    @is_replication.setter
    def is_replication(self, is_replication):
        """Sets the is_replication of this InstanceReplicationListInfo.

        是否是新加副本。

        :param is_replication: The is_replication of this InstanceReplicationListInfo.
        :type: bool
        """
        self._is_replication = is_replication

    @property
    def replication_id(self):
        """Gets the replication_id of this InstanceReplicationListInfo.

        副本id。

        :return: The replication_id of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        """Sets the replication_id of this InstanceReplicationListInfo.

        副本id。

        :param replication_id: The replication_id of this InstanceReplicationListInfo.
        :type: str
        """
        self._replication_id = replication_id

    @property
    def node_id(self):
        """Gets the node_id of this InstanceReplicationListInfo.

        节点id。

        :return: The node_id of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this InstanceReplicationListInfo.

        节点id。

        :param node_id: The node_id of this InstanceReplicationListInfo.
        :type: str
        """
        self._node_id = node_id

    @property
    def status(self):
        """Gets the status of this InstanceReplicationListInfo.

        副本状态。

        :return: The status of this InstanceReplicationListInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceReplicationListInfo.

        副本状态。

        :param status: The status of this InstanceReplicationListInfo.
        :type: str
        """
        self._status = status

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
        if not isinstance(other, InstanceReplicationListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
