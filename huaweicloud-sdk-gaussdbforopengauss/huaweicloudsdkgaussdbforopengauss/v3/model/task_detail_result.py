# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDetailResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_info': 'InstanceInfoResult',
        'job_id': 'str',
        'name': 'str',
        'status': 'str',
        'process': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'instance_info': 'instance_info',
        'job_id': 'job_id',
        'name': 'name',
        'status': 'status',
        'process': 'process',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, instance_info=None, job_id=None, name=None, status=None, process=None, fail_reason=None):
        """TaskDetailResult

        The model defined in huaweicloud sdk

        :param instance_info: 
        :type instance_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceInfoResult`
        :param job_id: 任务ID。
        :type job_id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。
        :type status: str
        :param process: 任务进度，单位：%。
        :type process: str
        :param fail_reason: 失败原因。
        :type fail_reason: str
        """
        
        

        self._instance_info = None
        self._job_id = None
        self._name = None
        self._status = None
        self._process = None
        self._fail_reason = None
        self.discriminator = None

        if instance_info is not None:
            self.instance_info = instance_info
        if job_id is not None:
            self.job_id = job_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if process is not None:
            self.process = process
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def instance_info(self):
        """Gets the instance_info of this TaskDetailResult.

        :return: The instance_info of this TaskDetailResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceInfoResult`
        """
        return self._instance_info

    @instance_info.setter
    def instance_info(self, instance_info):
        """Sets the instance_info of this TaskDetailResult.

        :param instance_info: The instance_info of this TaskDetailResult.
        :type instance_info: :class:`huaweicloudsdkgaussdbforopengauss.v3.InstanceInfoResult`
        """
        self._instance_info = instance_info

    @property
    def job_id(self):
        """Gets the job_id of this TaskDetailResult.

        任务ID。

        :return: The job_id of this TaskDetailResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this TaskDetailResult.

        任务ID。

        :param job_id: The job_id of this TaskDetailResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this TaskDetailResult.

        任务名称。

        :return: The name of this TaskDetailResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaskDetailResult.

        任务名称。

        :param name: The name of this TaskDetailResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this TaskDetailResult.

        任务状态。

        :return: The status of this TaskDetailResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskDetailResult.

        任务状态。

        :param status: The status of this TaskDetailResult.
        :type status: str
        """
        self._status = status

    @property
    def process(self):
        """Gets the process of this TaskDetailResult.

        任务进度，单位：%。

        :return: The process of this TaskDetailResult.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this TaskDetailResult.

        任务进度，单位：%。

        :param process: The process of this TaskDetailResult.
        :type process: str
        """
        self._process = process

    @property
    def fail_reason(self):
        """Gets the fail_reason of this TaskDetailResult.

        失败原因。

        :return: The fail_reason of this TaskDetailResult.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this TaskDetailResult.

        失败原因。

        :param fail_reason: The fail_reason of this TaskDetailResult.
        :type fail_reason: str
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
        if not isinstance(other, TaskDetailResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
