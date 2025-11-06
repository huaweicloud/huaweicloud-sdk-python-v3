# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildCommandRiskDetailListResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_num': 'int',
        'risk_list': 'list[BuildCommandRiskDetailResponseInfo]'
    }

    attribute_map = {
        'risk_num': 'risk_num',
        'risk_list': 'risk_list'
    }

    def __init__(self, risk_num=None, risk_list=None):
        r"""BuildCommandRiskDetailListResponseInfo

        The model defined in huaweicloud sdk

        :param risk_num: **参数解释** 镜像构建指令风险详情总数 **取值范围** 取值0-2147483547
        :type risk_num: int
        :param risk_list: **参数解释**: 镜像构建指令风险详情列表 **取值范围**: 取值0-2147483647 
        :type risk_list: list[:class:`huaweicloudsdkhss.v5.BuildCommandRiskDetailResponseInfo`]
        """
        
        

        self._risk_num = None
        self._risk_list = None
        self.discriminator = None

        if risk_num is not None:
            self.risk_num = risk_num
        if risk_list is not None:
            self.risk_list = risk_list

    @property
    def risk_num(self):
        r"""Gets the risk_num of this BuildCommandRiskDetailListResponseInfo.

        **参数解释** 镜像构建指令风险详情总数 **取值范围** 取值0-2147483547

        :return: The risk_num of this BuildCommandRiskDetailListResponseInfo.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this BuildCommandRiskDetailListResponseInfo.

        **参数解释** 镜像构建指令风险详情总数 **取值范围** 取值0-2147483547

        :param risk_num: The risk_num of this BuildCommandRiskDetailListResponseInfo.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def risk_list(self):
        r"""Gets the risk_list of this BuildCommandRiskDetailListResponseInfo.

        **参数解释**: 镜像构建指令风险详情列表 **取值范围**: 取值0-2147483647 

        :return: The risk_list of this BuildCommandRiskDetailListResponseInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.BuildCommandRiskDetailResponseInfo`]
        """
        return self._risk_list

    @risk_list.setter
    def risk_list(self, risk_list):
        r"""Sets the risk_list of this BuildCommandRiskDetailListResponseInfo.

        **参数解释**: 镜像构建指令风险详情列表 **取值范围**: 取值0-2147483647 

        :param risk_list: The risk_list of this BuildCommandRiskDetailListResponseInfo.
        :type risk_list: list[:class:`huaweicloudsdkhss.v5.BuildCommandRiskDetailResponseInfo`]
        """
        self._risk_list = risk_list

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
        if not isinstance(other, BuildCommandRiskDetailListResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
