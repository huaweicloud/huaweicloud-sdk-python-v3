# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpAttackTimelineStatsRequest:

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
        'domain_name': 'str',
        'stat_type': 'str',
        'group_by': 'str',
        'group_by_value': 'str',
        'interval': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'group_by': 'group_by',
        'group_by_value': 'group_by_value',
        'interval': 'interval',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, enterprise_project_id=None, domain_name=None, stat_type=None, group_by=None, group_by_value=None, interval=None, start_time=None, end_time=None):
        r"""ShowHttpAttackTimelineStatsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0
        :type enterprise_project_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param stat_type: 指标类型，当前仅支持req_num
        :type stat_type: str
        :param group_by: 分组类型，当前仅支持action，attack_category
        :type group_by: str
        :param group_by_value: 分组类型对应的具体的值，不传的话默认总和（例如：action指标类型：log、block、captcha、js_challenge） （例如：attack_category指标类型：cc、access_control、bot、web_app_attack）
        :type group_by_value: str
        :param interval: 时间粒度(单位：秒)，不同时间范围有不同的可选时间粒度。[0,1H]，可选时间粒度为1M、5M；(1H,1D]，可选时间粒度为1M、5M、1H；(1D,3D]，可选时间粒度为1M、5M、1H、1D；(3D,7D]，可选时间粒度为5M、1H、1D；(7D,30D]，可选时间粒度为1H、1D。其中M代表分钟，H代表小时，D代表天。
        :type interval: int
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        

        self._enterprise_project_id = None
        self._domain_name = None
        self._stat_type = None
        self._group_by = None
        self._group_by_value = None
        self._interval = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if domain_name is not None:
            self.domain_name = domain_name
        self.stat_type = stat_type
        self.group_by = group_by
        if group_by_value is not None:
            self.group_by_value = group_by_value
        self.interval = interval
        self.start_time = start_time
        self.end_time = end_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowHttpAttackTimelineStatsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :return: The enterprise_project_id of this ShowHttpAttackTimelineStatsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowHttpAttackTimelineStatsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :param enterprise_project_id: The enterprise_project_id of this ShowHttpAttackTimelineStatsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowHttpAttackTimelineStatsRequest.

        域名

        :return: The domain_name of this ShowHttpAttackTimelineStatsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowHttpAttackTimelineStatsRequest.

        域名

        :param domain_name: The domain_name of this ShowHttpAttackTimelineStatsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowHttpAttackTimelineStatsRequest.

        指标类型，当前仅支持req_num

        :return: The stat_type of this ShowHttpAttackTimelineStatsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowHttpAttackTimelineStatsRequest.

        指标类型，当前仅支持req_num

        :param stat_type: The stat_type of this ShowHttpAttackTimelineStatsRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowHttpAttackTimelineStatsRequest.

        分组类型，当前仅支持action，attack_category

        :return: The group_by of this ShowHttpAttackTimelineStatsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowHttpAttackTimelineStatsRequest.

        分组类型，当前仅支持action，attack_category

        :param group_by: The group_by of this ShowHttpAttackTimelineStatsRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def group_by_value(self):
        r"""Gets the group_by_value of this ShowHttpAttackTimelineStatsRequest.

        分组类型对应的具体的值，不传的话默认总和（例如：action指标类型：log、block、captcha、js_challenge） （例如：attack_category指标类型：cc、access_control、bot、web_app_attack）

        :return: The group_by_value of this ShowHttpAttackTimelineStatsRequest.
        :rtype: str
        """
        return self._group_by_value

    @group_by_value.setter
    def group_by_value(self, group_by_value):
        r"""Sets the group_by_value of this ShowHttpAttackTimelineStatsRequest.

        分组类型对应的具体的值，不传的话默认总和（例如：action指标类型：log、block、captcha、js_challenge） （例如：attack_category指标类型：cc、access_control、bot、web_app_attack）

        :param group_by_value: The group_by_value of this ShowHttpAttackTimelineStatsRequest.
        :type group_by_value: str
        """
        self._group_by_value = group_by_value

    @property
    def interval(self):
        r"""Gets the interval of this ShowHttpAttackTimelineStatsRequest.

        时间粒度(单位：秒)，不同时间范围有不同的可选时间粒度。[0,1H]，可选时间粒度为1M、5M；(1H,1D]，可选时间粒度为1M、5M、1H；(1D,3D]，可选时间粒度为1M、5M、1H、1D；(3D,7D]，可选时间粒度为5M、1H、1D；(7D,30D]，可选时间粒度为1H、1D。其中M代表分钟，H代表小时，D代表天。

        :return: The interval of this ShowHttpAttackTimelineStatsRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ShowHttpAttackTimelineStatsRequest.

        时间粒度(单位：秒)，不同时间范围有不同的可选时间粒度。[0,1H]，可选时间粒度为1M、5M；(1H,1D]，可选时间粒度为1M、5M、1H；(1D,3D]，可选时间粒度为1M、5M、1H、1D；(3D,7D]，可选时间粒度为5M、1H、1D；(7D,30D]，可选时间粒度为1H、1D。其中M代表分钟，H代表小时，D代表天。

        :param interval: The interval of this ShowHttpAttackTimelineStatsRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowHttpAttackTimelineStatsRequest.

        开始时间

        :return: The start_time of this ShowHttpAttackTimelineStatsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowHttpAttackTimelineStatsRequest.

        开始时间

        :param start_time: The start_time of this ShowHttpAttackTimelineStatsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowHttpAttackTimelineStatsRequest.

        结束时间

        :return: The end_time of this ShowHttpAttackTimelineStatsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowHttpAttackTimelineStatsRequest.

        结束时间

        :param end_time: The end_time of this ShowHttpAttackTimelineStatsRequest.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowHttpAttackTimelineStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
