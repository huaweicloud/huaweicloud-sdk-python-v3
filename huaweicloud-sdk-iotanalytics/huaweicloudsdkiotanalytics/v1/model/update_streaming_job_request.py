# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStreamingJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check': 'bool',
        'job_id': 'str',
        'body': 'dict(str, object)'
    }

    attribute_map = {
        'check': 'check',
        'job_id': 'job_id',
        'body': 'body'
    }

    def __init__(self, check=None, job_id=None, body=None):
        r"""UpdateStreamingJobRequest

        The model defined in huaweicloud sdk

        :param check: 是否需要校验配置是否正确
        :type check: bool
        :param job_id: 作业ID
        :type job_id: str
        :param body: 实时分析作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：实时分析算子配置指南。
        :type body: dict(str, object)
        """
        
        

        self._check = None
        self._job_id = None
        self._body = None
        self.discriminator = None

        if check is not None:
            self.check = check
        self.job_id = job_id
        if body is not None:
            self.body = body

    @property
    def check(self):
        r"""Gets the check of this UpdateStreamingJobRequest.

        是否需要校验配置是否正确

        :return: The check of this UpdateStreamingJobRequest.
        :rtype: bool
        """
        return self._check

    @check.setter
    def check(self, check):
        r"""Sets the check of this UpdateStreamingJobRequest.

        是否需要校验配置是否正确

        :param check: The check of this UpdateStreamingJobRequest.
        :type check: bool
        """
        self._check = check

    @property
    def job_id(self):
        r"""Gets the job_id of this UpdateStreamingJobRequest.

        作业ID

        :return: The job_id of this UpdateStreamingJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this UpdateStreamingJobRequest.

        作业ID

        :param job_id: The job_id of this UpdateStreamingJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def body(self):
        r"""Gets the body of this UpdateStreamingJobRequest.

        实时分析作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：实时分析算子配置指南。

        :return: The body of this UpdateStreamingJobRequest.
        :rtype: dict(str, object)
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateStreamingJobRequest.

        实时分析作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：实时分析算子配置指南。

        :param body: The body of this UpdateStreamingJobRequest.
        :type body: dict(str, object)
        """
        self._body = body

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
        if not isinstance(other, UpdateStreamingJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
