# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartInstanceResponse(SdkResponse):

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
        'instance_name': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instanceId',
        'instance_name': 'instanceName',
        'job_id': 'jobId'
    }

    def __init__(self, instance_id=None, instance_name=None, job_id=None):
        """RestartInstanceResponse

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID。
        :type instance_id: str
        :param instance_name: DDM实例名称。
        :type instance_name: str
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        super(RestartInstanceResponse, self).__init__()

        self._instance_id = None
        self._instance_name = None
        self._job_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if job_id is not None:
            self.job_id = job_id

    @property
    def instance_id(self):
        """Gets the instance_id of this RestartInstanceResponse.

        DDM实例ID。

        :return: The instance_id of this RestartInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RestartInstanceResponse.

        DDM实例ID。

        :param instance_id: The instance_id of this RestartInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this RestartInstanceResponse.

        DDM实例名称。

        :return: The instance_name of this RestartInstanceResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RestartInstanceResponse.

        DDM实例名称。

        :param instance_name: The instance_name of this RestartInstanceResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def job_id(self):
        """Gets the job_id of this RestartInstanceResponse.

        任务ID。

        :return: The job_id of this RestartInstanceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RestartInstanceResponse.

        任务ID。

        :param job_id: The job_id of this RestartInstanceResponse.
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
        if not isinstance(other, RestartInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
