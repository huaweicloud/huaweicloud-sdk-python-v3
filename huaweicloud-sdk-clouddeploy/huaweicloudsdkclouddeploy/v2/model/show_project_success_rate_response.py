# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProjectSuccessRateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'success_rate': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'task_count': 'int',
        'record_count': 'int',
        'success_record_count': 'int'
    }

    attribute_map = {
        'success_rate': 'success_rate',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'task_count': 'task_count',
        'record_count': 'record_count',
        'success_record_count': 'success_record_count'
    }

    def __init__(self, success_rate=None, project_id=None, project_name=None, start_date=None, end_date=None, task_count=None, record_count=None, success_record_count=None):
        """ShowProjectSuccessRateResponse

        The model defined in huaweicloud sdk

        :param success_rate: 成功率
        :type success_rate: str
        :param project_id: 项目id
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param start_date: 任务执行开始时间范围的左边界（包含），格式yyyy-MM-dd
        :type start_date: str
        :param end_date: 任务执行开始时间范围的右边界（包含），格式yyyy-MM-dd
        :type end_date: str
        :param task_count: 查询到的任务数
        :type task_count: int
        :param record_count: 查询到的任务执行记录数
        :type record_count: int
        :param success_record_count: 成功的任务执行记录数
        :type success_record_count: int
        """
        
        super(ShowProjectSuccessRateResponse, self).__init__()

        self._success_rate = None
        self._project_id = None
        self._project_name = None
        self._start_date = None
        self._end_date = None
        self._task_count = None
        self._record_count = None
        self._success_record_count = None
        self.discriminator = None

        if success_rate is not None:
            self.success_rate = success_rate
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if task_count is not None:
            self.task_count = task_count
        if record_count is not None:
            self.record_count = record_count
        if success_record_count is not None:
            self.success_record_count = success_record_count

    @property
    def success_rate(self):
        """Gets the success_rate of this ShowProjectSuccessRateResponse.

        成功率

        :return: The success_rate of this ShowProjectSuccessRateResponse.
        :rtype: str
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this ShowProjectSuccessRateResponse.

        成功率

        :param success_rate: The success_rate of this ShowProjectSuccessRateResponse.
        :type success_rate: str
        """
        self._success_rate = success_rate

    @property
    def project_id(self):
        """Gets the project_id of this ShowProjectSuccessRateResponse.

        项目id

        :return: The project_id of this ShowProjectSuccessRateResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowProjectSuccessRateResponse.

        项目id

        :param project_id: The project_id of this ShowProjectSuccessRateResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ShowProjectSuccessRateResponse.

        项目名称

        :return: The project_name of this ShowProjectSuccessRateResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ShowProjectSuccessRateResponse.

        项目名称

        :param project_name: The project_name of this ShowProjectSuccessRateResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def start_date(self):
        """Gets the start_date of this ShowProjectSuccessRateResponse.

        任务执行开始时间范围的左边界（包含），格式yyyy-MM-dd

        :return: The start_date of this ShowProjectSuccessRateResponse.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ShowProjectSuccessRateResponse.

        任务执行开始时间范围的左边界（包含），格式yyyy-MM-dd

        :param start_date: The start_date of this ShowProjectSuccessRateResponse.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ShowProjectSuccessRateResponse.

        任务执行开始时间范围的右边界（包含），格式yyyy-MM-dd

        :return: The end_date of this ShowProjectSuccessRateResponse.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ShowProjectSuccessRateResponse.

        任务执行开始时间范围的右边界（包含），格式yyyy-MM-dd

        :param end_date: The end_date of this ShowProjectSuccessRateResponse.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def task_count(self):
        """Gets the task_count of this ShowProjectSuccessRateResponse.

        查询到的任务数

        :return: The task_count of this ShowProjectSuccessRateResponse.
        :rtype: int
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        """Sets the task_count of this ShowProjectSuccessRateResponse.

        查询到的任务数

        :param task_count: The task_count of this ShowProjectSuccessRateResponse.
        :type task_count: int
        """
        self._task_count = task_count

    @property
    def record_count(self):
        """Gets the record_count of this ShowProjectSuccessRateResponse.

        查询到的任务执行记录数

        :return: The record_count of this ShowProjectSuccessRateResponse.
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this ShowProjectSuccessRateResponse.

        查询到的任务执行记录数

        :param record_count: The record_count of this ShowProjectSuccessRateResponse.
        :type record_count: int
        """
        self._record_count = record_count

    @property
    def success_record_count(self):
        """Gets the success_record_count of this ShowProjectSuccessRateResponse.

        成功的任务执行记录数

        :return: The success_record_count of this ShowProjectSuccessRateResponse.
        :rtype: int
        """
        return self._success_record_count

    @success_record_count.setter
    def success_record_count(self, success_record_count):
        """Sets the success_record_count of this ShowProjectSuccessRateResponse.

        成功的任务执行记录数

        :param success_record_count: The success_record_count of this ShowProjectSuccessRateResponse.
        :type success_record_count: int
        """
        self._success_record_count = success_record_count

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
        if not isinstance(other, ShowProjectSuccessRateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
