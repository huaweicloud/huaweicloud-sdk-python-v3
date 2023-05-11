# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerInformation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer': 'str',
        'account_name': 'str',
        'customer_id': 'str',
        'associated_on': 'str',
        'association_type': 'str',
        'label': 'str',
        'telephone': 'str',
        'verified_status': 'str',
        'country_code': 'str',
        'customer_type': 'int',
        'is_frozen': 'int',
        'account_managers': 'list[AccountManager]',
        'xaccount_id': 'str',
        'xaccount_type': 'str',
        'customer_level': 'str'
    }

    attribute_map = {
        'customer': 'customer',
        'account_name': 'account_name',
        'customer_id': 'customer_id',
        'associated_on': 'associated_on',
        'association_type': 'association_type',
        'label': 'label',
        'telephone': 'telephone',
        'verified_status': 'verified_status',
        'country_code': 'country_code',
        'customer_type': 'customer_type',
        'is_frozen': 'is_frozen',
        'account_managers': 'account_managers',
        'xaccount_id': 'xaccount_id',
        'xaccount_type': 'xaccount_type',
        'customer_level': 'customer_level'
    }

    def __init__(self, customer=None, account_name=None, customer_id=None, associated_on=None, association_type=None, label=None, telephone=None, verified_status=None, country_code=None, customer_type=None, is_frozen=None, account_managers=None, xaccount_id=None, xaccount_type=None, customer_level=None):
        """CustomerInformation

        The model defined in huaweicloud sdk

        :param customer: 实名认证名称。
        :type customer: str
        :param account_name: 客户经理登录名称。
        :type account_name: str
        :param customer_id: 客户账号ID。
        :type customer_id: str
        :param associated_on: 客户和伙伴关联时间。 UTC时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，如“2019-05-06T08:05:01Z”，其中，HH范围是0～23，mm和ss范围是0～59。
        :type associated_on: str
        :param association_type: 关联类型： 1：顾问销售2：代售
        :type association_type: str
        :param label: 标签。
        :type label: str
        :param telephone: 客户电话号码。
        :type telephone: str
        :param verified_status: 实名认证状态： -1：未实名认证0：实名认证审核中1：实名认证不通过2：已实名认证
        :type verified_status: str
        :param country_code: 国家码，电话号码的国家码前缀。 例如：中国 0086。
        :type country_code: str
        :param customer_type: 客户类型： -1：无类型0：个人1：企业 客户刚注册的时候，没有具体的客户类型，为“-1：无类型”，客户可以在账号中心通过设置客户类型或者在实名认证的时候，选择对应的企业/个人实名认证来决定自己的类型。
        :type customer_type: int
        :param is_frozen: 是否冻结： 0：否1：客户账号冻结2：客户账号和资源冻结 该字段预留。
        :type is_frozen: int
        :param account_managers: 该客户对应的客户经理信息，目前只支持1个，具体参见表2。
        :type account_managers: list[:class:`huaweicloudsdkbss.v2.AccountManager`]
        :param xaccount_id: 伙伴销售平台的用户唯一标识，该标识的具体值由伙伴分配。
        :type xaccount_id: str
        :param xaccount_type: 华为分配给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。
        :type xaccount_type: str
        :param customer_level: 客户等级。具体等级体系和权益请参见客户等级体系。 V0V1V2V3V4V5
        :type customer_level: str
        """
        
        

        self._customer = None
        self._account_name = None
        self._customer_id = None
        self._associated_on = None
        self._association_type = None
        self._label = None
        self._telephone = None
        self._verified_status = None
        self._country_code = None
        self._customer_type = None
        self._is_frozen = None
        self._account_managers = None
        self._xaccount_id = None
        self._xaccount_type = None
        self._customer_level = None
        self.discriminator = None

        if customer is not None:
            self.customer = customer
        self.account_name = account_name
        self.customer_id = customer_id
        if associated_on is not None:
            self.associated_on = associated_on
        if association_type is not None:
            self.association_type = association_type
        if label is not None:
            self.label = label
        if telephone is not None:
            self.telephone = telephone
        if verified_status is not None:
            self.verified_status = verified_status
        if country_code is not None:
            self.country_code = country_code
        if customer_type is not None:
            self.customer_type = customer_type
        if is_frozen is not None:
            self.is_frozen = is_frozen
        if account_managers is not None:
            self.account_managers = account_managers
        if xaccount_id is not None:
            self.xaccount_id = xaccount_id
        if xaccount_type is not None:
            self.xaccount_type = xaccount_type
        if customer_level is not None:
            self.customer_level = customer_level

    @property
    def customer(self):
        """Gets the customer of this CustomerInformation.

        实名认证名称。

        :return: The customer of this CustomerInformation.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerInformation.

        实名认证名称。

        :param customer: The customer of this CustomerInformation.
        :type customer: str
        """
        self._customer = customer

    @property
    def account_name(self):
        """Gets the account_name of this CustomerInformation.

        客户经理登录名称。

        :return: The account_name of this CustomerInformation.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this CustomerInformation.

        客户经理登录名称。

        :param account_name: The account_name of this CustomerInformation.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerInformation.

        客户账号ID。

        :return: The customer_id of this CustomerInformation.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerInformation.

        客户账号ID。

        :param customer_id: The customer_id of this CustomerInformation.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def associated_on(self):
        """Gets the associated_on of this CustomerInformation.

        客户和伙伴关联时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”，其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The associated_on of this CustomerInformation.
        :rtype: str
        """
        return self._associated_on

    @associated_on.setter
    def associated_on(self, associated_on):
        """Sets the associated_on of this CustomerInformation.

        客户和伙伴关联时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”，其中，HH范围是0～23，mm和ss范围是0～59。

        :param associated_on: The associated_on of this CustomerInformation.
        :type associated_on: str
        """
        self._associated_on = associated_on

    @property
    def association_type(self):
        """Gets the association_type of this CustomerInformation.

        关联类型： 1：顾问销售2：代售

        :return: The association_type of this CustomerInformation.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """Sets the association_type of this CustomerInformation.

        关联类型： 1：顾问销售2：代售

        :param association_type: The association_type of this CustomerInformation.
        :type association_type: str
        """
        self._association_type = association_type

    @property
    def label(self):
        """Gets the label of this CustomerInformation.

        标签。

        :return: The label of this CustomerInformation.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CustomerInformation.

        标签。

        :param label: The label of this CustomerInformation.
        :type label: str
        """
        self._label = label

    @property
    def telephone(self):
        """Gets the telephone of this CustomerInformation.

        客户电话号码。

        :return: The telephone of this CustomerInformation.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this CustomerInformation.

        客户电话号码。

        :param telephone: The telephone of this CustomerInformation.
        :type telephone: str
        """
        self._telephone = telephone

    @property
    def verified_status(self):
        """Gets the verified_status of this CustomerInformation.

        实名认证状态： -1：未实名认证0：实名认证审核中1：实名认证不通过2：已实名认证

        :return: The verified_status of this CustomerInformation.
        :rtype: str
        """
        return self._verified_status

    @verified_status.setter
    def verified_status(self, verified_status):
        """Sets the verified_status of this CustomerInformation.

        实名认证状态： -1：未实名认证0：实名认证审核中1：实名认证不通过2：已实名认证

        :param verified_status: The verified_status of this CustomerInformation.
        :type verified_status: str
        """
        self._verified_status = verified_status

    @property
    def country_code(self):
        """Gets the country_code of this CustomerInformation.

        国家码，电话号码的国家码前缀。 例如：中国 0086。

        :return: The country_code of this CustomerInformation.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this CustomerInformation.

        国家码，电话号码的国家码前缀。 例如：中国 0086。

        :param country_code: The country_code of this CustomerInformation.
        :type country_code: str
        """
        self._country_code = country_code

    @property
    def customer_type(self):
        """Gets the customer_type of this CustomerInformation.

        客户类型： -1：无类型0：个人1：企业 客户刚注册的时候，没有具体的客户类型，为“-1：无类型”，客户可以在账号中心通过设置客户类型或者在实名认证的时候，选择对应的企业/个人实名认证来决定自己的类型。

        :return: The customer_type of this CustomerInformation.
        :rtype: int
        """
        return self._customer_type

    @customer_type.setter
    def customer_type(self, customer_type):
        """Sets the customer_type of this CustomerInformation.

        客户类型： -1：无类型0：个人1：企业 客户刚注册的时候，没有具体的客户类型，为“-1：无类型”，客户可以在账号中心通过设置客户类型或者在实名认证的时候，选择对应的企业/个人实名认证来决定自己的类型。

        :param customer_type: The customer_type of this CustomerInformation.
        :type customer_type: int
        """
        self._customer_type = customer_type

    @property
    def is_frozen(self):
        """Gets the is_frozen of this CustomerInformation.

        是否冻结： 0：否1：客户账号冻结2：客户账号和资源冻结 该字段预留。

        :return: The is_frozen of this CustomerInformation.
        :rtype: int
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this CustomerInformation.

        是否冻结： 0：否1：客户账号冻结2：客户账号和资源冻结 该字段预留。

        :param is_frozen: The is_frozen of this CustomerInformation.
        :type is_frozen: int
        """
        self._is_frozen = is_frozen

    @property
    def account_managers(self):
        """Gets the account_managers of this CustomerInformation.

        该客户对应的客户经理信息，目前只支持1个，具体参见表2。

        :return: The account_managers of this CustomerInformation.
        :rtype: list[:class:`huaweicloudsdkbss.v2.AccountManager`]
        """
        return self._account_managers

    @account_managers.setter
    def account_managers(self, account_managers):
        """Sets the account_managers of this CustomerInformation.

        该客户对应的客户经理信息，目前只支持1个，具体参见表2。

        :param account_managers: The account_managers of this CustomerInformation.
        :type account_managers: list[:class:`huaweicloudsdkbss.v2.AccountManager`]
        """
        self._account_managers = account_managers

    @property
    def xaccount_id(self):
        """Gets the xaccount_id of this CustomerInformation.

        伙伴销售平台的用户唯一标识，该标识的具体值由伙伴分配。

        :return: The xaccount_id of this CustomerInformation.
        :rtype: str
        """
        return self._xaccount_id

    @xaccount_id.setter
    def xaccount_id(self, xaccount_id):
        """Sets the xaccount_id of this CustomerInformation.

        伙伴销售平台的用户唯一标识，该标识的具体值由伙伴分配。

        :param xaccount_id: The xaccount_id of this CustomerInformation.
        :type xaccount_id: str
        """
        self._xaccount_id = xaccount_id

    @property
    def xaccount_type(self):
        """Gets the xaccount_type of this CustomerInformation.

        华为分配给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :return: The xaccount_type of this CustomerInformation.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        """Sets the xaccount_type of this CustomerInformation.

        华为分配给合作伙伴的平台标识。 该标识的具体值由华为分配。获取方法请参见如何获取xaccountType的取值。

        :param xaccount_type: The xaccount_type of this CustomerInformation.
        :type xaccount_type: str
        """
        self._xaccount_type = xaccount_type

    @property
    def customer_level(self):
        """Gets the customer_level of this CustomerInformation.

        客户等级。具体等级体系和权益请参见客户等级体系。 V0V1V2V3V4V5

        :return: The customer_level of this CustomerInformation.
        :rtype: str
        """
        return self._customer_level

    @customer_level.setter
    def customer_level(self, customer_level):
        """Sets the customer_level of this CustomerInformation.

        客户等级。具体等级体系和权益请参见客户等级体系。 V0V1V2V3V4V5

        :param customer_level: The customer_level of this CustomerInformation.
        :type customer_level: str
        """
        self._customer_level = customer_level

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
        if not isinstance(other, CustomerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
