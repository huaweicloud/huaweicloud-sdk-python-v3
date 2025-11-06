# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVaultTopsResponseBodyVaults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'time': 'int',
        'dimension': 'str',
        'value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'id': 'id',
        'time': 'time',
        'dimension': 'dimension',
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, id=None, time=None, dimension=None, value=None, unit=None):
        r"""ListVaultTopsResponseBodyVaults

        The model defined in huaweicloud sdk

        :param id: 存储库ID
        :type id: str
        :param time: 指标时间，单位毫秒
        :type time: int
        :param dimension: 指标数据维度
        :type dimension: str
        :param value: 指标数据取值
        :type value: float
        :param unit: 指标数据的单位，例如：个、GB、%
        :type unit: str
        """
        
        

        self._id = None
        self._time = None
        self._dimension = None
        self._value = None
        self._unit = None
        self.discriminator = None

        self.id = id
        self.time = time
        self.dimension = dimension
        self.value = value
        if unit is not None:
            self.unit = unit

    @property
    def id(self):
        r"""Gets the id of this ListVaultTopsResponseBodyVaults.

        存储库ID

        :return: The id of this ListVaultTopsResponseBodyVaults.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListVaultTopsResponseBodyVaults.

        存储库ID

        :param id: The id of this ListVaultTopsResponseBodyVaults.
        :type id: str
        """
        self._id = id

    @property
    def time(self):
        r"""Gets the time of this ListVaultTopsResponseBodyVaults.

        指标时间，单位毫秒

        :return: The time of this ListVaultTopsResponseBodyVaults.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this ListVaultTopsResponseBodyVaults.

        指标时间，单位毫秒

        :param time: The time of this ListVaultTopsResponseBodyVaults.
        :type time: int
        """
        self._time = time

    @property
    def dimension(self):
        r"""Gets the dimension of this ListVaultTopsResponseBodyVaults.

        指标数据维度

        :return: The dimension of this ListVaultTopsResponseBodyVaults.
        :rtype: str
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        r"""Sets the dimension of this ListVaultTopsResponseBodyVaults.

        指标数据维度

        :param dimension: The dimension of this ListVaultTopsResponseBodyVaults.
        :type dimension: str
        """
        self._dimension = dimension

    @property
    def value(self):
        r"""Gets the value of this ListVaultTopsResponseBodyVaults.

        指标数据取值

        :return: The value of this ListVaultTopsResponseBodyVaults.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListVaultTopsResponseBodyVaults.

        指标数据取值

        :param value: The value of this ListVaultTopsResponseBodyVaults.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        r"""Gets the unit of this ListVaultTopsResponseBodyVaults.

        指标数据的单位，例如：个、GB、%

        :return: The unit of this ListVaultTopsResponseBodyVaults.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ListVaultTopsResponseBodyVaults.

        指标数据的单位，例如：个、GB、%

        :param unit: The unit of this ListVaultTopsResponseBodyVaults.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, ListVaultTopsResponseBodyVaults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
