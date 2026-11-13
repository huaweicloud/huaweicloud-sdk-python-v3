# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteApplicationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, application_id=None, tenant_id=None):
        r"""DeleteApplicationRequest

        The model defined in huaweicloud sdk

        :param application_id: **参数解释**： 应用ID。 **约束限制**： 不涉及。 **取值范围**： [1-256]个字符。 **默认取值**： 不涉及。
        :type application_id: str
        :param tenant_id: **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。
        :type tenant_id: str
        """
        
        

        self._application_id = None
        self._tenant_id = None
        self.discriminator = None

        self.application_id = application_id
        self.tenant_id = tenant_id

    @property
    def application_id(self):
        r"""Gets the application_id of this DeleteApplicationRequest.

        **参数解释**： 应用ID。 **约束限制**： 不涉及。 **取值范围**： [1-256]个字符。 **默认取值**： 不涉及。

        :return: The application_id of this DeleteApplicationRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this DeleteApplicationRequest.

        **参数解释**： 应用ID。 **约束限制**： 不涉及。 **取值范围**： [1-256]个字符。 **默认取值**： 不涉及。

        :param application_id: The application_id of this DeleteApplicationRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this DeleteApplicationRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :return: The tenant_id of this DeleteApplicationRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this DeleteApplicationRequest.

        **参数解释**： 租户ID。 **约束限制**： 不涉及。 **取值范围**： [1-50]个字符。 **默认取值**： 不涉及。

        :param tenant_id: The tenant_id of this DeleteApplicationRequest.
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
        if not isinstance(other, DeleteApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
