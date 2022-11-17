# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'entity_id': 'str',
        'entity_name': 'str',
        'group_type': 'str',
        'used': 'str',
        'size': 'str'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'entity_name': 'entity_name',
        'group_type': 'group_type',
        'used': 'used',
        'size': 'size'
    }

    def __init__(self, entity_id=None, entity_name=None, group_type=None, used=None, size=None):
        """DiskVolumes

        The model defined in huaweicloud sdk

        :param entity_id: 实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 当变更的实例类型是集群，如果变更的是shard组或者config组的参数模板，传值为组ID。如果变更的是mongos节点的参数模板，传值为节点ID。 - 当变更的实例类型是副本集或单节点，传值为实例ID。
        :type entity_id: str
        :param entity_name: 实例名称或组名称或节点名称
        :type entity_name: str
        :param group_type: group_type。取值范围： - mongos，表示集群mongos节点类型。 - shard，表示集群shard节点类型。 - config，表示集群config节点类型。 - replica，表示副本集类型。 - single，表示单节点类型。 - readonly，表示只读节点类型。
        :type group_type: str
        :param used: 使用量，保留两位小数，单位(GB)
        :type used: str
        :param size: 总大小，单位(GB)
        :type size: str
        """
        
        

        self._entity_id = None
        self._entity_name = None
        self._group_type = None
        self._used = None
        self._size = None
        self.discriminator = None

        self.entity_id = entity_id
        self.entity_name = entity_name
        self.group_type = group_type
        self.used = used
        self.size = size

    @property
    def entity_id(self):
        """Gets the entity_id of this DiskVolumes.

        实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 当变更的实例类型是集群，如果变更的是shard组或者config组的参数模板，传值为组ID。如果变更的是mongos节点的参数模板，传值为节点ID。 - 当变更的实例类型是副本集或单节点，传值为实例ID。

        :return: The entity_id of this DiskVolumes.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this DiskVolumes.

        实例ID或组ID或节点ID。可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。 - 当变更的实例类型是集群，如果变更的是shard组或者config组的参数模板，传值为组ID。如果变更的是mongos节点的参数模板，传值为节点ID。 - 当变更的实例类型是副本集或单节点，传值为实例ID。

        :param entity_id: The entity_id of this DiskVolumes.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def entity_name(self):
        """Gets the entity_name of this DiskVolumes.

        实例名称或组名称或节点名称

        :return: The entity_name of this DiskVolumes.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this DiskVolumes.

        实例名称或组名称或节点名称

        :param entity_name: The entity_name of this DiskVolumes.
        :type entity_name: str
        """
        self._entity_name = entity_name

    @property
    def group_type(self):
        """Gets the group_type of this DiskVolumes.

        group_type。取值范围： - mongos，表示集群mongos节点类型。 - shard，表示集群shard节点类型。 - config，表示集群config节点类型。 - replica，表示副本集类型。 - single，表示单节点类型。 - readonly，表示只读节点类型。

        :return: The group_type of this DiskVolumes.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this DiskVolumes.

        group_type。取值范围： - mongos，表示集群mongos节点类型。 - shard，表示集群shard节点类型。 - config，表示集群config节点类型。 - replica，表示副本集类型。 - single，表示单节点类型。 - readonly，表示只读节点类型。

        :param group_type: The group_type of this DiskVolumes.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def used(self):
        """Gets the used of this DiskVolumes.

        使用量，保留两位小数，单位(GB)

        :return: The used of this DiskVolumes.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this DiskVolumes.

        使用量，保留两位小数，单位(GB)

        :param used: The used of this DiskVolumes.
        :type used: str
        """
        self._used = used

    @property
    def size(self):
        """Gets the size of this DiskVolumes.

        总大小，单位(GB)

        :return: The size of this DiskVolumes.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DiskVolumes.

        总大小，单位(GB)

        :param size: The size of this DiskVolumes.
        :type size: str
        """
        self._size = size

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
        if not isinstance(other, DiskVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
