# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartJobSubmission:


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
        'delete_rows': 'int',
        'update_rows': 'int',
        'write_rows': 'int',
        'submission_id': 'int',
        'job_name': 'str',
        'creation_user': 'str',
        'creation_date': 'int',
        'progress': 'int',
        'status': 'str',
        'is_stoping_increment': 'bool',
        'is_execute_auto': 'bool',
        'last_update_date': 'int',
        'last_udpate_user': 'str',
        'is_delete_job': 'bool'
    }

    attribute_map = {
        'is_incrementing': 'isIncrementing',
        'delete_rows': 'delete_rows',
        'update_rows': 'update_rows',
        'write_rows': 'write_rows',
        'submission_id': 'submission-id',
        'job_name': 'job-name',
        'creation_user': 'creation-user',
        'creation_date': 'creation-date',
        'progress': 'progress',
        'status': 'status',
        'is_stoping_increment': 'isStopingIncrement',
        'is_execute_auto': 'is-execute-auto',
        'last_update_date': 'last-update-date',
        'last_udpate_user': 'last-udpate-user',
        'is_delete_job': 'isDeleteJob'
    }

    def __init__(self, is_incrementing=None, delete_rows=None, update_rows=None, write_rows=None, submission_id=None, job_name=None, creation_user=None, creation_date=None, progress=None, status=None, is_stoping_increment=None, is_execute_auto=None, last_update_date=None, last_udpate_user=None, is_delete_job=None):
        """StartJobSubmission - a model defined in huaweicloud sdk"""
        
        

        self._is_incrementing = None
        self._delete_rows = None
        self._update_rows = None
        self._write_rows = None
        self._submission_id = None
        self._job_name = None
        self._creation_user = None
        self._creation_date = None
        self._progress = None
        self._status = None
        self._is_stoping_increment = None
        self._is_execute_auto = None
        self._last_update_date = None
        self._last_udpate_user = None
        self._is_delete_job = None
        self.discriminator = None

        if is_incrementing is not None:
            self.is_incrementing = is_incrementing
        if delete_rows is not None:
            self.delete_rows = delete_rows
        if update_rows is not None:
            self.update_rows = update_rows
        if write_rows is not None:
            self.write_rows = write_rows
        if submission_id is not None:
            self.submission_id = submission_id
        self.job_name = job_name
        self.creation_user = creation_user
        self.creation_date = creation_date
        self.progress = progress
        self.status = status
        if is_stoping_increment is not None:
            self.is_stoping_increment = is_stoping_increment
        if is_execute_auto is not None:
            self.is_execute_auto = is_execute_auto
        if last_update_date is not None:
            self.last_update_date = last_update_date
        if last_udpate_user is not None:
            self.last_udpate_user = last_udpate_user
        if is_delete_job is not None:
            self.is_delete_job = is_delete_job

    @property
    def is_incrementing(self):
        """Gets the is_incrementing of this StartJobSubmission.

        作业是否为增量迁移

        :return: The is_incrementing of this StartJobSubmission.
        :rtype: bool
        """
        return self._is_incrementing

    @is_incrementing.setter
    def is_incrementing(self, is_incrementing):
        """Sets the is_incrementing of this StartJobSubmission.

        作业是否为增量迁移

        :param is_incrementing: The is_incrementing of this StartJobSubmission.
        :type: bool
        """
        self._is_incrementing = is_incrementing

    @property
    def delete_rows(self):
        """Gets the delete_rows of this StartJobSubmission.

        删除数据行数

        :return: The delete_rows of this StartJobSubmission.
        :rtype: int
        """
        return self._delete_rows

    @delete_rows.setter
    def delete_rows(self, delete_rows):
        """Sets the delete_rows of this StartJobSubmission.

        删除数据行数

        :param delete_rows: The delete_rows of this StartJobSubmission.
        :type: int
        """
        self._delete_rows = delete_rows

    @property
    def update_rows(self):
        """Gets the update_rows of this StartJobSubmission.

        更新数据行数

        :return: The update_rows of this StartJobSubmission.
        :rtype: int
        """
        return self._update_rows

    @update_rows.setter
    def update_rows(self, update_rows):
        """Sets the update_rows of this StartJobSubmission.

        更新数据行数

        :param update_rows: The update_rows of this StartJobSubmission.
        :type: int
        """
        self._update_rows = update_rows

    @property
    def write_rows(self):
        """Gets the write_rows of this StartJobSubmission.

        写入数据行数

        :return: The write_rows of this StartJobSubmission.
        :rtype: int
        """
        return self._write_rows

    @write_rows.setter
    def write_rows(self, write_rows):
        """Sets the write_rows of this StartJobSubmission.

        写入数据行数

        :param write_rows: The write_rows of this StartJobSubmission.
        :type: int
        """
        self._write_rows = write_rows

    @property
    def submission_id(self):
        """Gets the submission_id of this StartJobSubmission.

        作业提交id

        :return: The submission_id of this StartJobSubmission.
        :rtype: int
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id):
        """Sets the submission_id of this StartJobSubmission.

        作业提交id

        :param submission_id: The submission_id of this StartJobSubmission.
        :type: int
        """
        self._submission_id = submission_id

    @property
    def job_name(self):
        """Gets the job_name of this StartJobSubmission.

        作业名称

        :return: The job_name of this StartJobSubmission.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this StartJobSubmission.

        作业名称

        :param job_name: The job_name of this StartJobSubmission.
        :type: str
        """
        self._job_name = job_name

    @property
    def creation_user(self):
        """Gets the creation_user of this StartJobSubmission.

        创建用户

        :return: The creation_user of this StartJobSubmission.
        :rtype: str
        """
        return self._creation_user

    @creation_user.setter
    def creation_user(self, creation_user):
        """Sets the creation_user of this StartJobSubmission.

        创建用户

        :param creation_user: The creation_user of this StartJobSubmission.
        :type: str
        """
        self._creation_user = creation_user

    @property
    def creation_date(self):
        """Gets the creation_date of this StartJobSubmission.

        创建时间，单位：毫秒。

        :return: The creation_date of this StartJobSubmission.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this StartJobSubmission.

        创建时间，单位：毫秒。

        :param creation_date: The creation_date of this StartJobSubmission.
        :type: int
        """
        self._creation_date = creation_date

    @property
    def progress(self):
        """Gets the progress of this StartJobSubmission.

        作业进度，失败时为“-1”，其它情况为0～100

        :return: The progress of this StartJobSubmission.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this StartJobSubmission.

        作业进度，失败时为“-1”，其它情况为0～100

        :param progress: The progress of this StartJobSubmission.
        :type: int
        """
        self._progress = progress

    @property
    def status(self):
        """Gets the status of this StartJobSubmission.

        作业状态： - BOOTING：启动中。 - FAILURE_ON_SUBMIT：提交失败。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - UNKNOWN：未知。 - NEVER_EXECUTED：未被执行

        :return: The status of this StartJobSubmission.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StartJobSubmission.

        作业状态： - BOOTING：启动中。 - FAILURE_ON_SUBMIT：提交失败。 - RUNNING：运行中。 - SUCCEEDED：成功。 - FAILED：失败。 - UNKNOWN：未知。 - NEVER_EXECUTED：未被执行

        :param status: The status of this StartJobSubmission.
        :type: str
        """
        self._status = status

    @property
    def is_stoping_increment(self):
        """Gets the is_stoping_increment of this StartJobSubmission.

        是否停止增量迁移

        :return: The is_stoping_increment of this StartJobSubmission.
        :rtype: bool
        """
        return self._is_stoping_increment

    @is_stoping_increment.setter
    def is_stoping_increment(self, is_stoping_increment):
        """Sets the is_stoping_increment of this StartJobSubmission.

        是否停止增量迁移

        :param is_stoping_increment: The is_stoping_increment of this StartJobSubmission.
        :type: bool
        """
        self._is_stoping_increment = is_stoping_increment

    @property
    def is_execute_auto(self):
        """Gets the is_execute_auto of this StartJobSubmission.

        是否定时执行作业

        :return: The is_execute_auto of this StartJobSubmission.
        :rtype: bool
        """
        return self._is_execute_auto

    @is_execute_auto.setter
    def is_execute_auto(self, is_execute_auto):
        """Sets the is_execute_auto of this StartJobSubmission.

        是否定时执行作业

        :param is_execute_auto: The is_execute_auto of this StartJobSubmission.
        :type: bool
        """
        self._is_execute_auto = is_execute_auto

    @property
    def last_update_date(self):
        """Gets the last_update_date of this StartJobSubmission.

        作业最后更新时间

        :return: The last_update_date of this StartJobSubmission.
        :rtype: int
        """
        return self._last_update_date

    @last_update_date.setter
    def last_update_date(self, last_update_date):
        """Sets the last_update_date of this StartJobSubmission.

        作业最后更新时间

        :param last_update_date: The last_update_date of this StartJobSubmission.
        :type: int
        """
        self._last_update_date = last_update_date

    @property
    def last_udpate_user(self):
        """Gets the last_udpate_user of this StartJobSubmission.

        最后更新作业状态的用户

        :return: The last_udpate_user of this StartJobSubmission.
        :rtype: str
        """
        return self._last_udpate_user

    @last_udpate_user.setter
    def last_udpate_user(self, last_udpate_user):
        """Sets the last_udpate_user of this StartJobSubmission.

        最后更新作业状态的用户

        :param last_udpate_user: The last_udpate_user of this StartJobSubmission.
        :type: str
        """
        self._last_udpate_user = last_udpate_user

    @property
    def is_delete_job(self):
        """Gets the is_delete_job of this StartJobSubmission.

        作业执行完成后是否删除

        :return: The is_delete_job of this StartJobSubmission.
        :rtype: bool
        """
        return self._is_delete_job

    @is_delete_job.setter
    def is_delete_job(self, is_delete_job):
        """Sets the is_delete_job of this StartJobSubmission.

        作业执行完成后是否删除

        :param is_delete_job: The is_delete_job of this StartJobSubmission.
        :type: bool
        """
        self._is_delete_job = is_delete_job

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
        if not isinstance(other, StartJobSubmission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
