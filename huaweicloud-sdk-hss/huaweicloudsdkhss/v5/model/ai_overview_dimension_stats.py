# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiOverviewDimensionStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dimension': 'str',
        'alarm_count': 'int',
        'risk_count': 'int'
    }

    attribute_map = {
        'dimension': 'dimension',
        'alarm_count': 'alarm_count',
        'risk_count': 'risk_count'
    }

    def __init__(self, dimension=None, alarm_count=None, risk_count=None):
        r"""AiOverviewDimensionStats

        The model defined in huaweicloud sdk

        :param dimension: **参数解释**: 防护维度key，取值及含义如下： - consistency_detection：意图行为一致性检测 - command_control：命令执行控制 - file_access_control：文件访问控制 - sensitive_info_detection：敏感信息检测 - role_limit：角色限定（行为轨迹检测不覆盖此维度） - openclaw_detectors：记忆投毒防护（OpenClaw专属维度） - other：其他类  **取值范围**: consistency_detection、command_control、file_access_control、sensitive_info_detection、role_limit、openclaw_detectors、other 
        :type dimension: str
        :param alarm_count: **参数解释**： 告警数量，type&#x3D;alarm时返回 **取值范围**： 最小值0，最大值9223372036854775807 
        :type alarm_count: int
        :param risk_count: **参数解释**： 风险数量，type&#x3D;risk时返回，role_limit固定为0 **取值范围**： 最小值0，最大值9223372036854775807 
        :type risk_count: int
        """
        
        

        self._dimension = None
        self._alarm_count = None
        self._risk_count = None
        self.discriminator = None

        if dimension is not None:
            self.dimension = dimension
        if alarm_count is not None:
            self.alarm_count = alarm_count
        if risk_count is not None:
            self.risk_count = risk_count

    @property
    def dimension(self):
        r"""Gets the dimension of this AiOverviewDimensionStats.

        **参数解释**: 防护维度key，取值及含义如下： - consistency_detection：意图行为一致性检测 - command_control：命令执行控制 - file_access_control：文件访问控制 - sensitive_info_detection：敏感信息检测 - role_limit：角色限定（行为轨迹检测不覆盖此维度） - openclaw_detectors：记忆投毒防护（OpenClaw专属维度） - other：其他类  **取值范围**: consistency_detection、command_control、file_access_control、sensitive_info_detection、role_limit、openclaw_detectors、other 

        :return: The dimension of this AiOverviewDimensionStats.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        r"""Sets the dimension of this AiOverviewDimensionStats.

        **参数解释**: 防护维度key，取值及含义如下： - consistency_detection：意图行为一致性检测 - command_control：命令执行控制 - file_access_control：文件访问控制 - sensitive_info_detection：敏感信息检测 - role_limit：角色限定（行为轨迹检测不覆盖此维度） - openclaw_detectors：记忆投毒防护（OpenClaw专属维度） - other：其他类  **取值范围**: consistency_detection、command_control、file_access_control、sensitive_info_detection、role_limit、openclaw_detectors、other 

        :param dimension: The dimension of this AiOverviewDimensionStats.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def alarm_count(self):
        r"""Gets the alarm_count of this AiOverviewDimensionStats.

        **参数解释**： 告警数量，type=alarm时返回 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The alarm_count of this AiOverviewDimensionStats.
        :rtype: int
        """
        return self._alarm_count

    @alarm_count.setter
    def alarm_count(self, alarm_count):
        r"""Sets the alarm_count of this AiOverviewDimensionStats.

        **参数解释**： 告警数量，type=alarm时返回 **取值范围**： 最小值0，最大值9223372036854775807 

        :param alarm_count: The alarm_count of this AiOverviewDimensionStats.
        :type alarm_count: int
        """
        self._alarm_count = alarm_count

    @property
    def risk_count(self):
        r"""Gets the risk_count of this AiOverviewDimensionStats.

        **参数解释**： 风险数量，type=risk时返回，role_limit固定为0 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The risk_count of this AiOverviewDimensionStats.
        :rtype: int
        """
        return self._risk_count

    @risk_count.setter
    def risk_count(self, risk_count):
        r"""Sets the risk_count of this AiOverviewDimensionStats.

        **参数解释**： 风险数量，type=risk时返回，role_limit固定为0 **取值范围**： 最小值0，最大值9223372036854775807 

        :param risk_count: The risk_count of this AiOverviewDimensionStats.
        :type risk_count: int
        """
        self._risk_count = risk_count

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
        if not isinstance(other, AiOverviewDimensionStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
