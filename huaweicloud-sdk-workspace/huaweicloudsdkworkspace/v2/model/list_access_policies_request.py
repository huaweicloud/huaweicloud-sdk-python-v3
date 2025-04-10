# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_control_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'access_control_type': 'access_control_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, access_control_type=None, limit=None, offset=None):
        r"""ListAccessPoliciesRequest

        The model defined in huaweicloud sdk

        :param access_control_type: 接入策略控制类型 * ACCESS_TYPE： 接入类型 * IP_WHITE_LIST： IP白名单
        :type access_control_type: str
        :param limit: 每页数量,范围0-100,默认100。
        :type limit: int
        :param offset: 偏移量,范围0-99,默认0。
        :type offset: int
        """
        
        

        self._access_control_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if access_control_type is not None:
            self.access_control_type = access_control_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def access_control_type(self):
        r"""Gets the access_control_type of this ListAccessPoliciesRequest.

        接入策略控制类型 * ACCESS_TYPE： 接入类型 * IP_WHITE_LIST： IP白名单

        :return: The access_control_type of this ListAccessPoliciesRequest.
        :rtype: str
        """
        return self._access_control_type

    @access_control_type.setter
    def access_control_type(self, access_control_type):
        r"""Sets the access_control_type of this ListAccessPoliciesRequest.

        接入策略控制类型 * ACCESS_TYPE： 接入类型 * IP_WHITE_LIST： IP白名单

        :param access_control_type: The access_control_type of this ListAccessPoliciesRequest.
        :type access_control_type: str
        """
        self._access_control_type = access_control_type

    @property
    def limit(self):
        r"""Gets the limit of this ListAccessPoliciesRequest.

        每页数量,范围0-100,默认100。

        :return: The limit of this ListAccessPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAccessPoliciesRequest.

        每页数量,范围0-100,默认100。

        :param limit: The limit of this ListAccessPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAccessPoliciesRequest.

        偏移量,范围0-99,默认0。

        :return: The offset of this ListAccessPoliciesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAccessPoliciesRequest.

        偏移量,范围0-99,默认0。

        :param offset: The offset of this ListAccessPoliciesRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListAccessPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
