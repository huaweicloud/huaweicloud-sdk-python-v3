# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'replication_id': 'str',
        'node_id': 'str',
        'replication_ip': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'available_zone': 'str'
    }

    attribute_map = {
        'replication_id': 'replication_id',
        'node_id': 'node_id',
        'replication_ip': 'replication_ip',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'available_zone': 'available_zone'
    }

    def __init__(self, replication_id=None, node_id=None, replication_ip=None, group_id=None, group_name=None, available_zone=None):
        r"""ReplicationInfo

        The model defined in huaweicloud sdk

        :param replication_id: 副本ID
        :type replication_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param replication_ip: 副本IP
        :type replication_ip: str
        :param group_id: 组ID
        :type group_id: str
        :param group_name: 组名称
        :type group_name: str
        :param available_zone: 可用区
        :type available_zone: str
        """
        
        

        self._replication_id = None
        self._node_id = None
        self._replication_ip = None
        self._group_id = None
        self._group_name = None
        self._available_zone = None
        self.discriminator = None

        if replication_id is not None:
            self.replication_id = replication_id
        if node_id is not None:
            self.node_id = node_id
        if replication_ip is not None:
            self.replication_ip = replication_ip
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if available_zone is not None:
            self.available_zone = available_zone

    @property
    def replication_id(self):
        r"""Gets the replication_id of this ReplicationInfo.

        副本ID

        :return: The replication_id of this ReplicationInfo.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        r"""Sets the replication_id of this ReplicationInfo.

        副本ID

        :param replication_id: The replication_id of this ReplicationInfo.
        :type replication_id: str
        """
        self._replication_id = replication_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ReplicationInfo.

        节点ID

        :return: The node_id of this ReplicationInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ReplicationInfo.

        节点ID

        :param node_id: The node_id of this ReplicationInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def replication_ip(self):
        r"""Gets the replication_ip of this ReplicationInfo.

        副本IP

        :return: The replication_ip of this ReplicationInfo.
        :rtype: str
        """
        return self._replication_ip

    @replication_ip.setter
    def replication_ip(self, replication_ip):
        r"""Sets the replication_ip of this ReplicationInfo.

        副本IP

        :param replication_ip: The replication_ip of this ReplicationInfo.
        :type replication_ip: str
        """
        self._replication_ip = replication_ip

    @property
    def group_id(self):
        r"""Gets the group_id of this ReplicationInfo.

        组ID

        :return: The group_id of this ReplicationInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ReplicationInfo.

        组ID

        :param group_id: The group_id of this ReplicationInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ReplicationInfo.

        组名称

        :return: The group_name of this ReplicationInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ReplicationInfo.

        组名称

        :param group_name: The group_name of this ReplicationInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def available_zone(self):
        r"""Gets the available_zone of this ReplicationInfo.

        可用区

        :return: The available_zone of this ReplicationInfo.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        r"""Sets the available_zone of this ReplicationInfo.

        可用区

        :param available_zone: The available_zone of this ReplicationInfo.
        :type available_zone: str
        """
        self._available_zone = available_zone

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
        if not isinstance(other, ReplicationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
