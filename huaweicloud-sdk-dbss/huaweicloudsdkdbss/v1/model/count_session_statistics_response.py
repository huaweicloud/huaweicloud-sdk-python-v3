# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountSessionStatisticsResponse(SdkResponse):

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
        'session_statistics': 'list[SessionStatisticsBean]',
        'status': 'str'
    }

    attribute_map = {
        'generate_time': 'generate_time',
        'session_statistics': 'session_statistics',
        'status': 'status'
    }

    def __init__(self, generate_time=None, session_statistics=None, status=None):
        r"""CountSessionStatisticsResponse

        The model defined in huaweicloud sdk

        :param generate_time: 生成时间
        :type generate_time: str
        :param session_statistics: 统计数据列表
        :type session_statistics: list[:class:`huaweicloudsdkdbss.v1.SessionStatisticsBean`]
        :param status: 状态  - FINISHED：已完成  - RUNNING：运行中
        :type status: str
        """
        
        super(CountSessionStatisticsResponse, self).__init__()

        self._generate_time = None
        self._session_statistics = None
        self._status = None
        self.discriminator = None

        if generate_time is not None:
            self.generate_time = generate_time
        if session_statistics is not None:
            self.session_statistics = session_statistics
        if status is not None:
            self.status = status

    @property
    def generate_time(self):
        r"""Gets the generate_time of this CountSessionStatisticsResponse.

        生成时间

        :return: The generate_time of this CountSessionStatisticsResponse.
        :rtype: str
        """
        return self._generate_time

    @generate_time.setter
    def generate_time(self, generate_time):
        r"""Sets the generate_time of this CountSessionStatisticsResponse.

        生成时间

        :param generate_time: The generate_time of this CountSessionStatisticsResponse.
        :type generate_time: str
        """
        self._generate_time = generate_time

    @property
    def session_statistics(self):
        r"""Gets the session_statistics of this CountSessionStatisticsResponse.

        统计数据列表

        :return: The session_statistics of this CountSessionStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.SessionStatisticsBean`]
        """
        return self._session_statistics

    @session_statistics.setter
    def session_statistics(self, session_statistics):
        r"""Sets the session_statistics of this CountSessionStatisticsResponse.

        统计数据列表

        :param session_statistics: The session_statistics of this CountSessionStatisticsResponse.
        :type session_statistics: list[:class:`huaweicloudsdkdbss.v1.SessionStatisticsBean`]
        """
        self._session_statistics = session_statistics

    @property
    def status(self):
        r"""Gets the status of this CountSessionStatisticsResponse.

        状态  - FINISHED：已完成  - RUNNING：运行中

        :return: The status of this CountSessionStatisticsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountSessionStatisticsResponse.

        状态  - FINISHED：已完成  - RUNNING：运行中

        :param status: The status of this CountSessionStatisticsResponse.
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
        if not isinstance(other, CountSessionStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
