# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Components:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'role': 'str',
        'status': 'str',
        'distributed_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'role': 'role',
        'status': 'status',
        'distributed_id': 'distributed_id'
    }

    def __init__(self, id=None, role=None, status=None, distributed_id=None):
        """Components

        The model defined in huaweicloud sdk

        :param id: 组件id，当组件类型为DN，组件id为6001，则对应的值为dn_6001。
        :type id: str
        :param role: 节点类型，取值为“master”、“slave”，分别对应于主节点、备节点。
        :type role: str
        :param status: 组件状态。 Primary：该组件为主。 Normal：该组件状态正常。 Down：该组件处于宕机状态。 Standby：该组件为备。 StateFollower：该ETCD为备。 StateLeader：该ETCD为主。 StateCandidate：该ETCD为仲裁。
        :type status: str
        :param distributed_id: 分组id，只有dn组件有分组id，用于区分是否是同一个分片下的组件。其他组件为空字符串。
        :type distributed_id: str
        """
        
        

        self._id = None
        self._role = None
        self._status = None
        self._distributed_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if role is not None:
            self.role = role
        if status is not None:
            self.status = status
        if distributed_id is not None:
            self.distributed_id = distributed_id

    @property
    def id(self):
        """Gets the id of this Components.

        组件id，当组件类型为DN，组件id为6001，则对应的值为dn_6001。

        :return: The id of this Components.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Components.

        组件id，当组件类型为DN，组件id为6001，则对应的值为dn_6001。

        :param id: The id of this Components.
        :type id: str
        """
        self._id = id

    @property
    def role(self):
        """Gets the role of this Components.

        节点类型，取值为“master”、“slave”，分别对应于主节点、备节点。

        :return: The role of this Components.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Components.

        节点类型，取值为“master”、“slave”，分别对应于主节点、备节点。

        :param role: The role of this Components.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        """Gets the status of this Components.

        组件状态。 Primary：该组件为主。 Normal：该组件状态正常。 Down：该组件处于宕机状态。 Standby：该组件为备。 StateFollower：该ETCD为备。 StateLeader：该ETCD为主。 StateCandidate：该ETCD为仲裁。

        :return: The status of this Components.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Components.

        组件状态。 Primary：该组件为主。 Normal：该组件状态正常。 Down：该组件处于宕机状态。 Standby：该组件为备。 StateFollower：该ETCD为备。 StateLeader：该ETCD为主。 StateCandidate：该ETCD为仲裁。

        :param status: The status of this Components.
        :type status: str
        """
        self._status = status

    @property
    def distributed_id(self):
        """Gets the distributed_id of this Components.

        分组id，只有dn组件有分组id，用于区分是否是同一个分片下的组件。其他组件为空字符串。

        :return: The distributed_id of this Components.
        :rtype: str
        """
        return self._distributed_id

    @distributed_id.setter
    def distributed_id(self, distributed_id):
        """Sets the distributed_id of this Components.

        分组id，只有dn组件有分组id，用于区分是否是同一个分片下的组件。其他组件为空字符串。

        :param distributed_id: The distributed_id of this Components.
        :type distributed_id: str
        """
        self._distributed_id = distributed_id

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
        if not isinstance(other, Components):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
