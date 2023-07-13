# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeItem:

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
        'status': 'str',
        'role': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'spec_code': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'role': 'role',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'spec_code': 'spec_code',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, name=None, status=None, role=None, private_ip=None, public_ip=None, spec_code=None, availability_zone=None):
        """NodeItem

        The model defined in huaweicloud sdk

        :param id: 节点ID。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param status: 节点状态。
        :type status: str
        :param role: 节点角色。 取值： - master，mongos节点返回该值。 - Primary，shard组主节点、config组主节点、副本集主节点、单节点返回该值。 - Secondary，shard组备节点、config组备节点、副本集备节点返回该值。 - Hidden，shard组隐藏节点、config组隐藏节点、副本集隐藏节点返回该值。 - unknown，节点异常时返回该值。
        :type role: str
        :param private_ip: 节点内网IP。该参数仅针对集群实例的mongos节点、副本集实例、以及单节点实例有效，且在弹性云服务器创建成功后参数值存在，否则，值为\&quot;\&quot;。
        :type private_ip: str
        :param public_ip: 绑定的外网IP。该参数值为\&quot;\&quot;。该参数仅针对集群实例的mongos节点、副本集实例的主节点和备节点、以及单节点实例有效。
        :type public_ip: str
        :param spec_code: 资源规格编码。
        :type spec_code: str
        :param availability_zone: 可用区。
        :type availability_zone: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._role = None
        self._private_ip = None
        self._public_ip = None
        self._spec_code = None
        self._availability_zone = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.role = role
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.spec_code = spec_code
        self.availability_zone = availability_zone

    @property
    def id(self):
        """Gets the id of this NodeItem.

        节点ID。

        :return: The id of this NodeItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeItem.

        节点ID。

        :param id: The id of this NodeItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this NodeItem.

        节点名称。

        :return: The name of this NodeItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeItem.

        节点名称。

        :param name: The name of this NodeItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this NodeItem.

        节点状态。

        :return: The status of this NodeItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeItem.

        节点状态。

        :param status: The status of this NodeItem.
        :type status: str
        """
        self._status = status

    @property
    def role(self):
        """Gets the role of this NodeItem.

        节点角色。 取值： - master，mongos节点返回该值。 - Primary，shard组主节点、config组主节点、副本集主节点、单节点返回该值。 - Secondary，shard组备节点、config组备节点、副本集备节点返回该值。 - Hidden，shard组隐藏节点、config组隐藏节点、副本集隐藏节点返回该值。 - unknown，节点异常时返回该值。

        :return: The role of this NodeItem.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this NodeItem.

        节点角色。 取值： - master，mongos节点返回该值。 - Primary，shard组主节点、config组主节点、副本集主节点、单节点返回该值。 - Secondary，shard组备节点、config组备节点、副本集备节点返回该值。 - Hidden，shard组隐藏节点、config组隐藏节点、副本集隐藏节点返回该值。 - unknown，节点异常时返回该值。

        :param role: The role of this NodeItem.
        :type role: str
        """
        self._role = role

    @property
    def private_ip(self):
        """Gets the private_ip of this NodeItem.

        节点内网IP。该参数仅针对集群实例的mongos节点、副本集实例、以及单节点实例有效，且在弹性云服务器创建成功后参数值存在，否则，值为\"\"。

        :return: The private_ip of this NodeItem.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this NodeItem.

        节点内网IP。该参数仅针对集群实例的mongos节点、副本集实例、以及单节点实例有效，且在弹性云服务器创建成功后参数值存在，否则，值为\"\"。

        :param private_ip: The private_ip of this NodeItem.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this NodeItem.

        绑定的外网IP。该参数值为\"\"。该参数仅针对集群实例的mongos节点、副本集实例的主节点和备节点、以及单节点实例有效。

        :return: The public_ip of this NodeItem.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this NodeItem.

        绑定的外网IP。该参数值为\"\"。该参数仅针对集群实例的mongos节点、副本集实例的主节点和备节点、以及单节点实例有效。

        :param public_ip: The public_ip of this NodeItem.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def spec_code(self):
        """Gets the spec_code of this NodeItem.

        资源规格编码。

        :return: The spec_code of this NodeItem.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this NodeItem.

        资源规格编码。

        :param spec_code: The spec_code of this NodeItem.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def availability_zone(self):
        """Gets the availability_zone of this NodeItem.

        可用区。

        :return: The availability_zone of this NodeItem.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this NodeItem.

        可用区。

        :param availability_zone: The availability_zone of this NodeItem.
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
        if not isinstance(other, NodeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
