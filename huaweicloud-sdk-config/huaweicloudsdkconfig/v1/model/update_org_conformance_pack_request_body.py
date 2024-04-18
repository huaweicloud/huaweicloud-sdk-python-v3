# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOrgConformancePackRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'excluded_accounts': 'list[str]',
        'vars_structure': 'list[VarsStructure]'
    }

    attribute_map = {
        'name': 'name',
        'excluded_accounts': 'excluded_accounts',
        'vars_structure': 'vars_structure'
    }

    def __init__(self, name=None, excluded_accounts=None, vars_structure=None):
        """UpdateOrgConformancePackRequestBody

        The model defined in huaweicloud sdk

        :param name: 组织合规规则包名称。
        :type name: str
        :param excluded_accounts: 排除配置合规包的帐号。
        :type excluded_accounts: list[str]
        :param vars_structure: 合规规则包参数。
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        
        

        self._name = None
        self._excluded_accounts = None
        self._vars_structure = None
        self.discriminator = None

        self.name = name
        if excluded_accounts is not None:
            self.excluded_accounts = excluded_accounts
        if vars_structure is not None:
            self.vars_structure = vars_structure

    @property
    def name(self):
        """Gets the name of this UpdateOrgConformancePackRequestBody.

        组织合规规则包名称。

        :return: The name of this UpdateOrgConformancePackRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateOrgConformancePackRequestBody.

        组织合规规则包名称。

        :param name: The name of this UpdateOrgConformancePackRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def excluded_accounts(self):
        """Gets the excluded_accounts of this UpdateOrgConformancePackRequestBody.

        排除配置合规包的帐号。

        :return: The excluded_accounts of this UpdateOrgConformancePackRequestBody.
        :rtype: list[str]
        """
        return self._excluded_accounts

    @excluded_accounts.setter
    def excluded_accounts(self, excluded_accounts):
        """Sets the excluded_accounts of this UpdateOrgConformancePackRequestBody.

        排除配置合规包的帐号。

        :param excluded_accounts: The excluded_accounts of this UpdateOrgConformancePackRequestBody.
        :type excluded_accounts: list[str]
        """
        self._excluded_accounts = excluded_accounts

    @property
    def vars_structure(self):
        """Gets the vars_structure of this UpdateOrgConformancePackRequestBody.

        合规规则包参数。

        :return: The vars_structure of this UpdateOrgConformancePackRequestBody.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this UpdateOrgConformancePackRequestBody.

        合规规则包参数。

        :param vars_structure: The vars_structure of this UpdateOrgConformancePackRequestBody.
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

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
        if not isinstance(other, UpdateOrgConformancePackRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
