# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'object',
        'new_resource_spec_code': 'str',
        'attach_disk_size': 'int',
        'is_auto_pay': 'int'
    }

    attribute_map = {
        'server_id': 'server_id',
        'new_resource_spec_code': 'new_resource_spec_code',
        'attach_disk_size': 'attach_disk_size',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, server_id=None, new_resource_spec_code=None, attach_disk_size=None, is_auto_pay=None):
        """ChangeInstanceRequestBody

        The model defined in huaweicloud sdk

        :param server_id: 
        :type server_id: object
        :param new_resource_spec_code: 待变更云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50  已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。
        :type new_resource_spec_code: str
        :param attach_disk_size: 附加磁盘大小。单位TB  &gt; 说明： 附加磁盘和规格自带磁盘大小不能超过300TB。
        :type attach_disk_size: int
        :param is_auto_pay: 是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”
        :type is_auto_pay: int
        """
        
        

        self._server_id = None
        self._new_resource_spec_code = None
        self._attach_disk_size = None
        self._is_auto_pay = None
        self.discriminator = None

        self.server_id = server_id
        if new_resource_spec_code is not None:
            self.new_resource_spec_code = new_resource_spec_code
        if attach_disk_size is not None:
            self.attach_disk_size = attach_disk_size
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def server_id(self):
        """Gets the server_id of this ChangeInstanceRequestBody.

        :return: The server_id of this ChangeInstanceRequestBody.
        :rtype: object
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ChangeInstanceRequestBody.

        :param server_id: The server_id of this ChangeInstanceRequestBody.
        :type server_id: object
        """
        self._server_id = server_id

    @property
    def new_resource_spec_code(self):
        """Gets the new_resource_spec_code of this ChangeInstanceRequestBody.

        待变更云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50  已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :return: The new_resource_spec_code of this ChangeInstanceRequestBody.
        :rtype: str
        """
        return self._new_resource_spec_code

    @new_resource_spec_code.setter
    def new_resource_spec_code(self, new_resource_spec_code):
        """Sets the new_resource_spec_code of this ChangeInstanceRequestBody.

        待变更云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50  已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :param new_resource_spec_code: The new_resource_spec_code of this ChangeInstanceRequestBody.
        :type new_resource_spec_code: str
        """
        self._new_resource_spec_code = new_resource_spec_code

    @property
    def attach_disk_size(self):
        """Gets the attach_disk_size of this ChangeInstanceRequestBody.

        附加磁盘大小。单位TB  > 说明： 附加磁盘和规格自带磁盘大小不能超过300TB。

        :return: The attach_disk_size of this ChangeInstanceRequestBody.
        :rtype: int
        """
        return self._attach_disk_size

    @attach_disk_size.setter
    def attach_disk_size(self, attach_disk_size):
        """Sets the attach_disk_size of this ChangeInstanceRequestBody.

        附加磁盘大小。单位TB  > 说明： 附加磁盘和规格自带磁盘大小不能超过300TB。

        :param attach_disk_size: The attach_disk_size of this ChangeInstanceRequestBody.
        :type attach_disk_size: int
        """
        self._attach_disk_size = attach_disk_size

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ChangeInstanceRequestBody.

        是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”

        :return: The is_auto_pay of this ChangeInstanceRequestBody.
        :rtype: int
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ChangeInstanceRequestBody.

        是否自动支付，下单订购后，是否自动从客户的华为云账户中支付，而不需要客户手动去进行支付。 - 1：是（会自动选择折扣和优惠券进行优惠，然后自动从客户华为云账户中支付），自动支付失败后会生成订单成功(该订单应付金额是优惠后金额)、但订单状态为“待支付”，等待客户手动支付(手动支付时，客户还可以修改系统自动选择的折扣和优惠券) - 0：否（需要客户手动去支付，客户可以选择折扣和优惠券。）  默认值为“0”

        :param is_auto_pay: The is_auto_pay of this ChangeInstanceRequestBody.
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
        if not isinstance(other, ChangeInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
