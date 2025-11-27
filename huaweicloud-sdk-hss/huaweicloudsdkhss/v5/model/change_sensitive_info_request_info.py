# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeSensitiveInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sensitive_info_id': 'str',
        'operate_type': 'str'
    }

    attribute_map = {
        'sensitive_info_id': 'sensitive_info_id',
        'operate_type': 'operate_type'
    }

    def __init__(self, sensitive_info_id=None, operate_type=None):
        r"""ChangeSensitiveInfoRequestInfo

        The model defined in huaweicloud sdk

        :param sensitive_info_id: **参数解释**: 敏感信息编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type sensitive_info_id: str
        :param operate_type: **参数解释**: 操作敏感信息详情，处理方式 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - do_not_ignore：取消忽略  **默认取值**: do_not_ignore 
        :type operate_type: str
        """
        
        

        self._sensitive_info_id = None
        self._operate_type = None
        self.discriminator = None

        self.sensitive_info_id = sensitive_info_id
        if operate_type is not None:
            self.operate_type = operate_type

    @property
    def sensitive_info_id(self):
        r"""Gets the sensitive_info_id of this ChangeSensitiveInfoRequestInfo.

        **参数解释**: 敏感信息编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The sensitive_info_id of this ChangeSensitiveInfoRequestInfo.
        :rtype: str
        """
        return self._sensitive_info_id

    @sensitive_info_id.setter
    def sensitive_info_id(self, sensitive_info_id):
        r"""Sets the sensitive_info_id of this ChangeSensitiveInfoRequestInfo.

        **参数解释**: 敏感信息编号 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param sensitive_info_id: The sensitive_info_id of this ChangeSensitiveInfoRequestInfo.
        :type sensitive_info_id: str
        """
        self._sensitive_info_id = sensitive_info_id

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ChangeSensitiveInfoRequestInfo.

        **参数解释**: 操作敏感信息详情，处理方式 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - do_not_ignore：取消忽略  **默认取值**: do_not_ignore 

        :return: The operate_type of this ChangeSensitiveInfoRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ChangeSensitiveInfoRequestInfo.

        **参数解释**: 操作敏感信息详情，处理方式 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - do_not_ignore：取消忽略  **默认取值**: do_not_ignore 

        :param operate_type: The operate_type of this ChangeSensitiveInfoRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

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
        if not isinstance(other, ChangeSensitiveInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
