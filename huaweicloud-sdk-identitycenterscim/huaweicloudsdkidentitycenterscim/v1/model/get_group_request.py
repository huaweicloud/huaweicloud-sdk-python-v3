# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorization': 'str',
        'tenant_id': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'authorization': 'Authorization',
        'tenant_id': 'tenant_id',
        'group_id': 'group_id'
    }

    def __init__(self, authorization=None, tenant_id=None, group_id=None):
        r"""GetGroupRequest

        The model defined in huaweicloud sdk

        :param authorization: 承载令牌
        :type authorization: str
        :param tenant_id: 租户的全局唯一标识符（ID）
        :type tenant_id: str
        :param group_id: 用户组的全局唯一标识符（ID）
        :type group_id: str
        """
        
        

        self._authorization = None
        self._tenant_id = None
        self._group_id = None
        self.discriminator = None

        self.authorization = authorization
        self.tenant_id = tenant_id
        self.group_id = group_id

    @property
    def authorization(self):
        r"""Gets the authorization of this GetGroupRequest.

        承载令牌

        :return: The authorization of this GetGroupRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this GetGroupRequest.

        承载令牌

        :param authorization: The authorization of this GetGroupRequest.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this GetGroupRequest.

        租户的全局唯一标识符（ID）

        :return: The tenant_id of this GetGroupRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this GetGroupRequest.

        租户的全局唯一标识符（ID）

        :param tenant_id: The tenant_id of this GetGroupRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def group_id(self):
        r"""Gets the group_id of this GetGroupRequest.

        用户组的全局唯一标识符（ID）

        :return: The group_id of this GetGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GetGroupRequest.

        用户组的全局唯一标识符（ID）

        :param group_id: The group_id of this GetGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, GetGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
