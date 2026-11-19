# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAiOverviewStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'type': 'str',
        'begin_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, enterprise_project_id=None, type=None, begin_time=None, end_time=None):
        r"""ShowAiOverviewStatisticsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param type: **参数解释**: 查询类型（不传时返回全部数据） **约束限制**: 不涉及 **取值范围**: - alarm：告警数量统计 - risk：风险数量统计 - source：智能体防护信息  **默认取值**: 不涉及 
        :type type: str
        :param begin_time: **参数解释**: 开始时间，13位毫秒时间戳 **约束限制**: 需小于等于end_time **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type begin_time: int
        :param end_time: **参数解释**: 结束时间，13位毫秒时间戳 **约束限制**: 需大于等于begin_time **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type end_time: int
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if type is not None:
            self.type = type
        self.begin_time = begin_time
        self.end_time = end_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowAiOverviewStatisticsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowAiOverviewStatisticsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 查询类型（不传时返回全部数据） **约束限制**: 不涉及 **取值范围**: - alarm：告警数量统计 - risk：风险数量统计 - source：智能体防护信息  **默认取值**: 不涉及 

        :return: The type of this ShowAiOverviewStatisticsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 查询类型（不传时返回全部数据） **约束限制**: 不涉及 **取值范围**: - alarm：告警数量统计 - risk：风险数量统计 - source：智能体防护信息  **默认取值**: 不涉及 

        :param type: The type of this ShowAiOverviewStatisticsRequest.
        :type type: str
        """
        self._type = type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 开始时间，13位毫秒时间戳 **约束限制**: 需小于等于end_time **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The begin_time of this ShowAiOverviewStatisticsRequest.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 开始时间，13位毫秒时间戳 **约束限制**: 需小于等于end_time **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param begin_time: The begin_time of this ShowAiOverviewStatisticsRequest.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 结束时间，13位毫秒时间戳 **约束限制**: 需大于等于begin_time **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The end_time of this ShowAiOverviewStatisticsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowAiOverviewStatisticsRequest.

        **参数解释**: 结束时间，13位毫秒时间戳 **约束限制**: 需大于等于begin_time **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param end_time: The end_time of this ShowAiOverviewStatisticsRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowAiOverviewStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
