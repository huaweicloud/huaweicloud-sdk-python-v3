# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubCustomerInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'display_name': 'str',
        'status': 'int',
        'org_id': 'str',
        'org_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'display_name',
        'status': 'status',
        'org_id': 'org_id',
        'org_name': 'org_name'
    }

    def __init__(self, id=None, name=None, display_name=None, status=None, org_id=None, org_name=None):
        """SubCustomerInfoV2

        The model defined in huaweicloud sdk

        :param id: 企业子账号的客户ID。
        :type id: str
        :param name: 企业子账号的用户名。
        :type name: str
        :param display_name: 企业子账号的显示名称。 不限制特殊字符。
        :type display_name: str
        :param status: 子账号状态： 1：正常2：创建中3：关闭中4：已关闭101：子账号注册中102：子账号待激活
        :type status: int
        :param org_id: 子账号归属的组织单元ID。
        :type org_id: str
        :param org_name: 子账号归属的组织单元名称。  说明： 当子账号归属的组织是企业组织根节点时，本属性可能为空。
        :type org_name: str
        """
        
        

        self._id = None
        self._name = None
        self._display_name = None
        self._status = None
        self._org_id = None
        self._org_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if status is not None:
            self.status = status
        if org_id is not None:
            self.org_id = org_id
        if org_name is not None:
            self.org_name = org_name

    @property
    def id(self):
        """Gets the id of this SubCustomerInfoV2.

        企业子账号的客户ID。

        :return: The id of this SubCustomerInfoV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubCustomerInfoV2.

        企业子账号的客户ID。

        :param id: The id of this SubCustomerInfoV2.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SubCustomerInfoV2.

        企业子账号的用户名。

        :return: The name of this SubCustomerInfoV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubCustomerInfoV2.

        企业子账号的用户名。

        :param name: The name of this SubCustomerInfoV2.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this SubCustomerInfoV2.

        企业子账号的显示名称。 不限制特殊字符。

        :return: The display_name of this SubCustomerInfoV2.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this SubCustomerInfoV2.

        企业子账号的显示名称。 不限制特殊字符。

        :param display_name: The display_name of this SubCustomerInfoV2.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def status(self):
        """Gets the status of this SubCustomerInfoV2.

        子账号状态： 1：正常2：创建中3：关闭中4：已关闭101：子账号注册中102：子账号待激活

        :return: The status of this SubCustomerInfoV2.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubCustomerInfoV2.

        子账号状态： 1：正常2：创建中3：关闭中4：已关闭101：子账号注册中102：子账号待激活

        :param status: The status of this SubCustomerInfoV2.
        :type status: int
        """
        self._status = status

    @property
    def org_id(self):
        """Gets the org_id of this SubCustomerInfoV2.

        子账号归属的组织单元ID。

        :return: The org_id of this SubCustomerInfoV2.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this SubCustomerInfoV2.

        子账号归属的组织单元ID。

        :param org_id: The org_id of this SubCustomerInfoV2.
        :type org_id: str
        """
        self._org_id = org_id

    @property
    def org_name(self):
        """Gets the org_name of this SubCustomerInfoV2.

        子账号归属的组织单元名称。  说明： 当子账号归属的组织是企业组织根节点时，本属性可能为空。

        :return: The org_name of this SubCustomerInfoV2.
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this SubCustomerInfoV2.

        子账号归属的组织单元名称。  说明： 当子账号归属的组织是企业组织根节点时，本属性可能为空。

        :param org_name: The org_name of this SubCustomerInfoV2.
        :type org_name: str
        """
        self._org_name = org_name

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
        if not isinstance(other, SubCustomerInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
