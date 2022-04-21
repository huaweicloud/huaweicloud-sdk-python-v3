# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SelectedSetAlarmTaskReq:

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
        'status': 'str',
        'engine_type': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'engine_type': 'engine_type'
    }

    def __init__(self, job_id=None, status=None, engine_type=None):
        """SelectedSetAlarmTaskReq

        The model defined in huaweicloud sdk

        :param job_id: 任务ID
        :type job_id: str
        :param status: 任务状态
        :type status: str
        :param engine_type: 引擎类型
        :type engine_type: str
        """
        
        

        self._job_id = None
        self._status = None
        self._engine_type = None
        self.discriminator = None

        self.job_id = job_id
        self.status = status
        self.engine_type = engine_type

    @property
    def job_id(self):
        """Gets the job_id of this SelectedSetAlarmTaskReq.

        任务ID

        :return: The job_id of this SelectedSetAlarmTaskReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this SelectedSetAlarmTaskReq.

        任务ID

        :param job_id: The job_id of this SelectedSetAlarmTaskReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this SelectedSetAlarmTaskReq.

        任务状态

        :return: The status of this SelectedSetAlarmTaskReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SelectedSetAlarmTaskReq.

        任务状态

        :param status: The status of this SelectedSetAlarmTaskReq.
        :type status: str
        """
        self._status = status

    @property
    def engine_type(self):
        """Gets the engine_type of this SelectedSetAlarmTaskReq.

        引擎类型

        :return: The engine_type of this SelectedSetAlarmTaskReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this SelectedSetAlarmTaskReq.

        引擎类型

        :param engine_type: The engine_type of this SelectedSetAlarmTaskReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

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
        if not isinstance(other, SelectedSetAlarmTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
