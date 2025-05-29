# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobBuildTimeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'avg_build_time': 'float',
        'max_build_time': 'int',
        'min_build_time': 'int',
        'chart': 'list[ShowJobBuildTimeResultChart]'
    }

    attribute_map = {
        'job_id': 'job_id',
        'avg_build_time': 'avg_build_time',
        'max_build_time': 'max_build_time',
        'min_build_time': 'min_build_time',
        'chart': 'chart'
    }

    def __init__(self, job_id=None, avg_build_time=None, max_build_time=None, min_build_time=None, chart=None):
        r"""ShowJobBuildTimeResult

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param avg_build_time: 平均构建时长
        :type avg_build_time: float
        :param max_build_time: 最长时间
        :type max_build_time: int
        :param min_build_time: 最短时间
        :type min_build_time: int
        :param chart: 每日构建数据
        :type chart: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildTimeResultChart`]
        """
        
        

        self._job_id = None
        self._avg_build_time = None
        self._max_build_time = None
        self._min_build_time = None
        self._chart = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if avg_build_time is not None:
            self.avg_build_time = avg_build_time
        if max_build_time is not None:
            self.max_build_time = max_build_time
        if min_build_time is not None:
            self.min_build_time = min_build_time
        if chart is not None:
            self.chart = chart

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowJobBuildTimeResult.

        任务ID

        :return: The job_id of this ShowJobBuildTimeResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowJobBuildTimeResult.

        任务ID

        :param job_id: The job_id of this ShowJobBuildTimeResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def avg_build_time(self):
        r"""Gets the avg_build_time of this ShowJobBuildTimeResult.

        平均构建时长

        :return: The avg_build_time of this ShowJobBuildTimeResult.
        :rtype: float
        """
        return self._avg_build_time

    @avg_build_time.setter
    def avg_build_time(self, avg_build_time):
        r"""Sets the avg_build_time of this ShowJobBuildTimeResult.

        平均构建时长

        :param avg_build_time: The avg_build_time of this ShowJobBuildTimeResult.
        :type avg_build_time: float
        """
        self._avg_build_time = avg_build_time

    @property
    def max_build_time(self):
        r"""Gets the max_build_time of this ShowJobBuildTimeResult.

        最长时间

        :return: The max_build_time of this ShowJobBuildTimeResult.
        :rtype: int
        """
        return self._max_build_time

    @max_build_time.setter
    def max_build_time(self, max_build_time):
        r"""Sets the max_build_time of this ShowJobBuildTimeResult.

        最长时间

        :param max_build_time: The max_build_time of this ShowJobBuildTimeResult.
        :type max_build_time: int
        """
        self._max_build_time = max_build_time

    @property
    def min_build_time(self):
        r"""Gets the min_build_time of this ShowJobBuildTimeResult.

        最短时间

        :return: The min_build_time of this ShowJobBuildTimeResult.
        :rtype: int
        """
        return self._min_build_time

    @min_build_time.setter
    def min_build_time(self, min_build_time):
        r"""Sets the min_build_time of this ShowJobBuildTimeResult.

        最短时间

        :param min_build_time: The min_build_time of this ShowJobBuildTimeResult.
        :type min_build_time: int
        """
        self._min_build_time = min_build_time

    @property
    def chart(self):
        r"""Gets the chart of this ShowJobBuildTimeResult.

        每日构建数据

        :return: The chart of this ShowJobBuildTimeResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildTimeResultChart`]
        """
        return self._chart

    @chart.setter
    def chart(self, chart):
        r"""Sets the chart of this ShowJobBuildTimeResult.

        每日构建数据

        :param chart: The chart of this ShowJobBuildTimeResult.
        :type chart: list[:class:`huaweicloudsdkcodeartsbuild.v3.ShowJobBuildTimeResultChart`]
        """
        self._chart = chart

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
        if not isinstance(other, ShowJobBuildTimeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
