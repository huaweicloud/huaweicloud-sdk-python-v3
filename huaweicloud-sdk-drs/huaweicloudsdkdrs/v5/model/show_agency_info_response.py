# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAgencyInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_existed': 'bool',
        'name': 'str',
        'roles': 'list[AgencyRole]'
    }

    attribute_map = {
        'is_existed': 'is_existed',
        'name': 'name',
        'roles': 'roles'
    }

    def __init__(self, is_existed=None, name=None, roles=None):
        r"""ShowAgencyInfoResponse

        The model defined in huaweicloud sdk

        :param is_existed: 委托是否存在。
        :type is_existed: bool
        :param name: 委托名称。
        :type name: str
        :param roles: 委托绑定的权限策略信息。
        :type roles: list[:class:`huaweicloudsdkdrs.v5.AgencyRole`]
        """
        
        super(ShowAgencyInfoResponse, self).__init__()

        self._is_existed = None
        self._name = None
        self._roles = None
        self.discriminator = None

        if is_existed is not None:
            self.is_existed = is_existed
        if name is not None:
            self.name = name
        if roles is not None:
            self.roles = roles

    @property
    def is_existed(self):
        r"""Gets the is_existed of this ShowAgencyInfoResponse.

        委托是否存在。

        :return: The is_existed of this ShowAgencyInfoResponse.
        :rtype: bool
        """
        return self._is_existed

    @is_existed.setter
    def is_existed(self, is_existed):
        r"""Sets the is_existed of this ShowAgencyInfoResponse.

        委托是否存在。

        :param is_existed: The is_existed of this ShowAgencyInfoResponse.
        :type is_existed: bool
        """
        self._is_existed = is_existed

    @property
    def name(self):
        r"""Gets the name of this ShowAgencyInfoResponse.

        委托名称。

        :return: The name of this ShowAgencyInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAgencyInfoResponse.

        委托名称。

        :param name: The name of this ShowAgencyInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def roles(self):
        r"""Gets the roles of this ShowAgencyInfoResponse.

        委托绑定的权限策略信息。

        :return: The roles of this ShowAgencyInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.AgencyRole`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ShowAgencyInfoResponse.

        委托绑定的权限策略信息。

        :param roles: The roles of this ShowAgencyInfoResponse.
        :type roles: list[:class:`huaweicloudsdkdrs.v5.AgencyRole`]
        """
        self._roles = roles

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
        if not isinstance(other, ShowAgencyInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
