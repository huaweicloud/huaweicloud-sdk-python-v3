# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDiagnosisNodeRequest:

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
        'code': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'code': 'code',
        'instance_id': 'instance_id'
    }

    def __init__(self, task_id=None, code=None, instance_id=None):
        r"""ShowDiagnosisNodeRequest

        The model defined in huaweicloud sdk

        :param task_id: 诊断工单ID
        :type task_id: str
        :param code: 诊断步骤编码
        :type code: str
        :param instance_id: 被诊断实例ID
        :type instance_id: str
        """
        
        

        self._task_id = None
        self._code = None
        self._instance_id = None
        self.discriminator = None

        self.task_id = task_id
        self.code = code
        self.instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowDiagnosisNodeRequest.

        诊断工单ID

        :return: The task_id of this ShowDiagnosisNodeRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowDiagnosisNodeRequest.

        诊断工单ID

        :param task_id: The task_id of this ShowDiagnosisNodeRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def code(self):
        r"""Gets the code of this ShowDiagnosisNodeRequest.

        诊断步骤编码

        :return: The code of this ShowDiagnosisNodeRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowDiagnosisNodeRequest.

        诊断步骤编码

        :param code: The code of this ShowDiagnosisNodeRequest.
        :type code: str
        """
        self._code = code

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowDiagnosisNodeRequest.

        被诊断实例ID

        :return: The instance_id of this ShowDiagnosisNodeRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowDiagnosisNodeRequest.

        被诊断实例ID

        :param instance_id: The instance_id of this ShowDiagnosisNodeRequest.
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
        if not isinstance(other, ShowDiagnosisNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
