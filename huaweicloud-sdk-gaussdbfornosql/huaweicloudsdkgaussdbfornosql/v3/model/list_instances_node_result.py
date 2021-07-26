# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesNodeResult:


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
        'availability_zone': 'str',
        'support_reduce': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'role': 'role',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'spec_code': 'spec_code',
        'availability_zone': 'availability_zone',
        'support_reduce': 'support_reduce'
    }

    def __init__(self, id=None, name=None, status=None, role=None, private_ip=None, public_ip=None, spec_code=None, availability_zone=None, support_reduce=None):
        """ListInstancesNodeResult - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._status = None
        self._role = None
        self._private_ip = None
        self._public_ip = None
        self._spec_code = None
        self._availability_zone = None
        self._support_reduce = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.role = role
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.spec_code = spec_code
        self.availability_zone = availability_zone
        self.support_reduce = support_reduce

    @property
    def id(self):
        """Gets the id of this ListInstancesNodeResult.

        节点ID。

        :return: The id of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListInstancesNodeResult.

        节点ID。

        :param id: The id of this ListInstancesNodeResult.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListInstancesNodeResult.

        节点名称。

        :return: The name of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesNodeResult.

        节点名称。

        :param name: The name of this ListInstancesNodeResult.
        :type: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListInstancesNodeResult.

        节点状态。

        :return: The status of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesNodeResult.

        节点状态。

        :param status: The status of this ListInstancesNodeResult.
        :type: str
        """
        self._status = status

    @property
    def role(self):
        """Gets the role of this ListInstancesNodeResult.

        节点角色。 该参数仅对GaussDB(for Mongo)引擎的副本集实例有效。

        :return: The role of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ListInstancesNodeResult.

        节点角色。 该参数仅对GaussDB(for Mongo)引擎的副本集实例有效。

        :param role: The role of this ListInstancesNodeResult.
        :type: str
        """
        self._role = role

    @property
    def private_ip(self):
        """Gets the private_ip of this ListInstancesNodeResult.

        节点内网IP。在弹性云服务器创建成功后参数值存在，否则，值为\"\"。

        :return: The private_ip of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ListInstancesNodeResult.

        节点内网IP。在弹性云服务器创建成功后参数值存在，否则，值为\"\"。

        :param private_ip: The private_ip of this ListInstancesNodeResult.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this ListInstancesNodeResult.

        绑定的公网IP。该参数仅针对绑定了公网IP的节点有效。

        :return: The public_ip of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ListInstancesNodeResult.

        绑定的公网IP。该参数仅针对绑定了公网IP的节点有效。

        :param public_ip: The public_ip of this ListInstancesNodeResult.
        :type: str
        """
        self._public_ip = public_ip

    @property
    def spec_code(self):
        """Gets the spec_code of this ListInstancesNodeResult.

        资源规格编码。关于实例的规格信息，请参见查询所有实例规格信息中响应参数“flavors.spec_code”的值。

        :return: The spec_code of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ListInstancesNodeResult.

        资源规格编码。关于实例的规格信息，请参见查询所有实例规格信息中响应参数“flavors.spec_code”的值。

        :param spec_code: The spec_code of this ListInstancesNodeResult.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListInstancesNodeResult.

        可用区。

        :return: The availability_zone of this ListInstancesNodeResult.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListInstancesNodeResult.

        可用区。

        :param availability_zone: The availability_zone of this ListInstancesNodeResult.
        :type: str
        """
        self._availability_zone = availability_zone

    @property
    def support_reduce(self):
        """Gets the support_reduce of this ListInstancesNodeResult.

        是否支持节点缩容。 - true，表示该节点支持节点缩容。 - false，表示该节点不支持节点缩容。

        :return: The support_reduce of this ListInstancesNodeResult.
        :rtype: bool
        """
        return self._support_reduce

    @support_reduce.setter
    def support_reduce(self, support_reduce):
        """Sets the support_reduce of this ListInstancesNodeResult.

        是否支持节点缩容。 - true，表示该节点支持节点缩容。 - false，表示该节点不支持节点缩容。

        :param support_reduce: The support_reduce of this ListInstancesNodeResult.
        :type: bool
        """
        self._support_reduce = support_reduce

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListInstancesNodeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
