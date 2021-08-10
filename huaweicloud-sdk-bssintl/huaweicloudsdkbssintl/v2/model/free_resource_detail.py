# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreeResourceDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'free_resource_id': 'str',
        'free_resource_type_name': 'str',
        'quota_reuse_cycle': 'int',
        'quota_reuse_cycle_type': 'int',
        'usage_type_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'amount': 'float',
        'original_amount': 'float',
        'measure_id': 'int'
    }

    attribute_map = {
        'free_resource_id': 'free_resource_id',
        'free_resource_type_name': 'free_resource_type_name',
        'quota_reuse_cycle': 'quota_reuse_cycle',
        'quota_reuse_cycle_type': 'quota_reuse_cycle_type',
        'usage_type_name': 'usage_type_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'amount': 'amount',
        'original_amount': 'original_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, free_resource_id=None, free_resource_type_name=None, quota_reuse_cycle=None, quota_reuse_cycle_type=None, usage_type_name=None, start_time=None, end_time=None, amount=None, original_amount=None, measure_id=None):
        """FreeResourceDetail - a model defined in huaweicloud sdk"""
        
        

        self._free_resource_id = None
        self._free_resource_type_name = None
        self._quota_reuse_cycle = None
        self._quota_reuse_cycle_type = None
        self._usage_type_name = None
        self._start_time = None
        self._end_time = None
        self._amount = None
        self._original_amount = None
        self._measure_id = None
        self.discriminator = None

        if free_resource_id is not None:
            self.free_resource_id = free_resource_id
        if free_resource_type_name is not None:
            self.free_resource_type_name = free_resource_type_name
        if quota_reuse_cycle is not None:
            self.quota_reuse_cycle = quota_reuse_cycle
        if quota_reuse_cycle_type is not None:
            self.quota_reuse_cycle_type = quota_reuse_cycle_type
        if usage_type_name is not None:
            self.usage_type_name = usage_type_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if amount is not None:
            self.amount = amount
        if original_amount is not None:
            self.original_amount = original_amount
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def free_resource_id(self):
        """Gets the free_resource_id of this FreeResourceDetail.

        |参数名称：套餐包ID| |参数约束及描述：套餐包ID|

        :return: The free_resource_id of this FreeResourceDetail.
        :rtype: str
        """
        return self._free_resource_id

    @free_resource_id.setter
    def free_resource_id(self, free_resource_id):
        """Sets the free_resource_id of this FreeResourceDetail.

        |参数名称：套餐包ID| |参数约束及描述：套餐包ID|

        :param free_resource_id: The free_resource_id of this FreeResourceDetail.
        :type: str
        """
        self._free_resource_id = free_resource_id

    @property
    def free_resource_type_name(self):
        """Gets the free_resource_type_name of this FreeResourceDetail.

        |参数名称：免费资源类型名称| |参数约束及描述：免费资源类型名称|

        :return: The free_resource_type_name of this FreeResourceDetail.
        :rtype: str
        """
        return self._free_resource_type_name

    @free_resource_type_name.setter
    def free_resource_type_name(self, free_resource_type_name):
        """Sets the free_resource_type_name of this FreeResourceDetail.

        |参数名称：免费资源类型名称| |参数约束及描述：免费资源类型名称|

        :param free_resource_type_name: The free_resource_type_name of this FreeResourceDetail.
        :type: str
        """
        self._free_resource_type_name = free_resource_type_name

    @property
    def quota_reuse_cycle(self):
        """Gets the quota_reuse_cycle of this FreeResourceDetail.

        |参数名称：重用周期| |参数的约束及描述：重用周期|

        :return: The quota_reuse_cycle of this FreeResourceDetail.
        :rtype: int
        """
        return self._quota_reuse_cycle

    @quota_reuse_cycle.setter
    def quota_reuse_cycle(self, quota_reuse_cycle):
        """Sets the quota_reuse_cycle of this FreeResourceDetail.

        |参数名称：重用周期| |参数的约束及描述：重用周期|

        :param quota_reuse_cycle: The quota_reuse_cycle of this FreeResourceDetail.
        :type: int
        """
        self._quota_reuse_cycle = quota_reuse_cycle

    @property
    def quota_reuse_cycle_type(self):
        """Gets the quota_reuse_cycle_type of this FreeResourceDetail.

        |参数名称：重置周期类别| |参数的约束及描述：重置周期类别|

        :return: The quota_reuse_cycle_type of this FreeResourceDetail.
        :rtype: int
        """
        return self._quota_reuse_cycle_type

    @quota_reuse_cycle_type.setter
    def quota_reuse_cycle_type(self, quota_reuse_cycle_type):
        """Sets the quota_reuse_cycle_type of this FreeResourceDetail.

        |参数名称：重置周期类别| |参数的约束及描述：重置周期类别|

        :param quota_reuse_cycle_type: The quota_reuse_cycle_type of this FreeResourceDetail.
        :type: int
        """
        self._quota_reuse_cycle_type = quota_reuse_cycle_type

    @property
    def usage_type_name(self):
        """Gets the usage_type_name of this FreeResourceDetail.

        |参数名称：使用量类型名称| |参数约束及描述：使用量类型名称|

        :return: The usage_type_name of this FreeResourceDetail.
        :rtype: str
        """
        return self._usage_type_name

    @usage_type_name.setter
    def usage_type_name(self, usage_type_name):
        """Sets the usage_type_name of this FreeResourceDetail.

        |参数名称：使用量类型名称| |参数约束及描述：使用量类型名称|

        :param usage_type_name: The usage_type_name of this FreeResourceDetail.
        :type: str
        """
        self._usage_type_name = usage_type_name

    @property
    def start_time(self):
        """Gets the start_time of this FreeResourceDetail.

        |参数名称：开始时间| |参数约束及描述：开始时间|

        :return: The start_time of this FreeResourceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this FreeResourceDetail.

        |参数名称：开始时间| |参数约束及描述：开始时间|

        :param start_time: The start_time of this FreeResourceDetail.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this FreeResourceDetail.

        |参数名称：结束时间| |参数约束及描述：结束时间|

        :return: The end_time of this FreeResourceDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this FreeResourceDetail.

        |参数名称：结束时间| |参数约束及描述：结束时间|

        :param end_time: The end_time of this FreeResourceDetail.
        :type: str
        """
        self._end_time = end_time

    @property
    def amount(self):
        """Gets the amount of this FreeResourceDetail.

        |参数名称：免费资源剩余额度| |参数的约束及描述：免费资源剩余额度|

        :return: The amount of this FreeResourceDetail.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FreeResourceDetail.

        |参数名称：免费资源剩余额度| |参数的约束及描述：免费资源剩余额度|

        :param amount: The amount of this FreeResourceDetail.
        :type: float
        """
        self._amount = amount

    @property
    def original_amount(self):
        """Gets the original_amount of this FreeResourceDetail.

        |参数名称：免费资源原始额度| |参数的约束及描述：免费资源原始额度|

        :return: The original_amount of this FreeResourceDetail.
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this FreeResourceDetail.

        |参数名称：免费资源原始额度| |参数的约束及描述：免费资源原始额度|

        :param original_amount: The original_amount of this FreeResourceDetail.
        :type: float
        """
        self._original_amount = original_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this FreeResourceDetail.

        |参数名称：度量单位| |参数的约束及描述：度量单位|

        :return: The measure_id of this FreeResourceDetail.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this FreeResourceDetail.

        |参数名称：度量单位| |参数的约束及描述：度量单位|

        :param measure_id: The measure_id of this FreeResourceDetail.
        :type: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, FreeResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
