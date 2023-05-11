# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopFlinkJobsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trigger_savepoint': 'bool',
        'job_ids': 'list[int]'
    }

    attribute_map = {
        'trigger_savepoint': 'trigger_savepoint',
        'job_ids': 'job_ids'
    }

    def __init__(self, trigger_savepoint=None, job_ids=None):
        """StopFlinkJobsRequestBody

        The model defined in huaweicloud sdk

        :param trigger_savepoint: 在停止作业之前，用户可以选择是否对作业创建保存点，保存作业的状态信息。类型为boolean。  当triggerSavePoint为true时，表示创建保存点。 当triggerSavePoint为false时，表示不创建保存点。默认为false。
        :type trigger_savepoint: bool
        :param job_ids: 
        :type job_ids: list[int]
        """
        
        

        self._trigger_savepoint = None
        self._job_ids = None
        self.discriminator = None

        if trigger_savepoint is not None:
            self.trigger_savepoint = trigger_savepoint
        self.job_ids = job_ids

    @property
    def trigger_savepoint(self):
        """Gets the trigger_savepoint of this StopFlinkJobsRequestBody.

        在停止作业之前，用户可以选择是否对作业创建保存点，保存作业的状态信息。类型为boolean。  当triggerSavePoint为true时，表示创建保存点。 当triggerSavePoint为false时，表示不创建保存点。默认为false。

        :return: The trigger_savepoint of this StopFlinkJobsRequestBody.
        :rtype: bool
        """
        return self._trigger_savepoint

    @trigger_savepoint.setter
    def trigger_savepoint(self, trigger_savepoint):
        """Sets the trigger_savepoint of this StopFlinkJobsRequestBody.

        在停止作业之前，用户可以选择是否对作业创建保存点，保存作业的状态信息。类型为boolean。  当triggerSavePoint为true时，表示创建保存点。 当triggerSavePoint为false时，表示不创建保存点。默认为false。

        :param trigger_savepoint: The trigger_savepoint of this StopFlinkJobsRequestBody.
        :type trigger_savepoint: bool
        """
        self._trigger_savepoint = trigger_savepoint

    @property
    def job_ids(self):
        """Gets the job_ids of this StopFlinkJobsRequestBody.

        

        :return: The job_ids of this StopFlinkJobsRequestBody.
        :rtype: list[int]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        """Sets the job_ids of this StopFlinkJobsRequestBody.

        

        :param job_ids: The job_ids of this StopFlinkJobsRequestBody.
        :type job_ids: list[int]
        """
        self._job_ids = job_ids

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
        if not isinstance(other, StopFlinkJobsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
