# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationStructureBaseLine:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organizational_unit_name': 'str',
        'organizational_unit_type': 'OrganizationalUnitTypeForSetup',
        'accounts': 'list[AccountBaseline]'
    }

    attribute_map = {
        'organizational_unit_name': 'organizational_unit_name',
        'organizational_unit_type': 'organizational_unit_type',
        'accounts': 'accounts'
    }

    def __init__(self, organizational_unit_name=None, organizational_unit_type=None, accounts=None):
        r"""OrganizationStructureBaseLine

        The model defined in huaweicloud sdk

        :param organizational_unit_name: 注册OU名称。
        :type organizational_unit_name: str
        :param organizational_unit_type: 
        :type organizational_unit_type: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitTypeForSetup`
        :param accounts: 纳管账号基本信息。
        :type accounts: list[:class:`huaweicloudsdkrgc.v1.AccountBaseline`]
        """
        
        

        self._organizational_unit_name = None
        self._organizational_unit_type = None
        self._accounts = None
        self.discriminator = None

        if organizational_unit_name is not None:
            self.organizational_unit_name = organizational_unit_name
        self.organizational_unit_type = organizational_unit_type
        if accounts is not None:
            self.accounts = accounts

    @property
    def organizational_unit_name(self):
        r"""Gets the organizational_unit_name of this OrganizationStructureBaseLine.

        注册OU名称。

        :return: The organizational_unit_name of this OrganizationStructureBaseLine.
        :rtype: str
        """
        return self._organizational_unit_name

    @organizational_unit_name.setter
    def organizational_unit_name(self, organizational_unit_name):
        r"""Sets the organizational_unit_name of this OrganizationStructureBaseLine.

        注册OU名称。

        :param organizational_unit_name: The organizational_unit_name of this OrganizationStructureBaseLine.
        :type organizational_unit_name: str
        """
        self._organizational_unit_name = organizational_unit_name

    @property
    def organizational_unit_type(self):
        r"""Gets the organizational_unit_type of this OrganizationStructureBaseLine.

        :return: The organizational_unit_type of this OrganizationStructureBaseLine.
        :rtype: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitTypeForSetup`
        """
        return self._organizational_unit_type

    @organizational_unit_type.setter
    def organizational_unit_type(self, organizational_unit_type):
        r"""Sets the organizational_unit_type of this OrganizationStructureBaseLine.

        :param organizational_unit_type: The organizational_unit_type of this OrganizationStructureBaseLine.
        :type organizational_unit_type: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitTypeForSetup`
        """
        self._organizational_unit_type = organizational_unit_type

    @property
    def accounts(self):
        r"""Gets the accounts of this OrganizationStructureBaseLine.

        纳管账号基本信息。

        :return: The accounts of this OrganizationStructureBaseLine.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.AccountBaseline`]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        r"""Sets the accounts of this OrganizationStructureBaseLine.

        纳管账号基本信息。

        :param accounts: The accounts of this OrganizationStructureBaseLine.
        :type accounts: list[:class:`huaweicloudsdkrgc.v1.AccountBaseline`]
        """
        self._accounts = accounts

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
        if not isinstance(other, OrganizationStructureBaseLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
