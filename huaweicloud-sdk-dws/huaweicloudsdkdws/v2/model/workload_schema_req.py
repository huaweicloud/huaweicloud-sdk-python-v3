# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadSchemaReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_name': 'str',
        'perm_space': 'str'
    }

    attribute_map = {
        'schema_name': 'schema_name',
        'perm_space': 'perm_space'
    }

    def __init__(self, schema_name=None, perm_space=None):
        r"""WorkloadSchemaReq

        The model defined in huaweicloud sdk

        :param schema_name: **参数解释**： 模式空间名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type schema_name: str
        :param perm_space: **参数解释**： 模式空间阈值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type perm_space: str
        """
        
        

        self._schema_name = None
        self._perm_space = None
        self.discriminator = None

        self.schema_name = schema_name
        self.perm_space = perm_space

    @property
    def schema_name(self):
        r"""Gets the schema_name of this WorkloadSchemaReq.

        **参数解释**： 模式空间名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The schema_name of this WorkloadSchemaReq.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this WorkloadSchemaReq.

        **参数解释**： 模式空间名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param schema_name: The schema_name of this WorkloadSchemaReq.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def perm_space(self):
        r"""Gets the perm_space of this WorkloadSchemaReq.

        **参数解释**： 模式空间阈值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The perm_space of this WorkloadSchemaReq.
        :rtype: str
        """
        return self._perm_space

    @perm_space.setter
    def perm_space(self, perm_space):
        r"""Sets the perm_space of this WorkloadSchemaReq.

        **参数解释**： 模式空间阈值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param perm_space: The perm_space of this WorkloadSchemaReq.
        :type perm_space: str
        """
        self._perm_space = perm_space

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
        if not isinstance(other, WorkloadSchemaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
