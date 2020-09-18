# coding: utf-8

import pprint
import re

import six





class QuerySubCustomerListReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account_name': 'str',
        'customer': 'str',
        'offset': 'int',
        'limit': 'int',
        'label': 'str',
        'association_type': 'str',
        'associated_on_begin': 'str',
        'associated_on_end': 'str',
        'customer_id': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'customer': 'customer',
        'offset': 'offset',
        'limit': 'limit',
        'label': 'label',
        'association_type': 'association_type',
        'associated_on_begin': 'associated_on_begin',
        'associated_on_end': 'associated_on_end',
        'customer_id': 'customer_id',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, account_name=None, customer=None, offset=0, limit=10, label=None, association_type=None, associated_on_begin=None, associated_on_end=None, customer_id=None, indirect_partner_id=None):
        """QuerySubCustomerListReq - a model defined in huaweicloud sdk"""
        
        

        self._account_name = None
        self._customer = None
        self._offset = None
        self._limit = None
        self._label = None
        self._association_type = None
        self._associated_on_begin = None
        self._associated_on_end = None
        self._customer_id = None
        self._indirect_partner_id = None
        self.discriminator = None

        if account_name is not None:
            self.account_name = account_name
        if customer is not None:
            self.customer = customer
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if label is not None:
            self.label = label
        if association_type is not None:
            self.association_type = association_type
        if associated_on_begin is not None:
            self.associated_on_begin = associated_on_begin
        if associated_on_end is not None:
            self.associated_on_end = associated_on_end
        if customer_id is not None:
            self.customer_id = customer_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def account_name(self):
        """Gets the account_name of this QuerySubCustomerListReq.

        |参数名称：客户登录名称（如果客户创建了子用户，此处需要填写主账号登录名称。关于主账号和子用户的具体介绍请参见身份管理身份管理中“账号”和“IAM用户”的描述）。支持模糊查询。| |参数约束及描述：客户登录名称（如果客户创建了子用户，此处需要填写主账号登录名称。关于主账号和子用户的具体介绍请参见身份管理身份管理中“账号”和“IAM用户”的描述）。支持模糊查询。|

        :return: The account_name of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this QuerySubCustomerListReq.

        |参数名称：客户登录名称（如果客户创建了子用户，此处需要填写主账号登录名称。关于主账号和子用户的具体介绍请参见身份管理身份管理中“账号”和“IAM用户”的描述）。支持模糊查询。| |参数约束及描述：客户登录名称（如果客户创建了子用户，此处需要填写主账号登录名称。关于主账号和子用户的具体介绍请参见身份管理身份管理中“账号”和“IAM用户”的描述）。支持模糊查询。|

        :param account_name: The account_name of this QuerySubCustomerListReq.
        :type: str
        """
        self._account_name = account_name

    @property
    def customer(self):
        """Gets the customer of this QuerySubCustomerListReq.

        |参数名称：实名认证名称。支持模糊查询。| |参数约束及描述：实名认证名称。支持模糊查询。|

        :return: The customer of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this QuerySubCustomerListReq.

        |参数名称：实名认证名称。支持模糊查询。| |参数约束及描述：实名认证名称。支持模糊查询。|

        :param customer: The customer of this QuerySubCustomerListReq.
        :type: str
        """
        self._customer = customer

    @property
    def offset(self):
        """Gets the offset of this QuerySubCustomerListReq.

        |参数名称：偏移量，从0开始| |参数约束及描述： 偏移量，从0开始|

        :return: The offset of this QuerySubCustomerListReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QuerySubCustomerListReq.

        |参数名称：偏移量，从0开始| |参数约束及描述： 偏移量，从0开始|

        :param offset: The offset of this QuerySubCustomerListReq.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QuerySubCustomerListReq.

        |参数名称：每次查询的数量。默认10，最多100。| |参数约束及描述： 每次查询的数量。默认10，最多100。|

        :return: The limit of this QuerySubCustomerListReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QuerySubCustomerListReq.

        |参数名称：每次查询的数量。默认10，最多100。| |参数约束及描述： 每次查询的数量。默认10，最多100。|

        :param limit: The limit of this QuerySubCustomerListReq.
        :type: int
        """
        self._limit = limit

    @property
    def label(self):
        """Gets the label of this QuerySubCustomerListReq.

        |参数名称：标签，支持模糊查找。| |参数约束及描述：非必填，最大长度64|

        :return: The label of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this QuerySubCustomerListReq.

        |参数名称：标签，支持模糊查找。| |参数约束及描述：非必填，最大长度64|

        :param label: The label of this QuerySubCustomerListReq.
        :type: str
        """
        self._label = label

    @property
    def association_type(self):
        """Gets the association_type of this QuerySubCustomerListReq.

        |参数名称：关联类型1.推荐，2.垫付，3.转售| |参数约束及描述：非必填，最大长度2|

        :return: The association_type of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """Sets the association_type of this QuerySubCustomerListReq.

        |参数名称：关联类型1.推荐，2.垫付，3.转售| |参数约束及描述：非必填，最大长度2|

        :param association_type: The association_type of this QuerySubCustomerListReq.
        :type: str
        """
        self._association_type = association_type

    @property
    def associated_on_begin(self):
        """Gets the associated_on_begin of this QuerySubCustomerListReq.

        |参数名称：关联时间区间段开始，UTC时间。| |参数约束及描述：格式为：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。|

        :return: The associated_on_begin of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._associated_on_begin

    @associated_on_begin.setter
    def associated_on_begin(self, associated_on_begin):
        """Sets the associated_on_begin of this QuerySubCustomerListReq.

        |参数名称：关联时间区间段开始，UTC时间。| |参数约束及描述：格式为：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。|

        :param associated_on_begin: The associated_on_begin of this QuerySubCustomerListReq.
        :type: str
        """
        self._associated_on_begin = associated_on_begin

    @property
    def associated_on_end(self):
        """Gets the associated_on_end of this QuerySubCustomerListReq.

        |参数名称：关联时间区间段结束，UTC时间| |参数约束及描述：格式为：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。|

        :return: The associated_on_end of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._associated_on_end

    @associated_on_end.setter
    def associated_on_end(self, associated_on_end):
        """Sets the associated_on_end of this QuerySubCustomerListReq.

        |参数名称：关联时间区间段结束，UTC时间| |参数约束及描述：格式为：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。|

        :param associated_on_end: The associated_on_end of this QuerySubCustomerListReq.
        :type: str
        """
        self._associated_on_end = associated_on_end

    @property
    def customer_id(self):
        """Gets the customer_id of this QuerySubCustomerListReq.

        |参数名称：子客户ID| |参数约束及描述：非必填，最大长度64|

        :return: The customer_id of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this QuerySubCustomerListReq.

        |参数名称：子客户ID| |参数约束及描述：非必填，最大长度64|

        :param customer_id: The customer_id of this QuerySubCustomerListReq.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this QuerySubCustomerListReq.

        |参数名称：二级渠道商ID| |参数约束及描述：如果想查询二级渠道子客户的列表，该字段必须携带，最大长度64|

        :return: The indirect_partner_id of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this QuerySubCustomerListReq.

        |参数名称：二级渠道商ID| |参数约束及描述：如果想查询二级渠道子客户的列表，该字段必须携带，最大长度64|

        :param indirect_partner_id: The indirect_partner_id of this QuerySubCustomerListReq.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QuerySubCustomerListReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
