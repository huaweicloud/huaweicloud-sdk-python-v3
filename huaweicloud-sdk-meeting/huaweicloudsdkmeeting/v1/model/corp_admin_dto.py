# coding: utf-8

import pprint
import re

import six





class CorpAdminDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'account': 'str',
        'menu_template_id': 'str'
    }

    attribute_map = {
        'account': 'account',
        'menu_template_id': 'menuTemplateId'
    }

    def __init__(self, account=None, menu_template_id=None):
        """CorpAdminDTO - a model defined in huaweicloud sdk"""
        
        

        self._account = None
        self._menu_template_id = None
        self.discriminator = None

        self.account = account
        if menu_template_id is not None:
            self.menu_template_id = menu_template_id

    @property
    def account(self):
        """Gets the account of this CorpAdminDTO.

        企业用户账号。 maxLength：64 minLength：1

        :return: The account of this CorpAdminDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CorpAdminDTO.

        企业用户账号。 maxLength：64 minLength：1

        :param account: The account of this CorpAdminDTO.
        :type: str
        """
        self._account = account

    @property
    def menu_template_id(self):
        """Gets the menu_template_id of this CorpAdminDTO.

        菜单模板id，若不携带或为\\\"\\\"，则使用默认的菜单模板  约束 - 长度范围为0到32个字符

        :return: The menu_template_id of this CorpAdminDTO.
        :rtype: str
        """
        return self._menu_template_id

    @menu_template_id.setter
    def menu_template_id(self, menu_template_id):
        """Sets the menu_template_id of this CorpAdminDTO.

        菜单模板id，若不携带或为\\\"\\\"，则使用默认的菜单模板  约束 - 长度范围为0到32个字符

        :param menu_template_id: The menu_template_id of this CorpAdminDTO.
        :type: str
        """
        self._menu_template_id = menu_template_id

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
        if not isinstance(other, CorpAdminDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
