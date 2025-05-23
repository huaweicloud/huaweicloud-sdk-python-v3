# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStacksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stacks': 'list[Stack]'
    }

    attribute_map = {
        'stacks': 'stacks'
    }

    def __init__(self, stacks=None):
        r"""ListStacksResponse

        The model defined in huaweicloud sdk

        :param stacks: 资源栈列表。默认按照生成时间降序排序，最新生成的在最前
        :type stacks: list[:class:`huaweicloudsdkaos.v1.Stack`]
        """
        
        super(ListStacksResponse, self).__init__()

        self._stacks = None
        self.discriminator = None

        if stacks is not None:
            self.stacks = stacks

    @property
    def stacks(self):
        r"""Gets the stacks of this ListStacksResponse.

        资源栈列表。默认按照生成时间降序排序，最新生成的在最前

        :return: The stacks of this ListStacksResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.Stack`]
        """
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        r"""Sets the stacks of this ListStacksResponse.

        资源栈列表。默认按照生成时间降序排序，最新生成的在最前

        :param stacks: The stacks of this ListStacksResponse.
        :type stacks: list[:class:`huaweicloudsdkaos.v1.Stack`]
        """
        self._stacks = stacks

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
        if not isinstance(other, ListStacksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
