# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListJobInfoDetailResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'jobs': 'GetTaskDetailListRspJobs',
        'task_detail': 'str',
        'instance': 'GetTaskDetailListRspInstance',
        'entities': 'object',
        'fail_reason': 'str'
    }

    attribute_map = {
        'jobs': 'jobs',
        'task_detail': 'task_detail',
        'instance': 'instance',
        'entities': 'entities',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, jobs=None, task_detail=None, instance=None, entities=None, fail_reason=None):
        """ListJobInfoDetailResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._jobs = None
        self._task_detail = None
        self._instance = None
        self._entities = None
        self._fail_reason = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if task_detail is not None:
            self.task_detail = task_detail
        if instance is not None:
            self.instance = instance
        if entities is not None:
            self.entities = entities
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def jobs(self):
        """Gets the jobs of this ListJobInfoDetailResponse.


        :return: The jobs of this ListJobInfoDetailResponse.
        :rtype: GetTaskDetailListRspJobs
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ListJobInfoDetailResponse.


        :param jobs: The jobs of this ListJobInfoDetailResponse.
        :type: GetTaskDetailListRspJobs
        """
        self._jobs = jobs

    @property
    def task_detail(self):
        """Gets the task_detail of this ListJobInfoDetailResponse.

        任务执行的具体的参数信息，为空则不返回该字段。

        :return: The task_detail of this ListJobInfoDetailResponse.
        :rtype: str
        """
        return self._task_detail

    @task_detail.setter
    def task_detail(self, task_detail):
        """Sets the task_detail of this ListJobInfoDetailResponse.

        任务执行的具体的参数信息，为空则不返回该字段。

        :param task_detail: The task_detail of this ListJobInfoDetailResponse.
        :type: str
        """
        self._task_detail = task_detail

    @property
    def instance(self):
        """Gets the instance of this ListJobInfoDetailResponse.


        :return: The instance of this ListJobInfoDetailResponse.
        :rtype: GetTaskDetailListRspInstance
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ListJobInfoDetailResponse.


        :param instance: The instance of this ListJobInfoDetailResponse.
        :type: GetTaskDetailListRspInstance
        """
        self._instance = instance

    @property
    def entities(self):
        """Gets the entities of this ListJobInfoDetailResponse.

        根据不同的任务，显示不同的内容。

        :return: The entities of this ListJobInfoDetailResponse.
        :rtype: object
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ListJobInfoDetailResponse.

        根据不同的任务，显示不同的内容。

        :param entities: The entities of this ListJobInfoDetailResponse.
        :type: object
        """
        self._entities = entities

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ListJobInfoDetailResponse.

        任务执行失败时的错误信息。

        :return: The fail_reason of this ListJobInfoDetailResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ListJobInfoDetailResponse.

        任务执行失败时的错误信息。

        :param fail_reason: The fail_reason of this ListJobInfoDetailResponse.
        :type: str
        """
        self._fail_reason = fail_reason

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListJobInfoDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
