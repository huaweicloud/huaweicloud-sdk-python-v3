# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortStatusRequestInfo:

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
        'data_list': 'list[PortStatusRequestInfo]'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'data_list': 'data_list'
    }

    def __init__(self, operate_type=None, data_list=None):
        r"""ListPortStatusRequestInfo

        The model defined in huaweicloud sdk

        :param operate_type: **参数解释**: 端口状态，是否忽略 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore：取消忽略  **默认取值**: 不涉及 
        :type operate_type: str
        :param data_list: **参数解释**: 主机相关信息列表 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值200 **默认取值**: 不涉及 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.PortStatusRequestInfo`]
        """
        
        

        self._operate_type = None
        self._data_list = None
        self.discriminator = None

        if operate_type is not None:
            self.operate_type = operate_type
        if data_list is not None:
            self.data_list = data_list

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ListPortStatusRequestInfo.

        **参数解释**: 端口状态，是否忽略 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore：取消忽略  **默认取值**: 不涉及 

        :return: The operate_type of this ListPortStatusRequestInfo.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ListPortStatusRequestInfo.

        **参数解释**: 端口状态，是否忽略 **约束限制**: 不涉及 **取值范围**: - ignore：忽略 - not_ignore：取消忽略  **默认取值**: 不涉及 

        :param operate_type: The operate_type of this ListPortStatusRequestInfo.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def data_list(self):
        r"""Gets the data_list of this ListPortStatusRequestInfo.

        **参数解释**: 主机相关信息列表 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值200 **默认取值**: 不涉及 

        :return: The data_list of this ListPortStatusRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.PortStatusRequestInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListPortStatusRequestInfo.

        **参数解释**: 主机相关信息列表 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值200 **默认取值**: 不涉及 

        :param data_list: The data_list of this ListPortStatusRequestInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.PortStatusRequestInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListPortStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
