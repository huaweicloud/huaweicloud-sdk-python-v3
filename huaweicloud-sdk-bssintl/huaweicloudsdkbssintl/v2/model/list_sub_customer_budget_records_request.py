# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerBudgetRecordsRequest:

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
        'indirect_partner_id': 'str',
        'operation_type': 'str',
        'budget_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'indirect_partner_id': 'indirect_partner_id',
        'operation_type': 'operation_type',
        'budget_type': 'budget_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, customer_id=None, indirect_partner_id=None, operation_type=None, budget_type=None, offset=None, limit=None):
        r"""ListSubCustomerBudgetRecordsRequest

        The model defined in huaweicloud sdk

        :param customer_id: |参数名称：客户ID| |参数的约束及描述：该参数必填，范围限制：1-64|
        :type customer_id: str
        :param indirect_partner_id: |参数名称：云经销商ID| |参数的约束及描述：该参数非必填，范围限制：0-64，如果华为云总经销商（一级经销商）需要查询云经销商的子客户预算调整记录，必须携带该字段|
        :type indirect_partner_id: str
        :param operation_type: |参数名称：操作类别| |参数的约束及描述：该参数非必填，SETTING：设置，DELETE：解除关联关系，此参数不携带时，查询所有类型数据。此参数携带值不支持为空或者空串。|
        :type operation_type: str
        :param budget_type: |参数名称：预算模式| |参数的约束及描述：该参数非必填，MONTHLY：月度预算，PACKAGE：一次性预算，此参数不携带时，查询所有类型数据。此参数携带值不支持为空或者空串。|
        :type budget_type: str
        :param offset: |参数名称：偏移量| |参数的约束及描述：该参数非必填，范围限制：0-2147483647，从0开始，默认值为0。|
        :type offset: int
        :param limit: |参数名称：每次查询的数量| |参数的约束及描述：该参数非必填，范围限制：1-100，默认值为10。|
        :type limit: int
        """
        
        

        self._customer_id = None
        self._indirect_partner_id = None
        self._operation_type = None
        self._budget_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.customer_id = customer_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if operation_type is not None:
            self.operation_type = operation_type
        if budget_type is not None:
            self.budget_type = budget_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def customer_id(self):
        r"""Gets the customer_id of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：客户ID| |参数的约束及描述：该参数必填，范围限制：1-64|

        :return: The customer_id of this ListSubCustomerBudgetRecordsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：客户ID| |参数的约束及描述：该参数必填，范围限制：1-64|

        :param customer_id: The customer_id of this ListSubCustomerBudgetRecordsRequest.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：云经销商ID| |参数的约束及描述：该参数非必填，范围限制：0-64，如果华为云总经销商（一级经销商）需要查询云经销商的子客户预算调整记录，必须携带该字段|

        :return: The indirect_partner_id of this ListSubCustomerBudgetRecordsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：云经销商ID| |参数的约束及描述：该参数非必填，范围限制：0-64，如果华为云总经销商（一级经销商）需要查询云经销商的子客户预算调整记录，必须携带该字段|

        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerBudgetRecordsRequest.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：操作类别| |参数的约束及描述：该参数非必填，SETTING：设置，DELETE：解除关联关系，此参数不携带时，查询所有类型数据。此参数携带值不支持为空或者空串。|

        :return: The operation_type of this ListSubCustomerBudgetRecordsRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：操作类别| |参数的约束及描述：该参数非必填，SETTING：设置，DELETE：解除关联关系，此参数不携带时，查询所有类型数据。此参数携带值不支持为空或者空串。|

        :param operation_type: The operation_type of this ListSubCustomerBudgetRecordsRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def budget_type(self):
        r"""Gets the budget_type of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：预算模式| |参数的约束及描述：该参数非必填，MONTHLY：月度预算，PACKAGE：一次性预算，此参数不携带时，查询所有类型数据。此参数携带值不支持为空或者空串。|

        :return: The budget_type of this ListSubCustomerBudgetRecordsRequest.
        :rtype: str
        """
        return self._budget_type

    @budget_type.setter
    def budget_type(self, budget_type):
        r"""Sets the budget_type of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：预算模式| |参数的约束及描述：该参数非必填，MONTHLY：月度预算，PACKAGE：一次性预算，此参数不携带时，查询所有类型数据。此参数携带值不支持为空或者空串。|

        :param budget_type: The budget_type of this ListSubCustomerBudgetRecordsRequest.
        :type budget_type: str
        """
        self._budget_type = budget_type

    @property
    def offset(self):
        r"""Gets the offset of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：偏移量| |参数的约束及描述：该参数非必填，范围限制：0-2147483647，从0开始，默认值为0。|

        :return: The offset of this ListSubCustomerBudgetRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：偏移量| |参数的约束及描述：该参数非必填，范围限制：0-2147483647，从0开始，默认值为0。|

        :param offset: The offset of this ListSubCustomerBudgetRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：每次查询的数量| |参数的约束及描述：该参数非必填，范围限制：1-100，默认值为10。|

        :return: The limit of this ListSubCustomerBudgetRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubCustomerBudgetRecordsRequest.

        |参数名称：每次查询的数量| |参数的约束及描述：该参数非必填，范围限制：1-100，默认值为10。|

        :param limit: The limit of this ListSubCustomerBudgetRecordsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSubCustomerBudgetRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
