# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAgentPathResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'added': 'list[str]',
        'existed': 'list[str]'
    }

    attribute_map = {
        'added': 'added',
        'existed': 'existed'
    }

    def __init__(self, added=None, existed=None):
        """AddAgentPathResponse

        The model defined in huaweicloud sdk

        :param added: 新添加成功的路径列表
        :type added: list[str]
        :param existed: 已经存在的路径列表
        :type existed: list[str]
        """
        
        super(AddAgentPathResponse, self).__init__()

        self._added = None
        self._existed = None
        self.discriminator = None

        if added is not None:
            self.added = added
        if existed is not None:
            self.existed = existed

    @property
    def added(self):
        """Gets the added of this AddAgentPathResponse.

        新添加成功的路径列表

        :return: The added of this AddAgentPathResponse.
        :rtype: list[str]
        """
        return self._added

    @added.setter
    def added(self, added):
        """Sets the added of this AddAgentPathResponse.

        新添加成功的路径列表

        :param added: The added of this AddAgentPathResponse.
        :type added: list[str]
        """
        self._added = added

    @property
    def existed(self):
        """Gets the existed of this AddAgentPathResponse.

        已经存在的路径列表

        :return: The existed of this AddAgentPathResponse.
        :rtype: list[str]
        """
        return self._existed

    @existed.setter
    def existed(self, existed):
        """Sets the existed of this AddAgentPathResponse.

        已经存在的路径列表

        :param existed: The existed of this AddAgentPathResponse.
        :type existed: list[str]
        """
        self._existed = existed

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
        if not isinstance(other, AddAgentPathResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
