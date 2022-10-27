# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstanceVolumeOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'size': 'str',
        'group_id': 'str',
        'node_ids': 'list[str]'
    }

    attribute_map = {
        'size': 'size',
        'group_id': 'group_id',
        'node_ids': 'node_ids'
    }

    def __init__(self, size=None, group_id=None, node_ids=None):
        """ResizeInstanceVolumeOption

        The model defined in huaweicloud sdk

        :param size: 待扩容到的磁盘容量。取值为10的整数倍，并且大于当前磁盘容量。 - 对于集群实例，表示扩容到的单个shard组的磁盘容量。取值范围：10GB~2000GB。 - 对于副本集实例，表示扩容到的实例的磁盘容量，取值范围：10GB~2000GB。 - 对于单节点实例，表示扩容到的实例的磁盘容量，取值范围：10GB~1000GB。
        :type size: str
        :param group_id: 角色组ID。 - 对于集群实例，该参数为shard组ID。 - 对于副本集和单节点实例，不传该参数。
        :type group_id: str
        :param node_ids: 副本集只读节点磁盘扩容时，需要传入该参数，当前list只支持传入一个元素。
        :type node_ids: list[str]
        """
        
        

        self._size = None
        self._group_id = None
        self._node_ids = None
        self.discriminator = None

        self.size = size
        if group_id is not None:
            self.group_id = group_id
        if node_ids is not None:
            self.node_ids = node_ids

    @property
    def size(self):
        """Gets the size of this ResizeInstanceVolumeOption.

        待扩容到的磁盘容量。取值为10的整数倍，并且大于当前磁盘容量。 - 对于集群实例，表示扩容到的单个shard组的磁盘容量。取值范围：10GB~2000GB。 - 对于副本集实例，表示扩容到的实例的磁盘容量，取值范围：10GB~2000GB。 - 对于单节点实例，表示扩容到的实例的磁盘容量，取值范围：10GB~1000GB。

        :return: The size of this ResizeInstanceVolumeOption.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ResizeInstanceVolumeOption.

        待扩容到的磁盘容量。取值为10的整数倍，并且大于当前磁盘容量。 - 对于集群实例，表示扩容到的单个shard组的磁盘容量。取值范围：10GB~2000GB。 - 对于副本集实例，表示扩容到的实例的磁盘容量，取值范围：10GB~2000GB。 - 对于单节点实例，表示扩容到的实例的磁盘容量，取值范围：10GB~1000GB。

        :param size: The size of this ResizeInstanceVolumeOption.
        :type size: str
        """
        self._size = size

    @property
    def group_id(self):
        """Gets the group_id of this ResizeInstanceVolumeOption.

        角色组ID。 - 对于集群实例，该参数为shard组ID。 - 对于副本集和单节点实例，不传该参数。

        :return: The group_id of this ResizeInstanceVolumeOption.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ResizeInstanceVolumeOption.

        角色组ID。 - 对于集群实例，该参数为shard组ID。 - 对于副本集和单节点实例，不传该参数。

        :param group_id: The group_id of this ResizeInstanceVolumeOption.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def node_ids(self):
        """Gets the node_ids of this ResizeInstanceVolumeOption.

        副本集只读节点磁盘扩容时，需要传入该参数，当前list只支持传入一个元素。

        :return: The node_ids of this ResizeInstanceVolumeOption.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this ResizeInstanceVolumeOption.

        副本集只读节点磁盘扩容时，需要传入该参数，当前list只支持传入一个元素。

        :param node_ids: The node_ids of this ResizeInstanceVolumeOption.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

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
        if not isinstance(other, ResizeInstanceVolumeOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
