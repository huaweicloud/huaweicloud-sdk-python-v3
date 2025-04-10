# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

    def __init__(self, account_name=None, customer=None, offset=None, limit=None, label=None, association_type=None, associated_on_begin=None, associated_on_end=None, customer_id=None, indirect_partner_id=None):
        r"""QuerySubCustomerListReq

        The model defined in huaweicloud sdk

        :param account_name: 客户登录名称（如果客户创建了IAM用户，此处需要填写主账号登录名称。关于主账号和IAM用户的具体介绍请参见身份管理中“账号”和“IAM用户”的描述）。 支持模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type account_name: str
        :param customer: 客户的实名认证名称，支持模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type customer: str
        :param offset: 偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset &#x3D; 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。
        :type offset: int
        :param limit: 每次查询的客户数量。默认值为10。
        :type limit: int
        :param label: 标签，支持模糊查找。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询；不支持英文大小写模糊匹配查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type label: str
        :param association_type: 关联类型： 1：顾问销售2：代售 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type association_type: str
        :param associated_on_begin: 关联时间区间段开始，UTC时间。 格式：YYYY-MM-DD&#39;T&#39;hh:mm:ss&#39;Z&#39;，例如“2019-05-06T08:05:01Z”。 此参数不携带或携带值为null时，不作为筛选条件，不支持携带值为空串。
        :type associated_on_begin: str
        :param associated_on_end: 关联时间区间段结束，UTC时间。 格式：YYYY-MM-DD&#39;T&#39;hh:mm:ss&#39;Z&#39;，例如“2019-05-06T08:05:01Z”。 此参数不携带或携带值为null时，不作为筛选条件，不支持携带值为空串。
        :type associated_on_end: str
        :param customer_id: 客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id，或者可以从创建客户接口的响应获取domain_id。此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。
        :type customer_id: str
        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。
        :type indirect_partner_id: str
        """
        
        

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
        r"""Gets the account_name of this QuerySubCustomerListReq.

        客户登录名称（如果客户创建了IAM用户，此处需要填写主账号登录名称。关于主账号和IAM用户的具体介绍请参见身份管理中“账号”和“IAM用户”的描述）。 支持模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The account_name of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this QuerySubCustomerListReq.

        客户登录名称（如果客户创建了IAM用户，此处需要填写主账号登录名称。关于主账号和IAM用户的具体介绍请参见身份管理中“账号”和“IAM用户”的描述）。 支持模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param account_name: The account_name of this QuerySubCustomerListReq.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def customer(self):
        r"""Gets the customer of this QuerySubCustomerListReq.

        客户的实名认证名称，支持模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The customer of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        r"""Sets the customer of this QuerySubCustomerListReq.

        客户的实名认证名称，支持模糊查询。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param customer: The customer of this QuerySubCustomerListReq.
        :type customer: str
        """
        self._customer = customer

    @property
    def offset(self):
        r"""Gets the offset of this QuerySubCustomerListReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :return: The offset of this QuerySubCustomerListReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QuerySubCustomerListReq.

        偏移量，从0开始。默认值为0。  说明： offset用于分页处理，如不涉及分页，请使用默认值0。offset表示相对于满足条件的第一个数据的偏移量。如offset = 1，则返回满足条件的第二个数据至最后一个数据。 例如，满足查询条件的结果共10条数据，limit取值为10，offset取值为1，则返回的数据为2~10，第一条数据不返回。

        :param offset: The offset of this QuerySubCustomerListReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this QuerySubCustomerListReq.

        每次查询的客户数量。默认值为10。

        :return: The limit of this QuerySubCustomerListReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QuerySubCustomerListReq.

        每次查询的客户数量。默认值为10。

        :param limit: The limit of this QuerySubCustomerListReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def label(self):
        r"""Gets the label of this QuerySubCustomerListReq.

        标签，支持模糊查找。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询；不支持英文大小写模糊匹配查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The label of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this QuerySubCustomerListReq.

        标签，支持模糊查找。仅支持前缀匹配、后缀匹配、中间匹配；不支持携带空格查询；不支持英文大小写模糊匹配查询。 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param label: The label of this QuerySubCustomerListReq.
        :type label: str
        """
        self._label = label

    @property
    def association_type(self):
        r"""Gets the association_type of this QuerySubCustomerListReq.

        关联类型： 1：顾问销售2：代售 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The association_type of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        r"""Sets the association_type of this QuerySubCustomerListReq.

        关联类型： 1：顾问销售2：代售 此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param association_type: The association_type of this QuerySubCustomerListReq.
        :type association_type: str
        """
        self._association_type = association_type

    @property
    def associated_on_begin(self):
        r"""Gets the associated_on_begin of this QuerySubCustomerListReq.

        关联时间区间段开始，UTC时间。 格式：YYYY-MM-DD'T'hh:mm:ss'Z'，例如“2019-05-06T08:05:01Z”。 此参数不携带或携带值为null时，不作为筛选条件，不支持携带值为空串。

        :return: The associated_on_begin of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._associated_on_begin

    @associated_on_begin.setter
    def associated_on_begin(self, associated_on_begin):
        r"""Sets the associated_on_begin of this QuerySubCustomerListReq.

        关联时间区间段开始，UTC时间。 格式：YYYY-MM-DD'T'hh:mm:ss'Z'，例如“2019-05-06T08:05:01Z”。 此参数不携带或携带值为null时，不作为筛选条件，不支持携带值为空串。

        :param associated_on_begin: The associated_on_begin of this QuerySubCustomerListReq.
        :type associated_on_begin: str
        """
        self._associated_on_begin = associated_on_begin

    @property
    def associated_on_end(self):
        r"""Gets the associated_on_end of this QuerySubCustomerListReq.

        关联时间区间段结束，UTC时间。 格式：YYYY-MM-DD'T'hh:mm:ss'Z'，例如“2019-05-06T08:05:01Z”。 此参数不携带或携带值为null时，不作为筛选条件，不支持携带值为空串。

        :return: The associated_on_end of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._associated_on_end

    @associated_on_end.setter
    def associated_on_end(self, associated_on_end):
        r"""Sets the associated_on_end of this QuerySubCustomerListReq.

        关联时间区间段结束，UTC时间。 格式：YYYY-MM-DD'T'hh:mm:ss'Z'，例如“2019-05-06T08:05:01Z”。 此参数不携带或携带值为null时，不作为筛选条件，不支持携带值为空串。

        :param associated_on_end: The associated_on_end of this QuerySubCustomerListReq.
        :type associated_on_end: str
        """
        self._associated_on_end = associated_on_end

    @property
    def customer_id(self):
        r"""Gets the customer_id of this QuerySubCustomerListReq.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id，或者可以从创建客户接口的响应获取domain_id。此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :return: The customer_id of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        r"""Sets the customer_id of this QuerySubCustomerListReq.

        客户账号ID。您可以调用[查询客户列表](https://support.huaweicloud.com/api-bpconsole/mc_00021.html)接口获取customer_id，或者可以从创建客户接口的响应获取domain_id。此参数不携带或携带值为空串或携带值为null时，不作为筛选条件。

        :param customer_id: The customer_id of this QuerySubCustomerListReq.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def indirect_partner_id(self):
        r"""Gets the indirect_partner_id of this QuerySubCustomerListReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :return: The indirect_partner_id of this QuerySubCustomerListReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        r"""Sets the indirect_partner_id of this QuerySubCustomerListReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。如果需要查询云经销商的子客户列表，必须携带该字段。除此之外，此参数不做处理。

        :param indirect_partner_id: The indirect_partner_id of this QuerySubCustomerListReq.
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
        if not isinstance(other, QuerySubCustomerListReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
