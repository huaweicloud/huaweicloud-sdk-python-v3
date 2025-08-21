# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupPermissionResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope': 'str'
    }

    attribute_map = {
        'scope': 'scope'
    }

    def __init__(self, scope=None):
        r"""ListGroupPermissionResourcesRequest

        The model defined in huaweicloud sdk

        :param scope: **参数解释：** 创建资源类型。 **约束限制：** - group 代码组。 - project  项目。 - all 代码组和项目
        :type scope: str
        """
        
        

        self._scope = None
        self.discriminator = None

        if scope is not None:
            self.scope = scope

    @property
    def scope(self):
        r"""Gets the scope of this ListGroupPermissionResourcesRequest.

        **参数解释：** 创建资源类型。 **约束限制：** - group 代码组。 - project  项目。 - all 代码组和项目

        :return: The scope of this ListGroupPermissionResourcesRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ListGroupPermissionResourcesRequest.

        **参数解释：** 创建资源类型。 **约束限制：** - group 代码组。 - project  项目。 - all 代码组和项目

        :param scope: The scope of this ListGroupPermissionResourcesRequest.
        :type scope: str
        """
        self._scope = scope

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
        if not isinstance(other, ListGroupPermissionResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
