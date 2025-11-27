# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCdnDomainTopPathRequest:

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
        'domain_name': 'str',
        'stat_type': 'str',
        'service_area': 'str',
        'user_domain_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'domain_name': 'domain_name',
        'stat_type': 'stat_type',
        'service_area': 'service_area',
        'user_domain_id': 'user_domain_id'
    }

    def __init__(self, start_time=None, end_time=None, domain_name=None, stat_type=None, service_area=None, user_domain_id=None):
        r"""ListCdnDomainTopPathRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间戳，只能传0点毫秒时间戳
        :type start_time: int
        :param end_time: 查询结束时间戳，只能传0点毫秒时间戳
        :type end_time: int
        :param domain_name: 域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。
        :type domain_name: str
        :param stat_type: - 参数类型支持：flux(流量),req_num(请求数)
        :type stat_type: str
        :param service_area: 服务区域：mainland_china(大陆)，outside_mainland_china(海外)，默认为global(全球)
        :type service_area: str
        :param user_domain_id: 域名所属用户的domain_id。
        :type user_domain_id: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._domain_name = None
        self._stat_type = None
        self._service_area = None
        self._user_domain_id = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.domain_name = domain_name
        self.stat_type = stat_type
        if service_area is not None:
            self.service_area = service_area
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListCdnDomainTopPathRequest.

        查询起始时间戳，只能传0点毫秒时间戳

        :return: The start_time of this ListCdnDomainTopPathRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListCdnDomainTopPathRequest.

        查询起始时间戳，只能传0点毫秒时间戳

        :param start_time: The start_time of this ListCdnDomainTopPathRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListCdnDomainTopPathRequest.

        查询结束时间戳，只能传0点毫秒时间戳

        :return: The end_time of this ListCdnDomainTopPathRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListCdnDomainTopPathRequest.

        查询结束时间戳，只能传0点毫秒时间戳

        :param end_time: The end_time of this ListCdnDomainTopPathRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListCdnDomainTopPathRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :return: The domain_name of this ListCdnDomainTopPathRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListCdnDomainTopPathRequest.

        域名列表，多个域名以逗号（半角）分隔，如：www.test1.com,www.test2.com all表示查询名下全部域名。如果域名在查询时间段内无数据，结果将不返回该域名的信息。

        :param domain_name: The domain_name of this ListCdnDomainTopPathRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def stat_type(self):
        r"""Gets the stat_type of this ListCdnDomainTopPathRequest.

        - 参数类型支持：flux(流量),req_num(请求数)

        :return: The stat_type of this ListCdnDomainTopPathRequest.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this ListCdnDomainTopPathRequest.

        - 参数类型支持：flux(流量),req_num(请求数)

        :param stat_type: The stat_type of this ListCdnDomainTopPathRequest.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def service_area(self):
        r"""Gets the service_area of this ListCdnDomainTopPathRequest.

        服务区域：mainland_china(大陆)，outside_mainland_china(海外)，默认为global(全球)

        :return: The service_area of this ListCdnDomainTopPathRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        r"""Sets the service_area of this ListCdnDomainTopPathRequest.

        服务区域：mainland_china(大陆)，outside_mainland_china(海外)，默认为global(全球)

        :param service_area: The service_area of this ListCdnDomainTopPathRequest.
        :type service_area: str
        """
        self._service_area = service_area

    @property
    def user_domain_id(self):
        r"""Gets the user_domain_id of this ListCdnDomainTopPathRequest.

        域名所属用户的domain_id。

        :return: The user_domain_id of this ListCdnDomainTopPathRequest.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        r"""Sets the user_domain_id of this ListCdnDomainTopPathRequest.

        域名所属用户的domain_id。

        :param user_domain_id: The user_domain_id of this ListCdnDomainTopPathRequest.
        :type user_domain_id: str
        """
        self._user_domain_id = user_domain_id

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
        if not isinstance(other, ListCdnDomainTopPathRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
