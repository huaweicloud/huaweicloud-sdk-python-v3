# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition_values': 'list[str]',
        'create_time': 'datetime',
        'last_access_time': 'datetime',
        'parameters': 'dict(str, str)',
        'storage_descriptor': 'StorageDescriptor'
    }

    attribute_map = {
        'partition_values': 'partition_values',
        'create_time': 'create_time',
        'last_access_time': 'last_access_time',
        'parameters': 'parameters',
        'storage_descriptor': 'storage_descriptor'
    }

    def __init__(self, partition_values=None, create_time=None, last_access_time=None, parameters=None, storage_descriptor=None):
        r"""PartitionInput

        The model defined in huaweicloud sdk

        :param partition_values: 分区值列表
        :type partition_values: list[str]
        :param create_time: 创建时间
        :type create_time: datetime
        :param last_access_time: 最后访问时间
        :type last_access_time: datetime
        :param parameters: 参数信息
        :type parameters: dict(str, str)
        :param storage_descriptor: 
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        
        

        self._partition_values = None
        self._create_time = None
        self._last_access_time = None
        self._parameters = None
        self._storage_descriptor = None
        self.discriminator = None

        self.partition_values = partition_values
        self.create_time = create_time
        self.last_access_time = last_access_time
        self.parameters = parameters
        self.storage_descriptor = storage_descriptor

    @property
    def partition_values(self):
        r"""Gets the partition_values of this PartitionInput.

        分区值列表

        :return: The partition_values of this PartitionInput.
        :rtype: list[str]
        """
        return self._partition_values

    @partition_values.setter
    def partition_values(self, partition_values):
        r"""Sets the partition_values of this PartitionInput.

        分区值列表

        :param partition_values: The partition_values of this PartitionInput.
        :type partition_values: list[str]
        """
        self._partition_values = partition_values

    @property
    def create_time(self):
        r"""Gets the create_time of this PartitionInput.

        创建时间

        :return: The create_time of this PartitionInput.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PartitionInput.

        创建时间

        :param create_time: The create_time of this PartitionInput.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def last_access_time(self):
        r"""Gets the last_access_time of this PartitionInput.

        最后访问时间

        :return: The last_access_time of this PartitionInput.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        r"""Sets the last_access_time of this PartitionInput.

        最后访问时间

        :param last_access_time: The last_access_time of this PartitionInput.
        :type last_access_time: datetime
        """
        self._last_access_time = last_access_time

    @property
    def parameters(self):
        r"""Gets the parameters of this PartitionInput.

        参数信息

        :return: The parameters of this PartitionInput.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this PartitionInput.

        参数信息

        :param parameters: The parameters of this PartitionInput.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def storage_descriptor(self):
        r"""Gets the storage_descriptor of this PartitionInput.

        :return: The storage_descriptor of this PartitionInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        return self._storage_descriptor

    @storage_descriptor.setter
    def storage_descriptor(self, storage_descriptor):
        r"""Sets the storage_descriptor of this PartitionInput.

        :param storage_descriptor: The storage_descriptor of this PartitionInput.
        :type storage_descriptor: :class:`huaweicloudsdklakeformation.v1.StorageDescriptor`
        """
        self._storage_descriptor = storage_descriptor

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
        if not isinstance(other, PartitionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
