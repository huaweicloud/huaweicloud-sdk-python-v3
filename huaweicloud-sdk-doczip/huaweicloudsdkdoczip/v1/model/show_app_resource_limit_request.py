# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppResourceLimitRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'tenant_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, type=None, tenant_id=None):
        r"""ShowAppResourceLimitRequest

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 查询类型。 **约束限制**： 不涉及。 **取值范围**：   1：获取当前允许创建的应用数量。 **默认取值**： 1。
        :type type: int
        :param tenant_id: **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。
        :type tenant_id: str
        """
        
        

        self._type = None
        self._tenant_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.tenant_id = tenant_id

    @property
    def type(self):
        r"""Gets the type of this ShowAppResourceLimitRequest.

        **参数解释**： 查询类型。 **约束限制**： 不涉及。 **取值范围**：   1：获取当前允许创建的应用数量。 **默认取值**： 1。

        :return: The type of this ShowAppResourceLimitRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAppResourceLimitRequest.

        **参数解释**： 查询类型。 **约束限制**： 不涉及。 **取值范围**：   1：获取当前允许创建的应用数量。 **默认取值**： 1。

        :param type: The type of this ShowAppResourceLimitRequest.
        :type type: int
        """
        self._type = type

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowAppResourceLimitRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :return: The tenant_id of this ShowAppResourceLimitRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowAppResourceLimitRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :param tenant_id: The tenant_id of this ShowAppResourceLimitRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, ShowAppResourceLimitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
