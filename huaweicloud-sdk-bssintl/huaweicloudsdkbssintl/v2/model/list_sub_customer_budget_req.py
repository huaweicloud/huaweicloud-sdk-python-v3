# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerBudgetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_ids': 'list[str]',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_ids': 'customer_ids',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_ids=None, indirect_partner_id=None):
        """ListSubCustomerBudgetReq

        The model defined in huaweicloud sdk

        :param customer_ids: |参数名称：客户ID列表| |参数的约束及描述：必填，最大支持100个客户ID，如果其中有存在不是该伙伴的客户ID或者其中有存在与该伙伴不是转售关联类型的客户ID，在响应中不返回该客户信息。|
        :type customer_ids: list[str]
        :param indirect_partner_id: |参数名称：云经销商ID| |参数约束及描述：非必填，范围限制:0-64，如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。|
        :type indirect_partner_id: str
        """
        
        

        self._customer_ids = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_ids = customer_ids
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_ids(self):
        """Gets the customer_ids of this ListSubCustomerBudgetReq.

        |参数名称：客户ID列表| |参数的约束及描述：必填，最大支持100个客户ID，如果其中有存在不是该伙伴的客户ID或者其中有存在与该伙伴不是转售关联类型的客户ID，在响应中不返回该客户信息。|

        :return: The customer_ids of this ListSubCustomerBudgetReq.
        :rtype: list[str]
        """
        return self._customer_ids

    @customer_ids.setter
    def customer_ids(self, customer_ids):
        """Sets the customer_ids of this ListSubCustomerBudgetReq.

        |参数名称：客户ID列表| |参数的约束及描述：必填，最大支持100个客户ID，如果其中有存在不是该伙伴的客户ID或者其中有存在与该伙伴不是转售关联类型的客户ID，在响应中不返回该客户信息。|

        :param customer_ids: The customer_ids of this ListSubCustomerBudgetReq.
        :type customer_ids: list[str]
        """
        self._customer_ids = customer_ids

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListSubCustomerBudgetReq.

        |参数名称：云经销商ID| |参数约束及描述：非必填，范围限制:0-64，如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。|

        :return: The indirect_partner_id of this ListSubCustomerBudgetReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListSubCustomerBudgetReq.

        |参数名称：云经销商ID| |参数约束及描述：非必填，范围限制:0-64，如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。|

        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerBudgetReq.
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
        if not isinstance(other, ListSubCustomerBudgetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
