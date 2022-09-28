# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobTaskDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'inputs': 'list[TaskParameterDto]',
        'resources': 'TaskResourceDto'
    }

    attribute_map = {
        'task_name': 'task_name',
        'inputs': 'inputs',
        'resources': 'resources'
    }

    def __init__(self, task_name=None, inputs=None, resources=None):
        """JobTaskDto

        The model defined in huaweicloud sdk

        :param task_name: 子任务实际名称，取值范围[1,32]，只能以大小写字母开头，由大小写字母、数字、中划线（-）、下划线（_）组成，以大小写字符或数字结尾。需要和已有子任务的名称一致。
        :type task_name: str
        :param inputs: 任务的输入参数信息
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        :param resources: 
        :type resources: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        
        

        self._task_name = None
        self._inputs = None
        self._resources = None
        self.discriminator = None

        self.task_name = task_name
        if inputs is not None:
            self.inputs = inputs
        if resources is not None:
            self.resources = resources

    @property
    def task_name(self):
        """Gets the task_name of this JobTaskDto.

        子任务实际名称，取值范围[1,32]，只能以大小写字母开头，由大小写字母、数字、中划线（-）、下划线（_）组成，以大小写字符或数字结尾。需要和已有子任务的名称一致。

        :return: The task_name of this JobTaskDto.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this JobTaskDto.

        子任务实际名称，取值范围[1,32]，只能以大小写字母开头，由大小写字母、数字、中划线（-）、下划线（_）组成，以大小写字符或数字结尾。需要和已有子任务的名称一致。

        :param task_name: The task_name of this JobTaskDto.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def inputs(self):
        """Gets the inputs of this JobTaskDto.

        任务的输入参数信息

        :return: The inputs of this JobTaskDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this JobTaskDto.

        任务的输入参数信息

        :param inputs: The inputs of this JobTaskDto.
        :type inputs: list[:class:`huaweicloudsdkeihealth.v1.TaskParameterDto`]
        """
        self._inputs = inputs

    @property
    def resources(self):
        """Gets the resources of this JobTaskDto.


        :return: The resources of this JobTaskDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this JobTaskDto.


        :param resources: The resources of this JobTaskDto.
        :type resources: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        self._resources = resources

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
        if not isinstance(other, JobTaskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
