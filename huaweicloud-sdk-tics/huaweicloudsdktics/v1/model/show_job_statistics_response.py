# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_cnt': 'int',
        'job_ins_cnt': 'int',
        'job_ins_fail_cnt': 'int',
        'job_ins_intercept_cnt': 'int',
        'job_ins_success_cnt': 'int'
    }

    attribute_map = {
        'job_cnt': 'job_cnt',
        'job_ins_cnt': 'job_ins_cnt',
        'job_ins_fail_cnt': 'job_ins_fail_cnt',
        'job_ins_intercept_cnt': 'job_ins_intercept_cnt',
        'job_ins_success_cnt': 'job_ins_success_cnt'
    }

    def __init__(self, job_cnt=None, job_ins_cnt=None, job_ins_fail_cnt=None, job_ins_intercept_cnt=None, job_ins_success_cnt=None):
        """ShowJobStatisticsResponse

        The model defined in huaweicloud sdk

        :param job_cnt: 作业数量统计
        :type job_cnt: int
        :param job_ins_cnt: 作业实例次数
        :type job_ins_cnt: int
        :param job_ins_fail_cnt: 作业实例失败次数
        :type job_ins_fail_cnt: int
        :param job_ins_intercept_cnt: 作业实例拦截次数
        :type job_ins_intercept_cnt: int
        :param job_ins_success_cnt: 作业实例成功次数
        :type job_ins_success_cnt: int
        """
        
        super(ShowJobStatisticsResponse, self).__init__()

        self._job_cnt = None
        self._job_ins_cnt = None
        self._job_ins_fail_cnt = None
        self._job_ins_intercept_cnt = None
        self._job_ins_success_cnt = None
        self.discriminator = None

        if job_cnt is not None:
            self.job_cnt = job_cnt
        if job_ins_cnt is not None:
            self.job_ins_cnt = job_ins_cnt
        if job_ins_fail_cnt is not None:
            self.job_ins_fail_cnt = job_ins_fail_cnt
        if job_ins_intercept_cnt is not None:
            self.job_ins_intercept_cnt = job_ins_intercept_cnt
        if job_ins_success_cnt is not None:
            self.job_ins_success_cnt = job_ins_success_cnt

    @property
    def job_cnt(self):
        """Gets the job_cnt of this ShowJobStatisticsResponse.

        作业数量统计

        :return: The job_cnt of this ShowJobStatisticsResponse.
        :rtype: int
        """
        return self._job_cnt

    @job_cnt.setter
    def job_cnt(self, job_cnt):
        """Sets the job_cnt of this ShowJobStatisticsResponse.

        作业数量统计

        :param job_cnt: The job_cnt of this ShowJobStatisticsResponse.
        :type job_cnt: int
        """
        self._job_cnt = job_cnt

    @property
    def job_ins_cnt(self):
        """Gets the job_ins_cnt of this ShowJobStatisticsResponse.

        作业实例次数

        :return: The job_ins_cnt of this ShowJobStatisticsResponse.
        :rtype: int
        """
        return self._job_ins_cnt

    @job_ins_cnt.setter
    def job_ins_cnt(self, job_ins_cnt):
        """Sets the job_ins_cnt of this ShowJobStatisticsResponse.

        作业实例次数

        :param job_ins_cnt: The job_ins_cnt of this ShowJobStatisticsResponse.
        :type job_ins_cnt: int
        """
        self._job_ins_cnt = job_ins_cnt

    @property
    def job_ins_fail_cnt(self):
        """Gets the job_ins_fail_cnt of this ShowJobStatisticsResponse.

        作业实例失败次数

        :return: The job_ins_fail_cnt of this ShowJobStatisticsResponse.
        :rtype: int
        """
        return self._job_ins_fail_cnt

    @job_ins_fail_cnt.setter
    def job_ins_fail_cnt(self, job_ins_fail_cnt):
        """Sets the job_ins_fail_cnt of this ShowJobStatisticsResponse.

        作业实例失败次数

        :param job_ins_fail_cnt: The job_ins_fail_cnt of this ShowJobStatisticsResponse.
        :type job_ins_fail_cnt: int
        """
        self._job_ins_fail_cnt = job_ins_fail_cnt

    @property
    def job_ins_intercept_cnt(self):
        """Gets the job_ins_intercept_cnt of this ShowJobStatisticsResponse.

        作业实例拦截次数

        :return: The job_ins_intercept_cnt of this ShowJobStatisticsResponse.
        :rtype: int
        """
        return self._job_ins_intercept_cnt

    @job_ins_intercept_cnt.setter
    def job_ins_intercept_cnt(self, job_ins_intercept_cnt):
        """Sets the job_ins_intercept_cnt of this ShowJobStatisticsResponse.

        作业实例拦截次数

        :param job_ins_intercept_cnt: The job_ins_intercept_cnt of this ShowJobStatisticsResponse.
        :type job_ins_intercept_cnt: int
        """
        self._job_ins_intercept_cnt = job_ins_intercept_cnt

    @property
    def job_ins_success_cnt(self):
        """Gets the job_ins_success_cnt of this ShowJobStatisticsResponse.

        作业实例成功次数

        :return: The job_ins_success_cnt of this ShowJobStatisticsResponse.
        :rtype: int
        """
        return self._job_ins_success_cnt

    @job_ins_success_cnt.setter
    def job_ins_success_cnt(self, job_ins_success_cnt):
        """Sets the job_ins_success_cnt of this ShowJobStatisticsResponse.

        作业实例成功次数

        :param job_ins_success_cnt: The job_ins_success_cnt of this ShowJobStatisticsResponse.
        :type job_ins_success_cnt: int
        """
        self._job_ins_success_cnt = job_ins_success_cnt

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
        if not isinstance(other, ShowJobStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
