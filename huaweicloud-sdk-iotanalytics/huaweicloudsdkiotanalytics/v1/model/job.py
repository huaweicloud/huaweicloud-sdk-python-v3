# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

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
        'job_name': 'str',
        'tags': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'job_type': 'str',
        'export_path': 'str',
        'merge_result_file': 'bool',
        'sql_job': 'SqlJob',
        'schedule': 'Schedule'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'tags': 'tags',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'job_type': 'job_type',
        'export_path': 'export_path',
        'merge_result_file': 'merge_result_file',
        'sql_job': 'sql_job',
        'schedule': 'schedule'
    }

    def __init__(self, job_id=None, job_name=None, tags=None, created_time=None, modified_time=None, job_type=None, export_path=None, merge_result_file=None, sql_job=None, schedule=None):
        """Job

        The model defined in huaweicloud sdk

        :param job_id: 仅在响应返回。作业ID。
        :type job_id: str
        :param job_name: 作业名称。只能包含数字、英文字母、中文字母、下划线以及中划线。长度为1~128。
        :type job_name: str
        :param tags: 标签。只能包含数字、英文字母、中文字符、下划线、中划线、逗号以及斜杠。长度为0~128。
        :type tags: str
        :param created_time: 仅在响应返回。创建时间。
        :type created_time: str
        :param modified_time: 仅在响应返回。更新时间。
        :type modified_time: str
        :param job_type: 作业类型。目前仅支持SqlJob.
        :type job_type: str
        :param export_path: 作业查询结果导出到OBS的路径。覆写已存在文件。
        :type export_path: str
        :param merge_result_file: 导出文件时是否合并结果文件。true：合并成一个结果文件；false：不合并结果文件。
        :type merge_result_file: bool
        :param sql_job: 
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJob`
        :param schedule: 
        :type schedule: :class:`huaweicloudsdkiotanalytics.v1.Schedule`
        """
        
        

        self._job_id = None
        self._job_name = None
        self._tags = None
        self._created_time = None
        self._modified_time = None
        self._job_type = None
        self._export_path = None
        self._merge_result_file = None
        self._sql_job = None
        self._schedule = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        self.job_name = job_name
        if tags is not None:
            self.tags = tags
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        self.job_type = job_type
        if export_path is not None:
            self.export_path = export_path
        if merge_result_file is not None:
            self.merge_result_file = merge_result_file
        if sql_job is not None:
            self.sql_job = sql_job
        if schedule is not None:
            self.schedule = schedule

    @property
    def job_id(self):
        """Gets the job_id of this Job.

        仅在响应返回。作业ID。

        :return: The job_id of this Job.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Job.

        仅在响应返回。作业ID。

        :param job_id: The job_id of this Job.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this Job.

        作业名称。只能包含数字、英文字母、中文字母、下划线以及中划线。长度为1~128。

        :return: The job_name of this Job.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this Job.

        作业名称。只能包含数字、英文字母、中文字母、下划线以及中划线。长度为1~128。

        :param job_name: The job_name of this Job.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def tags(self):
        """Gets the tags of this Job.

        标签。只能包含数字、英文字母、中文字符、下划线、中划线、逗号以及斜杠。长度为0~128。

        :return: The tags of this Job.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Job.

        标签。只能包含数字、英文字母、中文字符、下划线、中划线、逗号以及斜杠。长度为0~128。

        :param tags: The tags of this Job.
        :type tags: str
        """
        self._tags = tags

    @property
    def created_time(self):
        """Gets the created_time of this Job.

        仅在响应返回。创建时间。

        :return: The created_time of this Job.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Job.

        仅在响应返回。创建时间。

        :param created_time: The created_time of this Job.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this Job.

        仅在响应返回。更新时间。

        :return: The modified_time of this Job.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this Job.

        仅在响应返回。更新时间。

        :param modified_time: The modified_time of this Job.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def job_type(self):
        """Gets the job_type of this Job.

        作业类型。目前仅支持SqlJob.

        :return: The job_type of this Job.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this Job.

        作业类型。目前仅支持SqlJob.

        :param job_type: The job_type of this Job.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def export_path(self):
        """Gets the export_path of this Job.

        作业查询结果导出到OBS的路径。覆写已存在文件。

        :return: The export_path of this Job.
        :rtype: str
        """
        return self._export_path

    @export_path.setter
    def export_path(self, export_path):
        """Sets the export_path of this Job.

        作业查询结果导出到OBS的路径。覆写已存在文件。

        :param export_path: The export_path of this Job.
        :type export_path: str
        """
        self._export_path = export_path

    @property
    def merge_result_file(self):
        """Gets the merge_result_file of this Job.

        导出文件时是否合并结果文件。true：合并成一个结果文件；false：不合并结果文件。

        :return: The merge_result_file of this Job.
        :rtype: bool
        """
        return self._merge_result_file

    @merge_result_file.setter
    def merge_result_file(self, merge_result_file):
        """Sets the merge_result_file of this Job.

        导出文件时是否合并结果文件。true：合并成一个结果文件；false：不合并结果文件。

        :param merge_result_file: The merge_result_file of this Job.
        :type merge_result_file: bool
        """
        self._merge_result_file = merge_result_file

    @property
    def sql_job(self):
        """Gets the sql_job of this Job.

        :return: The sql_job of this Job.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.SqlJob`
        """
        return self._sql_job

    @sql_job.setter
    def sql_job(self, sql_job):
        """Sets the sql_job of this Job.

        :param sql_job: The sql_job of this Job.
        :type sql_job: :class:`huaweicloudsdkiotanalytics.v1.SqlJob`
        """
        self._sql_job = sql_job

    @property
    def schedule(self):
        """Gets the schedule of this Job.

        :return: The schedule of this Job.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.Schedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Job.

        :param schedule: The schedule of this Job.
        :type schedule: :class:`huaweicloudsdkiotanalytics.v1.Schedule`
        """
        self._schedule = schedule

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
