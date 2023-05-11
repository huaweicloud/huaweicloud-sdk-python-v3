# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCustomersBalancesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_infos': 'list[CustomerInfoV2]',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_infos': 'customer_infos',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_infos=None, indirect_partner_id=None):
        """QueryCustomersBalancesReq

        The model defined in huaweicloud sdk

        :param customer_infos: 客户信息列表。 具体请参见表1。
        :type customer_infos: list[:class:`huaweicloudsdkbss.v2.CustomerInfoV2`]
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  华为云总经销商（一级经销商）查询云经销商（二级经销商）子客户的账户余额时，需要携带该参数。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        """
        
        

        self._customer_infos = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_infos = customer_infos
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_infos(self):
        """Gets the customer_infos of this QueryCustomersBalancesReq.

        客户信息列表。 具体请参见表1。

        :return: The customer_infos of this QueryCustomersBalancesReq.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CustomerInfoV2`]
        """
        return self._customer_infos

    @customer_infos.setter
    def customer_infos(self, customer_infos):
        """Sets the customer_infos of this QueryCustomersBalancesReq.

        客户信息列表。 具体请参见表1。

        :param customer_infos: The customer_infos of this QueryCustomersBalancesReq.
        :type customer_infos: list[:class:`huaweicloudsdkbss.v2.CustomerInfoV2`]
        """
        self._customer_infos = customer_infos

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QueryCustomersBalancesReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  华为云总经销商（一级经销商）查询云经销商（二级经销商）子客户的账户余额时，需要携带该参数。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this QueryCustomersBalancesReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QueryCustomersBalancesReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。  华为云总经销商（一级经销商）查询云经销商（二级经销商）子客户的账户余额时，需要携带该参数。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this QueryCustomersBalancesReq.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, QueryCustomersBalancesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
