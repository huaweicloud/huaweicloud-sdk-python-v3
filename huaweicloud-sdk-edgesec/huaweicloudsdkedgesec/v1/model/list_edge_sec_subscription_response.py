# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeSecSubscriptionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'waf_domain_num': 'int',
        'waf_rule_num': 'int',
        'ddos_domain_num': 'int',
        'product_infos': 'list[EdgeSecProductResource]'
    }

    attribute_map = {
        'waf_domain_num': 'waf_domain_num',
        'waf_rule_num': 'waf_rule_num',
        'ddos_domain_num': 'ddos_domain_num',
        'product_infos': 'product_infos'
    }

    def __init__(self, waf_domain_num=None, waf_rule_num=None, ddos_domain_num=None, product_infos=None):
        """ListEdgeSecSubscriptionResponse

        The model defined in huaweicloud sdk

        :param waf_domain_num: 已经添加的WAF防护域名数量
        :type waf_domain_num: int
        :param waf_rule_num: 已经添加的WAF IP黑白规则数量
        :type waf_rule_num: int
        :param ddos_domain_num: 已经添加的DDoS防护域名数量
        :type ddos_domain_num: int
        :param product_infos: 产品信息
        :type product_infos: list[:class:`huaweicloudsdkedgesec.v1.EdgeSecProductResource`]
        """
        
        super(ListEdgeSecSubscriptionResponse, self).__init__()

        self._waf_domain_num = None
        self._waf_rule_num = None
        self._ddos_domain_num = None
        self._product_infos = None
        self.discriminator = None

        if waf_domain_num is not None:
            self.waf_domain_num = waf_domain_num
        if waf_rule_num is not None:
            self.waf_rule_num = waf_rule_num
        if ddos_domain_num is not None:
            self.ddos_domain_num = ddos_domain_num
        if product_infos is not None:
            self.product_infos = product_infos

    @property
    def waf_domain_num(self):
        """Gets the waf_domain_num of this ListEdgeSecSubscriptionResponse.

        已经添加的WAF防护域名数量

        :return: The waf_domain_num of this ListEdgeSecSubscriptionResponse.
        :rtype: int
        """
        return self._waf_domain_num

    @waf_domain_num.setter
    def waf_domain_num(self, waf_domain_num):
        """Sets the waf_domain_num of this ListEdgeSecSubscriptionResponse.

        已经添加的WAF防护域名数量

        :param waf_domain_num: The waf_domain_num of this ListEdgeSecSubscriptionResponse.
        :type waf_domain_num: int
        """
        self._waf_domain_num = waf_domain_num

    @property
    def waf_rule_num(self):
        """Gets the waf_rule_num of this ListEdgeSecSubscriptionResponse.

        已经添加的WAF IP黑白规则数量

        :return: The waf_rule_num of this ListEdgeSecSubscriptionResponse.
        :rtype: int
        """
        return self._waf_rule_num

    @waf_rule_num.setter
    def waf_rule_num(self, waf_rule_num):
        """Sets the waf_rule_num of this ListEdgeSecSubscriptionResponse.

        已经添加的WAF IP黑白规则数量

        :param waf_rule_num: The waf_rule_num of this ListEdgeSecSubscriptionResponse.
        :type waf_rule_num: int
        """
        self._waf_rule_num = waf_rule_num

    @property
    def ddos_domain_num(self):
        """Gets the ddos_domain_num of this ListEdgeSecSubscriptionResponse.

        已经添加的DDoS防护域名数量

        :return: The ddos_domain_num of this ListEdgeSecSubscriptionResponse.
        :rtype: int
        """
        return self._ddos_domain_num

    @ddos_domain_num.setter
    def ddos_domain_num(self, ddos_domain_num):
        """Sets the ddos_domain_num of this ListEdgeSecSubscriptionResponse.

        已经添加的DDoS防护域名数量

        :param ddos_domain_num: The ddos_domain_num of this ListEdgeSecSubscriptionResponse.
        :type ddos_domain_num: int
        """
        self._ddos_domain_num = ddos_domain_num

    @property
    def product_infos(self):
        """Gets the product_infos of this ListEdgeSecSubscriptionResponse.

        产品信息

        :return: The product_infos of this ListEdgeSecSubscriptionResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.EdgeSecProductResource`]
        """
        return self._product_infos

    @product_infos.setter
    def product_infos(self, product_infos):
        """Sets the product_infos of this ListEdgeSecSubscriptionResponse.

        产品信息

        :param product_infos: The product_infos of this ListEdgeSecSubscriptionResponse.
        :type product_infos: list[:class:`huaweicloudsdkedgesec.v1.EdgeSecProductResource`]
        """
        self._product_infos = product_infos

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
        if not isinstance(other, ListEdgeSecSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
