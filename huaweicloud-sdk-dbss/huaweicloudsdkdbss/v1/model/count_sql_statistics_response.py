# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountSqlStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'generate_time': 'str',
        'sql_statistics': 'list[SQLStatisticsBean]',
        'status': 'str'
    }

    attribute_map = {
        'generate_time': 'generate_time',
        'sql_statistics': 'sql_statistics',
        'status': 'status'
    }

    def __init__(self, generate_time=None, sql_statistics=None, status=None):
        r"""CountSqlStatisticsResponse

        The model defined in huaweicloud sdk

        :param generate_time: 生成时间
        :type generate_time: str
        :param sql_statistics: SQL统计数据
        :type sql_statistics: list[:class:`huaweicloudsdkdbss.v1.SQLStatisticsBean`]
        :param status: 状态  - FINISHED：已完成  - RUNNING：运行中
        :type status: str
        """
        
        super(CountSqlStatisticsResponse, self).__init__()

        self._generate_time = None
        self._sql_statistics = None
        self._status = None
        self.discriminator = None

        if generate_time is not None:
            self.generate_time = generate_time
        if sql_statistics is not None:
            self.sql_statistics = sql_statistics
        if status is not None:
            self.status = status

    @property
    def generate_time(self):
        r"""Gets the generate_time of this CountSqlStatisticsResponse.

        生成时间

        :return: The generate_time of this CountSqlStatisticsResponse.
        :rtype: str
        """
        return self._generate_time

    @generate_time.setter
    def generate_time(self, generate_time):
        r"""Sets the generate_time of this CountSqlStatisticsResponse.

        生成时间

        :param generate_time: The generate_time of this CountSqlStatisticsResponse.
        :type generate_time: str
        """
        self._generate_time = generate_time

    @property
    def sql_statistics(self):
        r"""Gets the sql_statistics of this CountSqlStatisticsResponse.

        SQL统计数据

        :return: The sql_statistics of this CountSqlStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.SQLStatisticsBean`]
        """
        return self._sql_statistics

    @sql_statistics.setter
    def sql_statistics(self, sql_statistics):
        r"""Sets the sql_statistics of this CountSqlStatisticsResponse.

        SQL统计数据

        :param sql_statistics: The sql_statistics of this CountSqlStatisticsResponse.
        :type sql_statistics: list[:class:`huaweicloudsdkdbss.v1.SQLStatisticsBean`]
        """
        self._sql_statistics = sql_statistics

    @property
    def status(self):
        r"""Gets the status of this CountSqlStatisticsResponse.

        状态  - FINISHED：已完成  - RUNNING：运行中

        :return: The status of this CountSqlStatisticsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountSqlStatisticsResponse.

        状态  - FINISHED：已完成  - RUNNING：运行中

        :param status: The status of this CountSqlStatisticsResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CountSqlStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
