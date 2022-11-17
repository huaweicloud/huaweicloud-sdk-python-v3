# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingPolicyActionV1:

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
        'instance_number': 'int',
        'instance_percentage': 'int'
    }

    attribute_map = {
        'operation': 'operation',
        'instance_number': 'instance_number',
        'instance_percentage': 'instance_percentage'
    }

    def __init__(self, operation=None, instance_number=None, instance_percentage=None):
        """ScalingPolicyActionV1

        The model defined in huaweicloud sdk

        :param operation: 操作选项。ADD：添加实例。REMOVE/REDUCE：移除实例。SET：设置实例数为
        :type operation: str
        :param instance_number: 操作实例个数，默认为1。当配额为默认配额时，取值范围如下：  operation为SET时，取值范围为：0~300。 operation为ADD或REMOVE/REDUCE时，取值范围为：1~300。 说明： 配置参数时，instance_number和instance_percentage参数只能选其中一个进行配置。
        :type instance_number: int
        :param instance_percentage: 操作实例百分比，将伸缩组容量增加、减少或设置为伸缩组当前实例个数的百分比。操作为ADD或REMOVE/REDUCE时取值范围为1到20000的整数，操作为SET时取值范围为0到20000的整数。  当instance_number和instance_percentage参数均无配置时，则操作实例个数为1。  配置参数时，instance_number和instance_percentage参数只能选其中一个进行配置。
        :type instance_percentage: int
        """
        
        

        self._operation = None
        self._instance_number = None
        self._instance_percentage = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if instance_number is not None:
            self.instance_number = instance_number
        if instance_percentage is not None:
            self.instance_percentage = instance_percentage

    @property
    def operation(self):
        """Gets the operation of this ScalingPolicyActionV1.

        操作选项。ADD：添加实例。REMOVE/REDUCE：移除实例。SET：设置实例数为

        :return: The operation of this ScalingPolicyActionV1.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ScalingPolicyActionV1.

        操作选项。ADD：添加实例。REMOVE/REDUCE：移除实例。SET：设置实例数为

        :param operation: The operation of this ScalingPolicyActionV1.
        :type operation: str
        """
        self._operation = operation

    @property
    def instance_number(self):
        """Gets the instance_number of this ScalingPolicyActionV1.

        操作实例个数，默认为1。当配额为默认配额时，取值范围如下：  operation为SET时，取值范围为：0~300。 operation为ADD或REMOVE/REDUCE时，取值范围为：1~300。 说明： 配置参数时，instance_number和instance_percentage参数只能选其中一个进行配置。

        :return: The instance_number of this ScalingPolicyActionV1.
        :rtype: int
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """Sets the instance_number of this ScalingPolicyActionV1.

        操作实例个数，默认为1。当配额为默认配额时，取值范围如下：  operation为SET时，取值范围为：0~300。 operation为ADD或REMOVE/REDUCE时，取值范围为：1~300。 说明： 配置参数时，instance_number和instance_percentage参数只能选其中一个进行配置。

        :param instance_number: The instance_number of this ScalingPolicyActionV1.
        :type instance_number: int
        """
        self._instance_number = instance_number

    @property
    def instance_percentage(self):
        """Gets the instance_percentage of this ScalingPolicyActionV1.

        操作实例百分比，将伸缩组容量增加、减少或设置为伸缩组当前实例个数的百分比。操作为ADD或REMOVE/REDUCE时取值范围为1到20000的整数，操作为SET时取值范围为0到20000的整数。  当instance_number和instance_percentage参数均无配置时，则操作实例个数为1。  配置参数时，instance_number和instance_percentage参数只能选其中一个进行配置。

        :return: The instance_percentage of this ScalingPolicyActionV1.
        :rtype: int
        """
        return self._instance_percentage

    @instance_percentage.setter
    def instance_percentage(self, instance_percentage):
        """Sets the instance_percentage of this ScalingPolicyActionV1.

        操作实例百分比，将伸缩组容量增加、减少或设置为伸缩组当前实例个数的百分比。操作为ADD或REMOVE/REDUCE时取值范围为1到20000的整数，操作为SET时取值范围为0到20000的整数。  当instance_number和instance_percentage参数均无配置时，则操作实例个数为1。  配置参数时，instance_number和instance_percentage参数只能选其中一个进行配置。

        :param instance_percentage: The instance_percentage of this ScalingPolicyActionV1.
        :type instance_percentage: int
        """
        self._instance_percentage = instance_percentage

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
        if not isinstance(other, ScalingPolicyActionV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
