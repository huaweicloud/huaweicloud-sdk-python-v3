# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartPromptlyDataLevelTableCompareJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'job_id': 'str',
        'compare_job_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'job_id': 'job_id',
        'compare_job_id': 'compare_job_id'
    }

    def __init__(self, x_language=None, job_id=None, compare_job_id=None):
        """StartPromptlyDataLevelTableCompareJobRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param job_id: 任务ID。
        :type job_id: str
        :param compare_job_id: 对比任务ID。
        :type compare_job_id: str
        """
        
        

        self._x_language = None
        self._job_id = None
        self._compare_job_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.job_id = job_id
        self.compare_job_id = compare_job_id

    @property
    def x_language(self):
        """Gets the x_language of this StartPromptlyDataLevelTableCompareJobRequest.

        请求语言类型。

        :return: The x_language of this StartPromptlyDataLevelTableCompareJobRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this StartPromptlyDataLevelTableCompareJobRequest.

        请求语言类型。

        :param x_language: The x_language of this StartPromptlyDataLevelTableCompareJobRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def job_id(self):
        """Gets the job_id of this StartPromptlyDataLevelTableCompareJobRequest.

        任务ID。

        :return: The job_id of this StartPromptlyDataLevelTableCompareJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StartPromptlyDataLevelTableCompareJobRequest.

        任务ID。

        :param job_id: The job_id of this StartPromptlyDataLevelTableCompareJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def compare_job_id(self):
        """Gets the compare_job_id of this StartPromptlyDataLevelTableCompareJobRequest.

        对比任务ID。

        :return: The compare_job_id of this StartPromptlyDataLevelTableCompareJobRequest.
        :rtype: str
        """
        return self._compare_job_id

    @compare_job_id.setter
    def compare_job_id(self, compare_job_id):
        """Sets the compare_job_id of this StartPromptlyDataLevelTableCompareJobRequest.

        对比任务ID。

        :param compare_job_id: The compare_job_id of this StartPromptlyDataLevelTableCompareJobRequest.
        :type compare_job_id: str
        """
        self._compare_job_id = compare_job_id

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
        if not isinstance(other, StartPromptlyDataLevelTableCompareJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
