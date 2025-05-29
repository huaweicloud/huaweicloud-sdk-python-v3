# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobBuildTimeResultChart:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'daily_build_number': 'str',
        'build_number': 'int',
        'build_time': 'int',
        'build_result': 'str'
    }

    attribute_map = {
        'daily_build_number': 'daily_build_number',
        'build_number': 'build_number',
        'build_time': 'build_time',
        'build_result': 'build_result'
    }

    def __init__(self, daily_build_number=None, build_number=None, build_time=None, build_result=None):
        r"""ShowJobBuildTimeResultChart

        The model defined in huaweicloud sdk

        :param daily_build_number: 构建每日编号
        :type daily_build_number: str
        :param build_number: 构建编号
        :type build_number: int
        :param build_time: 步骤执行时长，单位s
        :type build_time: int
        :param build_result: 构建结果
        :type build_result: str
        """
        
        

        self._daily_build_number = None
        self._build_number = None
        self._build_time = None
        self._build_result = None
        self.discriminator = None

        if daily_build_number is not None:
            self.daily_build_number = daily_build_number
        if build_number is not None:
            self.build_number = build_number
        if build_time is not None:
            self.build_time = build_time
        if build_result is not None:
            self.build_result = build_result

    @property
    def daily_build_number(self):
        r"""Gets the daily_build_number of this ShowJobBuildTimeResultChart.

        构建每日编号

        :return: The daily_build_number of this ShowJobBuildTimeResultChart.
        :rtype: str
        """
        return self._daily_build_number

    @daily_build_number.setter
    def daily_build_number(self, daily_build_number):
        r"""Sets the daily_build_number of this ShowJobBuildTimeResultChart.

        构建每日编号

        :param daily_build_number: The daily_build_number of this ShowJobBuildTimeResultChart.
        :type daily_build_number: str
        """
        self._daily_build_number = daily_build_number

    @property
    def build_number(self):
        r"""Gets the build_number of this ShowJobBuildTimeResultChart.

        构建编号

        :return: The build_number of this ShowJobBuildTimeResultChart.
        :rtype: int
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        r"""Sets the build_number of this ShowJobBuildTimeResultChart.

        构建编号

        :param build_number: The build_number of this ShowJobBuildTimeResultChart.
        :type build_number: int
        """
        self._build_number = build_number

    @property
    def build_time(self):
        r"""Gets the build_time of this ShowJobBuildTimeResultChart.

        步骤执行时长，单位s

        :return: The build_time of this ShowJobBuildTimeResultChart.
        :rtype: int
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        r"""Sets the build_time of this ShowJobBuildTimeResultChart.

        步骤执行时长，单位s

        :param build_time: The build_time of this ShowJobBuildTimeResultChart.
        :type build_time: int
        """
        self._build_time = build_time

    @property
    def build_result(self):
        r"""Gets the build_result of this ShowJobBuildTimeResultChart.

        构建结果

        :return: The build_result of this ShowJobBuildTimeResultChart.
        :rtype: str
        """
        return self._build_result

    @build_result.setter
    def build_result(self, build_result):
        r"""Sets the build_result of this ShowJobBuildTimeResultChart.

        构建结果

        :param build_result: The build_result of this ShowJobBuildTimeResultChart.
        :type build_result: str
        """
        self._build_result = build_result

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
        if not isinstance(other, ShowJobBuildTimeResultChart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
