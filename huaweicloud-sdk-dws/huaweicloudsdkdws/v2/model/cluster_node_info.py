# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterNodeInfo:

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
        'sub_status': 'str',
        'spec': 'str',
        'inst_create_type': 'str',
        'alias_name': 'str',
        'az_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'sub_status': 'sub_status',
        'spec': 'spec',
        'inst_create_type': 'inst_create_type',
        'alias_name': 'alias_name',
        'az_code': 'az_code'
    }

    def __init__(self, id=None, name=None, status=None, sub_status=None, spec=None, inst_create_type=None, alias_name=None, az_code=None):
        r"""ClusterNodeInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 节点ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 节点名称。 **取值范围**： 不涉及。
        :type name: str
        :param status: **参数解释**： 节点状态。 **取值范围**： 不涉及。
        :type status: str
        :param sub_status: **参数解释**： 节点子状态。 **取值范围**： 不涉及。
        :type sub_status: str
        :param spec: **参数解释**： 节点规格。 **取值范围**： 不涉及。
        :type spec: str
        :param inst_create_type: **参数解释**： 实例创建类型。 **取值范围**： - INST：已使用 - NODE：空闲节点
        :type inst_create_type: str
        :param alias_name: **参数解释**： 节点别名。 **取值范围**： 不涉及。
        :type alias_name: str
        :param az_code: **参数解释**： 可用区编码。 **取值范围**： 不涉及。
        :type az_code: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._sub_status = None
        self._spec = None
        self._inst_create_type = None
        self._alias_name = None
        self._az_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if sub_status is not None:
            self.sub_status = sub_status
        if spec is not None:
            self.spec = spec
        if inst_create_type is not None:
            self.inst_create_type = inst_create_type
        if alias_name is not None:
            self.alias_name = alias_name
        if az_code is not None:
            self.az_code = az_code

    @property
    def id(self):
        r"""Gets the id of this ClusterNodeInfo.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :return: The id of this ClusterNodeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ClusterNodeInfo.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。

        :param id: The id of this ClusterNodeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ClusterNodeInfo.

        **参数解释**： 节点名称。 **取值范围**： 不涉及。

        :return: The name of this ClusterNodeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClusterNodeInfo.

        **参数解释**： 节点名称。 **取值范围**： 不涉及。

        :param name: The name of this ClusterNodeInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ClusterNodeInfo.

        **参数解释**： 节点状态。 **取值范围**： 不涉及。

        :return: The status of this ClusterNodeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClusterNodeInfo.

        **参数解释**： 节点状态。 **取值范围**： 不涉及。

        :param status: The status of this ClusterNodeInfo.
        :type status: str
        """
        self._status = status

    @property
    def sub_status(self):
        r"""Gets the sub_status of this ClusterNodeInfo.

        **参数解释**： 节点子状态。 **取值范围**： 不涉及。

        :return: The sub_status of this ClusterNodeInfo.
        :rtype: str
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        r"""Sets the sub_status of this ClusterNodeInfo.

        **参数解释**： 节点子状态。 **取值范围**： 不涉及。

        :param sub_status: The sub_status of this ClusterNodeInfo.
        :type sub_status: str
        """
        self._sub_status = sub_status

    @property
    def spec(self):
        r"""Gets the spec of this ClusterNodeInfo.

        **参数解释**： 节点规格。 **取值范围**： 不涉及。

        :return: The spec of this ClusterNodeInfo.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ClusterNodeInfo.

        **参数解释**： 节点规格。 **取值范围**： 不涉及。

        :param spec: The spec of this ClusterNodeInfo.
        :type spec: str
        """
        self._spec = spec

    @property
    def inst_create_type(self):
        r"""Gets the inst_create_type of this ClusterNodeInfo.

        **参数解释**： 实例创建类型。 **取值范围**： - INST：已使用 - NODE：空闲节点

        :return: The inst_create_type of this ClusterNodeInfo.
        :rtype: str
        """
        return self._inst_create_type

    @inst_create_type.setter
    def inst_create_type(self, inst_create_type):
        r"""Sets the inst_create_type of this ClusterNodeInfo.

        **参数解释**： 实例创建类型。 **取值范围**： - INST：已使用 - NODE：空闲节点

        :param inst_create_type: The inst_create_type of this ClusterNodeInfo.
        :type inst_create_type: str
        """
        self._inst_create_type = inst_create_type

    @property
    def alias_name(self):
        r"""Gets the alias_name of this ClusterNodeInfo.

        **参数解释**： 节点别名。 **取值范围**： 不涉及。

        :return: The alias_name of this ClusterNodeInfo.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this ClusterNodeInfo.

        **参数解释**： 节点别名。 **取值范围**： 不涉及。

        :param alias_name: The alias_name of this ClusterNodeInfo.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def az_code(self):
        r"""Gets the az_code of this ClusterNodeInfo.

        **参数解释**： 可用区编码。 **取值范围**： 不涉及。

        :return: The az_code of this ClusterNodeInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this ClusterNodeInfo.

        **参数解释**： 可用区编码。 **取值范围**： 不涉及。

        :param az_code: The az_code of this ClusterNodeInfo.
        :type az_code: str
        """
        self._az_code = az_code

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
        if not isinstance(other, ClusterNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
