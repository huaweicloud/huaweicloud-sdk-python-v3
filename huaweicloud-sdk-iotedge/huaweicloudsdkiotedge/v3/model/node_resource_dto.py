# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeResourceDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'memory': 'int',
        'storage': 'int',
        'pods': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'storage': 'storage',
        'pods': 'pods'
    }

    def __init__(self, cpu=None, memory=None, storage=None, pods=None):
        r"""NodeResourceDTO

        The model defined in huaweicloud sdk

        :param cpu: 节点cpu，单位个
        :type cpu: int
        :param memory: 节点内存，单位Byte
        :type memory: int
        :param storage: 磁盘，单位Byte
        :type storage: int
        :param pods: 容器pod数量
        :type pods: int
        """
        
        

        self._cpu = None
        self._memory = None
        self._storage = None
        self._pods = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if storage is not None:
            self.storage = storage
        if pods is not None:
            self.pods = pods

    @property
    def cpu(self):
        r"""Gets the cpu of this NodeResourceDTO.

        节点cpu，单位个

        :return: The cpu of this NodeResourceDTO.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this NodeResourceDTO.

        节点cpu，单位个

        :param cpu: The cpu of this NodeResourceDTO.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this NodeResourceDTO.

        节点内存，单位Byte

        :return: The memory of this NodeResourceDTO.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this NodeResourceDTO.

        节点内存，单位Byte

        :param memory: The memory of this NodeResourceDTO.
        :type memory: int
        """
        self._memory = memory

    @property
    def storage(self):
        r"""Gets the storage of this NodeResourceDTO.

        磁盘，单位Byte

        :return: The storage of this NodeResourceDTO.
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this NodeResourceDTO.

        磁盘，单位Byte

        :param storage: The storage of this NodeResourceDTO.
        :type storage: int
        """
        self._storage = storage

    @property
    def pods(self):
        r"""Gets the pods of this NodeResourceDTO.

        容器pod数量

        :return: The pods of this NodeResourceDTO.
        :rtype: int
        """
        return self._pods

    @pods.setter
    def pods(self, pods):
        r"""Sets the pods of this NodeResourceDTO.

        容器pod数量

        :param pods: The pods of this NodeResourceDTO.
        :type pods: int
        """
        self._pods = pods

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
        if not isinstance(other, NodeResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
