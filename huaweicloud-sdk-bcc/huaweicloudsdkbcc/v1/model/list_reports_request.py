# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReportsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'report_setting_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'report_setting_id': 'report_setting_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, report_setting_id=None, start_time=None, end_time=None, marker=None, limit=None):
        r"""ListReportsRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param report_setting_id: 报告配置id
        :type report_setting_id: str
        :param start_time: 生成报告的起始时间，例如：2025-03-20T09:31:45Z。
        :type start_time: str
        :param end_time: 生成报告的截止时间，例如：2025-03-21T09:31:45Z。
        :type end_time: str
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。
        :type marker: str
        :param limit: 单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。
        :type limit: int
        """
        
        

        self._domain_id = None
        self._report_setting_id = None
        self._start_time = None
        self._end_time = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if report_setting_id is not None:
            self.report_setting_id = report_setting_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListReportsRequest.

        账号ID

        :return: The domain_id of this ListReportsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListReportsRequest.

        账号ID

        :param domain_id: The domain_id of this ListReportsRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def report_setting_id(self):
        r"""Gets the report_setting_id of this ListReportsRequest.

        报告配置id

        :return: The report_setting_id of this ListReportsRequest.
        :rtype: str
        """
        return self._report_setting_id

    @report_setting_id.setter
    def report_setting_id(self, report_setting_id):
        r"""Sets the report_setting_id of this ListReportsRequest.

        报告配置id

        :param report_setting_id: The report_setting_id of this ListReportsRequest.
        :type report_setting_id: str
        """
        self._report_setting_id = report_setting_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListReportsRequest.

        生成报告的起始时间，例如：2025-03-20T09:31:45Z。

        :return: The start_time of this ListReportsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListReportsRequest.

        生成报告的起始时间，例如：2025-03-20T09:31:45Z。

        :param start_time: The start_time of this ListReportsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListReportsRequest.

        生成报告的截止时间，例如：2025-03-21T09:31:45Z。

        :return: The end_time of this ListReportsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListReportsRequest.

        生成报告的截止时间，例如：2025-03-21T09:31:45Z。

        :param end_time: The end_time of this ListReportsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def marker(self):
        r"""Gets the marker of this ListReportsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :return: The marker of this ListReportsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListReportsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :param marker: The marker of this ListReportsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListReportsRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :return: The limit of this ListReportsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListReportsRequest.

        单次查询的条数限制,取值范围(0,100]，默认值为10，用于限制结果数据条数。

        :param limit: The limit of this ListReportsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListReportsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
