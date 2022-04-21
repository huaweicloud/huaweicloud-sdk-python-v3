# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkCalcSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'driver_memory': 'str',
        'driver_cores': 'int',
        'executor_memory': 'str',
        'executor_cores': 'int',
        'num_executors': 'int'
    }

    attribute_map = {
        'driver_memory': 'driver_memory',
        'driver_cores': 'driver_cores',
        'executor_memory': 'executor_memory',
        'executor_cores': 'executor_cores',
        'num_executors': 'num_executors'
    }

    def __init__(self, driver_memory=None, driver_cores=None, executor_memory=None, executor_cores=None, num_executors=None):
        """SparkCalcSpec

        The model defined in huaweicloud sdk

        :param driver_memory: driver内存
        :type driver_memory: str
        :param driver_cores: driver核数
        :type driver_cores: int
        :param executor_memory: executor内存
        :type executor_memory: str
        :param executor_cores: executor核数
        :type executor_cores: int
        :param num_executors: executor个数
        :type num_executors: int
        """
        
        

        self._driver_memory = None
        self._driver_cores = None
        self._executor_memory = None
        self._executor_cores = None
        self._num_executors = None
        self.discriminator = None

        self.driver_memory = driver_memory
        self.driver_cores = driver_cores
        self.executor_memory = executor_memory
        self.executor_cores = executor_cores
        self.num_executors = num_executors

    @property
    def driver_memory(self):
        """Gets the driver_memory of this SparkCalcSpec.

        driver内存

        :return: The driver_memory of this SparkCalcSpec.
        :rtype: str
        """
        return self._driver_memory

    @driver_memory.setter
    def driver_memory(self, driver_memory):
        """Sets the driver_memory of this SparkCalcSpec.

        driver内存

        :param driver_memory: The driver_memory of this SparkCalcSpec.
        :type driver_memory: str
        """
        self._driver_memory = driver_memory

    @property
    def driver_cores(self):
        """Gets the driver_cores of this SparkCalcSpec.

        driver核数

        :return: The driver_cores of this SparkCalcSpec.
        :rtype: int
        """
        return self._driver_cores

    @driver_cores.setter
    def driver_cores(self, driver_cores):
        """Sets the driver_cores of this SparkCalcSpec.

        driver核数

        :param driver_cores: The driver_cores of this SparkCalcSpec.
        :type driver_cores: int
        """
        self._driver_cores = driver_cores

    @property
    def executor_memory(self):
        """Gets the executor_memory of this SparkCalcSpec.

        executor内存

        :return: The executor_memory of this SparkCalcSpec.
        :rtype: str
        """
        return self._executor_memory

    @executor_memory.setter
    def executor_memory(self, executor_memory):
        """Sets the executor_memory of this SparkCalcSpec.

        executor内存

        :param executor_memory: The executor_memory of this SparkCalcSpec.
        :type executor_memory: str
        """
        self._executor_memory = executor_memory

    @property
    def executor_cores(self):
        """Gets the executor_cores of this SparkCalcSpec.

        executor核数

        :return: The executor_cores of this SparkCalcSpec.
        :rtype: int
        """
        return self._executor_cores

    @executor_cores.setter
    def executor_cores(self, executor_cores):
        """Sets the executor_cores of this SparkCalcSpec.

        executor核数

        :param executor_cores: The executor_cores of this SparkCalcSpec.
        :type executor_cores: int
        """
        self._executor_cores = executor_cores

    @property
    def num_executors(self):
        """Gets the num_executors of this SparkCalcSpec.

        executor个数

        :return: The num_executors of this SparkCalcSpec.
        :rtype: int
        """
        return self._num_executors

    @num_executors.setter
    def num_executors(self, num_executors):
        """Sets the num_executors of this SparkCalcSpec.

        executor个数

        :param num_executors: The num_executors of this SparkCalcSpec.
        :type num_executors: int
        """
        self._num_executors = num_executors

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
        if not isinstance(other, SparkCalcSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
