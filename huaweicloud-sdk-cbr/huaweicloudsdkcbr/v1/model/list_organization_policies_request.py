# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'operation_type': 'operation_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, operation_type=None, limit=None, offset=None):
        r"""ListOrganizationPoliciesRequest

        The model defined in huaweicloud sdk

        :param operation_type: 组织策略类型
        :type operation_type: str
        :param limit: 每页显示的条目数量，正整数
        :type limit: int
        :param offset: 偏移值，正整数
        :type offset: int
        """
        
        

        self._operation_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.operation_type = operation_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def operation_type(self):
        r"""Gets the operation_type of this ListOrganizationPoliciesRequest.

        组织策略类型

        :return: The operation_type of this ListOrganizationPoliciesRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this ListOrganizationPoliciesRequest.

        组织策略类型

        :param operation_type: The operation_type of this ListOrganizationPoliciesRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def limit(self):
        r"""Gets the limit of this ListOrganizationPoliciesRequest.

        每页显示的条目数量，正整数

        :return: The limit of this ListOrganizationPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrganizationPoliciesRequest.

        每页显示的条目数量，正整数

        :param limit: The limit of this ListOrganizationPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOrganizationPoliciesRequest.

        偏移值，正整数

        :return: The offset of this ListOrganizationPoliciesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOrganizationPoliciesRequest.

        偏移值，正整数

        :param offset: The offset of this ListOrganizationPoliciesRequest.
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
        if not isinstance(other, ListOrganizationPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
