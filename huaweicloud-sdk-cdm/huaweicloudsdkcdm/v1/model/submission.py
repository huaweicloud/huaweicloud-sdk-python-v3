# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Submission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_incrementing': 'bool',
        'job_name': 'str',
        'counters': 'Counters',
        'is_stoping_increment': 'str',
        'is_execute_auto': 'bool',
        'last_update_date': 'int',
        'last_udpate_user': 'str',
        'is_delete_job': 'bool',
        'creation_user': 'str',
        'creation_date': 'int',
        'external_id': 'str',
        'progress': 'float',
        'submission_id': 'int',
        'delete_rows': 'int',
        'update_rows': 'int',
        'write_rows': 'int',
        'execute_date': 'int',
        'status': 'str',
        'error_details': 'str',
        'error_summary': 'str'
    }

    attribute_map = {
        'is_incrementing': 'isIncrementing',
        'job_name': 'job-name',
        'counters': 'counters',
        'is_stoping_increment': 'isStopingIncrement',
        'is_execute_auto': 'is-execute-auto',
        'last_update_date': 'last-update-date',
        'last_udpate_user': 'last-udpate-user',
        'is_delete_job': 'isDeleteJob',
        'creation_user': 'creation-user',
        'creation_date': 'creation-date',
        'external_id': 'external-id',
        'progress': 'progress',
        'submission_id': 'submission-id',
        'delete_rows': 'delete_rows',
        'update_rows': 'update_rows',
        'write_rows': 'write_rows',
        'execute_date': 'execute-date',
        'status': 'status',
        'error_details': 'error-details',
        'error_summary': 'error-summary'
    }

    def __init__(self, is_incrementing=None, job_name=None, counters=None, is_stoping_increment=None, is_execute_auto=None, last_update_date=None, last_udpate_user=None, is_delete_job=None, creation_user=None, creation_date=None, external_id=None, progress=None, submission_id=None, delete_rows=None, update_rows=None, write_rows=None, execute_date=None, status=None, error_details=None, error_summary=None):
        """Submission

        The model defined in huaweicloud sdk

        :param is_incrementing: 作业是否为增量迁移
        :type is_incrementing: bool
        :param job_name: 作业名称
        :type job_name: str
        :param counters: 
        :type counters: :class:`huaweicloudsdkcdm.v1.Counters`
        :param is_stoping_increment: 是否停止增量迁移
        :type is_stoping_increment: str
        :param is_execute_auto: 是否定时执行作业
        :type is_execute_auto: bool
        :param last_update_date: 作业最后更新时间
        :type last_update_date: int
        :param last_udpate_user: 最后更新作业状态的用户
        :type last_udpate_user: str
        :param is_delete_job: 作业执行完成后是否删除
        :type is_delete_job: bool
        :param creation_user: 创建用户
        :type creation_user: str
        :param creation_date: 创建时间
        :type creation_date: int
        :param external_id: 作业ID
        :type external_id: str
        :param progress: 作业进度，失败时为“-1”，其它情况为0～100
        :type progress: float
        :param submission_id: 作业提交id
        :type submission_id: int
        :param delete_rows: 删除数据行数
        :type delete_rows: int
        :param update_rows: 更新数据行数
        :type update_rows: int
        :param write_rows: 写入数据行数
        :type write_rows: int
        :param execute_date: 执行时间
        :type execute_date: int
        :param status: 作业状态： - BOOTING：启动中。 - FAILURE_ON_SUBMIT：提交失败。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - UNKNOWN：未知。 - NEVER_EXECUTED：未被执行
        :type status: str
        :param error_details: 错误详情，当“status”为“FAILED”时才有此字段。
        :type error_details: str
        :param error_summary: 错误总结，当“status”为“FAILED”时才有此字段。
        :type error_summary: str
        """
        
        

        self._is_incrementing = None
        self._job_name = None
        self._counters = None
        self._is_stoping_increment = None
        self._is_execute_auto = None
        self._last_update_date = None
        self._last_udpate_user = None
        self._is_delete_job = None
        self._creation_user = None
        self._creation_date = None
        self._external_id = None
        self._progress = None
        self._submission_id = None
        self._delete_rows = None
        self._update_rows = None
        self._write_rows = None
        self._execute_date = None
        self._status = None
        self._error_details = None
        self._error_summary = None
        self.discriminator = None

        self.is_incrementing = is_incrementing
        self.job_name = job_name
        if counters is not None:
            self.counters = counters
        self.is_stoping_increment = is_stoping_increment
        self.is_execute_auto = is_execute_auto
        self.last_update_date = last_update_date
        self.last_udpate_user = last_udpate_user
        self.is_delete_job = is_delete_job
        self.creation_user = creation_user
        self.creation_date = creation_date
        self.external_id = external_id
        self.progress = progress
        if submission_id is not None:
            self.submission_id = submission_id
        if delete_rows is not None:
            self.delete_rows = delete_rows
        if update_rows is not None:
            self.update_rows = update_rows
        if write_rows is not None:
            self.write_rows = write_rows
        if execute_date is not None:
            self.execute_date = execute_date
        self.status = status
        if error_details is not None:
            self.error_details = error_details
        if error_summary is not None:
            self.error_summary = error_summary

    @property
    def is_incrementing(self):
        """Gets the is_incrementing of this Submission.

        作业是否为增量迁移

        :return: The is_incrementing of this Submission.
        :rtype: bool
        """
        return self._is_incrementing

    @is_incrementing.setter
    def is_incrementing(self, is_incrementing):
        """Sets the is_incrementing of this Submission.

        作业是否为增量迁移

        :param is_incrementing: The is_incrementing of this Submission.
        :type is_incrementing: bool
        """
        self._is_incrementing = is_incrementing

    @property
    def job_name(self):
        """Gets the job_name of this Submission.

        作业名称

        :return: The job_name of this Submission.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this Submission.

        作业名称

        :param job_name: The job_name of this Submission.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def counters(self):
        """Gets the counters of this Submission.

        :return: The counters of this Submission.
        :rtype: :class:`huaweicloudsdkcdm.v1.Counters`
        """
        return self._counters

    @counters.setter
    def counters(self, counters):
        """Sets the counters of this Submission.

        :param counters: The counters of this Submission.
        :type counters: :class:`huaweicloudsdkcdm.v1.Counters`
        """
        self._counters = counters

    @property
    def is_stoping_increment(self):
        """Gets the is_stoping_increment of this Submission.

        是否停止增量迁移

        :return: The is_stoping_increment of this Submission.
        :rtype: str
        """
        return self._is_stoping_increment

    @is_stoping_increment.setter
    def is_stoping_increment(self, is_stoping_increment):
        """Sets the is_stoping_increment of this Submission.

        是否停止增量迁移

        :param is_stoping_increment: The is_stoping_increment of this Submission.
        :type is_stoping_increment: str
        """
        self._is_stoping_increment = is_stoping_increment

    @property
    def is_execute_auto(self):
        """Gets the is_execute_auto of this Submission.

        是否定时执行作业

        :return: The is_execute_auto of this Submission.
        :rtype: bool
        """
        return self._is_execute_auto

    @is_execute_auto.setter
    def is_execute_auto(self, is_execute_auto):
        """Sets the is_execute_auto of this Submission.

        是否定时执行作业

        :param is_execute_auto: The is_execute_auto of this Submission.
        :type is_execute_auto: bool
        """
        self._is_execute_auto = is_execute_auto

    @property
    def last_update_date(self):
        """Gets the last_update_date of this Submission.

        作业最后更新时间

        :return: The last_update_date of this Submission.
        :rtype: int
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this Submission.

        作业最后更新时间

        :param last_update_date: The last_update_date of this Submission.
        :type last_update_date: int
        """
        self._last_update_date = last_update_date

    @property
    def last_udpate_user(self):
        """Gets the last_udpate_user of this Submission.

        最后更新作业状态的用户

        :return: The last_udpate_user of this Submission.
        :rtype: str
        """
        return self._last_udpate_user

    @last_udpate_user.setter
    def last_udpate_user(self, last_udpate_user):
        """Sets the last_udpate_user of this Submission.

        最后更新作业状态的用户

        :param last_udpate_user: The last_udpate_user of this Submission.
        :type last_udpate_user: str
        """
        self._last_udpate_user = last_udpate_user

    @property
    def is_delete_job(self):
        """Gets the is_delete_job of this Submission.

        作业执行完成后是否删除

        :return: The is_delete_job of this Submission.
        :rtype: bool
        """
        return self._is_delete_job

    @is_delete_job.setter
    def is_delete_job(self, is_delete_job):
        """Sets the is_delete_job of this Submission.

        作业执行完成后是否删除

        :param is_delete_job: The is_delete_job of this Submission.
        :type is_delete_job: bool
        """
        self._is_delete_job = is_delete_job

    @property
    def creation_user(self):
        """Gets the creation_user of this Submission.

        创建用户

        :return: The creation_user of this Submission.
        :rtype: str
        """
        return self._creation_user

    @creation_user.setter
    def creation_user(self, creation_user):
        """Sets the creation_user of this Submission.

        创建用户

        :param creation_user: The creation_user of this Submission.
        :type creation_user: str
        """
        self._creation_user = creation_user

    @property
    def creation_date(self):
        """Gets the creation_date of this Submission.

        创建时间

        :return: The creation_date of this Submission.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Submission.

        创建时间

        :param creation_date: The creation_date of this Submission.
        :type creation_date: int
        """
        self._creation_date = creation_date

    @property
    def external_id(self):
        """Gets the external_id of this Submission.

        作业ID

        :return: The external_id of this Submission.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Submission.

        作业ID

        :param external_id: The external_id of this Submission.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def progress(self):
        """Gets the progress of this Submission.

        作业进度，失败时为“-1”，其它情况为0～100

        :return: The progress of this Submission.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Submission.

        作业进度，失败时为“-1”，其它情况为0～100

        :param progress: The progress of this Submission.
        :type progress: float
        """
        self._progress = progress

    @property
    def submission_id(self):
        """Gets the submission_id of this Submission.

        作业提交id

        :return: The submission_id of this Submission.
        :rtype: int
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id):
        """Sets the submission_id of this Submission.

        作业提交id

        :param submission_id: The submission_id of this Submission.
        :type submission_id: int
        """
        self._submission_id = submission_id

    @property
    def delete_rows(self):
        """Gets the delete_rows of this Submission.

        删除数据行数

        :return: The delete_rows of this Submission.
        :rtype: int
        """
        return self._delete_rows

    @delete_rows.setter
    def delete_rows(self, delete_rows):
        """Sets the delete_rows of this Submission.

        删除数据行数

        :param delete_rows: The delete_rows of this Submission.
        :type delete_rows: int
        """
        self._delete_rows = delete_rows

    @property
    def update_rows(self):
        """Gets the update_rows of this Submission.

        更新数据行数

        :return: The update_rows of this Submission.
        :rtype: int
        """
        return self._update_rows

    @update_rows.setter
    def update_rows(self, update_rows):
        """Sets the update_rows of this Submission.

        更新数据行数

        :param update_rows: The update_rows of this Submission.
        :type update_rows: int
        """
        self._update_rows = update_rows

    @property
    def write_rows(self):
        """Gets the write_rows of this Submission.

        写入数据行数

        :return: The write_rows of this Submission.
        :rtype: int
        """
        return self._write_rows

    @write_rows.setter
    def write_rows(self, write_rows):
        """Sets the write_rows of this Submission.

        写入数据行数

        :param write_rows: The write_rows of this Submission.
        :type write_rows: int
        """
        self._write_rows = write_rows

    @property
    def execute_date(self):
        """Gets the execute_date of this Submission.

        执行时间

        :return: The execute_date of this Submission.
        :rtype: int
        """
        return self._execute_date

    @execute_date.setter
    def execute_date(self, execute_date):
        """Sets the execute_date of this Submission.

        执行时间

        :param execute_date: The execute_date of this Submission.
        :type execute_date: int
        """
        self._execute_date = execute_date

    @property
    def status(self):
        """Gets the status of this Submission.

        作业状态： - BOOTING：启动中。 - FAILURE_ON_SUBMIT：提交失败。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - UNKNOWN：未知。 - NEVER_EXECUTED：未被执行

        :return: The status of this Submission.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Submission.

        作业状态： - BOOTING：启动中。 - FAILURE_ON_SUBMIT：提交失败。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - UNKNOWN：未知。 - NEVER_EXECUTED：未被执行

        :param status: The status of this Submission.
        :type status: str
        """
        self._status = status

    @property
    def error_details(self):
        """Gets the error_details of this Submission.

        错误详情，当“status”为“FAILED”时才有此字段。

        :return: The error_details of this Submission.
        :rtype: str
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this Submission.

        错误详情，当“status”为“FAILED”时才有此字段。

        :param error_details: The error_details of this Submission.
        :type error_details: str
        """
        self._error_details = error_details

    @property
    def error_summary(self):
        """Gets the error_summary of this Submission.

        错误总结，当“status”为“FAILED”时才有此字段。

        :return: The error_summary of this Submission.
        :rtype: str
        """
        return self._error_summary

    @error_summary.setter
    def error_summary(self, error_summary):
        """Sets the error_summary of this Submission.

        错误总结，当“status”为“FAILED”时才有此字段。

        :param error_summary: The error_summary of this Submission.
        :type error_summary: str
        """
        self._error_summary = error_summary

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
        if not isinstance(other, Submission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
