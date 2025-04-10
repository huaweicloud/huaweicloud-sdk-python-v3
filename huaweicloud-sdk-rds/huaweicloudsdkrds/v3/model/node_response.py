# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeResponse:

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
        'name': 'str',
        'role': 'str',
        'status': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'status': 'status',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, name=None, role=None, status=None, availability_zone=None):
        r"""NodeResponse

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param role: 节点类型，取值为“master”、“slave”或“readreplica”，分别对应于主节点、备节点和只读节点。
        :type role: str
        :param status: 节点状态。
        :type status: str
        :param availability_zone: 可用区。
        :type availability_zone: str
        """
        
        

        self._id = None
        self._name = None
        self._role = None
        self._status = None
        self._availability_zone = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.role = role
        self.status = status
        self.availability_zone = availability_zone

    @property
    def id(self):
        r"""Gets the id of this NodeResponse.

        节点ID。

        :return: The id of this NodeResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NodeResponse.

        节点ID。

        :param id: The id of this NodeResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NodeResponse.

        节点名称。

        :return: The name of this NodeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NodeResponse.

        节点名称。

        :param name: The name of this NodeResponse.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this NodeResponse.

        节点类型，取值为“master”、“slave”或“readreplica”，分别对应于主节点、备节点和只读节点。

        :return: The role of this NodeResponse.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this NodeResponse.

        节点类型，取值为“master”、“slave”或“readreplica”，分别对应于主节点、备节点和只读节点。

        :param role: The role of this NodeResponse.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        r"""Gets the status of this NodeResponse.

        节点状态。

        :return: The status of this NodeResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeResponse.

        节点状态。

        :param status: The status of this NodeResponse.
        :type status: str
        """
        self._status = status

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this NodeResponse.

        可用区。

        :return: The availability_zone of this NodeResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this NodeResponse.

        可用区。

        :param availability_zone: The availability_zone of this NodeResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, NodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
