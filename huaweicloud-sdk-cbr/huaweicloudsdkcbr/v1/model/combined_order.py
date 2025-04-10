# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CombinedOrder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'combined_order_id': 'str',
        'combined_order_ecs_num': 'int',
        'combined_order_num': 'int'
    }

    attribute_map = {
        'combined_order_id': 'combined_order_id',
        'combined_order_ecs_num': 'combined_order_ecs_num',
        'combined_order_num': 'combined_order_num'
    }

    def __init__(self, combined_order_id=None, combined_order_ecs_num=None, combined_order_num=None):
        r"""CombinedOrder

        The model defined in huaweicloud sdk

        :param combined_order_id: 组合订单 ID
        :type combined_order_id: str
        :param combined_order_ecs_num: 组合订单中 ECS 服务器数量，当前批量最大为 500。  最小值：1  最大值：1000
        :type combined_order_ecs_num: int
        :param combined_order_num: 组合订单数量。  最小值：1  最大值：1000
        :type combined_order_num: int
        """
        
        

        self._combined_order_id = None
        self._combined_order_ecs_num = None
        self._combined_order_num = None
        self.discriminator = None

        if combined_order_id is not None:
            self.combined_order_id = combined_order_id
        if combined_order_ecs_num is not None:
            self.combined_order_ecs_num = combined_order_ecs_num
        if combined_order_num is not None:
            self.combined_order_num = combined_order_num

    @property
    def combined_order_id(self):
        r"""Gets the combined_order_id of this CombinedOrder.

        组合订单 ID

        :return: The combined_order_id of this CombinedOrder.
        :rtype: str
        """
        return self._combined_order_id

    @combined_order_id.setter
    def combined_order_id(self, combined_order_id):
        r"""Sets the combined_order_id of this CombinedOrder.

        组合订单 ID

        :param combined_order_id: The combined_order_id of this CombinedOrder.
        :type combined_order_id: str
        """
        self._combined_order_id = combined_order_id

    @property
    def combined_order_ecs_num(self):
        r"""Gets the combined_order_ecs_num of this CombinedOrder.

        组合订单中 ECS 服务器数量，当前批量最大为 500。  最小值：1  最大值：1000

        :return: The combined_order_ecs_num of this CombinedOrder.
        :rtype: int
        """
        return self._combined_order_ecs_num

    @combined_order_ecs_num.setter
    def combined_order_ecs_num(self, combined_order_ecs_num):
        r"""Sets the combined_order_ecs_num of this CombinedOrder.

        组合订单中 ECS 服务器数量，当前批量最大为 500。  最小值：1  最大值：1000

        :param combined_order_ecs_num: The combined_order_ecs_num of this CombinedOrder.
        :type combined_order_ecs_num: int
        """
        self._combined_order_ecs_num = combined_order_ecs_num

    @property
    def combined_order_num(self):
        r"""Gets the combined_order_num of this CombinedOrder.

        组合订单数量。  最小值：1  最大值：1000

        :return: The combined_order_num of this CombinedOrder.
        :rtype: int
        """
        return self._combined_order_num

    @combined_order_num.setter
    def combined_order_num(self, combined_order_num):
        r"""Sets the combined_order_num of this CombinedOrder.

        组合订单数量。  最小值：1  最大值：1000

        :param combined_order_num: The combined_order_num of this CombinedOrder.
        :type combined_order_num: int
        """
        self._combined_order_num = combined_order_num

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
        if not isinstance(other, CombinedOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
