# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiagnosisTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id'
    }

    def __init__(self, task_id=None, instance_id=None):
        r"""ShowDiagnosisTaskRequest

        The model defined in huaweicloud sdk

        :param task_id: 诊断工单ID
        :type task_id: str
        :param instance_id: 非必填，被诊断实例的ID，传入后查询该实例诊断报告
        :type instance_id: str
        """
        
        

        self._task_id = None
        self._instance_id = None
        self.discriminator = None

        self.task_id = task_id
        self.instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowDiagnosisTaskRequest.

        诊断工单ID

        :return: The task_id of this ShowDiagnosisTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowDiagnosisTaskRequest.

        诊断工单ID

        :param task_id: The task_id of this ShowDiagnosisTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDiagnosisTaskRequest.

        非必填，被诊断实例的ID，传入后查询该实例诊断报告

        :return: The instance_id of this ShowDiagnosisTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDiagnosisTaskRequest.

        非必填，被诊断实例的ID，传入后查询该实例诊断报告

        :param instance_id: The instance_id of this ShowDiagnosisTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ShowDiagnosisTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
