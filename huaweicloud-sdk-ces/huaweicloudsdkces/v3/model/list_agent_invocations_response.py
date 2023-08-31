# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentInvocationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'invocations': 'list[InvocationInfo]',
        'count': 'int'
    }

    attribute_map = {
        'invocations': 'invocations',
        'count': 'count'
    }

    def __init__(self, invocations=None, count=None):
        """ListAgentInvocationsResponse

        The model defined in huaweicloud sdk

        :param invocations: 任务列表
        :type invocations: list[:class:`huaweicloudsdkces.v3.InvocationInfo`]
        :param count: 任务列表总量
        :type count: int
        """
        
        super(ListAgentInvocationsResponse, self).__init__()

        self._invocations = None
        self._count = None
        self.discriminator = None

        if invocations is not None:
            self.invocations = invocations
        if count is not None:
            self.count = count

    @property
    def invocations(self):
        """Gets the invocations of this ListAgentInvocationsResponse.

        任务列表

        :return: The invocations of this ListAgentInvocationsResponse.
        :rtype: list[:class:`huaweicloudsdkces.v3.InvocationInfo`]
        """
        return self._invocations

    @invocations.setter
    def invocations(self, invocations):
        """Sets the invocations of this ListAgentInvocationsResponse.

        任务列表

        :param invocations: The invocations of this ListAgentInvocationsResponse.
        :type invocations: list[:class:`huaweicloudsdkces.v3.InvocationInfo`]
        """
        self._invocations = invocations

    @property
    def count(self):
        """Gets the count of this ListAgentInvocationsResponse.

        任务列表总量

        :return: The count of this ListAgentInvocationsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAgentInvocationsResponse.

        任务列表总量

        :param count: The count of this ListAgentInvocationsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListAgentInvocationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
