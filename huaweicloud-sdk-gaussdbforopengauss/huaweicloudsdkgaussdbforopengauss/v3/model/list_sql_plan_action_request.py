# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlPlanActionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'x_language': 'str',
        'body': 'QuerySqlPlanStateRequest'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, instance_id=None, node_id=None, x_language=None, body=None):
        r"""ListSqlPlanActionRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type instance_id: str
        :param node_id: **参数解释**: 节点ID，仅支持非日志类型的CN或主DN、备DN节点。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type node_id: str
        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param body: Body of the ListSqlPlanActionRequest
        :type body: :class:`huaweicloudsdkgaussdbforopengauss.v3.QuerySqlPlanStateRequest`
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_id = node_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSqlPlanActionRequest.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The instance_id of this ListSqlPlanActionRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSqlPlanActionRequest.

        **参数解释**: 实例ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListSqlPlanActionRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListSqlPlanActionRequest.

        **参数解释**: 节点ID，仅支持非日志类型的CN或主DN、备DN节点。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The node_id of this ListSqlPlanActionRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListSqlPlanActionRequest.

        **参数解释**: 节点ID，仅支持非日志类型的CN或主DN、备DN节点。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param node_id: The node_id of this ListSqlPlanActionRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSqlPlanActionRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListSqlPlanActionRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSqlPlanActionRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListSqlPlanActionRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this ListSqlPlanActionRequest.

        :return: The body of this ListSqlPlanActionRequest.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.QuerySqlPlanStateRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListSqlPlanActionRequest.

        :param body: The body of this ListSqlPlanActionRequest.
        :type body: :class:`huaweicloudsdkgaussdbforopengauss.v3.QuerySqlPlanStateRequest`
        """
        self._body = body

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
        if not isinstance(other, ListSqlPlanActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
