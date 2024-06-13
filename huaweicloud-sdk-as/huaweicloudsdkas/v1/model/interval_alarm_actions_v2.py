# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntervalAlarmActionsV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation': 'str',
        'limits': 'int',
        'size': 'int',
        'lower_bound': 'int',
        'upper_bound': 'int'
    }

    attribute_map = {
        'operation': 'operation',
        'limits': 'limits',
        'size': 'size',
        'lower_bound': 'lower_bound',
        'upper_bound': 'upper_bound'
    }

    def __init__(self, operation=None, limits=None, size=None, lower_bound=None, upper_bound=None):
        """IntervalAlarmActionsV2

        The model defined in huaweicloud sdk

        :param operation: 操作选项，默认为ADD。 当scaling_resource_type为SCALING_GROUP，支持如下操作： ADD：增加 REMOVE/REDUCE：减少 SET：设置为 当scaling_resource_type为BANDWIDTH，支持如下操作： ADD：增加 REDUCE：减少
        :type operation: str
        :param limits: 操作限制。当scaling_resource_type为BANDWIDTH，且operation不为SET时，limits参数生效，单位为Mbit/s。此时，当operation为ADD时，limits表示带宽可调整的上限；当operation为REDUCE时，limits表示带宽可调整的下限。
        :type limits: int
        :param size: 操作大小，取值范围为0到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size为实例个数,取值范围为0-300的整数，默认为1。当scaling_resource_type为BANDWIDTH时，size表示带宽大小，单位为Mbit/s，取值范围为1到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size和percentage参数只能选其中一个进行配置。
        :type size: int
        :param lower_bound: 
        :type lower_bound: int
        :param upper_bound: 
        :type upper_bound: int
        """
        
        

        self._operation = None
        self._limits = None
        self._size = None
        self._lower_bound = None
        self._upper_bound = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if limits is not None:
            self.limits = limits
        if size is not None:
            self.size = size
        if lower_bound is not None:
            self.lower_bound = lower_bound
        if upper_bound is not None:
            self.upper_bound = upper_bound

    @property
    def operation(self):
        """Gets the operation of this IntervalAlarmActionsV2.

        操作选项，默认为ADD。 当scaling_resource_type为SCALING_GROUP，支持如下操作： ADD：增加 REMOVE/REDUCE：减少 SET：设置为 当scaling_resource_type为BANDWIDTH，支持如下操作： ADD：增加 REDUCE：减少

        :return: The operation of this IntervalAlarmActionsV2.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this IntervalAlarmActionsV2.

        操作选项，默认为ADD。 当scaling_resource_type为SCALING_GROUP，支持如下操作： ADD：增加 REMOVE/REDUCE：减少 SET：设置为 当scaling_resource_type为BANDWIDTH，支持如下操作： ADD：增加 REDUCE：减少

        :param operation: The operation of this IntervalAlarmActionsV2.
        :type operation: str
        """
        self._operation = operation

    @property
    def limits(self):
        """Gets the limits of this IntervalAlarmActionsV2.

        操作限制。当scaling_resource_type为BANDWIDTH，且operation不为SET时，limits参数生效，单位为Mbit/s。此时，当operation为ADD时，limits表示带宽可调整的上限；当operation为REDUCE时，limits表示带宽可调整的下限。

        :return: The limits of this IntervalAlarmActionsV2.
        :rtype: int
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this IntervalAlarmActionsV2.

        操作限制。当scaling_resource_type为BANDWIDTH，且operation不为SET时，limits参数生效，单位为Mbit/s。此时，当operation为ADD时，limits表示带宽可调整的上限；当operation为REDUCE时，limits表示带宽可调整的下限。

        :param limits: The limits of this IntervalAlarmActionsV2.
        :type limits: int
        """
        self._limits = limits

    @property
    def size(self):
        """Gets the size of this IntervalAlarmActionsV2.

        操作大小，取值范围为0到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size为实例个数,取值范围为0-300的整数，默认为1。当scaling_resource_type为BANDWIDTH时，size表示带宽大小，单位为Mbit/s，取值范围为1到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size和percentage参数只能选其中一个进行配置。

        :return: The size of this IntervalAlarmActionsV2.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this IntervalAlarmActionsV2.

        操作大小，取值范围为0到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size为实例个数,取值范围为0-300的整数，默认为1。当scaling_resource_type为BANDWIDTH时，size表示带宽大小，单位为Mbit/s，取值范围为1到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size和percentage参数只能选其中一个进行配置。

        :param size: The size of this IntervalAlarmActionsV2.
        :type size: int
        """
        self._size = size

    @property
    def lower_bound(self):
        """Gets the lower_bound of this IntervalAlarmActionsV2.

        :return: The lower_bound of this IntervalAlarmActionsV2.
        :rtype: int
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, lower_bound):
        """Sets the lower_bound of this IntervalAlarmActionsV2.

        :param lower_bound: The lower_bound of this IntervalAlarmActionsV2.
        :type lower_bound: int
        """
        self._lower_bound = lower_bound

    @property
    def upper_bound(self):
        """Gets the upper_bound of this IntervalAlarmActionsV2.

        :return: The upper_bound of this IntervalAlarmActionsV2.
        :rtype: int
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, upper_bound):
        """Sets the upper_bound of this IntervalAlarmActionsV2.

        :param upper_bound: The upper_bound of this IntervalAlarmActionsV2.
        :type upper_bound: int
        """
        self._upper_bound = upper_bound

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
        if not isinstance(other, IntervalAlarmActionsV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
