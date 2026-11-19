# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrendRiskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline_risk_num': 'int',
        'asset_risk_num': 'int',
        'alarm_risk_num': 'int',
        'vul_risk_num': 'int',
        'update_time': 'int',
        'time': 'int',
        'score': 'float'
    }

    attribute_map = {
        'baseline_risk_num': 'baseline_risk_num',
        'asset_risk_num': 'asset_risk_num',
        'alarm_risk_num': 'alarm_risk_num',
        'vul_risk_num': 'vul_risk_num',
        'update_time': 'update_time',
        'time': 'time',
        'score': 'score'
    }

    def __init__(self, baseline_risk_num=None, asset_risk_num=None, alarm_risk_num=None, vul_risk_num=None, update_time=None, time=None, score=None):
        r"""TrendRiskInfo

        The model defined in huaweicloud sdk

        :param baseline_risk_num: **参数解释**: 基线风险数量 **取值范围**: 最小值0，最大值2147483647 
        :type baseline_risk_num: int
        :param asset_risk_num: **参数解释**: 资产风险数量 **取值范围**: 最小值0，最大值2147483647 
        :type asset_risk_num: int
        :param alarm_risk_num: **参数解释**: 告警数量 **取值范围**: 最小值0，最大值2147483647 
        :type alarm_risk_num: int
        :param vul_risk_num: **参数解释**: 漏洞数 **取值范围**: 最小值0，最大值2147483647 
        :type vul_risk_num: int
        :param update_time: **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type update_time: int
        :param time: **参数解释**: 时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 
        :type time: int
        :param score: **参数解释**: 分数 **取值范围**: 最小值0，最大值100 
        :type score: float
        """
        
        

        self._baseline_risk_num = None
        self._asset_risk_num = None
        self._alarm_risk_num = None
        self._vul_risk_num = None
        self._update_time = None
        self._time = None
        self._score = None
        self.discriminator = None

        if baseline_risk_num is not None:
            self.baseline_risk_num = baseline_risk_num
        if asset_risk_num is not None:
            self.asset_risk_num = asset_risk_num
        if alarm_risk_num is not None:
            self.alarm_risk_num = alarm_risk_num
        if vul_risk_num is not None:
            self.vul_risk_num = vul_risk_num
        if update_time is not None:
            self.update_time = update_time
        if time is not None:
            self.time = time
        if score is not None:
            self.score = score

    @property
    def baseline_risk_num(self):
        r"""Gets the baseline_risk_num of this TrendRiskInfo.

        **参数解释**: 基线风险数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The baseline_risk_num of this TrendRiskInfo.
        :rtype: int
        """
        return self._baseline_risk_num

    @baseline_risk_num.setter
    def baseline_risk_num(self, baseline_risk_num):
        r"""Sets the baseline_risk_num of this TrendRiskInfo.

        **参数解释**: 基线风险数量 **取值范围**: 最小值0，最大值2147483647 

        :param baseline_risk_num: The baseline_risk_num of this TrendRiskInfo.
        :type baseline_risk_num: int
        """
        self._baseline_risk_num = baseline_risk_num

    @property
    def asset_risk_num(self):
        r"""Gets the asset_risk_num of this TrendRiskInfo.

        **参数解释**: 资产风险数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The asset_risk_num of this TrendRiskInfo.
        :rtype: int
        """
        return self._asset_risk_num

    @asset_risk_num.setter
    def asset_risk_num(self, asset_risk_num):
        r"""Sets the asset_risk_num of this TrendRiskInfo.

        **参数解释**: 资产风险数量 **取值范围**: 最小值0，最大值2147483647 

        :param asset_risk_num: The asset_risk_num of this TrendRiskInfo.
        :type asset_risk_num: int
        """
        self._asset_risk_num = asset_risk_num

    @property
    def alarm_risk_num(self):
        r"""Gets the alarm_risk_num of this TrendRiskInfo.

        **参数解释**: 告警数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The alarm_risk_num of this TrendRiskInfo.
        :rtype: int
        """
        return self._alarm_risk_num

    @alarm_risk_num.setter
    def alarm_risk_num(self, alarm_risk_num):
        r"""Sets the alarm_risk_num of this TrendRiskInfo.

        **参数解释**: 告警数量 **取值范围**: 最小值0，最大值2147483647 

        :param alarm_risk_num: The alarm_risk_num of this TrendRiskInfo.
        :type alarm_risk_num: int
        """
        self._alarm_risk_num = alarm_risk_num

    @property
    def vul_risk_num(self):
        r"""Gets the vul_risk_num of this TrendRiskInfo.

        **参数解释**: 漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_risk_num of this TrendRiskInfo.
        :rtype: int
        """
        return self._vul_risk_num

    @vul_risk_num.setter
    def vul_risk_num(self, vul_risk_num):
        r"""Sets the vul_risk_num of this TrendRiskInfo.

        **参数解释**: 漏洞数 **取值范围**: 最小值0，最大值2147483647 

        :param vul_risk_num: The vul_risk_num of this TrendRiskInfo.
        :type vul_risk_num: int
        """
        self._vul_risk_num = vul_risk_num

    @property
    def update_time(self):
        r"""Gets the update_time of this TrendRiskInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The update_time of this TrendRiskInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TrendRiskInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param update_time: The update_time of this TrendRiskInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def time(self):
        r"""Gets the time of this TrendRiskInfo.

        **参数解释**: 时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The time of this TrendRiskInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this TrendRiskInfo.

        **参数解释**: 时间，毫秒级时间戳 **取值范围**: 最小值0，最大值9223372036854775807 

        :param time: The time of this TrendRiskInfo.
        :type time: int
        """
        self._time = time

    @property
    def score(self):
        r"""Gets the score of this TrendRiskInfo.

        **参数解释**: 分数 **取值范围**: 最小值0，最大值100 

        :return: The score of this TrendRiskInfo.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this TrendRiskInfo.

        **参数解释**: 分数 **取值范围**: 最小值0，最大值100 

        :param score: The score of this TrendRiskInfo.
        :type score: float
        """
        self._score = score

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
        if not isinstance(other, TrendRiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
