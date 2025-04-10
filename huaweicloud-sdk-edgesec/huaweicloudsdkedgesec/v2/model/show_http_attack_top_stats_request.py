# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpAttackTopStatsRequest:

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
        'limit': 'int',
        'time_type': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'group_by': 'group_by',
        'limit': 'limit',
        'time_type': 'time_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, enterprise_project_id=None, domain_name=None, stat_type=None, group_by=None, limit=None, time_type=None, start_time=None, end_time=None):
        r"""ShowHttpAttackTopStatsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0
        :type enterprise_project_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param stat_type: 指标类型。例如：req_num（请求次数）、bw（带宽）。目前只支持req_num
        :type stat_type: str
        :param group_by: 分组类型。响应值按分组类型进行统计，类型可为：host（请求的服务器域名）、sip（请求的客户端IP）、url（请求URL）、rule（自定义的策略类型描述）、user-agent（用户代理）、method（请求方法）、country（国家维度统计）。
        :type group_by: str
        :param limit: 限制Top数量(不超过100，默认为10)
        :type limit: int
        :param time_type: 时间枚举（LATEST（最近30mins）、TODAY（今天）、CUSTOMIZE（自定义，昨天到近30天任意整数天内））
        :type time_type: str
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        """
        
        

        self._enterprise_project_id = None
        self._domain_name = None
        self._stat_type = None
        self._group_by = None
        self._limit = None
        self._time_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if domain_name is not None:
            self.domain_name = domain_name
        self.stat_type = stat_type
        self.group_by = group_by
        if limit is not None:
            self.limit = limit
        self.time_type = time_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowHttpAttackTopStatsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :return: The enterprise_project_id of this ShowHttpAttackTopStatsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowHttpAttackTopStatsRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id，默认为0

        :param enterprise_project_id: The enterprise_project_id of this ShowHttpAttackTopStatsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowHttpAttackTopStatsRequest.

        域名

        :return: The domain_name of this ShowHttpAttackTopStatsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowHttpAttackTopStatsRequest.

        域名

        :param domain_name: The domain_name of this ShowHttpAttackTopStatsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowHttpAttackTopStatsRequest.

        指标类型。例如：req_num（请求次数）、bw（带宽）。目前只支持req_num

        :return: The stat_type of this ShowHttpAttackTopStatsRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowHttpAttackTopStatsRequest.

        指标类型。例如：req_num（请求次数）、bw（带宽）。目前只支持req_num

        :param stat_type: The stat_type of this ShowHttpAttackTopStatsRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def group_by(self):
        r"""Gets the group_by of this ShowHttpAttackTopStatsRequest.

        分组类型。响应值按分组类型进行统计，类型可为：host（请求的服务器域名）、sip（请求的客户端IP）、url（请求URL）、rule（自定义的策略类型描述）、user-agent（用户代理）、method（请求方法）、country（国家维度统计）。

        :return: The group_by of this ShowHttpAttackTopStatsRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ShowHttpAttackTopStatsRequest.

        分组类型。响应值按分组类型进行统计，类型可为：host（请求的服务器域名）、sip（请求的客户端IP）、url（请求URL）、rule（自定义的策略类型描述）、user-agent（用户代理）、method（请求方法）、country（国家维度统计）。

        :param group_by: The group_by of this ShowHttpAttackTopStatsRequest.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def limit(self):
        r"""Gets the limit of this ShowHttpAttackTopStatsRequest.

        限制Top数量(不超过100，默认为10)

        :return: The limit of this ShowHttpAttackTopStatsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowHttpAttackTopStatsRequest.

        限制Top数量(不超过100，默认为10)

        :param limit: The limit of this ShowHttpAttackTopStatsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def time_type(self):
        r"""Gets the time_type of this ShowHttpAttackTopStatsRequest.

        时间枚举（LATEST（最近30mins）、TODAY（今天）、CUSTOMIZE（自定义，昨天到近30天任意整数天内））

        :return: The time_type of this ShowHttpAttackTopStatsRequest.
        :rtype: str
        """
        return self._time_type

    @time_type.setter
    def time_type(self, time_type):
        r"""Sets the time_type of this ShowHttpAttackTopStatsRequest.

        时间枚举（LATEST（最近30mins）、TODAY（今天）、CUSTOMIZE（自定义，昨天到近30天任意整数天内））

        :param time_type: The time_type of this ShowHttpAttackTopStatsRequest.
        :type time_type: str
        """
        self._time_type = time_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowHttpAttackTopStatsRequest.

        开始时间

        :return: The start_time of this ShowHttpAttackTopStatsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowHttpAttackTopStatsRequest.

        开始时间

        :param start_time: The start_time of this ShowHttpAttackTopStatsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowHttpAttackTopStatsRequest.

        结束时间

        :return: The end_time of this ShowHttpAttackTopStatsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowHttpAttackTopStatsRequest.

        结束时间

        :param end_time: The end_time of this ShowHttpAttackTopStatsRequest.
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
        if not isinstance(other, ShowHttpAttackTopStatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
