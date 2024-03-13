# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListControlViolationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'organization_unit_id': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'organization_unit_id': 'organization_unit_id'
    }

    def __init__(self, account_id=None, organization_unit_id=None):
        """ListControlViolationsRequest

        The model defined in huaweicloud sdk

        :param account_id: 账户ID，用于过滤不合规资源。
        :type account_id: str
        :param organization_unit_id: 注册OU ID，用于过滤不合规资源。
        :type organization_unit_id: str
        """
        
        

        self._account_id = None
        self._organization_unit_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id

    @property
    def account_id(self):
        """Gets the account_id of this ListControlViolationsRequest.

        账户ID，用于过滤不合规资源。

        :return: The account_id of this ListControlViolationsRequest.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ListControlViolationsRequest.

        账户ID，用于过滤不合规资源。

        :param account_id: The account_id of this ListControlViolationsRequest.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this ListControlViolationsRequest.

        注册OU ID，用于过滤不合规资源。

        :return: The organization_unit_id of this ListControlViolationsRequest.
        :rtype: str
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this ListControlViolationsRequest.

        注册OU ID，用于过滤不合规资源。

        :param organization_unit_id: The organization_unit_id of this ListControlViolationsRequest.
        :type organization_unit_id: str
        """
        self._organization_unit_id = organization_unit_id

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
        if not isinstance(other, ListControlViolationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
