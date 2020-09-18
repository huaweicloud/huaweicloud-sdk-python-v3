# coding: utf-8

import pprint
import re

import six





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
        'new_sub_customer': 'NewCustomerV2'
    }

    attribute_map = {
        'party_id': 'party_id',
        'display_name': 'display_name',
        'sub_customer_association_type': 'sub_customer_association_type',
        'permission_ids': 'permission_ids',
        'new_sub_customer': 'new_sub_customer'
    }

    def __init__(self, party_id=None, display_name=None, sub_customer_association_type=None, permission_ids=None, new_sub_customer=None):
        """CreateSubCustomerReqV2 - a model defined in huaweicloud sdk"""
        
        

        self._party_id = None
        self._display_name = None
        self._sub_customer_association_type = None
        self._permission_ids = None
        self._new_sub_customer = None
        self.discriminator = None

        self.party_id = party_id
        if display_name is not None:
            self.display_name = display_name
        if sub_customer_association_type is not None:
            self.sub_customer_association_type = sub_customer_association_type
        if permission_ids is not None:
            self.permission_ids = permission_ids
        self.new_sub_customer = new_sub_customer

    @property
    def party_id(self):
        """Gets the party_id of this CreateSubCustomerReqV2.

        |参数名称：子账号挂载的组织单元，填写组织单元的Party ID，通过查询企业组织结构接口的响应获得。| |参数约束及描述：子账号挂载的组织单元，填写组织单元的Party ID，通过查询企业组织结构接口的响应获得。|

        :return: The party_id of this CreateSubCustomerReqV2.
        :rtype: str
        """
        return self._party_id

    @party_id.setter
    def party_id(self, party_id):
        """Sets the party_id of this CreateSubCustomerReqV2.

        |参数名称：子账号挂载的组织单元，填写组织单元的Party ID，通过查询企业组织结构接口的响应获得。| |参数约束及描述：子账号挂载的组织单元，填写组织单元的Party ID，通过查询企业组织结构接口的响应获得。|

        :param party_id: The party_id of this CreateSubCustomerReqV2.
        :type: str
        """
        self._party_id = party_id

    @property
    def display_name(self):
        """Gets the display_name of this CreateSubCustomerReqV2.

        |参数名称：企业子账号的显示名称不限制特殊字符。| |参数约束及描述：企业子账号的显示名称不限制特殊字符。|

        :return: The display_name of this CreateSubCustomerReqV2.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateSubCustomerReqV2.

        |参数名称：企业子账号的显示名称不限制特殊字符。| |参数约束及描述：企业子账号的显示名称不限制特殊字符。|

        :param display_name: The display_name of this CreateSubCustomerReqV2.
        :type: str
        """
        self._display_name = display_name

    @property
    def sub_customer_association_type(self):
        """Gets the sub_customer_association_type of this CreateSubCustomerReqV2.

        |参数名称：子账号关联类型：1：同一法人。注：关联类型目前只能是同一法人。| |参数的约束及描述：子账号关联类型：1：同一法人。注：关联类型目前只能是同一法人。|

        :return: The sub_customer_association_type of this CreateSubCustomerReqV2.
        :rtype: int
        """
        return self._sub_customer_association_type

    @sub_customer_association_type.setter
    def sub_customer_association_type(self, sub_customer_association_type):
        """Sets the sub_customer_association_type of this CreateSubCustomerReqV2.

        |参数名称：子账号关联类型：1：同一法人。注：关联类型目前只能是同一法人。| |参数的约束及描述：子账号关联类型：1：同一法人。注：关联类型目前只能是同一法人。|

        :param sub_customer_association_type: The sub_customer_association_type of this CreateSubCustomerReqV2.
        :type: int
        """
        self._sub_customer_association_type = sub_customer_association_type

    @property
    def permission_ids(self):
        """Gets the permission_ids of this CreateSubCustomerReqV2.

        |参数名称：申请的权限列表。支持的权限项参见表 权限项定义列表| |参数约束以及描述：申请的权限列表。支持的权限项参见表 权限项定义列表|

        :return: The permission_ids of this CreateSubCustomerReqV2.
        :rtype: list[str]
        """
        return self._permission_ids

    @permission_ids.setter
    def permission_ids(self, permission_ids):
        """Sets the permission_ids of this CreateSubCustomerReqV2.

        |参数名称：申请的权限列表。支持的权限项参见表 权限项定义列表| |参数约束以及描述：申请的权限列表。支持的权限项参见表 权限项定义列表|

        :param permission_ids: The permission_ids of this CreateSubCustomerReqV2.
        :type: list[str]
        """
        self._permission_ids = permission_ids

    @property
    def new_sub_customer(self):
        """Gets the new_sub_customer of this CreateSubCustomerReqV2.


        :return: The new_sub_customer of this CreateSubCustomerReqV2.
        :rtype: NewCustomerV2
        """
        return self._new_sub_customer

    @new_sub_customer.setter
    def new_sub_customer(self, new_sub_customer):
        """Sets the new_sub_customer of this CreateSubCustomerReqV2.


        :param new_sub_customer: The new_sub_customer of this CreateSubCustomerReqV2.
        :type: NewCustomerV2
        """
        self._new_sub_customer = new_sub_customer

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
        if not isinstance(other, CreateSubCustomerReqV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
