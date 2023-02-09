# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLastHistoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'build_number': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'result': 'str',
        'commit_id': 'str'
    }

    attribute_map = {
        'record_id': 'record_id',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'build_number': 'build_number',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'result': 'result',
        'commit_id': 'commit_id'
    }

    def __init__(self, record_id=None, job_id=None, job_name=None, build_number=None, start_time=None, end_time=None, result=None, commit_id=None):
        """ShowLastHistoryResponse

        The model defined in huaweicloud sdk

        :param record_id: 构建记录id--唯一key
        :type record_id: str
        :param job_id: 构建任务ID
        :type job_id: str
        :param job_name: 构建任务名称
        :type job_name: str
        :param build_number: 构建编号
        :type build_number: int
        :param start_time: 构建开始时间
        :type start_time: str
        :param end_time: 构建结束时间
        :type end_time: str
        :param result: 构建执行结果
        :type result: str
        :param commit_id: commitId
        :type commit_id: str
        """
        
        super(ShowLastHistoryResponse, self).__init__()

        self._record_id = None
        self._job_id = None
        self._job_name = None
        self._build_number = None
        self._start_time = None
        self._end_time = None
        self._result = None
        self._commit_id = None
        self.discriminator = None

        if record_id is not None:
            self.record_id = record_id
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if build_number is not None:
            self.build_number = build_number
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if result is not None:
            self.result = result
        if commit_id is not None:
            self.commit_id = commit_id

    @property
    def record_id(self):
        """Gets the record_id of this ShowLastHistoryResponse.

        构建记录id--唯一key

        :return: The record_id of this ShowLastHistoryResponse.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this ShowLastHistoryResponse.

        构建记录id--唯一key

        :param record_id: The record_id of this ShowLastHistoryResponse.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def job_id(self):
        """Gets the job_id of this ShowLastHistoryResponse.

        构建任务ID

        :return: The job_id of this ShowLastHistoryResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowLastHistoryResponse.

        构建任务ID

        :param job_id: The job_id of this ShowLastHistoryResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this ShowLastHistoryResponse.

        构建任务名称

        :return: The job_name of this ShowLastHistoryResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowLastHistoryResponse.

        构建任务名称

        :param job_name: The job_name of this ShowLastHistoryResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def build_number(self):
        """Gets the build_number of this ShowLastHistoryResponse.

        构建编号

        :return: The build_number of this ShowLastHistoryResponse.
        :rtype: int
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this ShowLastHistoryResponse.

        构建编号

        :param build_number: The build_number of this ShowLastHistoryResponse.
        :type build_number: int
        """
        self._build_number = build_number

    @property
    def start_time(self):
        """Gets the start_time of this ShowLastHistoryResponse.

        构建开始时间

        :return: The start_time of this ShowLastHistoryResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowLastHistoryResponse.

        构建开始时间

        :param start_time: The start_time of this ShowLastHistoryResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowLastHistoryResponse.

        构建结束时间

        :return: The end_time of this ShowLastHistoryResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowLastHistoryResponse.

        构建结束时间

        :param end_time: The end_time of this ShowLastHistoryResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def result(self):
        """Gets the result of this ShowLastHistoryResponse.

        构建执行结果

        :return: The result of this ShowLastHistoryResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ShowLastHistoryResponse.

        构建执行结果

        :param result: The result of this ShowLastHistoryResponse.
        :type result: str
        """
        self._result = result

    @property
    def commit_id(self):
        """Gets the commit_id of this ShowLastHistoryResponse.

        commitId

        :return: The commit_id of this ShowLastHistoryResponse.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this ShowLastHistoryResponse.

        commitId

        :param commit_id: The commit_id of this ShowLastHistoryResponse.
        :type commit_id: str
        """
        self._commit_id = commit_id

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
        if not isinstance(other, ShowLastHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
