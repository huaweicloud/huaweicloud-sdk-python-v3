# coding: utf-8

import pprint
import re

import six





class CreateRequestBodyKafkaCreateInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'spec': 'str',
        'storage': 'int',
        'az': 'str'
    }

    attribute_map = {
        'spec': 'spec',
        'storage': 'storage',
        'az': 'az'
    }

    def __init__(self, spec=None, storage=None, az=None):
        """CreateRequestBodyKafkaCreateInfo - a model defined in huaweicloud sdk"""
        
        

        self._spec = None
        self._storage = None
        self._az = None
        self.discriminator = None

        if spec is not None:
            self.spec = spec
        if storage is not None:
            self.storage = storage
        if az is not None:
            self.az = az

    @property
    def spec(self):
        """Gets the spec of this CreateRequestBodyKafkaCreateInfo.

        kafka实例规格，可选：mini：基准带宽100MB/s，small：基准带宽300MB/s，middle：基准带宽600MB/s，high：基准带宽1200MB/s

        :return: The spec of this CreateRequestBodyKafkaCreateInfo.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this CreateRequestBodyKafkaCreateInfo.

        kafka实例规格，可选：mini：基准带宽100MB/s，small：基准带宽300MB/s，middle：基准带宽600MB/s，high：基准带宽1200MB/s

        :param spec: The spec of this CreateRequestBodyKafkaCreateInfo.
        :type: str
        """
        self._spec = spec

    @property
    def storage(self):
        """Gets the storage of this CreateRequestBodyKafkaCreateInfo.

        存储空间(单位：GB），至多9000，mini版至少300，small至少1200，middle至少2400，high至少4800

        :return: The storage of this CreateRequestBodyKafkaCreateInfo.
        :rtype: int
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this CreateRequestBodyKafkaCreateInfo.

        存储空间(单位：GB），至多9000，mini版至少300，small至少1200，middle至少2400，high至少4800

        :param storage: The storage of this CreateRequestBodyKafkaCreateInfo.
        :type: int
        """
        self._storage = storage

    @property
    def az(self):
        """Gets the az of this CreateRequestBodyKafkaCreateInfo.

        kafka实例可用区

        :return: The az of this CreateRequestBodyKafkaCreateInfo.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        """Sets the az of this CreateRequestBodyKafkaCreateInfo.

        kafka实例可用区

        :param az: The az of this CreateRequestBodyKafkaCreateInfo.
        :type: str
        """
        self._az = az

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRequestBodyKafkaCreateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
