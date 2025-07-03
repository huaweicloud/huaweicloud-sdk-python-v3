# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartKibanaPublicReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_size': 'int',
        'elb_white_list': 'StartKibanaPublicReqElbWhitelist',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'eip_size': 'eip_size',
        'elb_white_list': 'elb_white_list',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, eip_size=None, elb_white_list=None, is_auto_pay=None):
        r"""StartKibanaPublicReq

        The model defined in huaweicloud sdk

        :param eip_size: 带宽。单位：Mbit/s
        :type eip_size: int
        :param elb_white_list: 
        :type elb_white_list: :class:`huaweicloudsdkcss.v1.StartKibanaPublicReqElbWhitelist`
        :param is_auto_pay: 是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。  - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。 - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。
        :type is_auto_pay: int
        """
        
        

        self._eip_size = None
        self._elb_white_list = None
        self._is_auto_pay = None
        self.discriminator = None

        self.eip_size = eip_size
        self.elb_white_list = elb_white_list
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def eip_size(self):
        r"""Gets the eip_size of this StartKibanaPublicReq.

        带宽。单位：Mbit/s

        :return: The eip_size of this StartKibanaPublicReq.
        :rtype: int
        """
        return self._eip_size

    @eip_size.setter
    def eip_size(self, eip_size):
        r"""Sets the eip_size of this StartKibanaPublicReq.

        带宽。单位：Mbit/s

        :param eip_size: The eip_size of this StartKibanaPublicReq.
        :type eip_size: int
        """
        self._eip_size = eip_size

    @property
    def elb_white_list(self):
        r"""Gets the elb_white_list of this StartKibanaPublicReq.

        :return: The elb_white_list of this StartKibanaPublicReq.
        :rtype: :class:`huaweicloudsdkcss.v1.StartKibanaPublicReqElbWhitelist`
        """
        return self._elb_white_list

    @elb_white_list.setter
    def elb_white_list(self, elb_white_list):
        r"""Sets the elb_white_list of this StartKibanaPublicReq.

        :param elb_white_list: The elb_white_list of this StartKibanaPublicReq.
        :type elb_white_list: :class:`huaweicloudsdkcss.v1.StartKibanaPublicReqElbWhitelist`
        """
        self._elb_white_list = elb_white_list

    @property
    def is_auto_pay(self):
        r"""Gets the is_auto_pay of this StartKibanaPublicReq.

        是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。  - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。 - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :return: The is_auto_pay of this StartKibanaPublicReq.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        r"""Sets the is_auto_pay of this StartKibanaPublicReq.

        是否自动支付。下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。该参数适用于包周期集群。  - 1: 是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券)。 - 0: 否（需要客户手动去支付，客户可以选择折扣和优惠券）。默认值为“0”。

        :param is_auto_pay: The is_auto_pay of this StartKibanaPublicReq.
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
        if not isinstance(other, StartKibanaPublicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
