# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateHostRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_type': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, operate_type=None, host_id_list=None):
        r"""OperateHostRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: **参数解释**： 操作类型 **约束限制**： 不涉及 **取值范围**： - ignore：忽略 - un_ignore：取消忽略  **默认取值**： 不涉及 
        :type operate_type: str
        :param host_id_list: **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type host_id_list: list[str]
        """
        
        

        self._operate_type = None
        self._host_id_list = None
        self.discriminator = None

        self.operate_type = operate_type
        self.host_id_list = host_id_list

    @property
    def operate_type(self):
        r"""Gets the operate_type of this OperateHostRequestInfo.

        **参数解释**： 操作类型 **约束限制**： 不涉及 **取值范围**： - ignore：忽略 - un_ignore：取消忽略  **默认取值**： 不涉及 

        :return: The operate_type of this OperateHostRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this OperateHostRequestInfo.

        **参数解释**： 操作类型 **约束限制**： 不涉及 **取值范围**： - ignore：忽略 - un_ignore：取消忽略  **默认取值**： 不涉及 

        :param operate_type: The operate_type of this OperateHostRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this OperateHostRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The host_id_list of this OperateHostRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this OperateHostRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param host_id_list: The host_id_list of this OperateHostRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, OperateHostRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
