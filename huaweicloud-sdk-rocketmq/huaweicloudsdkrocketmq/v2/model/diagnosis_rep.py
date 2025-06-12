# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnosisRep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'node_id_list': 'list[str]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'node_id_list': 'node_id_list'
    }

    def __init__(self, group_name=None, node_id_list=None):
        r"""DiagnosisRep

        The model defined in huaweicloud sdk

        :param group_name: **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type group_name: str
        :param node_id_list: **参数解释**： 节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type node_id_list: list[str]
        """
        
        

        self._group_name = None
        self._node_id_list = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if node_id_list is not None:
            self.node_id_list = node_id_list

    @property
    def group_name(self):
        r"""Gets the group_name of this DiagnosisRep.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The group_name of this DiagnosisRep.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this DiagnosisRep.

        **参数解释**： 消费组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param group_name: The group_name of this DiagnosisRep.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def node_id_list(self):
        r"""Gets the node_id_list of this DiagnosisRep.

        **参数解释**： 节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The node_id_list of this DiagnosisRep.
        :rtype: list[str]
        """
        return self._node_id_list

    @node_id_list.setter
    def node_id_list(self, node_id_list):
        r"""Sets the node_id_list of this DiagnosisRep.

        **参数解释**： 节点ID列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param node_id_list: The node_id_list of this DiagnosisRep.
        :type node_id_list: list[str]
        """
        self._node_id_list = node_id_list

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
        if not isinstance(other, DiagnosisRep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
