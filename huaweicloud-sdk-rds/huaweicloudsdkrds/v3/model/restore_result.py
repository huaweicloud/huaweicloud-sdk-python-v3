# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'job_id': 'job_id'
    }

    def __init__(self, instance_id=None, job_id=None):
        r"""RestoreResult

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param job_id: 工作流id
        :type job_id: str
        """
        
        

        self._instance_id = None
        self._job_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RestoreResult.

        实例ID

        :return: The instance_id of this RestoreResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RestoreResult.

        实例ID

        :param instance_id: The instance_id of this RestoreResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def job_id(self):
        r"""Gets the job_id of this RestoreResult.

        工作流id

        :return: The job_id of this RestoreResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RestoreResult.

        工作流id

        :param job_id: The job_id of this RestoreResult.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, RestoreResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
