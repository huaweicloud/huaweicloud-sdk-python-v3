# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActivateNodeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'cpu_order_id': 'str',
        'npu_gpu_order_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'cpu_order_id': 'cpu_order_id',
        'npu_gpu_order_id': 'npu_gpu_order_id'
    }

    def __init__(self, order_id=None, cpu_order_id=None, npu_gpu_order_id=None):
        """ActivateNodeRequestBody

        The model defined in huaweicloud sdk

        :param order_id: 订单ID，小型轻型设备激活时使用的订单
        :type order_id: str
        :param cpu_order_id: 订单ID，大型设备使用CPU时激活的订单
        :type cpu_order_id: str
        :param npu_gpu_order_id: 订单ID，大型设备使用GPU/NPU时激活的订单
        :type npu_gpu_order_id: str
        """
        
        

        self._order_id = None
        self._cpu_order_id = None
        self._npu_gpu_order_id = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if cpu_order_id is not None:
            self.cpu_order_id = cpu_order_id
        if npu_gpu_order_id is not None:
            self.npu_gpu_order_id = npu_gpu_order_id

    @property
    def order_id(self):
        """Gets the order_id of this ActivateNodeRequestBody.

        订单ID，小型轻型设备激活时使用的订单

        :return: The order_id of this ActivateNodeRequestBody.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ActivateNodeRequestBody.

        订单ID，小型轻型设备激活时使用的订单

        :param order_id: The order_id of this ActivateNodeRequestBody.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def cpu_order_id(self):
        """Gets the cpu_order_id of this ActivateNodeRequestBody.

        订单ID，大型设备使用CPU时激活的订单

        :return: The cpu_order_id of this ActivateNodeRequestBody.
        :rtype: str
        """
        return self._cpu_order_id

    @cpu_order_id.setter
    def cpu_order_id(self, cpu_order_id):
        """Sets the cpu_order_id of this ActivateNodeRequestBody.

        订单ID，大型设备使用CPU时激活的订单

        :param cpu_order_id: The cpu_order_id of this ActivateNodeRequestBody.
        :type cpu_order_id: str
        """
        self._cpu_order_id = cpu_order_id

    @property
    def npu_gpu_order_id(self):
        """Gets the npu_gpu_order_id of this ActivateNodeRequestBody.

        订单ID，大型设备使用GPU/NPU时激活的订单

        :return: The npu_gpu_order_id of this ActivateNodeRequestBody.
        :rtype: str
        """
        return self._npu_gpu_order_id

    @npu_gpu_order_id.setter
    def npu_gpu_order_id(self, npu_gpu_order_id):
        """Sets the npu_gpu_order_id of this ActivateNodeRequestBody.

        订单ID，大型设备使用GPU/NPU时激活的订单

        :param npu_gpu_order_id: The npu_gpu_order_id of this ActivateNodeRequestBody.
        :type npu_gpu_order_id: str
        """
        self._npu_gpu_order_id = npu_gpu_order_id

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
        if not isinstance(other, ActivateNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
