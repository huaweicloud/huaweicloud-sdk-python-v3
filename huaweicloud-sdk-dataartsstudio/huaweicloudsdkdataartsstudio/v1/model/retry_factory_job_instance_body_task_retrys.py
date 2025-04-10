# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetryFactoryJobInstanceBodyTaskRetrys:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'plan_time': 'int',
        'submit_time': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'plan_time': 'plan_time',
        'submit_time': 'submit_time'
    }

    def __init__(self, job_id=None, plan_time=None, submit_time=None):
        r"""RetryFactoryJobInstanceBodyTaskRetrys

        The model defined in huaweicloud sdk

        :param job_id: 作业id，当前重跑实例的作业id。
        :type job_id: int
        :param plan_time: 实例计划时间，13位时间戳，可通过查询作业实例列表接口获取。
        :type plan_time: int
        :param submit_time: 实例提交时间，13位时间戳，可通过查询作业实例列表接口获取。
        :type submit_time: int
        """
        
        

        self._job_id = None
        self._plan_time = None
        self._submit_time = None
        self.discriminator = None

        self.job_id = job_id
        self.plan_time = plan_time
        self.submit_time = submit_time

    @property
    def job_id(self):
        r"""Gets the job_id of this RetryFactoryJobInstanceBodyTaskRetrys.

        作业id，当前重跑实例的作业id。

        :return: The job_id of this RetryFactoryJobInstanceBodyTaskRetrys.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RetryFactoryJobInstanceBodyTaskRetrys.

        作业id，当前重跑实例的作业id。

        :param job_id: The job_id of this RetryFactoryJobInstanceBodyTaskRetrys.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def plan_time(self):
        r"""Gets the plan_time of this RetryFactoryJobInstanceBodyTaskRetrys.

        实例计划时间，13位时间戳，可通过查询作业实例列表接口获取。

        :return: The plan_time of this RetryFactoryJobInstanceBodyTaskRetrys.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        r"""Sets the plan_time of this RetryFactoryJobInstanceBodyTaskRetrys.

        实例计划时间，13位时间戳，可通过查询作业实例列表接口获取。

        :param plan_time: The plan_time of this RetryFactoryJobInstanceBodyTaskRetrys.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def submit_time(self):
        r"""Gets the submit_time of this RetryFactoryJobInstanceBodyTaskRetrys.

        实例提交时间，13位时间戳，可通过查询作业实例列表接口获取。

        :return: The submit_time of this RetryFactoryJobInstanceBodyTaskRetrys.
        :rtype: int
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        r"""Sets the submit_time of this RetryFactoryJobInstanceBodyTaskRetrys.

        实例提交时间，13位时间戳，可通过查询作业实例列表接口获取。

        :param submit_time: The submit_time of this RetryFactoryJobInstanceBodyTaskRetrys.
        :type submit_time: int
        """
        self._submit_time = submit_time

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
        if not isinstance(other, RetryFactoryJobInstanceBodyTaskRetrys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
