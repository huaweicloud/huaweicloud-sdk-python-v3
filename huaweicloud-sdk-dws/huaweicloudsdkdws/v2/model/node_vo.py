# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeVo:

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
        'inst_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'inst_type': 'inst_type'
    }

    def __init__(self, id=None, name=None, status=None, inst_type=None):
        r"""NodeVo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 节点实例ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 节点实例名称。 **取值范围**： 不涉及。
        :type name: str
        :param status: **参数解释**： 节点状态。 **取值范围**： - ACTIVE：正常。 - FAILED：不可用。
        :type status: str
        :param inst_type: **参数解释**： 节点类型。 **取值范围**： - cn：协调节点。 - dn：数据节点。
        :type inst_type: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._inst_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if inst_type is not None:
            self.inst_type = inst_type

    @property
    def id(self):
        r"""Gets the id of this NodeVo.

        **参数解释**： 节点实例ID。 **取值范围**： 不涉及。

        :return: The id of this NodeVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NodeVo.

        **参数解释**： 节点实例ID。 **取值范围**： 不涉及。

        :param id: The id of this NodeVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NodeVo.

        **参数解释**： 节点实例名称。 **取值范围**： 不涉及。

        :return: The name of this NodeVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NodeVo.

        **参数解释**： 节点实例名称。 **取值范围**： 不涉及。

        :param name: The name of this NodeVo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this NodeVo.

        **参数解释**： 节点状态。 **取值范围**： - ACTIVE：正常。 - FAILED：不可用。

        :return: The status of this NodeVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NodeVo.

        **参数解释**： 节点状态。 **取值范围**： - ACTIVE：正常。 - FAILED：不可用。

        :param status: The status of this NodeVo.
        :type status: str
        """
        self._status = status

    @property
    def inst_type(self):
        r"""Gets the inst_type of this NodeVo.

        **参数解释**： 节点类型。 **取值范围**： - cn：协调节点。 - dn：数据节点。

        :return: The inst_type of this NodeVo.
        :rtype: str
        """
        return self._inst_type

    @inst_type.setter
    def inst_type(self, inst_type):
        r"""Sets the inst_type of this NodeVo.

        **参数解释**： 节点类型。 **取值范围**： - cn：协调节点。 - dn：数据节点。

        :param inst_type: The inst_type of this NodeVo.
        :type inst_type: str
        """
        self._inst_type = inst_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
