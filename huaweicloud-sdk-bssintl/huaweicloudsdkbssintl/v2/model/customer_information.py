# coding: utf-8

import pprint
import re

import six





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
        """CustomerInformation - a model defined in huaweicloud sdk"""
        
        

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

        |参数名称：实名认证名称。虚拟账号下，该字段无效。| |参数约束及描述：实名认证名称。虚拟账号下，该字段无效。|

        :return: The customer of this CustomerInformation.
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerInformation.

        |参数名称：实名认证名称。虚拟账号下，该字段无效。| |参数约束及描述：实名认证名称。虚拟账号下，该字段无效。|

        :param customer: The customer of this CustomerInformation.
        :type: str
        """
        self._customer = customer

    @property
    def account_name(self):
        """Gets the account_name of this CustomerInformation.

        |参数名称：客户登录名称（如果客户创建了子用户，此处返回主账号登录名称）。| |参数约束及描述：客户登录名称（如果客户创建了子用户，此处返回主账号登录名称）。|

        :return: The account_name of this CustomerInformation.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this CustomerInformation.

        |参数名称：客户登录名称（如果客户创建了子用户，此处返回主账号登录名称）。| |参数约束及描述：客户登录名称（如果客户创建了子用户，此处返回主账号登录名称）。|

        :param account_name: The account_name of this CustomerInformation.
        :type: str
        """
        self._account_name = account_name

    @property
    def customer_id(self):
        """Gets the customer_id of this CustomerInformation.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :return: The customer_id of this CustomerInformation.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this CustomerInformation.

        |参数名称：客户ID。| |参数约束及描述：客户ID。|

        :param customer_id: The customer_id of this CustomerInformation.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def associated_on(self):
        """Gets the associated_on of this CustomerInformation.

        |参数名称：客户和伙伴关联时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”，其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：客户和伙伴关联时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”，其中，HH范围是0～23，mm和ss范围是0～59。|

        :return: The associated_on of this CustomerInformation.
        :rtype: str
        """
        return self._associated_on

    @associated_on.setter
    def associated_on(self, associated_on):
        """Sets the associated_on of this CustomerInformation.

        |参数名称：客户和伙伴关联时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”，其中，HH范围是0～23，mm和ss范围是0～59。| |参数约束及描述：客户和伙伴关联时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”，其中，HH范围是0～23，mm和ss范围是0～59。|

        :param associated_on: The associated_on of this CustomerInformation.
        :type: str
        """
        self._associated_on = associated_on

    @property
    def association_type(self):
        """Gets the association_type of this CustomerInformation.

        |参数名称：合作模式。1：推荐2：垫付3：转售| |参数约束及描述：合作模式。1：推荐2：垫付3：转售|

        :return: The association_type of this CustomerInformation.
        :rtype: str
        """
        return self._association_type

    @association_type.setter
    def association_type(self, association_type):
        """Sets the association_type of this CustomerInformation.

        |参数名称：合作模式。1：推荐2：垫付3：转售| |参数约束及描述：合作模式。1：推荐2：垫付3：转售|

        :param association_type: The association_type of this CustomerInformation.
        :type: str
        """
        self._association_type = association_type

    @property
    def label(self):
        """Gets the label of this CustomerInformation.

        |参数名称：标签，支持模糊查找。虚拟账号下，该字段无效。| |参数约束及描述：标签，支持模糊查找。虚拟账号下，该字段无效。|

        :return: The label of this CustomerInformation.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CustomerInformation.

        |参数名称：标签，支持模糊查找。虚拟账号下，该字段无效。| |参数约束及描述：标签，支持模糊查找。虚拟账号下，该字段无效。|

        :param label: The label of this CustomerInformation.
        :type: str
        """
        self._label = label

    @property
    def telephone(self):
        """Gets the telephone of this CustomerInformation.

        |参数名称：客户电话号码。虚拟账号下，该字段无效。| |参数约束及描述：客户电话号码。虚拟账号下，该字段无效。|

        :return: The telephone of this CustomerInformation.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this CustomerInformation.

        |参数名称：客户电话号码。虚拟账号下，该字段无效。| |参数约束及描述：客户电话号码。虚拟账号下，该字段无效。|

        :param telephone: The telephone of this CustomerInformation.
        :type: str
        """
        self._telephone = telephone

    @property
    def verified_status(self):
        """Gets the verified_status of this CustomerInformation.

        |参数名称：实名认证状态，虚拟账号下，该字段无效。：null：实名认证开关关闭；-1：未实名认证；0：实名认证审核中；1：实名认证不通过；2：已实名认证；3：实名认证失败。| |参数约束及描述：实名认证状态，虚拟账号下，该字段无效。：null：实名认证开关关闭；-1：未实名认证；0：实名认证审核中；1：实名认证不通过；2：已实名认证；3：实名认证失败。|

        :return: The verified_status of this CustomerInformation.
        :rtype: str
        """
        return self._verified_status

    @verified_status.setter
    def verified_status(self, verified_status):
        """Sets the verified_status of this CustomerInformation.

        |参数名称：实名认证状态，虚拟账号下，该字段无效。：null：实名认证开关关闭；-1：未实名认证；0：实名认证审核中；1：实名认证不通过；2：已实名认证；3：实名认证失败。| |参数约束及描述：实名认证状态，虚拟账号下，该字段无效。：null：实名认证开关关闭；-1：未实名认证；0：实名认证审核中；1：实名认证不通过；2：已实名认证；3：实名认证失败。|

        :param verified_status: The verified_status of this CustomerInformation.
        :type: str
        """
        self._verified_status = verified_status

    @property
    def country_code(self):
        """Gets the country_code of this CustomerInformation.

        |参数名称：国家码，电话号码的国家码前缀。虚拟账号下，该字段无效。例如：中国 0086。| |参数约束及描述：国家码，电话号码的国家码前缀。虚拟账号下，该字段无效。例如：中国 0086。|

        :return: The country_code of this CustomerInformation.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this CustomerInformation.

        |参数名称：国家码，电话号码的国家码前缀。虚拟账号下，该字段无效。例如：中国 0086。| |参数约束及描述：国家码，电话号码的国家码前缀。虚拟账号下，该字段无效。例如：中国 0086。|

        :param country_code: The country_code of this CustomerInformation.
        :type: str
        """
        self._country_code = country_code

    @property
    def customer_type(self):
        """Gets the customer_type of this CustomerInformation.

        |参数名称：客户类型，虚拟账号下，该字段无效。：-1：无类型0：个人1：企业客户刚注册的时候，没有具体的客户类型，为“-1：无类型”，客户可以在账号中心通过设置客户类型或者在实名认证的时候，选择对应的企业/个人实名认证来决定自己的类型。| |参数的约束及描述：客户类型，虚拟账号下，该字段无效。：-1：无类型0：个人1：企业客户刚注册的时候，没有具体的客户类型，为“-1：无类型”，客户可以在账号中心通过设置客户类型或者在实名认证的时候，选择对应的企业/个人实名认证来决定自己的类型。|

        :return: The customer_type of this CustomerInformation.
        :rtype: int
        """
        return self._customer_type

    @customer_type.setter
    def customer_type(self, customer_type):
        """Sets the customer_type of this CustomerInformation.

        |参数名称：客户类型，虚拟账号下，该字段无效。：-1：无类型0：个人1：企业客户刚注册的时候，没有具体的客户类型，为“-1：无类型”，客户可以在账号中心通过设置客户类型或者在实名认证的时候，选择对应的企业/个人实名认证来决定自己的类型。| |参数的约束及描述：客户类型，虚拟账号下，该字段无效。：-1：无类型0：个人1：企业客户刚注册的时候，没有具体的客户类型，为“-1：无类型”，客户可以在账号中心通过设置客户类型或者在实名认证的时候，选择对应的企业/个人实名认证来决定自己的类型。|

        :param customer_type: The customer_type of this CustomerInformation.
        :type: int
        """
        self._customer_type = customer_type

    @property
    def is_frozen(self):
        """Gets the is_frozen of this CustomerInformation.

        |参数名称：是否伙伴冻结，注意，只有转售子客户才能被伙伴冻结：0：否1：是| |参数的约束及描述：是否伙伴冻结，注意，只有转售子客户才能被伙伴冻结：0：否1：是|

        :return: The is_frozen of this CustomerInformation.
        :rtype: int
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        """Sets the is_frozen of this CustomerInformation.

        |参数名称：是否伙伴冻结，注意，只有转售子客户才能被伙伴冻结：0：否1：是| |参数的约束及描述：是否伙伴冻结，注意，只有转售子客户才能被伙伴冻结：0：否1：是|

        :param is_frozen: The is_frozen of this CustomerInformation.
        :type: int
        """
        self._is_frozen = is_frozen

    @property
    def account_managers(self):
        """Gets the account_managers of this CustomerInformation.

        |参数名称：客户经理名称列表，目前只支持1个| |参数约束以及描述：客户经理名称列表，目前只支持1个|

        :return: The account_managers of this CustomerInformation.
        :rtype: list[AccountManager]
        """
        return self._account_managers

    @account_managers.setter
    def account_managers(self, account_managers):
        """Sets the account_managers of this CustomerInformation.

        |参数名称：客户经理名称列表，目前只支持1个| |参数约束以及描述：客户经理名称列表，目前只支持1个|

        :param account_managers: The account_managers of this CustomerInformation.
        :type: list[AccountManager]
        """
        self._account_managers = account_managers

    @property
    def xaccount_id(self):
        """Gets the xaccount_id of this CustomerInformation.

        |参数名称：伙伴销售平台的用户唯一标识| |参数的约束及描述：该标识的具体值由伙伴分配|

        :return: The xaccount_id of this CustomerInformation.
        :rtype: str
        """
        return self._xaccount_id

    @xaccount_id.setter
    def xaccount_id(self, xaccount_id):
        """Sets the xaccount_id of this CustomerInformation.

        |参数名称：伙伴销售平台的用户唯一标识| |参数的约束及描述：该标识的具体值由伙伴分配|

        :param xaccount_id: The xaccount_id of this CustomerInformation.
        :type: str
        """
        self._xaccount_id = xaccount_id

    @property
    def xaccount_type(self):
        """Gets the xaccount_type of this CustomerInformation.

        |参数名称：华为分给合作伙伴的平台标识| |参数的约束及描述：该标识的具体值由华为分配|

        :return: The xaccount_type of this CustomerInformation.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        """Sets the xaccount_type of this CustomerInformation.

        |参数名称：华为分给合作伙伴的平台标识| |参数的约束及描述：该标识的具体值由华为分配|

        :param xaccount_type: The xaccount_type of this CustomerInformation.
        :type: str
        """
        self._xaccount_type = xaccount_type

    @property
    def customer_level(self):
        """Gets the customer_level of this CustomerInformation.

        |参数名称：客户等级| |参数的约束及描述：V0、V1、V2、V3、V4、V5|

        :return: The customer_level of this CustomerInformation.
        :rtype: str
        """
        return self._customer_level

    @customer_level.setter
    def customer_level(self, customer_level):
        """Sets the customer_level of this CustomerInformation.

        |参数名称：客户等级| |参数的约束及描述：V0、V1、V2、V3、V4、V5|

        :param customer_level: The customer_level of this CustomerInformation.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CustomerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
