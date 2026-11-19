# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectStatusStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_type': 'str',
        'total_num': 'int',
        'unprotected_num': 'int',
        'protected_num': 'int',
        'risk_num': 'int',
        'clean_num': 'int'
    }

    attribute_map = {
        'protect_type': 'protect_type',
        'total_num': 'total_num',
        'unprotected_num': 'unprotected_num',
        'protected_num': 'protected_num',
        'risk_num': 'risk_num',
        'clean_num': 'clean_num'
    }

    def __init__(self, protect_type=None, total_num=None, unprotected_num=None, protected_num=None, risk_num=None, clean_num=None):
        r"""ProtectStatusStatistics

        The model defined in huaweicloud sdk

        :param protect_type: **参数解释**: 防护类型 **取值范围**: - host：主机 - container：容器 - application：应用 - serverless：Serverless 
        :type protect_type: str
        :param total_num: **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        :param unprotected_num: **参数解释**: 未防护数 **取值范围**: 最小值0，最大值2147483647 
        :type unprotected_num: int
        :param protected_num: **参数解释**: 已防护数，只在serverless类型返回 **取值范围**: 最小值0，最大值2147483647 
        :type protected_num: int
        :param risk_num: **参数解释**: 有风险数 **取值范围**: 最小值0，最大值2147483647 
        :type risk_num: int
        :param clean_num: **参数解释**: 无风险数 **取值范围**: 最小值0，最大值2147483647 
        :type clean_num: int
        """
        
        

        self._protect_type = None
        self._total_num = None
        self._unprotected_num = None
        self._protected_num = None
        self._risk_num = None
        self._clean_num = None
        self.discriminator = None

        if protect_type is not None:
            self.protect_type = protect_type
        if total_num is not None:
            self.total_num = total_num
        if unprotected_num is not None:
            self.unprotected_num = unprotected_num
        if protected_num is not None:
            self.protected_num = protected_num
        if risk_num is not None:
            self.risk_num = risk_num
        if clean_num is not None:
            self.clean_num = clean_num

    @property
    def protect_type(self):
        r"""Gets the protect_type of this ProtectStatusStatistics.

        **参数解释**: 防护类型 **取值范围**: - host：主机 - container：容器 - application：应用 - serverless：Serverless 

        :return: The protect_type of this ProtectStatusStatistics.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this ProtectStatusStatistics.

        **参数解释**: 防护类型 **取值范围**: - host：主机 - container：容器 - application：应用 - serverless：Serverless 

        :param protect_type: The protect_type of this ProtectStatusStatistics.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def total_num(self):
        r"""Gets the total_num of this ProtectStatusStatistics.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this ProtectStatusStatistics.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ProtectStatusStatistics.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this ProtectStatusStatistics.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def unprotected_num(self):
        r"""Gets the unprotected_num of this ProtectStatusStatistics.

        **参数解释**: 未防护数 **取值范围**: 最小值0，最大值2147483647 

        :return: The unprotected_num of this ProtectStatusStatistics.
        :rtype: int
        """
        return self._unprotected_num

    @unprotected_num.setter
    def unprotected_num(self, unprotected_num):
        r"""Sets the unprotected_num of this ProtectStatusStatistics.

        **参数解释**: 未防护数 **取值范围**: 最小值0，最大值2147483647 

        :param unprotected_num: The unprotected_num of this ProtectStatusStatistics.
        :type unprotected_num: int
        """
        self._unprotected_num = unprotected_num

    @property
    def protected_num(self):
        r"""Gets the protected_num of this ProtectStatusStatistics.

        **参数解释**: 已防护数，只在serverless类型返回 **取值范围**: 最小值0，最大值2147483647 

        :return: The protected_num of this ProtectStatusStatistics.
        :rtype: int
        """
        return self._protected_num

    @protected_num.setter
    def protected_num(self, protected_num):
        r"""Sets the protected_num of this ProtectStatusStatistics.

        **参数解释**: 已防护数，只在serverless类型返回 **取值范围**: 最小值0，最大值2147483647 

        :param protected_num: The protected_num of this ProtectStatusStatistics.
        :type protected_num: int
        """
        self._protected_num = protected_num

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ProtectStatusStatistics.

        **参数解释**: 有风险数 **取值范围**: 最小值0，最大值2147483647 

        :return: The risk_num of this ProtectStatusStatistics.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ProtectStatusStatistics.

        **参数解释**: 有风险数 **取值范围**: 最小值0，最大值2147483647 

        :param risk_num: The risk_num of this ProtectStatusStatistics.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def clean_num(self):
        r"""Gets the clean_num of this ProtectStatusStatistics.

        **参数解释**: 无风险数 **取值范围**: 最小值0，最大值2147483647 

        :return: The clean_num of this ProtectStatusStatistics.
        :rtype: int
        """
        return self._clean_num

    @clean_num.setter
    def clean_num(self, clean_num):
        r"""Sets the clean_num of this ProtectStatusStatistics.

        **参数解释**: 无风险数 **取值范围**: 最小值0，最大值2147483647 

        :param clean_num: The clean_num of this ProtectStatusStatistics.
        :type clean_num: int
        """
        self._clean_num = clean_num

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
        if not isinstance(other, ProtectStatusStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
