# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishAppReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'accounts': 'list[AccountInfo]',
        'items': 'list[PublishApp]'
    }

    attribute_map = {
        'accounts': 'accounts',
        'items': 'items'
    }

    def __init__(self, accounts=None, items=None):
        """PublishAppReq

        The model defined in huaweicloud sdk

        :param accounts: 用户(组),单次最多允许操作100个用户(组)
        :type accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.AccountInfo`]
        :param items: 发布应用列表(单次最多20个应用)
        :type items: list[:class:`huaweicloudsdkworkspaceapp.v1.PublishApp`]
        """
        
        

        self._accounts = None
        self._items = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        self.items = items

    @property
    def accounts(self):
        """Gets the accounts of this PublishAppReq.

        用户(组),单次最多允许操作100个用户(组)

        :return: The accounts of this PublishAppReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.AccountInfo`]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this PublishAppReq.

        用户(组),单次最多允许操作100个用户(组)

        :param accounts: The accounts of this PublishAppReq.
        :type accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.AccountInfo`]
        """
        self._accounts = accounts

    @property
    def items(self):
        """Gets the items of this PublishAppReq.

        发布应用列表(单次最多20个应用)

        :return: The items of this PublishAppReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.PublishApp`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this PublishAppReq.

        发布应用列表(单次最多20个应用)

        :param items: The items of this PublishAppReq.
        :type items: list[:class:`huaweicloudsdkworkspaceapp.v1.PublishApp`]
        """
        self._items = items

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
        if not isinstance(other, PublishAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
