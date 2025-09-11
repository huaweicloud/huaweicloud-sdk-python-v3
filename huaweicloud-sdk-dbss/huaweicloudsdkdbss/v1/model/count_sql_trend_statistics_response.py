# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountSqlTrendStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count_statistics': 'list[CountStatisticsBean]',
        'generate_time': 'str',
        'status': 'str'
    }

    attribute_map = {
        'count_statistics': 'count_statistics',
        'generate_time': 'generate_time',
        'status': 'status'
    }

    def __init__(self, count_statistics=None, generate_time=None, status=None):
        r"""CountSqlTrendStatisticsResponse

        The model defined in huaweicloud sdk

        :param count_statistics: 列表数据
        :type count_statistics: list[:class:`huaweicloudsdkdbss.v1.CountStatisticsBean`]
        :param generate_time: 生成时间
        :type generate_time: str
        :param status: 状态  - FINISHED：已完成  - RUNNING：运行中
        :type status: str
        """
        
        super(CountSqlTrendStatisticsResponse, self).__init__()

        self._count_statistics = None
        self._generate_time = None
        self._status = None
        self.discriminator = None

        if count_statistics is not None:
            self.count_statistics = count_statistics
        if generate_time is not None:
            self.generate_time = generate_time
        if status is not None:
            self.status = status

    @property
    def count_statistics(self):
        r"""Gets the count_statistics of this CountSqlTrendStatisticsResponse.

        列表数据

        :return: The count_statistics of this CountSqlTrendStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.CountStatisticsBean`]
        """
        return self._count_statistics

    @count_statistics.setter
    def count_statistics(self, count_statistics):
        r"""Sets the count_statistics of this CountSqlTrendStatisticsResponse.

        列表数据

        :param count_statistics: The count_statistics of this CountSqlTrendStatisticsResponse.
        :type count_statistics: list[:class:`huaweicloudsdkdbss.v1.CountStatisticsBean`]
        """
        self._count_statistics = count_statistics

    @property
    def generate_time(self):
        r"""Gets the generate_time of this CountSqlTrendStatisticsResponse.

        生成时间

        :return: The generate_time of this CountSqlTrendStatisticsResponse.
        :rtype: str
        """
        return self._generate_time

    @generate_time.setter
    def generate_time(self, generate_time):
        r"""Sets the generate_time of this CountSqlTrendStatisticsResponse.

        生成时间

        :param generate_time: The generate_time of this CountSqlTrendStatisticsResponse.
        :type generate_time: str
        """
        self._generate_time = generate_time

    @property
    def status(self):
        r"""Gets the status of this CountSqlTrendStatisticsResponse.

        状态  - FINISHED：已完成  - RUNNING：运行中

        :return: The status of this CountSqlTrendStatisticsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountSqlTrendStatisticsResponse.

        状态  - FINISHED：已完成  - RUNNING：运行中

        :param status: The status of this CountSqlTrendStatisticsResponse.
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
        if not isinstance(other, CountSqlTrendStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
