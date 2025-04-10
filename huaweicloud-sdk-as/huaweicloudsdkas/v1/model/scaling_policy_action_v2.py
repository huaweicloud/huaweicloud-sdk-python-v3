# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingPolicyActionV2:

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
        'size': 'int',
        'percentage': 'int',
        'limits': 'int'
    }

    attribute_map = {
        'operation': 'operation',
        'size': 'size',
        'percentage': 'percentage',
        'limits': 'limits'
    }

    def __init__(self, operation=None, size=None, percentage=None, limits=None):
        r"""ScalingPolicyActionV2

        The model defined in huaweicloud sdk

        :param operation: 操作选项，默认为ADD。 当scaling_resource_type为SCALING_GROUP，支持如下操作： - ADD：增加 - REMOVE/REDUCE：减少 - SET：设置为 当scaling_resource_type为BANDWIDTH，支持如下操作： - ADD：增加 - REDUCE：减少 - SET：设置为
        :type operation: str
        :param size: 操作大小，取值范围为0到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size为实例个数,取值范围为0-300的整数，默认为1。当scaling_resource_type为BANDWIDTH时，size表示带宽大小，单位为Mbit/s，取值范围为1到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size和percentage参数只能选其中一个进行配置。
        :type size: int
        :param percentage: 操作百分比，取值为0到20000的整数。当scaling_resource_type为SCALING_GROUP时，size和instance_percentage参数均无配置，则size默认为1。当scaling_resource_type为BANDWIDTH时，不支持配置instance_percentage参数。
        :type percentage: int
        :param limits: 操作限制。当scaling_resource_type为BANDWIDTH，且operation不为SET时，limits参数生效，单位为Mbit/s。此时，当operation为ADD时，limits表示带宽可调整的上限；当operation为REDUCE时，limits表示带宽可调整的下限。
        :type limits: int
        """
        
        

        self._operation = None
        self._size = None
        self._percentage = None
        self._limits = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if size is not None:
            self.size = size
        if percentage is not None:
            self.percentage = percentage
        if limits is not None:
            self.limits = limits

    @property
    def operation(self):
        r"""Gets the operation of this ScalingPolicyActionV2.

        操作选项，默认为ADD。 当scaling_resource_type为SCALING_GROUP，支持如下操作： - ADD：增加 - REMOVE/REDUCE：减少 - SET：设置为 当scaling_resource_type为BANDWIDTH，支持如下操作： - ADD：增加 - REDUCE：减少 - SET：设置为

        :return: The operation of this ScalingPolicyActionV2.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ScalingPolicyActionV2.

        操作选项，默认为ADD。 当scaling_resource_type为SCALING_GROUP，支持如下操作： - ADD：增加 - REMOVE/REDUCE：减少 - SET：设置为 当scaling_resource_type为BANDWIDTH，支持如下操作： - ADD：增加 - REDUCE：减少 - SET：设置为

        :param operation: The operation of this ScalingPolicyActionV2.
        :type operation: str
        """
        self._operation = operation

    @property
    def size(self):
        r"""Gets the size of this ScalingPolicyActionV2.

        操作大小，取值范围为0到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size为实例个数,取值范围为0-300的整数，默认为1。当scaling_resource_type为BANDWIDTH时，size表示带宽大小，单位为Mbit/s，取值范围为1到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size和percentage参数只能选其中一个进行配置。

        :return: The size of this ScalingPolicyActionV2.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ScalingPolicyActionV2.

        操作大小，取值范围为0到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size为实例个数,取值范围为0-300的整数，默认为1。当scaling_resource_type为BANDWIDTH时，size表示带宽大小，单位为Mbit/s，取值范围为1到300的整数，默认为1。当scaling_resource_type为SCALING_GROUP时，size和percentage参数只能选其中一个进行配置。

        :param size: The size of this ScalingPolicyActionV2.
        :type size: int
        """
        self._size = size

    @property
    def percentage(self):
        r"""Gets the percentage of this ScalingPolicyActionV2.

        操作百分比，取值为0到20000的整数。当scaling_resource_type为SCALING_GROUP时，size和instance_percentage参数均无配置，则size默认为1。当scaling_resource_type为BANDWIDTH时，不支持配置instance_percentage参数。

        :return: The percentage of this ScalingPolicyActionV2.
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        r"""Sets the percentage of this ScalingPolicyActionV2.

        操作百分比，取值为0到20000的整数。当scaling_resource_type为SCALING_GROUP时，size和instance_percentage参数均无配置，则size默认为1。当scaling_resource_type为BANDWIDTH时，不支持配置instance_percentage参数。

        :param percentage: The percentage of this ScalingPolicyActionV2.
        :type percentage: int
        """
        self._percentage = percentage

    @property
    def limits(self):
        r"""Gets the limits of this ScalingPolicyActionV2.

        操作限制。当scaling_resource_type为BANDWIDTH，且operation不为SET时，limits参数生效，单位为Mbit/s。此时，当operation为ADD时，limits表示带宽可调整的上限；当operation为REDUCE时，limits表示带宽可调整的下限。

        :return: The limits of this ScalingPolicyActionV2.
        :rtype: int
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this ScalingPolicyActionV2.

        操作限制。当scaling_resource_type为BANDWIDTH，且operation不为SET时，limits参数生效，单位为Mbit/s。此时，当operation为ADD时，limits表示带宽可调整的上限；当operation为REDUCE时，limits表示带宽可调整的下限。

        :param limits: The limits of this ScalingPolicyActionV2.
        :type limits: int
        """
        self._limits = limits

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
        if not isinstance(other, ScalingPolicyActionV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
