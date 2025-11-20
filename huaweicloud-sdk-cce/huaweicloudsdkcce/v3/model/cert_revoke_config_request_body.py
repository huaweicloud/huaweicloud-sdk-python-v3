# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CertRevokeConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'agency_id': 'str'
    }

    attribute_map = {
        'user_id': 'userId',
        'agency_id': 'agencyId'
    }

    def __init__(self, user_id=None, agency_id=None):
        r"""CertRevokeConfigRequestBody

        The model defined in huaweicloud sdk

        :param user_id: **参数解释**： 用户ID，获取方式参见本接口的接口约束 **约束限制**： 与agencyId互斥，二选一填写 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type user_id: str
        :param agency_id: **参数解释**： 用户ID，获取方式参见[如何获取用户ID](cce_02_0249.xml#section1) **约束限制**： 与agencyId互斥，二选一填写 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type agency_id: str
        """
        
        

        self._user_id = None
        self._agency_id = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if agency_id is not None:
            self.agency_id = agency_id

    @property
    def user_id(self):
        r"""Gets the user_id of this CertRevokeConfigRequestBody.

        **参数解释**： 用户ID，获取方式参见本接口的接口约束 **约束限制**： 与agencyId互斥，二选一填写 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The user_id of this CertRevokeConfigRequestBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CertRevokeConfigRequestBody.

        **参数解释**： 用户ID，获取方式参见本接口的接口约束 **约束限制**： 与agencyId互斥，二选一填写 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param user_id: The user_id of this CertRevokeConfigRequestBody.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def agency_id(self):
        r"""Gets the agency_id of this CertRevokeConfigRequestBody.

        **参数解释**： 用户ID，获取方式参见[如何获取用户ID](cce_02_0249.xml#section1) **约束限制**： 与agencyId互斥，二选一填写 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The agency_id of this CertRevokeConfigRequestBody.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        r"""Sets the agency_id of this CertRevokeConfigRequestBody.

        **参数解释**： 用户ID，获取方式参见[如何获取用户ID](cce_02_0249.xml#section1) **约束限制**： 与agencyId互斥，二选一填写 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param agency_id: The agency_id of this CertRevokeConfigRequestBody.
        :type agency_id: str
        """
        self._agency_id = agency_id

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
        if not isinstance(other, CertRevokeConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
