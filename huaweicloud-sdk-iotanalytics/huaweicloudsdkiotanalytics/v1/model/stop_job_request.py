# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopJobRequest:

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
        'trigger_savepoint': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'trigger_savepoint': 'trigger_savepoint'
    }

    def __init__(self, job_id=None, trigger_savepoint=None):
        """StopJobRequest

        The model defined in huaweicloud sdk

        :param job_id: 作业ID
        :type job_id: str
        :param trigger_savepoint: 停止作业触发savepoint
        :type trigger_savepoint: bool
        """
        
        

        self._job_id = None
        self._trigger_savepoint = None
        self.discriminator = None

        self.job_id = job_id
        if trigger_savepoint is not None:
            self.trigger_savepoint = trigger_savepoint

    @property
    def job_id(self):
        """Gets the job_id of this StopJobRequest.

        作业ID

        :return: The job_id of this StopJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StopJobRequest.

        作业ID

        :param job_id: The job_id of this StopJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def trigger_savepoint(self):
        """Gets the trigger_savepoint of this StopJobRequest.

        停止作业触发savepoint

        :return: The trigger_savepoint of this StopJobRequest.
        :rtype: bool
        """
        return self._trigger_savepoint

    @trigger_savepoint.setter
    def trigger_savepoint(self, trigger_savepoint):
        """Sets the trigger_savepoint of this StopJobRequest.

        停止作业触发savepoint

        :param trigger_savepoint: The trigger_savepoint of this StopJobRequest.
        :type trigger_savepoint: bool
        """
        self._trigger_savepoint = trigger_savepoint

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
        if not isinstance(other, StopJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
