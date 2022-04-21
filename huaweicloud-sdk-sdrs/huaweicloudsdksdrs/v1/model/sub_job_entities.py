# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubJobEntities:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'replication_pair_id': 'str',
        'volume_ids': 'str',
        'server_group_id': 'str',
        'protected_instance_id': 'str',
        'native_server_id': 'str',
        'nic_id': 'str'
    }

    attribute_map = {
        'replication_pair_id': 'replication_pair_id',
        'volume_ids': 'volume_ids',
        'server_group_id': 'server_group_id',
        'protected_instance_id': 'protected_instance_id',
        'native_server_id': 'native_server_id',
        'nic_id': 'nic_id'
    }

    def __init__(self, replication_pair_id=None, volume_ids=None, server_group_id=None, protected_instance_id=None, native_server_id=None, nic_id=None):
        """SubJobEntities

        The model defined in huaweicloud sdk

        :param replication_pair_id: 复制对ID
        :type replication_pair_id: str
        :param volume_ids: 组成复制对的云硬盘ID
        :type volume_ids: str
        :param server_group_id: 保护组ID
        :type server_group_id: str
        :param protected_instance_id: 保护实例ID
        :type protected_instance_id: str
        :param native_server_id: 容灾站点服务器ID
        :type native_server_id: str
        :param nic_id: 网卡ID
        :type nic_id: str
        """
        
        

        self._replication_pair_id = None
        self._volume_ids = None
        self._server_group_id = None
        self._protected_instance_id = None
        self._native_server_id = None
        self._nic_id = None
        self.discriminator = None

        if replication_pair_id is not None:
            self.replication_pair_id = replication_pair_id
        if volume_ids is not None:
            self.volume_ids = volume_ids
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if protected_instance_id is not None:
            self.protected_instance_id = protected_instance_id
        if native_server_id is not None:
            self.native_server_id = native_server_id
        if nic_id is not None:
            self.nic_id = nic_id

    @property
    def replication_pair_id(self):
        """Gets the replication_pair_id of this SubJobEntities.

        复制对ID

        :return: The replication_pair_id of this SubJobEntities.
        :rtype: str
        """
        return self._replication_pair_id

    @replication_pair_id.setter
    def replication_pair_id(self, replication_pair_id):
        """Sets the replication_pair_id of this SubJobEntities.

        复制对ID

        :param replication_pair_id: The replication_pair_id of this SubJobEntities.
        :type replication_pair_id: str
        """
        self._replication_pair_id = replication_pair_id

    @property
    def volume_ids(self):
        """Gets the volume_ids of this SubJobEntities.

        组成复制对的云硬盘ID

        :return: The volume_ids of this SubJobEntities.
        :rtype: str
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this SubJobEntities.

        组成复制对的云硬盘ID

        :param volume_ids: The volume_ids of this SubJobEntities.
        :type volume_ids: str
        """
        self._volume_ids = volume_ids

    @property
    def server_group_id(self):
        """Gets the server_group_id of this SubJobEntities.

        保护组ID

        :return: The server_group_id of this SubJobEntities.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this SubJobEntities.

        保护组ID

        :param server_group_id: The server_group_id of this SubJobEntities.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def protected_instance_id(self):
        """Gets the protected_instance_id of this SubJobEntities.

        保护实例ID

        :return: The protected_instance_id of this SubJobEntities.
        :rtype: str
        """
        return self._protected_instance_id

    @protected_instance_id.setter
    def protected_instance_id(self, protected_instance_id):
        """Sets the protected_instance_id of this SubJobEntities.

        保护实例ID

        :param protected_instance_id: The protected_instance_id of this SubJobEntities.
        :type protected_instance_id: str
        """
        self._protected_instance_id = protected_instance_id

    @property
    def native_server_id(self):
        """Gets the native_server_id of this SubJobEntities.

        容灾站点服务器ID

        :return: The native_server_id of this SubJobEntities.
        :rtype: str
        """
        return self._native_server_id

    @native_server_id.setter
    def native_server_id(self, native_server_id):
        """Sets the native_server_id of this SubJobEntities.

        容灾站点服务器ID

        :param native_server_id: The native_server_id of this SubJobEntities.
        :type native_server_id: str
        """
        self._native_server_id = native_server_id

    @property
    def nic_id(self):
        """Gets the nic_id of this SubJobEntities.

        网卡ID

        :return: The nic_id of this SubJobEntities.
        :rtype: str
        """
        return self._nic_id

    @nic_id.setter
    def nic_id(self, nic_id):
        """Sets the nic_id of this SubJobEntities.

        网卡ID

        :param nic_id: The nic_id of this SubJobEntities.
        :type nic_id: str
        """
        self._nic_id = nic_id

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
        if not isinstance(other, SubJobEntities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
