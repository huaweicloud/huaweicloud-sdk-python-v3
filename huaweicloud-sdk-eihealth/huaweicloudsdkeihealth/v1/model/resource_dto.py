# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_type': 'str',
        'cpu': 'str',
        'memory': 'str',
        'gpu_type': 'str',
        'gpu': 'str'
    }

    attribute_map = {
        'cpu_type': 'cpu_type',
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu_type': 'gpu_type',
        'gpu': 'gpu'
    }

    def __init__(self, cpu_type=None, cpu=None, memory=None, gpu_type=None, gpu=None):
        """ResourceDto

        The model defined in huaweicloud sdk

        :param cpu_type: cpu架构类型，不填默认X86
        :type cpu_type: str
        :param cpu: cpu申请使用量，取值范围[0.1-128]，单位C，支持一位小数。对于应用，不填默认1C；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业-&gt;流程-&gt;应用
        :type cpu: str
        :param memory: 内存申请使用量，取值范围[0.1-512]，单位G，支持一位小数。对于应用，不填默认1G；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业-&gt;流程-&gt;应用
        :type memory: str
        :param gpu_type: gpu架构类型，取值范围 &#39; &#39;|GPU|D910|D310。对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业-&gt;流程-&gt;应用
        :type gpu_type: str
        :param gpu: gpu申请使用量，取值范围[0-16]，仅支持整数，D910有特殊约束，申请数量需要是0,1,2,4,8。对于应用，不填默认0；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业-&gt;流程-&gt;应用
        :type gpu: str
        """
        
        

        self._cpu_type = None
        self._cpu = None
        self._memory = None
        self._gpu_type = None
        self._gpu = None
        self.discriminator = None

        if cpu_type is not None:
            self.cpu_type = cpu_type
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if gpu_type is not None:
            self.gpu_type = gpu_type
        if gpu is not None:
            self.gpu = gpu

    @property
    def cpu_type(self):
        """Gets the cpu_type of this ResourceDto.

        cpu架构类型，不填默认X86

        :return: The cpu_type of this ResourceDto.
        :rtype: str
        """
        return self._cpu_type

    @cpu_type.setter
    def cpu_type(self, cpu_type):
        """Sets the cpu_type of this ResourceDto.

        cpu架构类型，不填默认X86

        :param cpu_type: The cpu_type of this ResourceDto.
        :type cpu_type: str
        """
        self._cpu_type = cpu_type

    @property
    def cpu(self):
        """Gets the cpu of this ResourceDto.

        cpu申请使用量，取值范围[0.1-128]，单位C，支持一位小数。对于应用，不填默认1C；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :return: The cpu of this ResourceDto.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this ResourceDto.

        cpu申请使用量，取值范围[0.1-128]，单位C，支持一位小数。对于应用，不填默认1C；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :param cpu: The cpu of this ResourceDto.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        """Gets the memory of this ResourceDto.

        内存申请使用量，取值范围[0.1-512]，单位G，支持一位小数。对于应用，不填默认1G；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :return: The memory of this ResourceDto.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ResourceDto.

        内存申请使用量，取值范围[0.1-512]，单位G，支持一位小数。对于应用，不填默认1G；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :param memory: The memory of this ResourceDto.
        :type memory: str
        """
        self._memory = memory

    @property
    def gpu_type(self):
        """Gets the gpu_type of this ResourceDto.

        gpu架构类型，取值范围 ' '|GPU|D910|D310。对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :return: The gpu_type of this ResourceDto.
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """Sets the gpu_type of this ResourceDto.

        gpu架构类型，取值范围 ' '|GPU|D910|D310。对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :param gpu_type: The gpu_type of this ResourceDto.
        :type gpu_type: str
        """
        self._gpu_type = gpu_type

    @property
    def gpu(self):
        """Gets the gpu of this ResourceDto.

        gpu申请使用量，取值范围[0-16]，仅支持整数，D910有特殊约束，申请数量需要是0,1,2,4,8。对于应用，不填默认0；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :return: The gpu of this ResourceDto.
        :rtype: str
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        """Sets the gpu of this ResourceDto.

        gpu申请使用量，取值范围[0-16]，仅支持整数，D910有特殊约束，申请数量需要是0,1,2,4,8。对于应用，不填默认0；对于流程和作业，不填默认使用前一级的配置，填值会覆盖更新。覆盖关系：作业->流程->应用

        :param gpu: The gpu of this ResourceDto.
        :type gpu: str
        """
        self._gpu = gpu

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
        if not isinstance(other, ResourceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
