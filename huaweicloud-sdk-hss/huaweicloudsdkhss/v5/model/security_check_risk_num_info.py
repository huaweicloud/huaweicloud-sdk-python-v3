# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckRiskNumInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_risk_num': 'int',
        'compare_status': 'str',
        'compare_num': 'int',
        'high_risk_num': 'int'
    }

    attribute_map = {
        'total_risk_num': 'total_risk_num',
        'compare_status': 'compare_status',
        'compare_num': 'compare_num',
        'high_risk_num': 'high_risk_num'
    }

    def __init__(self, total_risk_num=None, compare_status=None, compare_num=None, high_risk_num=None):
        r"""SecurityCheckRiskNumInfo

        The model defined in huaweicloud sdk

        :param total_risk_num: **参数解释**： 风险总数 **取值范围**： 不涉及 
        :type total_risk_num: int
        :param compare_status: **参数解释**： 与上一周期比较的状态 **取值范围**： - lower：降低 - increase：增加 - equals：持平 
        :type compare_status: str
        :param compare_num: **参数解释**： 与上一周期相差的数量的绝对值 **取值范围**： 不涉及 
        :type compare_num: int
        :param high_risk_num: **参数解释**： 高危风险数量 **取值范围**： 不涉及 
        :type high_risk_num: int
        """
        
        

        self._total_risk_num = None
        self._compare_status = None
        self._compare_num = None
        self._high_risk_num = None
        self.discriminator = None

        if total_risk_num is not None:
            self.total_risk_num = total_risk_num
        if compare_status is not None:
            self.compare_status = compare_status
        if compare_num is not None:
            self.compare_num = compare_num
        if high_risk_num is not None:
            self.high_risk_num = high_risk_num

    @property
    def total_risk_num(self):
        r"""Gets the total_risk_num of this SecurityCheckRiskNumInfo.

        **参数解释**： 风险总数 **取值范围**： 不涉及 

        :return: The total_risk_num of this SecurityCheckRiskNumInfo.
        :rtype: int
        """
        return self._total_risk_num

    @total_risk_num.setter
    def total_risk_num(self, total_risk_num):
        r"""Sets the total_risk_num of this SecurityCheckRiskNumInfo.

        **参数解释**： 风险总数 **取值范围**： 不涉及 

        :param total_risk_num: The total_risk_num of this SecurityCheckRiskNumInfo.
        :type total_risk_num: int
        """
        self._total_risk_num = total_risk_num

    @property
    def compare_status(self):
        r"""Gets the compare_status of this SecurityCheckRiskNumInfo.

        **参数解释**： 与上一周期比较的状态 **取值范围**： - lower：降低 - increase：增加 - equals：持平 

        :return: The compare_status of this SecurityCheckRiskNumInfo.
        :rtype: str
        """
        return self._compare_status

    @compare_status.setter
    def compare_status(self, compare_status):
        r"""Sets the compare_status of this SecurityCheckRiskNumInfo.

        **参数解释**： 与上一周期比较的状态 **取值范围**： - lower：降低 - increase：增加 - equals：持平 

        :param compare_status: The compare_status of this SecurityCheckRiskNumInfo.
        :type compare_status: str
        """
        self._compare_status = compare_status

    @property
    def compare_num(self):
        r"""Gets the compare_num of this SecurityCheckRiskNumInfo.

        **参数解释**： 与上一周期相差的数量的绝对值 **取值范围**： 不涉及 

        :return: The compare_num of this SecurityCheckRiskNumInfo.
        :rtype: int
        """
        return self._compare_num

    @compare_num.setter
    def compare_num(self, compare_num):
        r"""Sets the compare_num of this SecurityCheckRiskNumInfo.

        **参数解释**： 与上一周期相差的数量的绝对值 **取值范围**： 不涉及 

        :param compare_num: The compare_num of this SecurityCheckRiskNumInfo.
        :type compare_num: int
        """
        self._compare_num = compare_num

    @property
    def high_risk_num(self):
        r"""Gets the high_risk_num of this SecurityCheckRiskNumInfo.

        **参数解释**： 高危风险数量 **取值范围**： 不涉及 

        :return: The high_risk_num of this SecurityCheckRiskNumInfo.
        :rtype: int
        """
        return self._high_risk_num

    @high_risk_num.setter
    def high_risk_num(self, high_risk_num):
        r"""Sets the high_risk_num of this SecurityCheckRiskNumInfo.

        **参数解释**： 高危风险数量 **取值范围**： 不涉及 

        :param high_risk_num: The high_risk_num of this SecurityCheckRiskNumInfo.
        :type high_risk_num: int
        """
        self._high_risk_num = high_risk_num

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SecurityCheckRiskNumInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
