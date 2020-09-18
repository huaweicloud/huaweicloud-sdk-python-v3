# coding: utf-8

import pprint
import re

import six





class PackageUsageInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'order_instance_id': 'str',
        'resource_type_name': 'str',
        'quota_reuse_mode': 'int',
        'quota_reuse_cycle': 'int',
        'quota_reuse_cycle_type': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'balance': 'float',
        'total': 'float',
        'measurement_name': 'str',
        'region_code': 'str'
    }

    attribute_map = {
        'order_instance_id': 'order_instance_id',
        'resource_type_name': 'resource_type_name',
        'quota_reuse_mode': 'quota_reuse_mode',
        'quota_reuse_cycle': 'quota_reuse_cycle',
        'quota_reuse_cycle_type': 'quota_reuse_cycle_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'balance': 'balance',
        'total': 'total',
        'measurement_name': 'measurement_name',
        'region_code': 'region_code'
    }

    def __init__(self, order_instance_id=None, resource_type_name=None, quota_reuse_mode=None, quota_reuse_cycle=None, quota_reuse_cycle_type=None, start_time=None, end_time=None, balance=None, total=None, measurement_name=None, region_code=None):
        """PackageUsageInfo - a model defined in huaweicloud sdk"""
        
        

        self._order_instance_id = None
        self._resource_type_name = None
        self._quota_reuse_mode = None
        self._quota_reuse_cycle = None
        self._quota_reuse_cycle_type = None
        self._start_time = None
        self._end_time = None
        self._balance = None
        self._total = None
        self._measurement_name = None
        self._region_code = None
        self.discriminator = None

        if order_instance_id is not None:
            self.order_instance_id = order_instance_id
        if resource_type_name is not None:
            self.resource_type_name = resource_type_name
        if quota_reuse_mode is not None:
            self.quota_reuse_mode = quota_reuse_mode
        if quota_reuse_cycle is not None:
            self.quota_reuse_cycle = quota_reuse_cycle
        if quota_reuse_cycle_type is not None:
            self.quota_reuse_cycle_type = quota_reuse_cycle_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if balance is not None:
            self.balance = balance
        if total is not None:
            self.total = total
        if measurement_name is not None:
            self.measurement_name = measurement_name
        if region_code is not None:
            self.region_code = region_code

    @property
    def order_instance_id(self):
        """Gets the order_instance_id of this PackageUsageInfo.

        |参数名称：订购实例ID| |参数的约束及描述：订购实例ID|

        :return: The order_instance_id of this PackageUsageInfo.
        :rtype: str
        """
        return self._order_instance_id

    @order_instance_id.setter
    def order_instance_id(self, order_instance_id):
        """Sets the order_instance_id of this PackageUsageInfo.

        |参数名称：订购实例ID| |参数的约束及描述：订购实例ID|

        :param order_instance_id: The order_instance_id of this PackageUsageInfo.
        :type: str
        """
        self._order_instance_id = order_instance_id

    @property
    def resource_type_name(self):
        """Gets the resource_type_name of this PackageUsageInfo.

        |参数名称：资源类型名称| |参数的约束及描述：资源类型名称|

        :return: The resource_type_name of this PackageUsageInfo.
        :rtype: str
        """
        return self._resource_type_name

    @resource_type_name.setter
    def resource_type_name(self, resource_type_name):
        """Sets the resource_type_name of this PackageUsageInfo.

        |参数名称：资源类型名称| |参数的约束及描述：资源类型名称|

        :param resource_type_name: The resource_type_name of this PackageUsageInfo.
        :type: str
        """
        self._resource_type_name = resource_type_name

    @property
    def quota_reuse_mode(self):
        """Gets the quota_reuse_mode of this PackageUsageInfo.

        |参数名称：重用模式| |参数的约束及描述：重用模式: 1：可重用2：不可重用|

        :return: The quota_reuse_mode of this PackageUsageInfo.
        :rtype: int
        """
        return self._quota_reuse_mode

    @quota_reuse_mode.setter
    def quota_reuse_mode(self, quota_reuse_mode):
        """Sets the quota_reuse_mode of this PackageUsageInfo.

        |参数名称：重用模式| |参数的约束及描述：重用模式: 1：可重用2：不可重用|

        :param quota_reuse_mode: The quota_reuse_mode of this PackageUsageInfo.
        :type: int
        """
        self._quota_reuse_mode = quota_reuse_mode

    @property
    def quota_reuse_cycle(self):
        """Gets the quota_reuse_cycle of this PackageUsageInfo.

        |参数名称：重用周期| |参数的约束及描述：重用周期，只有quotaReuseMode为可重用，该字段才有意义.1：小时2：天3：周4：月5：年|

        :return: The quota_reuse_cycle of this PackageUsageInfo.
        :rtype: int
        """
        return self._quota_reuse_cycle

    @quota_reuse_cycle.setter
    def quota_reuse_cycle(self, quota_reuse_cycle):
        """Sets the quota_reuse_cycle of this PackageUsageInfo.

        |参数名称：重用周期| |参数的约束及描述：重用周期，只有quotaReuseMode为可重用，该字段才有意义.1：小时2：天3：周4：月5：年|

        :param quota_reuse_cycle: The quota_reuse_cycle of this PackageUsageInfo.
        :type: int
        """
        self._quota_reuse_cycle = quota_reuse_cycle

    @property
    def quota_reuse_cycle_type(self):
        """Gets the quota_reuse_cycle_type of this PackageUsageInfo.

        |参数名称：重用周期类别| |参数的约束及描述：重置周期类别，只有quotaReuseMode为可重用，该字段才有意义1：按自然周期重置2：按订购周期重置|

        :return: The quota_reuse_cycle_type of this PackageUsageInfo.
        :rtype: int
        """
        return self._quota_reuse_cycle_type

    @quota_reuse_cycle_type.setter
    def quota_reuse_cycle_type(self, quota_reuse_cycle_type):
        """Sets the quota_reuse_cycle_type of this PackageUsageInfo.

        |参数名称：重用周期类别| |参数的约束及描述：重置周期类别，只有quotaReuseMode为可重用，该字段才有意义1：按自然周期重置2：按订购周期重置|

        :param quota_reuse_cycle_type: The quota_reuse_cycle_type of this PackageUsageInfo.
        :type: int
        """
        self._quota_reuse_cycle_type = quota_reuse_cycle_type

    @property
    def start_time(self):
        """Gets the start_time of this PackageUsageInfo.

        |参数名称：开始时间，格式UTC| |参数的约束及描述：1）如果quotaReuseMode为可重用，则此时间为当前时间所在的重用周期的开始时间2）如果quotaReuseMode为不可重用，则此时间为订购实例的生效时间，|

        :return: The start_time of this PackageUsageInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PackageUsageInfo.

        |参数名称：开始时间，格式UTC| |参数的约束及描述：1）如果quotaReuseMode为可重用，则此时间为当前时间所在的重用周期的开始时间2）如果quotaReuseMode为不可重用，则此时间为订购实例的生效时间，|

        :param start_time: The start_time of this PackageUsageInfo.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this PackageUsageInfo.

        |参数名称：结束时间，格式UTC| |参数的约束及描述：1）如果quotaReuseMode为可重用，则此时间为当前时间所在的重用周期的结束时间2）如果quotaReuseMode为不可重用，则此时间为订购实例的失效时间|

        :return: The end_time of this PackageUsageInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PackageUsageInfo.

        |参数名称：结束时间，格式UTC| |参数的约束及描述：1）如果quotaReuseMode为可重用，则此时间为当前时间所在的重用周期的结束时间2）如果quotaReuseMode为不可重用，则此时间为订购实例的失效时间|

        :param end_time: The end_time of this PackageUsageInfo.
        :type: str
        """
        self._end_time = end_time

    @property
    def balance(self):
        """Gets the balance of this PackageUsageInfo.

        |参数名称：套餐包内资源剩余量| |参数的约束及描述：套餐包内资源剩余量|

        :return: The balance of this PackageUsageInfo.
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this PackageUsageInfo.

        |参数名称：套餐包内资源剩余量| |参数的约束及描述：套餐包内资源剩余量|

        :param balance: The balance of this PackageUsageInfo.
        :type: float
        """
        self._balance = balance

    @property
    def total(self):
        """Gets the total of this PackageUsageInfo.

        |参数名称：套餐包的资源总量| |参数的约束及描述：套餐包的资源总量|

        :return: The total of this PackageUsageInfo.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PackageUsageInfo.

        |参数名称：套餐包的资源总量| |参数的约束及描述：套餐包的资源总量|

        :param total: The total of this PackageUsageInfo.
        :type: float
        """
        self._total = total

    @property
    def measurement_name(self):
        """Gets the measurement_name of this PackageUsageInfo.

        |参数名称：套餐包资源的度量单位名称| |参数的约束及描述：套餐包资源的度量单位名称|

        :return: The measurement_name of this PackageUsageInfo.
        :rtype: str
        """
        return self._measurement_name

    @measurement_name.setter
    def measurement_name(self, measurement_name):
        """Sets the measurement_name of this PackageUsageInfo.

        |参数名称：套餐包资源的度量单位名称| |参数的约束及描述：套餐包资源的度量单位名称|

        :param measurement_name: The measurement_name of this PackageUsageInfo.
        :type: str
        """
        self._measurement_name = measurement_name

    @property
    def region_code(self):
        """Gets the region_code of this PackageUsageInfo.

        |参数名称：区域编码| |参数的约束及描述：区域编码|

        :return: The region_code of this PackageUsageInfo.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this PackageUsageInfo.

        |参数名称：区域编码| |参数的约束及描述：区域编码|

        :param region_code: The region_code of this PackageUsageInfo.
        :type: str
        """
        self._region_code = region_code

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
        if not isinstance(other, PackageUsageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
