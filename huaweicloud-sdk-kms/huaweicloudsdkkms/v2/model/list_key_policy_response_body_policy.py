# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeyPolicyResponseBodyPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'validity_period': 'ListKeyPolicyResponseBodyPolicyValidityPeriod',
        'allowed_access_point': 'list[str]',
        'allowed_data_security_zone': 'list[str]'
    }

    attribute_map = {
        'version': 'version',
        'validity_period': 'validityPeriod',
        'allowed_access_point': 'allowedAccessPoint',
        'allowed_data_security_zone': 'allowed_data_security_zone'
    }

    def __init__(self, version=None, validity_period=None, allowed_access_point=None, allowed_data_security_zone=None):
        r"""ListKeyPolicyResponseBodyPolicy

        The model defined in huaweicloud sdk

        :param version: **参数解释：** 密钥策略版本 **取值范围：** 不涉及
        :type version: str
        :param validity_period: 
        :type validity_period: :class:`huaweicloudsdkkms.v2.ListKeyPolicyResponseBodyPolicyValidityPeriod`
        :param allowed_access_point: **参数解释：** 允许访问的接入点ID列表 **取值范围：** 不涉及
        :type allowed_access_point: list[str]
        :param allowed_data_security_zone: **参数解释：** 允许访问的数据安全专区ID列表 **取值范围：** 不涉及
        :type allowed_data_security_zone: list[str]
        """
        
        

        self._version = None
        self._validity_period = None
        self._allowed_access_point = None
        self._allowed_data_security_zone = None
        self.discriminator = None

        self.version = version
        if validity_period is not None:
            self.validity_period = validity_period
        if allowed_access_point is not None:
            self.allowed_access_point = allowed_access_point
        if allowed_data_security_zone is not None:
            self.allowed_data_security_zone = allowed_data_security_zone

    @property
    def version(self):
        r"""Gets the version of this ListKeyPolicyResponseBodyPolicy.

        **参数解释：** 密钥策略版本 **取值范围：** 不涉及

        :return: The version of this ListKeyPolicyResponseBodyPolicy.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListKeyPolicyResponseBodyPolicy.

        **参数解释：** 密钥策略版本 **取值范围：** 不涉及

        :param version: The version of this ListKeyPolicyResponseBodyPolicy.
        :type version: str
        """
        self._version = version

    @property
    def validity_period(self):
        r"""Gets the validity_period of this ListKeyPolicyResponseBodyPolicy.

        :return: The validity_period of this ListKeyPolicyResponseBodyPolicy.
        :rtype: :class:`huaweicloudsdkkms.v2.ListKeyPolicyResponseBodyPolicyValidityPeriod`
        """
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        r"""Sets the validity_period of this ListKeyPolicyResponseBodyPolicy.

        :param validity_period: The validity_period of this ListKeyPolicyResponseBodyPolicy.
        :type validity_period: :class:`huaweicloudsdkkms.v2.ListKeyPolicyResponseBodyPolicyValidityPeriod`
        """
        self._validity_period = validity_period

    @property
    def allowed_access_point(self):
        r"""Gets the allowed_access_point of this ListKeyPolicyResponseBodyPolicy.

        **参数解释：** 允许访问的接入点ID列表 **取值范围：** 不涉及

        :return: The allowed_access_point of this ListKeyPolicyResponseBodyPolicy.
        :rtype: list[str]
        """
        return self._allowed_access_point

    @allowed_access_point.setter
    def allowed_access_point(self, allowed_access_point):
        r"""Sets the allowed_access_point of this ListKeyPolicyResponseBodyPolicy.

        **参数解释：** 允许访问的接入点ID列表 **取值范围：** 不涉及

        :param allowed_access_point: The allowed_access_point of this ListKeyPolicyResponseBodyPolicy.
        :type allowed_access_point: list[str]
        """
        self._allowed_access_point = allowed_access_point

    @property
    def allowed_data_security_zone(self):
        r"""Gets the allowed_data_security_zone of this ListKeyPolicyResponseBodyPolicy.

        **参数解释：** 允许访问的数据安全专区ID列表 **取值范围：** 不涉及

        :return: The allowed_data_security_zone of this ListKeyPolicyResponseBodyPolicy.
        :rtype: list[str]
        """
        return self._allowed_data_security_zone

    @allowed_data_security_zone.setter
    def allowed_data_security_zone(self, allowed_data_security_zone):
        r"""Sets the allowed_data_security_zone of this ListKeyPolicyResponseBodyPolicy.

        **参数解释：** 允许访问的数据安全专区ID列表 **取值范围：** 不涉及

        :param allowed_data_security_zone: The allowed_data_security_zone of this ListKeyPolicyResponseBodyPolicy.
        :type allowed_data_security_zone: list[str]
        """
        self._allowed_data_security_zone = allowed_data_security_zone

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
        if not isinstance(other, ListKeyPolicyResponseBodyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
