# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppGroupAuthorizeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_group_ids': 'list[str]',
        'accounts': 'list[AccountInfo]'
    }

    attribute_map = {
        'app_group_ids': 'app_group_ids',
        'accounts': 'accounts'
    }

    def __init__(self, app_group_ids=None, accounts=None):
        """AppGroupAuthorizeReq

        The model defined in huaweicloud sdk

        :param app_group_ids: 应用组ID,最多同时操作10个
        :type app_group_ids: list[str]
        :param accounts: 用户(组),单次最多允许操作50个用户(组)
        :type accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.AccountInfo`]
        """
        
        

        self._app_group_ids = None
        self._accounts = None
        self.discriminator = None

        self.app_group_ids = app_group_ids
        self.accounts = accounts

    @property
    def app_group_ids(self):
        """Gets the app_group_ids of this AppGroupAuthorizeReq.

        应用组ID,最多同时操作10个

        :return: The app_group_ids of this AppGroupAuthorizeReq.
        :rtype: list[str]
        """
        return self._app_group_ids

    @app_group_ids.setter
    def app_group_ids(self, app_group_ids):
        """Sets the app_group_ids of this AppGroupAuthorizeReq.

        应用组ID,最多同时操作10个

        :param app_group_ids: The app_group_ids of this AppGroupAuthorizeReq.
        :type app_group_ids: list[str]
        """
        self._app_group_ids = app_group_ids

    @property
    def accounts(self):
        """Gets the accounts of this AppGroupAuthorizeReq.

        用户(组),单次最多允许操作50个用户(组)

        :return: The accounts of this AppGroupAuthorizeReq.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.AccountInfo`]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this AppGroupAuthorizeReq.

        用户(组),单次最多允许操作50个用户(组)

        :param accounts: The accounts of this AppGroupAuthorizeReq.
        :type accounts: list[:class:`huaweicloudsdkworkspaceapp.v1.AccountInfo`]
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
        if not isinstance(other, AppGroupAuthorizeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
