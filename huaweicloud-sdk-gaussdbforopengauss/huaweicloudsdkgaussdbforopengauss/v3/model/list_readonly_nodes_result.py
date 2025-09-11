# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReadonlyNodesResult:

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
        'availability_zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, id=None, name=None, status=None, availability_zone=None):
        r"""ListReadonlyNodesResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type id: str
        :param name: **参数解释**: 节点名称。 **取值范围**: 不涉及。
        :type name: str
        :param status: **参数解释**: 节点状态。 **取值范围**:  - normal：节点正常。  - abnormal：节点异常。  - creating：节点正在创建。  - createfail：节点创建失败。
        :type status: str
        :param availability_zone: **参数解释**: 节点所在的可用区。 **取值范围**: 不涉及。
        :type availability_zone: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._availability_zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def id(self):
        r"""Gets the id of this ListReadonlyNodesResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The id of this ListReadonlyNodesResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListReadonlyNodesResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param id: The id of this ListReadonlyNodesResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListReadonlyNodesResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :return: The name of this ListReadonlyNodesResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListReadonlyNodesResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :param name: The name of this ListReadonlyNodesResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListReadonlyNodesResult.

        **参数解释**: 节点状态。 **取值范围**:  - normal：节点正常。  - abnormal：节点异常。  - creating：节点正在创建。  - createfail：节点创建失败。

        :return: The status of this ListReadonlyNodesResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListReadonlyNodesResult.

        **参数解释**: 节点状态。 **取值范围**:  - normal：节点正常。  - abnormal：节点异常。  - creating：节点正在创建。  - createfail：节点创建失败。

        :param status: The status of this ListReadonlyNodesResult.
        :type status: str
        """
        self._status = status

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListReadonlyNodesResult.

        **参数解释**: 节点所在的可用区。 **取值范围**: 不涉及。

        :return: The availability_zone of this ListReadonlyNodesResult.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListReadonlyNodesResult.

        **参数解释**: 节点所在的可用区。 **取值范围**: 不涉及。

        :param availability_zone: The availability_zone of this ListReadonlyNodesResult.
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
        if not isinstance(other, ListReadonlyNodesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
