# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityprovidersResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sso_type': 'str',
        'id': 'str',
        'description': 'str',
        'enabled': 'bool',
        'remote_ids': 'list[str]',
        'links': 'IdentityprovidersLinks'
    }

    attribute_map = {
        'sso_type': 'sso_type',
        'id': 'id',
        'description': 'description',
        'enabled': 'enabled',
        'remote_ids': 'remote_ids',
        'links': 'links'
    }

    def __init__(self, sso_type=None, id=None, description=None, enabled=None, remote_ids=None, links=None):
        """IdentityprovidersResult

        The model defined in huaweicloud sdk

        :param sso_type: 身份提供商类型。当前支持virtual_user_sso和iam_user_sso两种。当返回为空字符串或者null时，默认为缺省类型virtual_user_sso类型。
        :type sso_type: str
        :param id: 身份提供商ID。
        :type id: str
        :param description: 身份提供商描述信息。
        :type description: str
        :param enabled: 身份提供商是否启用，true为启用，false为停用，默认为false。
        :type enabled: bool
        :param remote_ids: 身份提供商的联邦用户ID列表。
        :type remote_ids: list[str]
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.IdentityprovidersLinks`
        """
        
        

        self._sso_type = None
        self._id = None
        self._description = None
        self._enabled = None
        self._remote_ids = None
        self._links = None
        self.discriminator = None

        self.sso_type = sso_type
        self.id = id
        self.description = description
        self.enabled = enabled
        self.remote_ids = remote_ids
        self.links = links

    @property
    def sso_type(self):
        """Gets the sso_type of this IdentityprovidersResult.

        身份提供商类型。当前支持virtual_user_sso和iam_user_sso两种。当返回为空字符串或者null时，默认为缺省类型virtual_user_sso类型。

        :return: The sso_type of this IdentityprovidersResult.
        :rtype: str
        """
        return self._sso_type

    @sso_type.setter
    def sso_type(self, sso_type):
        """Sets the sso_type of this IdentityprovidersResult.

        身份提供商类型。当前支持virtual_user_sso和iam_user_sso两种。当返回为空字符串或者null时，默认为缺省类型virtual_user_sso类型。

        :param sso_type: The sso_type of this IdentityprovidersResult.
        :type sso_type: str
        """
        self._sso_type = sso_type

    @property
    def id(self):
        """Gets the id of this IdentityprovidersResult.

        身份提供商ID。

        :return: The id of this IdentityprovidersResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityprovidersResult.

        身份提供商ID。

        :param id: The id of this IdentityprovidersResult.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this IdentityprovidersResult.

        身份提供商描述信息。

        :return: The description of this IdentityprovidersResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IdentityprovidersResult.

        身份提供商描述信息。

        :param description: The description of this IdentityprovidersResult.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this IdentityprovidersResult.

        身份提供商是否启用，true为启用，false为停用，默认为false。

        :return: The enabled of this IdentityprovidersResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IdentityprovidersResult.

        身份提供商是否启用，true为启用，false为停用，默认为false。

        :param enabled: The enabled of this IdentityprovidersResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def remote_ids(self):
        """Gets the remote_ids of this IdentityprovidersResult.

        身份提供商的联邦用户ID列表。

        :return: The remote_ids of this IdentityprovidersResult.
        :rtype: list[str]
        """
        return self._remote_ids

    @remote_ids.setter
    def remote_ids(self, remote_ids):
        """Sets the remote_ids of this IdentityprovidersResult.

        身份提供商的联邦用户ID列表。

        :param remote_ids: The remote_ids of this IdentityprovidersResult.
        :type remote_ids: list[str]
        """
        self._remote_ids = remote_ids

    @property
    def links(self):
        """Gets the links of this IdentityprovidersResult.

        :return: The links of this IdentityprovidersResult.
        :rtype: :class:`huaweicloudsdkiam.v3.IdentityprovidersLinks`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IdentityprovidersResult.

        :param links: The links of this IdentityprovidersResult.
        :type links: :class:`huaweicloudsdkiam.v3.IdentityprovidersLinks`
        """
        self._links = links

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
        if not isinstance(other, IdentityprovidersResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
