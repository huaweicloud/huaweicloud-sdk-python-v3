# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'submission_time': 'str',
        'completion_time': 'str',
        'stage_ids': 'list[int]',
        'job_group': 'str',
        'status': 'str',
        'num_tasks': 'int',
        'num_active_tasks': 'int',
        'num_completed_tasks': 'int',
        'num_skipped_tasks': 'int',
        'num_failed_tasks': 'int',
        'num_killed_tasks': 'int',
        'num_completed_indices': 'int',
        'num_active_stages': 'int',
        'num_completed_stages': 'int',
        'num_skipped_stages': 'int',
        'num_failed_stages': 'int',
        'killed_tasks_summary': 'dict(str, int)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'submission_time': 'submission_time',
        'completion_time': 'completion_time',
        'stage_ids': 'stage_ids',
        'job_group': 'job_group',
        'status': 'status',
        'num_tasks': 'num_tasks',
        'num_active_tasks': 'num_active_tasks',
        'num_completed_tasks': 'num_completed_tasks',
        'num_skipped_tasks': 'num_skipped_tasks',
        'num_failed_tasks': 'num_failed_tasks',
        'num_killed_tasks': 'num_killed_tasks',
        'num_completed_indices': 'num_completed_indices',
        'num_active_stages': 'num_active_stages',
        'num_completed_stages': 'num_completed_stages',
        'num_skipped_stages': 'num_skipped_stages',
        'num_failed_stages': 'num_failed_stages',
        'killed_tasks_summary': 'killed_tasks_summary'
    }

    def __init__(self, id=None, name=None, description=None, submission_time=None, completion_time=None, stage_ids=None, job_group=None, status=None, num_tasks=None, num_active_tasks=None, num_completed_tasks=None, num_skipped_tasks=None, num_failed_tasks=None, num_killed_tasks=None, num_completed_indices=None, num_active_stages=None, num_completed_stages=None, num_skipped_stages=None, num_failed_stages=None, killed_tasks_summary=None):
        """SubJob

        The model defined in huaweicloud sdk

        :param id: 子作业ID，对应开源spark JobData的jobId。
        :type id: int
        :param name: 子作业name，对应开源spark JobData的name。
        :type name: str
        :param description: 子作业description，对应开源spark JobData的description。
        :type description: str
        :param submission_time: 子作业submission_time，对应开源spark JobData的submissionTime。
        :type submission_time: str
        :param completion_time: 子作业completion_time，对应开源spark JobData的completionTime。
        :type completion_time: str
        :param stage_ids: 子作业stage_ids，对应开源spark JobData的stageIds。
        :type stage_ids: list[int]
        :param job_group: 对应DLI的作业ID，对应开源spark JobData的jobGroup。
        :type job_group: str
        :param status: 子作业状态，对应开源spark JobData的status。
        :type status: str
        :param num_tasks: 子作业task的个数，对应开源spark JobData的numTasks。
        :type num_tasks: int
        :param num_active_tasks: 子作业正在运行的task个数，对应开源spark JobData的numActiveTasks。
        :type num_active_tasks: int
        :param num_completed_tasks: 子作业已经完成的task个数，对应开源spark JobData的numCompletedTasks。
        :type num_completed_tasks: int
        :param num_skipped_tasks: 子作业跳过的task个数，对应开源spark JobData的numSkippedTasks。
        :type num_skipped_tasks: int
        :param num_failed_tasks: 子作业跳失败的task个数，对应开源spark JobData的numFailedTasks。
        :type num_failed_tasks: int
        :param num_killed_tasks: 子作业kill掉的task个数，对应开源spark JobData的numKilledTasks。
        :type num_killed_tasks: int
        :param num_completed_indices: 子作业完成指数，对应开源spark JobData的numCompletedIndices。
        :type num_completed_indices: int
        :param num_active_stages: 子作业正在运行的stage个数，对应开源spark JobData的numActiveStages。
        :type num_active_stages: int
        :param num_completed_stages: 子作业已经完成的stage个数，对应开源spark JobData的numCompletedStages。
        :type num_completed_stages: int
        :param num_skipped_stages: 子作业跳过的stage个数，对应开源spark JobData的numSkippedStages。
        :type num_skipped_stages: int
        :param num_failed_stages: 子作业失败的stage个数，对应开源spark JobData的numFailedStages。
        :type num_failed_stages: int
        :param killed_tasks_summary: 子作业killed_tasks_summary，对应开源spark JobData的killedTasksSummary。
        :type killed_tasks_summary: dict(str, int)
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._submission_time = None
        self._completion_time = None
        self._stage_ids = None
        self._job_group = None
        self._status = None
        self._num_tasks = None
        self._num_active_tasks = None
        self._num_completed_tasks = None
        self._num_skipped_tasks = None
        self._num_failed_tasks = None
        self._num_killed_tasks = None
        self._num_completed_indices = None
        self._num_active_stages = None
        self._num_completed_stages = None
        self._num_skipped_stages = None
        self._num_failed_stages = None
        self._killed_tasks_summary = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if submission_time is not None:
            self.submission_time = submission_time
        if completion_time is not None:
            self.completion_time = completion_time
        if stage_ids is not None:
            self.stage_ids = stage_ids
        if job_group is not None:
            self.job_group = job_group
        if status is not None:
            self.status = status
        if num_tasks is not None:
            self.num_tasks = num_tasks
        if num_active_tasks is not None:
            self.num_active_tasks = num_active_tasks
        if num_completed_tasks is not None:
            self.num_completed_tasks = num_completed_tasks
        if num_skipped_tasks is not None:
            self.num_skipped_tasks = num_skipped_tasks
        if num_failed_tasks is not None:
            self.num_failed_tasks = num_failed_tasks
        if num_killed_tasks is not None:
            self.num_killed_tasks = num_killed_tasks
        if num_completed_indices is not None:
            self.num_completed_indices = num_completed_indices
        if num_active_stages is not None:
            self.num_active_stages = num_active_stages
        if num_completed_stages is not None:
            self.num_completed_stages = num_completed_stages
        if num_skipped_stages is not None:
            self.num_skipped_stages = num_skipped_stages
        if num_failed_stages is not None:
            self.num_failed_stages = num_failed_stages
        if killed_tasks_summary is not None:
            self.killed_tasks_summary = killed_tasks_summary

    @property
    def id(self):
        """Gets the id of this SubJob.

        子作业ID，对应开源spark JobData的jobId。

        :return: The id of this SubJob.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubJob.

        子作业ID，对应开源spark JobData的jobId。

        :param id: The id of this SubJob.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SubJob.

        子作业name，对应开源spark JobData的name。

        :return: The name of this SubJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubJob.

        子作业name，对应开源spark JobData的name。

        :param name: The name of this SubJob.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this SubJob.

        子作业description，对应开源spark JobData的description。

        :return: The description of this SubJob.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubJob.

        子作业description，对应开源spark JobData的description。

        :param description: The description of this SubJob.
        :type description: str
        """
        self._description = description

    @property
    def submission_time(self):
        """Gets the submission_time of this SubJob.

        子作业submission_time，对应开源spark JobData的submissionTime。

        :return: The submission_time of this SubJob.
        :rtype: str
        """
        return self._submission_time

    @submission_time.setter
    def submission_time(self, submission_time):
        """Sets the submission_time of this SubJob.

        子作业submission_time，对应开源spark JobData的submissionTime。

        :param submission_time: The submission_time of this SubJob.
        :type submission_time: str
        """
        self._submission_time = submission_time

    @property
    def completion_time(self):
        """Gets the completion_time of this SubJob.

        子作业completion_time，对应开源spark JobData的completionTime。

        :return: The completion_time of this SubJob.
        :rtype: str
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this SubJob.

        子作业completion_time，对应开源spark JobData的completionTime。

        :param completion_time: The completion_time of this SubJob.
        :type completion_time: str
        """
        self._completion_time = completion_time

    @property
    def stage_ids(self):
        """Gets the stage_ids of this SubJob.

        子作业stage_ids，对应开源spark JobData的stageIds。

        :return: The stage_ids of this SubJob.
        :rtype: list[int]
        """
        return self._stage_ids

    @stage_ids.setter
    def stage_ids(self, stage_ids):
        """Sets the stage_ids of this SubJob.

        子作业stage_ids，对应开源spark JobData的stageIds。

        :param stage_ids: The stage_ids of this SubJob.
        :type stage_ids: list[int]
        """
        self._stage_ids = stage_ids

    @property
    def job_group(self):
        """Gets the job_group of this SubJob.

        对应DLI的作业ID，对应开源spark JobData的jobGroup。

        :return: The job_group of this SubJob.
        :rtype: str
        """
        return self._job_group

    @job_group.setter
    def job_group(self, job_group):
        """Sets the job_group of this SubJob.

        对应DLI的作业ID，对应开源spark JobData的jobGroup。

        :param job_group: The job_group of this SubJob.
        :type job_group: str
        """
        self._job_group = job_group

    @property
    def status(self):
        """Gets the status of this SubJob.

        子作业状态，对应开源spark JobData的status。

        :return: The status of this SubJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubJob.

        子作业状态，对应开源spark JobData的status。

        :param status: The status of this SubJob.
        :type status: str
        """
        self._status = status

    @property
    def num_tasks(self):
        """Gets the num_tasks of this SubJob.

        子作业task的个数，对应开源spark JobData的numTasks。

        :return: The num_tasks of this SubJob.
        :rtype: int
        """
        return self._num_tasks

    @num_tasks.setter
    def num_tasks(self, num_tasks):
        """Sets the num_tasks of this SubJob.

        子作业task的个数，对应开源spark JobData的numTasks。

        :param num_tasks: The num_tasks of this SubJob.
        :type num_tasks: int
        """
        self._num_tasks = num_tasks

    @property
    def num_active_tasks(self):
        """Gets the num_active_tasks of this SubJob.

        子作业正在运行的task个数，对应开源spark JobData的numActiveTasks。

        :return: The num_active_tasks of this SubJob.
        :rtype: int
        """
        return self._num_active_tasks

    @num_active_tasks.setter
    def num_active_tasks(self, num_active_tasks):
        """Sets the num_active_tasks of this SubJob.

        子作业正在运行的task个数，对应开源spark JobData的numActiveTasks。

        :param num_active_tasks: The num_active_tasks of this SubJob.
        :type num_active_tasks: int
        """
        self._num_active_tasks = num_active_tasks

    @property
    def num_completed_tasks(self):
        """Gets the num_completed_tasks of this SubJob.

        子作业已经完成的task个数，对应开源spark JobData的numCompletedTasks。

        :return: The num_completed_tasks of this SubJob.
        :rtype: int
        """
        return self._num_completed_tasks

    @num_completed_tasks.setter
    def num_completed_tasks(self, num_completed_tasks):
        """Sets the num_completed_tasks of this SubJob.

        子作业已经完成的task个数，对应开源spark JobData的numCompletedTasks。

        :param num_completed_tasks: The num_completed_tasks of this SubJob.
        :type num_completed_tasks: int
        """
        self._num_completed_tasks = num_completed_tasks

    @property
    def num_skipped_tasks(self):
        """Gets the num_skipped_tasks of this SubJob.

        子作业跳过的task个数，对应开源spark JobData的numSkippedTasks。

        :return: The num_skipped_tasks of this SubJob.
        :rtype: int
        """
        return self._num_skipped_tasks

    @num_skipped_tasks.setter
    def num_skipped_tasks(self, num_skipped_tasks):
        """Sets the num_skipped_tasks of this SubJob.

        子作业跳过的task个数，对应开源spark JobData的numSkippedTasks。

        :param num_skipped_tasks: The num_skipped_tasks of this SubJob.
        :type num_skipped_tasks: int
        """
        self._num_skipped_tasks = num_skipped_tasks

    @property
    def num_failed_tasks(self):
        """Gets the num_failed_tasks of this SubJob.

        子作业跳失败的task个数，对应开源spark JobData的numFailedTasks。

        :return: The num_failed_tasks of this SubJob.
        :rtype: int
        """
        return self._num_failed_tasks

    @num_failed_tasks.setter
    def num_failed_tasks(self, num_failed_tasks):
        """Sets the num_failed_tasks of this SubJob.

        子作业跳失败的task个数，对应开源spark JobData的numFailedTasks。

        :param num_failed_tasks: The num_failed_tasks of this SubJob.
        :type num_failed_tasks: int
        """
        self._num_failed_tasks = num_failed_tasks

    @property
    def num_killed_tasks(self):
        """Gets the num_killed_tasks of this SubJob.

        子作业kill掉的task个数，对应开源spark JobData的numKilledTasks。

        :return: The num_killed_tasks of this SubJob.
        :rtype: int
        """
        return self._num_killed_tasks

    @num_killed_tasks.setter
    def num_killed_tasks(self, num_killed_tasks):
        """Sets the num_killed_tasks of this SubJob.

        子作业kill掉的task个数，对应开源spark JobData的numKilledTasks。

        :param num_killed_tasks: The num_killed_tasks of this SubJob.
        :type num_killed_tasks: int
        """
        self._num_killed_tasks = num_killed_tasks

    @property
    def num_completed_indices(self):
        """Gets the num_completed_indices of this SubJob.

        子作业完成指数，对应开源spark JobData的numCompletedIndices。

        :return: The num_completed_indices of this SubJob.
        :rtype: int
        """
        return self._num_completed_indices

    @num_completed_indices.setter
    def num_completed_indices(self, num_completed_indices):
        """Sets the num_completed_indices of this SubJob.

        子作业完成指数，对应开源spark JobData的numCompletedIndices。

        :param num_completed_indices: The num_completed_indices of this SubJob.
        :type num_completed_indices: int
        """
        self._num_completed_indices = num_completed_indices

    @property
    def num_active_stages(self):
        """Gets the num_active_stages of this SubJob.

        子作业正在运行的stage个数，对应开源spark JobData的numActiveStages。

        :return: The num_active_stages of this SubJob.
        :rtype: int
        """
        return self._num_active_stages

    @num_active_stages.setter
    def num_active_stages(self, num_active_stages):
        """Sets the num_active_stages of this SubJob.

        子作业正在运行的stage个数，对应开源spark JobData的numActiveStages。

        :param num_active_stages: The num_active_stages of this SubJob.
        :type num_active_stages: int
        """
        self._num_active_stages = num_active_stages

    @property
    def num_completed_stages(self):
        """Gets the num_completed_stages of this SubJob.

        子作业已经完成的stage个数，对应开源spark JobData的numCompletedStages。

        :return: The num_completed_stages of this SubJob.
        :rtype: int
        """
        return self._num_completed_stages

    @num_completed_stages.setter
    def num_completed_stages(self, num_completed_stages):
        """Sets the num_completed_stages of this SubJob.

        子作业已经完成的stage个数，对应开源spark JobData的numCompletedStages。

        :param num_completed_stages: The num_completed_stages of this SubJob.
        :type num_completed_stages: int
        """
        self._num_completed_stages = num_completed_stages

    @property
    def num_skipped_stages(self):
        """Gets the num_skipped_stages of this SubJob.

        子作业跳过的stage个数，对应开源spark JobData的numSkippedStages。

        :return: The num_skipped_stages of this SubJob.
        :rtype: int
        """
        return self._num_skipped_stages

    @num_skipped_stages.setter
    def num_skipped_stages(self, num_skipped_stages):
        """Sets the num_skipped_stages of this SubJob.

        子作业跳过的stage个数，对应开源spark JobData的numSkippedStages。

        :param num_skipped_stages: The num_skipped_stages of this SubJob.
        :type num_skipped_stages: int
        """
        self._num_skipped_stages = num_skipped_stages

    @property
    def num_failed_stages(self):
        """Gets the num_failed_stages of this SubJob.

        子作业失败的stage个数，对应开源spark JobData的numFailedStages。

        :return: The num_failed_stages of this SubJob.
        :rtype: int
        """
        return self._num_failed_stages

    @num_failed_stages.setter
    def num_failed_stages(self, num_failed_stages):
        """Sets the num_failed_stages of this SubJob.

        子作业失败的stage个数，对应开源spark JobData的numFailedStages。

        :param num_failed_stages: The num_failed_stages of this SubJob.
        :type num_failed_stages: int
        """
        self._num_failed_stages = num_failed_stages

    @property
    def killed_tasks_summary(self):
        """Gets the killed_tasks_summary of this SubJob.

        子作业killed_tasks_summary，对应开源spark JobData的killedTasksSummary。

        :return: The killed_tasks_summary of this SubJob.
        :rtype: dict(str, int)
        """
        return self._killed_tasks_summary

    @killed_tasks_summary.setter
    def killed_tasks_summary(self, killed_tasks_summary):
        """Sets the killed_tasks_summary of this SubJob.

        子作业killed_tasks_summary，对应开源spark JobData的killedTasksSummary。

        :param killed_tasks_summary: The killed_tasks_summary of this SubJob.
        :type killed_tasks_summary: dict(str, int)
        """
        self._killed_tasks_summary = killed_tasks_summary

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
        if not isinstance(other, SubJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
