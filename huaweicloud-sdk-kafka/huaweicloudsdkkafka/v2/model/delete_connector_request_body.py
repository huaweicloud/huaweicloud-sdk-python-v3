# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConnectorRequestBody:

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
        'csb_instance_product_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'csb_instance_product_id': 'csb_instance_product_id'
    }

    def __init__(self, order_id=None, csb_instance_product_id=None):
        """DeleteConnectorRequestBody

        The model defined in huaweicloud sdk

        :param order_id: cbc生成实例变更的订单 按需实例不传入此参数。 包周期实例传入删除connector时生成的订单，由cbc调用时传入。
        :type order_id: str
        :param csb_instance_product_id: 包周期实例变更时的product id 按需实例不传入此参数。 包周期实例传入对变更实例规格的product，由cbc调用时传入。 
        :type csb_instance_product_id: str
        """
        
        

        self._order_id = None
        self._csb_instance_product_id = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if csb_instance_product_id is not None:
            self.csb_instance_product_id = csb_instance_product_id

    @property
    def order_id(self):
        """Gets the order_id of this DeleteConnectorRequestBody.

        cbc生成实例变更的订单 按需实例不传入此参数。 包周期实例传入删除connector时生成的订单，由cbc调用时传入。

        :return: The order_id of this DeleteConnectorRequestBody.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this DeleteConnectorRequestBody.

        cbc生成实例变更的订单 按需实例不传入此参数。 包周期实例传入删除connector时生成的订单，由cbc调用时传入。

        :param order_id: The order_id of this DeleteConnectorRequestBody.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def csb_instance_product_id(self):
        """Gets the csb_instance_product_id of this DeleteConnectorRequestBody.

        包周期实例变更时的product id 按需实例不传入此参数。 包周期实例传入对变更实例规格的product，由cbc调用时传入。 

        :return: The csb_instance_product_id of this DeleteConnectorRequestBody.
        :rtype: str
        """
        return self._csb_instance_product_id

    @csb_instance_product_id.setter
    def csb_instance_product_id(self, csb_instance_product_id):
        """Sets the csb_instance_product_id of this DeleteConnectorRequestBody.

        包周期实例变更时的product id 按需实例不传入此参数。 包周期实例传入对变更实例规格的product，由cbc调用时传入。 

        :param csb_instance_product_id: The csb_instance_product_id of this DeleteConnectorRequestBody.
        :type csb_instance_product_id: str
        """
        self._csb_instance_product_id = csb_instance_product_id

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
        if not isinstance(other, DeleteConnectorRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
