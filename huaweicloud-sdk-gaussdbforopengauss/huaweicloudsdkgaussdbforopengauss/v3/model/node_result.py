# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeResult:

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
        'availability_zone': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'component_names': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'status': 'status',
        'availability_zone': 'availability_zone',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'component_names': 'component_names'
    }

    def __init__(self, id=None, name=None, role=None, status=None, availability_zone=None, private_ip=None, public_ip=None, component_names=None):
        r"""NodeResult

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param role: 节点类型，取值为“master”、“slave”，分别对应于主节点、备节点。
        :type role: str
        :param status: 节点状态。
        :type status: str
        :param availability_zone: 可用区。
        :type availability_zone: str
        :param private_ip: 节点内网IP。分布式实例类型下该参数仅针对CN节点有效，主备版实例类型下该参数对所有节点有效，且在弹性云服务器创建成功后参数值存在。
        :type private_ip: str
        :param public_ip: 绑定的外网IP。分布式实例类型下该参数仅针对CN节点有效，主备版实例类型下该参数对所有节点有效，且在弹性云服务器创建成功并绑定弹性公网IP后参数值存在。
        :type public_ip: str
        :param component_names: 节点上组件信息（例组件ID:分布式ID），多个组件信息用;隔开。
        :type component_names: str
        """
        
        

        self._id = None
        self._name = None
        self._role = None
        self._status = None
        self._availability_zone = None
        self._private_ip = None
        self._public_ip = None
        self._component_names = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.role = role
        self.status = status
        self.availability_zone = availability_zone
        self.private_ip = private_ip
        self.public_ip = public_ip
        if component_names is not None:
            self.component_names = component_names

    @property
    def id(self):
        r"""Gets the id of this NodeResult.

        节点ID。

        :return: The id of this NodeResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NodeResult.

        节点ID。

        :param id: The id of this NodeResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NodeResult.

        节点名称。

        :return: The name of this NodeResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NodeResult.

        节点名称。

        :param name: The name of this NodeResult.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this NodeResult.

        节点类型，取值为“master”、“slave”，分别对应于主节点、备节点。

        :return: The role of this NodeResult.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this NodeResult.

        节点类型，取值为“master”、“slave”，分别对应于主节点、备节点。

        :param role: The role of this NodeResult.
        :type role: str
        """
        self._role = role

    @property
    def status(self):
        r"""Gets the status of this NodeResult.

        节点状态。

        :return: The status of this NodeResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeResult.

        节点状态。

        :param status: The status of this NodeResult.
        :type status: str
        """
        self._status = status

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this NodeResult.

        可用区。

        :return: The availability_zone of this NodeResult.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this NodeResult.

        可用区。

        :param availability_zone: The availability_zone of this NodeResult.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def private_ip(self):
        r"""Gets the private_ip of this NodeResult.

        节点内网IP。分布式实例类型下该参数仅针对CN节点有效，主备版实例类型下该参数对所有节点有效，且在弹性云服务器创建成功后参数值存在。

        :return: The private_ip of this NodeResult.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this NodeResult.

        节点内网IP。分布式实例类型下该参数仅针对CN节点有效，主备版实例类型下该参数对所有节点有效，且在弹性云服务器创建成功后参数值存在。

        :param private_ip: The private_ip of this NodeResult.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this NodeResult.

        绑定的外网IP。分布式实例类型下该参数仅针对CN节点有效，主备版实例类型下该参数对所有节点有效，且在弹性云服务器创建成功并绑定弹性公网IP后参数值存在。

        :return: The public_ip of this NodeResult.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this NodeResult.

        绑定的外网IP。分布式实例类型下该参数仅针对CN节点有效，主备版实例类型下该参数对所有节点有效，且在弹性云服务器创建成功并绑定弹性公网IP后参数值存在。

        :param public_ip: The public_ip of this NodeResult.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def component_names(self):
        r"""Gets the component_names of this NodeResult.

        节点上组件信息（例组件ID:分布式ID），多个组件信息用;隔开。

        :return: The component_names of this NodeResult.
        :rtype: str
        """
        return self._component_names

    @component_names.setter
    def component_names(self, component_names):
        r"""Sets the component_names of this NodeResult.

        节点上组件信息（例组件ID:分布式ID），多个组件信息用;隔开。

        :param component_names: The component_names of this NodeResult.
        :type component_names: str
        """
        self._component_names = component_names

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
        if not isinstance(other, NodeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
