# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessPolicyObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_objects_list': 'list[AccessPolicyObjectInfo]',
        'total': 'int'
    }

    attribute_map = {
        'policy_objects_list': 'policy_objects_list',
        'total': 'total'
    }

    def __init__(self, policy_objects_list=None, total=None):
        """ListAccessPolicyObjectsResponse

        The model defined in huaweicloud sdk

        :param policy_objects_list: 查询接入策略应用对象响应。
        :type policy_objects_list: list[:class:`huaweicloudsdkworkspace.v2.AccessPolicyObjectInfo`]
        :param total: 对象总数。
        :type total: int
        """
        
        super(ListAccessPolicyObjectsResponse, self).__init__()

        self._policy_objects_list = None
        self._total = None
        self.discriminator = None

        if policy_objects_list is not None:
            self.policy_objects_list = policy_objects_list
        if total is not None:
            self.total = total

    @property
    def policy_objects_list(self):
        """Gets the policy_objects_list of this ListAccessPolicyObjectsResponse.

        查询接入策略应用对象响应。

        :return: The policy_objects_list of this ListAccessPolicyObjectsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AccessPolicyObjectInfo`]
        """
        return self._policy_objects_list

    @policy_objects_list.setter
    def policy_objects_list(self, policy_objects_list):
        """Sets the policy_objects_list of this ListAccessPolicyObjectsResponse.

        查询接入策略应用对象响应。

        :param policy_objects_list: The policy_objects_list of this ListAccessPolicyObjectsResponse.
        :type policy_objects_list: list[:class:`huaweicloudsdkworkspace.v2.AccessPolicyObjectInfo`]
        """
        self._policy_objects_list = policy_objects_list

    @property
    def total(self):
        """Gets the total of this ListAccessPolicyObjectsResponse.

        对象总数。

        :return: The total of this ListAccessPolicyObjectsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAccessPolicyObjectsResponse.

        对象总数。

        :param total: The total of this ListAccessPolicyObjectsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAccessPolicyObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
