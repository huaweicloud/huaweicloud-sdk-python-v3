# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFuncReservedInstanceMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_num': 'list[SlaReportsValue]',
        'reserved_instance_num': 'list[SlaReportsValue]'
    }

    attribute_map = {
        'instance_num': 'instanceNum',
        'reserved_instance_num': 'reservedInstanceNum'
    }

    def __init__(self, instance_num=None, reserved_instance_num=None):
        """ShowFuncReservedInstanceMetricsResponse

        The model defined in huaweicloud sdk

        :param instance_num: 弹性实例指标
        :type instance_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        :param reserved_instance_num: 预留实例指标
        :type reserved_instance_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        
        super(ShowFuncReservedInstanceMetricsResponse, self).__init__()

        self._instance_num = None
        self._reserved_instance_num = None
        self.discriminator = None

        if instance_num is not None:
            self.instance_num = instance_num
        if reserved_instance_num is not None:
            self.reserved_instance_num = reserved_instance_num

    @property
    def instance_num(self):
        """Gets the instance_num of this ShowFuncReservedInstanceMetricsResponse.

        弹性实例指标

        :return: The instance_num of this ShowFuncReservedInstanceMetricsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        """Sets the instance_num of this ShowFuncReservedInstanceMetricsResponse.

        弹性实例指标

        :param instance_num: The instance_num of this ShowFuncReservedInstanceMetricsResponse.
        :type instance_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._instance_num = instance_num

    @property
    def reserved_instance_num(self):
        """Gets the reserved_instance_num of this ShowFuncReservedInstanceMetricsResponse.

        预留实例指标

        :return: The reserved_instance_num of this ShowFuncReservedInstanceMetricsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        return self._reserved_instance_num

    @reserved_instance_num.setter
    def reserved_instance_num(self, reserved_instance_num):
        """Sets the reserved_instance_num of this ShowFuncReservedInstanceMetricsResponse.

        预留实例指标

        :param reserved_instance_num: The reserved_instance_num of this ShowFuncReservedInstanceMetricsResponse.
        :type reserved_instance_num: list[:class:`huaweicloudsdkfunctiongraph.v2.SlaReportsValue`]
        """
        self._reserved_instance_num = reserved_instance_num

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
        if not isinstance(other, ShowFuncReservedInstanceMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
