# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetrieveEnterpriseMultiAccountCouponReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'coupon_id': 'str',
        'sub_coupon_id': 'str',
        'trans_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'coupon_id': 'coupon_id',
        'sub_coupon_id': 'sub_coupon_id',
        'trans_id': 'trans_id'
    }

    def __init__(self, customer_id=None, coupon_id=None, sub_coupon_id=None, trans_id=None):
        r"""RetrieveEnterpriseMultiAccountCouponReq

        The model defined in huaweicloud sdk

        :param customer_id: 企业子账号的客户ID。您可以调用查询企业子账号列表接口，获取响应参数“id”的返回值。
        :type customer_id: str
        :param coupon_id: 优惠券ID。您可以调用查询企业子账号可回收优惠券列表接口，获取响应参数“coupon_id”的返回值。
        :type coupon_id: str
        :param sub_coupon_id: 子优惠券ID。您可以调用查询企业子账号可回收优惠券列表接口，获取响应参数“sub_coupon_id”的返回值。
        :type sub_coupon_id: str
        :param trans_id: 交易序列号，用于防止重复提交。 如果接口调用方不传，则企业管理微服务后台生成如果接口调用方传入，则请采用UUID保证全局唯一 此参数不携带或携带值为null或携带值为空串时，由系统自动生成。
        :type trans_id: str
        """
        
        

        self._customer_id = None
        self._coupon_id = None
        self._sub_coupon_id = None
        self._trans_id = None
        self.discriminator = None

        self.customer_id = customer_id
        self.coupon_id = coupon_id
        self.sub_coupon_id = sub_coupon_id
        if trans_id is not None:
            self.trans_id = trans_id

    @property
    def customer_id(self):
        r"""Gets the customer_id of this RetrieveEnterpriseMultiAccountCouponReq.

        企业子账号的客户ID。您可以调用查询企业子账号列表接口，获取响应参数“id”的返回值。

        :return: The customer_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this RetrieveEnterpriseMultiAccountCouponReq.

        企业子账号的客户ID。您可以调用查询企业子账号列表接口，获取响应参数“id”的返回值。

        :param customer_id: The customer_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def coupon_id(self):
        r"""Gets the coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.

        优惠券ID。您可以调用查询企业子账号可回收优惠券列表接口，获取响应参数“coupon_id”的返回值。

        :return: The coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        r"""Sets the coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.

        优惠券ID。您可以调用查询企业子账号可回收优惠券列表接口，获取响应参数“coupon_id”的返回值。

        :param coupon_id: The coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :type coupon_id: str
        """
        self._coupon_id = coupon_id

    @property
    def sub_coupon_id(self):
        r"""Gets the sub_coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.

        子优惠券ID。您可以调用查询企业子账号可回收优惠券列表接口，获取响应参数“sub_coupon_id”的返回值。

        :return: The sub_coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :rtype: str
        """
        return self._sub_coupon_id

    @sub_coupon_id.setter
    def sub_coupon_id(self, sub_coupon_id):
        r"""Sets the sub_coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.

        子优惠券ID。您可以调用查询企业子账号可回收优惠券列表接口，获取响应参数“sub_coupon_id”的返回值。

        :param sub_coupon_id: The sub_coupon_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :type sub_coupon_id: str
        """
        self._sub_coupon_id = sub_coupon_id

    @property
    def trans_id(self):
        r"""Gets the trans_id of this RetrieveEnterpriseMultiAccountCouponReq.

        交易序列号，用于防止重复提交。 如果接口调用方不传，则企业管理微服务后台生成如果接口调用方传入，则请采用UUID保证全局唯一 此参数不携带或携带值为null或携带值为空串时，由系统自动生成。

        :return: The trans_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :rtype: str
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        r"""Sets the trans_id of this RetrieveEnterpriseMultiAccountCouponReq.

        交易序列号，用于防止重复提交。 如果接口调用方不传，则企业管理微服务后台生成如果接口调用方传入，则请采用UUID保证全局唯一 此参数不携带或携带值为null或携带值为空串时，由系统自动生成。

        :param trans_id: The trans_id of this RetrieveEnterpriseMultiAccountCouponReq.
        :type trans_id: str
        """
        self._trans_id = trans_id

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
        if not isinstance(other, RetrieveEnterpriseMultiAccountCouponReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
