# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopDomainNamesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'stat_type': 'str',
        'service_area': 'str',
        'limit': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type',
        'service_area': 'service_area',
        'limit': 'limit',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, start_time=None, end_time=None, stat_type=None, service_area=None, limit=None, enterprise_project_id=None):
        r"""ShowTopDomainNamesRequest

        The model defined in huaweicloud sdk

        :param start_time: - 查询起始时间戳，时间戳应设置需为整点时间戳，设置方式如下： - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)
        :type start_time: int
        :param end_time: - 查询结束时间戳，时间戳应设置需为整点时间戳，设置方式如下： - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)
        :type end_time: int
        :param stat_type: - 统计类型 - 目前只支持bw（带宽），flux（流量），req_num（请求总数）
        :type stat_type: str
        :param service_area: 服务区域：mainland_china(中国大陆)，outside_mainland_china(中国大陆境外)，默认为mainland_china，当查询回源类指标时该参数无效。
        :type service_area: str
        :param limit: top域名查询数量,默认为20,最大为500，最小为0
        :type limit: int
        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子账号调用接口时，该参数必传。
        :type enterprise_project_id: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self._service_area = None
        self._limit = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.stat_type = stat_type
        if service_area is not None:
            self.service_area = service_area
        if limit is not None:
            self.limit = limit
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowTopDomainNamesRequest.

        - 查询起始时间戳，时间戳应设置需为整点时间戳，设置方式如下： - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :return: The start_time of this ShowTopDomainNamesRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowTopDomainNamesRequest.

        - 查询起始时间戳，时间戳应设置需为整点时间戳，设置方式如下： - interval为3600时，start_time设置为整小时时刻点，如：1631239200000(对应2021-09-10 10:00:00) - interval为86400时，start_time设置为东8区零点时刻点，如：1631203200000(对应2021-09-10 00:00:00)

        :param start_time: The start_time of this ShowTopDomainNamesRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTopDomainNamesRequest.

        - 查询结束时间戳，时间戳应设置需为整点时间戳，设置方式如下： - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :return: The end_time of this ShowTopDomainNamesRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTopDomainNamesRequest.

        - 查询结束时间戳，时间戳应设置需为整点时间戳，设置方式如下： - interval为3600时，end_time设置为整小时时刻点，如：1631325600000(对应2021-09-11 10:00:00) - interval为86400时，end_time设置为东8区零点时刻点，如：1631376000000(对应2021-09-12 00:00:00)

        :param end_time: The end_time of this ShowTopDomainNamesRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ShowTopDomainNamesRequest.

        - 统计类型 - 目前只支持bw（带宽），flux（流量），req_num（请求总数）

        :return: The stat_type of this ShowTopDomainNamesRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ShowTopDomainNamesRequest.

        - 统计类型 - 目前只支持bw（带宽），flux（流量），req_num（请求总数）

        :param stat_type: The stat_type of this ShowTopDomainNamesRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def service_area(self):
        r"""Gets the service_area of this ShowTopDomainNamesRequest.

        服务区域：mainland_china(中国大陆)，outside_mainland_china(中国大陆境外)，默认为mainland_china，当查询回源类指标时该参数无效。

        :return: The service_area of this ShowTopDomainNamesRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this ShowTopDomainNamesRequest.

        服务区域：mainland_china(中国大陆)，outside_mainland_china(中国大陆境外)，默认为mainland_china，当查询回源类指标时该参数无效。

        :param service_area: The service_area of this ShowTopDomainNamesRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def limit(self):
        r"""Gets the limit of this ShowTopDomainNamesRequest.

        top域名查询数量,默认为20,最大为500，最小为0

        :return: The limit of this ShowTopDomainNamesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowTopDomainNamesRequest.

        top域名查询数量,默认为20,最大为500，最小为0

        :param limit: The limit of this ShowTopDomainNamesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowTopDomainNamesRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this ShowTopDomainNamesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowTopDomainNamesRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this ShowTopDomainNamesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ShowTopDomainNamesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
