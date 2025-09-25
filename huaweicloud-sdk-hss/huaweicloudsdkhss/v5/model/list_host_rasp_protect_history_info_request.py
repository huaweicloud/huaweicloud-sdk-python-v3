# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostRaspProtectHistoryInfoRequest:

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
        'region': 'str',
        'host_id': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'limit': 'int',
        'offset': 'int',
        'alarm_level': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'region': 'region',
        'host_id': 'host_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'alarm_level': 'alarm_level'
    }

    def __init__(self, enterprise_project_id=None, region=None, host_id=None, start_time=None, end_time=None, limit=None, offset=None, alarm_level=None):
        r"""ListHostRaspProtectHistoryInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param host_id: **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param start_time: **参数解释**: 查询起始时间，单位毫秒，不可早于30天前，如早于30天前，则按照30天前计算。 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000 **默认取值**: 不涉及 
        :type start_time: int
        :param end_time: **参数解释**: 查询终止时间，单位毫秒，不可早于start_time，且与start_time相差不可超过30天，否则按照start_time的1天后计算。 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000 **默认取值**: 不涉及 
        :type end_time: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param alarm_level: **参数解释**: 告警等级 **约束限制**: 不涉及 **取值范围**: - 1 : 紧急。 - 2 : 重要。 - 3 : 次要。 - 4 : 提示。  **默认取值**: 不涉及 
        :type alarm_level: int
        """
        
        

        self._enterprise_project_id = None
        self._region = None
        self._host_id = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._alarm_level = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if region is not None:
            self.region = region
        if host_id is not None:
            self.host_id = host_id
        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        self.offset = offset
        if alarm_level is not None:
            self.alarm_level = alarm_level

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListHostRaspProtectHistoryInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def region(self):
        r"""Gets the region of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListHostRaspProtectHistoryInfoRequest.
        :type region: str
        """
        self._region = region

    @property
    def host_id(self):
        r"""Gets the host_id of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 服务器ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListHostRaspProtectHistoryInfoRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 查询起始时间，单位毫秒，不可早于30天前，如早于30天前，则按照30天前计算。 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000 **默认取值**: 不涉及 

        :return: The start_time of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 查询起始时间，单位毫秒，不可早于30天前，如早于30天前，则按照30天前计算。 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000 **默认取值**: 不涉及 

        :param start_time: The start_time of this ListHostRaspProtectHistoryInfoRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 查询终止时间，单位毫秒，不可早于start_time，且与start_time相差不可超过30天，否则按照start_time的1天后计算。 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000 **默认取值**: 不涉及 

        :return: The end_time of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 查询终止时间，单位毫秒，不可早于start_time，且与start_time相差不可超过30天，否则按照start_time的1天后计算。 **约束限制**: 不涉及 **取值范围**: 取值0-4070880000000 **默认取值**: 不涉及 

        :param end_time: The end_time of this ListHostRaspProtectHistoryInfoRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListHostRaspProtectHistoryInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListHostRaspProtectHistoryInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 告警等级 **约束限制**: 不涉及 **取值范围**: - 1 : 紧急。 - 2 : 重要。 - 3 : 次要。 - 4 : 提示。  **默认取值**: 不涉及 

        :return: The alarm_level of this ListHostRaspProtectHistoryInfoRequest.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this ListHostRaspProtectHistoryInfoRequest.

        **参数解释**: 告警等级 **约束限制**: 不涉及 **取值范围**: - 1 : 紧急。 - 2 : 重要。 - 3 : 次要。 - 4 : 提示。  **默认取值**: 不涉及 

        :param alarm_level: The alarm_level of this ListHostRaspProtectHistoryInfoRequest.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

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
        if not isinstance(other, ListHostRaspProtectHistoryInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
