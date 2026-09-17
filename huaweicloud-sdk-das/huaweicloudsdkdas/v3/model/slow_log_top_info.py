# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogTopInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_name': 'str',
        'count': 'int',
        'percent': 'float',
        'total': 'int'
    }

    attribute_map = {
        'object_name': 'object_name',
        'count': 'count',
        'percent': 'percent',
        'total': 'total'
    }

    def __init__(self, object_name=None, count=None, percent=None, total=None):
        r"""SlowLogTopInfo

        The model defined in huaweicloud sdk

        :param object_name: 对象名称
        :type object_name: str
        :param count: 数量
        :type count: int
        :param percent: 占比
        :type percent: float
        :param total: 总数
        :type total: int
        """
        
        

        self._object_name = None
        self._count = None
        self._percent = None
        self._total = None
        self.discriminator = None

        if object_name is not None:
            self.object_name = object_name
        if count is not None:
            self.count = count
        if percent is not None:
            self.percent = percent
        if total is not None:
            self.total = total

    @property
    def object_name(self):
        r"""Gets the object_name of this SlowLogTopInfo.

        对象名称

        :return: The object_name of this SlowLogTopInfo.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this SlowLogTopInfo.

        对象名称

        :param object_name: The object_name of this SlowLogTopInfo.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def count(self):
        r"""Gets the count of this SlowLogTopInfo.

        数量

        :return: The count of this SlowLogTopInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this SlowLogTopInfo.

        数量

        :param count: The count of this SlowLogTopInfo.
        :type count: int
        """
        self._count = count

    @property
    def percent(self):
        r"""Gets the percent of this SlowLogTopInfo.

        占比

        :return: The percent of this SlowLogTopInfo.
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        r"""Sets the percent of this SlowLogTopInfo.

        占比

        :param percent: The percent of this SlowLogTopInfo.
        :type percent: float
        """
        self._percent = percent

    @property
    def total(self):
        r"""Gets the total of this SlowLogTopInfo.

        总数

        :return: The total of this SlowLogTopInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SlowLogTopInfo.

        总数

        :param total: The total of this SlowLogTopInfo.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, SlowLogTopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
