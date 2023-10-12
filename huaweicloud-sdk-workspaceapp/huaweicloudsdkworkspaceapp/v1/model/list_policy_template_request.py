# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'policy_group_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'policy_group_name': 'policy_group_name'
    }

    def __init__(self, offset=None, limit=None, policy_group_name=None):
        """ListPolicyTemplateRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]
        :type limit: int
        :param policy_group_name: 根据策略模板名字过滤结果。
        :type policy_group_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._policy_group_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name

    @property
    def offset(self):
        """Gets the offset of this ListPolicyTemplateRequest.

        查询的偏移量

        :return: The offset of this ListPolicyTemplateRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPolicyTemplateRequest.

        查询的偏移量

        :param offset: The offset of this ListPolicyTemplateRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPolicyTemplateRequest.

        查询的数量，值区间[1-100]

        :return: The limit of this ListPolicyTemplateRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPolicyTemplateRequest.

        查询的数量，值区间[1-100]

        :param limit: The limit of this ListPolicyTemplateRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def policy_group_name(self):
        """Gets the policy_group_name of this ListPolicyTemplateRequest.

        根据策略模板名字过滤结果。

        :return: The policy_group_name of this ListPolicyTemplateRequest.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        """Sets the policy_group_name of this ListPolicyTemplateRequest.

        根据策略模板名字过滤结果。

        :param policy_group_name: The policy_group_name of this ListPolicyTemplateRequest.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

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
        if not isinstance(other, ListPolicyTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
