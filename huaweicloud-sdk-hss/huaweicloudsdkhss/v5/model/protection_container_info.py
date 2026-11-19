# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionContainerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_name': 'str',
        'container_status': 'str',
        'image_name': 'str',
        'cpu_limit': 'str',
        'memory_limit': 'str',
        'restart_count': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'container_name': 'container_name',
        'container_status': 'container_status',
        'image_name': 'image_name',
        'cpu_limit': 'cpu_limit',
        'memory_limit': 'memory_limit',
        'restart_count': 'restart_count',
        'create_time': 'create_time'
    }

    def __init__(self, container_name=None, container_status=None, image_name=None, cpu_limit=None, memory_limit=None, restart_count=None, create_time=None):
        r"""ProtectionContainerInfo

        The model defined in huaweicloud sdk

        :param container_name: **参数解释**: 容器名称 **取值范围**: 字符长度0-65535位 
        :type container_name: str
        :param container_status: **参数解释**: 容器状态 **取值范围**: 字符长度0-65535位 
        :type container_status: str
        :param image_name: **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 
        :type image_name: str
        :param cpu_limit: **参数解释**: cpu限制值 **取值范围**: 字符长度0-65535位 
        :type cpu_limit: str
        :param memory_limit: **参数解释**: 内存限制值 **取值范围**: 字符长度0-65535位 
        :type memory_limit: str
        :param restart_count: **参数解释**: 重启次数 **取值范围**: 字符长度0-65535位 
        :type restart_count: str
        :param create_time: **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type create_time: int
        """
        
        

        self._container_name = None
        self._container_status = None
        self._image_name = None
        self._cpu_limit = None
        self._memory_limit = None
        self._restart_count = None
        self._create_time = None
        self.discriminator = None

        if container_name is not None:
            self.container_name = container_name
        if container_status is not None:
            self.container_status = container_status
        if image_name is not None:
            self.image_name = image_name
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if memory_limit is not None:
            self.memory_limit = memory_limit
        if restart_count is not None:
            self.restart_count = restart_count
        if create_time is not None:
            self.create_time = create_time

    @property
    def container_name(self):
        r"""Gets the container_name of this ProtectionContainerInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度0-65535位 

        :return: The container_name of this ProtectionContainerInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ProtectionContainerInfo.

        **参数解释**: 容器名称 **取值范围**: 字符长度0-65535位 

        :param container_name: The container_name of this ProtectionContainerInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_status(self):
        r"""Gets the container_status of this ProtectionContainerInfo.

        **参数解释**: 容器状态 **取值范围**: 字符长度0-65535位 

        :return: The container_status of this ProtectionContainerInfo.
        :rtype: str
        """
        return self._container_status

    @container_status.setter
    def container_status(self, container_status):
        r"""Sets the container_status of this ProtectionContainerInfo.

        **参数解释**: 容器状态 **取值范围**: 字符长度0-65535位 

        :param container_status: The container_status of this ProtectionContainerInfo.
        :type container_status: str
        """
        self._container_status = container_status

    @property
    def image_name(self):
        r"""Gets the image_name of this ProtectionContainerInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :return: The image_name of this ProtectionContainerInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ProtectionContainerInfo.

        **参数解释**: 镜像名称 **取值范围**: 字符长度0-65535位 

        :param image_name: The image_name of this ProtectionContainerInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this ProtectionContainerInfo.

        **参数解释**: cpu限制值 **取值范围**: 字符长度0-65535位 

        :return: The cpu_limit of this ProtectionContainerInfo.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this ProtectionContainerInfo.

        **参数解释**: cpu限制值 **取值范围**: 字符长度0-65535位 

        :param cpu_limit: The cpu_limit of this ProtectionContainerInfo.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def memory_limit(self):
        r"""Gets the memory_limit of this ProtectionContainerInfo.

        **参数解释**: 内存限制值 **取值范围**: 字符长度0-65535位 

        :return: The memory_limit of this ProtectionContainerInfo.
        :rtype: str
        """
        return self._memory_limit

    @memory_limit.setter
    def memory_limit(self, memory_limit):
        r"""Sets the memory_limit of this ProtectionContainerInfo.

        **参数解释**: 内存限制值 **取值范围**: 字符长度0-65535位 

        :param memory_limit: The memory_limit of this ProtectionContainerInfo.
        :type memory_limit: str
        """
        self._memory_limit = memory_limit

    @property
    def restart_count(self):
        r"""Gets the restart_count of this ProtectionContainerInfo.

        **参数解释**: 重启次数 **取值范围**: 字符长度0-65535位 

        :return: The restart_count of this ProtectionContainerInfo.
        :rtype: str
        """
        return self._restart_count

    @restart_count.setter
    def restart_count(self, restart_count):
        r"""Sets the restart_count of this ProtectionContainerInfo.

        **参数解释**: 重启次数 **取值范围**: 字符长度0-65535位 

        :param restart_count: The restart_count of this ProtectionContainerInfo.
        :type restart_count: str
        """
        self._restart_count = restart_count

    @property
    def create_time(self):
        r"""Gets the create_time of this ProtectionContainerInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The create_time of this ProtectionContainerInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ProtectionContainerInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this ProtectionContainerInfo.
        :type create_time: int
        """
        self._create_time = create_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProtectionContainerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
