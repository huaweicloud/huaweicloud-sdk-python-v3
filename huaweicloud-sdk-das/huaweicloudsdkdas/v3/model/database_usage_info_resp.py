# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseUsageInfoResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'total_cpu': 'float',
        'total_memory': 'float'
    }

    attribute_map = {
        'database_name': 'database_name',
        'total_cpu': 'total_cpu',
        'total_memory': 'total_memory'
    }

    def __init__(self, database_name=None, total_cpu=None, total_memory=None):
        r"""DatabaseUsageInfoResp

        The model defined in huaweicloud sdk

        :param database_name: 数据库名称
        :type database_name: str
        :param total_cpu: 该数据库的cpu占比
        :type total_cpu: float
        :param total_memory: 该数据库的内存占比
        :type total_memory: float
        """
        
        

        self._database_name = None
        self._total_cpu = None
        self._total_memory = None
        self.discriminator = None

        if database_name is not None:
            self.database_name = database_name
        if total_cpu is not None:
            self.total_cpu = total_cpu
        if total_memory is not None:
            self.total_memory = total_memory

    @property
    def database_name(self):
        r"""Gets the database_name of this DatabaseUsageInfoResp.

        数据库名称

        :return: The database_name of this DatabaseUsageInfoResp.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DatabaseUsageInfoResp.

        数据库名称

        :param database_name: The database_name of this DatabaseUsageInfoResp.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def total_cpu(self):
        r"""Gets the total_cpu of this DatabaseUsageInfoResp.

        该数据库的cpu占比

        :return: The total_cpu of this DatabaseUsageInfoResp.
        :rtype: float
        """
        return self._total_cpu

    @total_cpu.setter
    def total_cpu(self, total_cpu):
        r"""Sets the total_cpu of this DatabaseUsageInfoResp.

        该数据库的cpu占比

        :param total_cpu: The total_cpu of this DatabaseUsageInfoResp.
        :type total_cpu: float
        """
        self._total_cpu = total_cpu

    @property
    def total_memory(self):
        r"""Gets the total_memory of this DatabaseUsageInfoResp.

        该数据库的内存占比

        :return: The total_memory of this DatabaseUsageInfoResp.
        :rtype: float
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        r"""Sets the total_memory of this DatabaseUsageInfoResp.

        该数据库的内存占比

        :param total_memory: The total_memory of this DatabaseUsageInfoResp.
        :type total_memory: float
        """
        self._total_memory = total_memory

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
        if not isinstance(other, DatabaseUsageInfoResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
