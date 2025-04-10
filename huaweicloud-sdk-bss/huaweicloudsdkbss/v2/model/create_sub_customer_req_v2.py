# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubCustomerReqV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'party_id': 'str',
        'display_name': 'str',
        'sub_customer_association_type': 'int',
        'permission_ids': 'list[str]',
        'new_sub_customer': 'NewCustomerV2',
        'financial_custody': 'int'
    }

    attribute_map = {
        'party_id': 'party_id',
        'display_name': 'display_name',
        'sub_customer_association_type': 'sub_customer_association_type',
        'permission_ids': 'permission_ids',
        'new_sub_customer': 'new_sub_customer',
        'financial_custody': 'financial_custody'
    }

    def __init__(self, party_id=None, display_name=None, sub_customer_association_type=None, permission_ids=None, new_sub_customer=None, financial_custody=None):
        r"""CreateSubCustomerReqV2

        The model defined in huaweicloud sdk

        :param party_id: 企业子账号挂载的组织单元。 组织单元的Party ID，通过查询企业组织结构接口的响应获得。
        :type party_id: str
        :param display_name: 企业子账号的显示名称，不限制特殊字符。
        :type display_name: str
        :param sub_customer_association_type: 子账号关联类型：1：同一法人。 关联类型目前只能是同一法人。
        :type sub_customer_association_type: int
        :param permission_ids: 申请的权限列表。 支持的权限项请参见下表。当financial_custody为1时，此参数不生效，默认指定权限项：READ_FINANCE_INFO、READ_CONSUME_BILL、SHARE-BIZ-DISCOUNT-TO-SUB。
        :type permission_ids: list[str]
        :param new_sub_customer: 
        :type new_sub_customer: :class:`huaweicloudsdkbss.v2.NewCustomerV2`
        :param financial_custody: 是否开通财务托管，0：不开通；1：开通。默认值0，默认不开通。
        :type financial_custody: int
        """
        
        

        self._party_id = None
        self._display_name = None
        self._sub_customer_association_type = None
        self._permission_ids = None
        self._new_sub_customer = None
        self._financial_custody = None
        self.discriminator = None

        self.party_id = party_id
        if display_name is not None:
            self.display_name = display_name
        self.sub_customer_association_type = sub_customer_association_type
        if permission_ids is not None:
            self.permission_ids = permission_ids
        self.new_sub_customer = new_sub_customer
        if financial_custody is not None:
            self.financial_custody = financial_custody

    @property
    def party_id(self):
        r"""Gets the party_id of this CreateSubCustomerReqV2.

        企业子账号挂载的组织单元。 组织单元的Party ID，通过查询企业组织结构接口的响应获得。

        :return: The party_id of this CreateSubCustomerReqV2.
        :rtype: str
        """
        return self._party_id

    @party_id.setter
    def party_id(self, party_id):
        r"""Sets the party_id of this CreateSubCustomerReqV2.

        企业子账号挂载的组织单元。 组织单元的Party ID，通过查询企业组织结构接口的响应获得。

        :param party_id: The party_id of this CreateSubCustomerReqV2.
        :type party_id: str
        """
        self._party_id = party_id

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateSubCustomerReqV2.

        企业子账号的显示名称，不限制特殊字符。

        :return: The display_name of this CreateSubCustomerReqV2.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateSubCustomerReqV2.

        企业子账号的显示名称，不限制特殊字符。

        :param display_name: The display_name of this CreateSubCustomerReqV2.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def sub_customer_association_type(self):
        r"""Gets the sub_customer_association_type of this CreateSubCustomerReqV2.

        子账号关联类型：1：同一法人。 关联类型目前只能是同一法人。

        :return: The sub_customer_association_type of this CreateSubCustomerReqV2.
        :rtype: int
        """
        return self._sub_customer_association_type

    @sub_customer_association_type.setter
    def sub_customer_association_type(self, sub_customer_association_type):
        r"""Sets the sub_customer_association_type of this CreateSubCustomerReqV2.

        子账号关联类型：1：同一法人。 关联类型目前只能是同一法人。

        :param sub_customer_association_type: The sub_customer_association_type of this CreateSubCustomerReqV2.
        :type sub_customer_association_type: int
        """
        self._sub_customer_association_type = sub_customer_association_type

    @property
    def permission_ids(self):
        r"""Gets the permission_ids of this CreateSubCustomerReqV2.

        申请的权限列表。 支持的权限项请参见下表。当financial_custody为1时，此参数不生效，默认指定权限项：READ_FINANCE_INFO、READ_CONSUME_BILL、SHARE-BIZ-DISCOUNT-TO-SUB。

        :return: The permission_ids of this CreateSubCustomerReqV2.
        :rtype: list[str]
        """
        return self._permission_ids

    @permission_ids.setter
    def permission_ids(self, permission_ids):
        r"""Sets the permission_ids of this CreateSubCustomerReqV2.

        申请的权限列表。 支持的权限项请参见下表。当financial_custody为1时，此参数不生效，默认指定权限项：READ_FINANCE_INFO、READ_CONSUME_BILL、SHARE-BIZ-DISCOUNT-TO-SUB。

        :param permission_ids: The permission_ids of this CreateSubCustomerReqV2.
        :type permission_ids: list[str]
        """
        self._permission_ids = permission_ids

    @property
    def new_sub_customer(self):
        r"""Gets the new_sub_customer of this CreateSubCustomerReqV2.

        :return: The new_sub_customer of this CreateSubCustomerReqV2.
        :rtype: :class:`huaweicloudsdkbss.v2.NewCustomerV2`
        """
        return self._new_sub_customer

    @new_sub_customer.setter
    def new_sub_customer(self, new_sub_customer):
        r"""Sets the new_sub_customer of this CreateSubCustomerReqV2.

        :param new_sub_customer: The new_sub_customer of this CreateSubCustomerReqV2.
        :type new_sub_customer: :class:`huaweicloudsdkbss.v2.NewCustomerV2`
        """
        self._new_sub_customer = new_sub_customer

    @property
    def financial_custody(self):
        r"""Gets the financial_custody of this CreateSubCustomerReqV2.

        是否开通财务托管，0：不开通；1：开通。默认值0，默认不开通。

        :return: The financial_custody of this CreateSubCustomerReqV2.
        :rtype: int
        """
        return self._financial_custody

    @financial_custody.setter
    def financial_custody(self, financial_custody):
        r"""Sets the financial_custody of this CreateSubCustomerReqV2.

        是否开通财务托管，0：不开通；1：开通。默认值0，默认不开通。

        :param financial_custody: The financial_custody of this CreateSubCustomerReqV2.
        :type financial_custody: int
        """
        self._financial_custody = financial_custody

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
        if not isinstance(other, CreateSubCustomerReqV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
