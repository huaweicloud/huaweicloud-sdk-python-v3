# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStackResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_resources': 'list[StackResource]'
    }

    attribute_map = {
        'stack_resources': 'stack_resources'
    }

    def __init__(self, stack_resources=None):
        """ListStackResourcesResponse

        The model defined in huaweicloud sdk

        :param stack_resources: 资源栈中所管理的资源信息列表
        :type stack_resources: list[:class:`huaweicloudsdkaos.v1.StackResource`]
        """
        
        super(ListStackResourcesResponse, self).__init__()

        self._stack_resources = None
        self.discriminator = None

        if stack_resources is not None:
            self.stack_resources = stack_resources

    @property
    def stack_resources(self):
        """Gets the stack_resources of this ListStackResourcesResponse.

        资源栈中所管理的资源信息列表

        :return: The stack_resources of this ListStackResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.StackResource`]
        """
        return self._stack_resources

    @stack_resources.setter
    def stack_resources(self, stack_resources):
        """Sets the stack_resources of this ListStackResourcesResponse.

        资源栈中所管理的资源信息列表

        :param stack_resources: The stack_resources of this ListStackResourcesResponse.
        :type stack_resources: list[:class:`huaweicloudsdkaos.v1.StackResource`]
        """
        self._stack_resources = stack_resources

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
        if not isinstance(other, ListStackResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
