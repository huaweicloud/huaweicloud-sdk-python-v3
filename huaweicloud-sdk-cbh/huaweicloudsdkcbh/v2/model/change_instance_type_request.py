# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'availability_zone': 'str',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'server_id': 'server_id',
        'availability_zone': 'availability_zone',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, server_id=None, availability_zone=None, is_auto_pay=None):
        r"""ChangeInstanceTypeRequest

        The model defined in huaweicloud sdk

        :param server_id: 实例id
        :type server_id: str
        :param availability_zone: 可用分区名称。  可参考接口\&quot;获取服务可用区\&quot;获取
        :type availability_zone: str
        :param is_auto_pay: 是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”
        :type is_auto_pay: int
        """
        
        

        self._server_id = None
        self._availability_zone = None
        self._is_auto_pay = None
        self.discriminator = None

        self.server_id = server_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def server_id(self):
        r"""Gets the server_id of this ChangeInstanceTypeRequest.

        实例id

        :return: The server_id of this ChangeInstanceTypeRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ChangeInstanceTypeRequest.

        实例id

        :param server_id: The server_id of this ChangeInstanceTypeRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ChangeInstanceTypeRequest.

        可用分区名称。  可参考接口\"获取服务可用区\"获取

        :return: The availability_zone of this ChangeInstanceTypeRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ChangeInstanceTypeRequest.

        可用分区名称。  可参考接口\"获取服务可用区\"获取

        :param availability_zone: The availability_zone of this ChangeInstanceTypeRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this ChangeInstanceTypeRequest.

        是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”

        :return: The is_auto_pay of this ChangeInstanceTypeRequest.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this ChangeInstanceTypeRequest.

        是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”

        :param is_auto_pay: The is_auto_pay of this ChangeInstanceTypeRequest.
        :type is_auto_pay: int
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, ChangeInstanceTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
