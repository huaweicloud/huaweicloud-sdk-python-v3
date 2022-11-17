# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLifeCycleHooksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lifecycle_hooks': 'list[LifecycleHookList]'
    }

    attribute_map = {
        'lifecycle_hooks': 'lifecycle_hooks'
    }

    def __init__(self, lifecycle_hooks=None):
        """ListLifeCycleHooksResponse

        The model defined in huaweicloud sdk

        :param lifecycle_hooks: 生命周期挂钩列表。
        :type lifecycle_hooks: list[:class:`huaweicloudsdkas.v1.LifecycleHookList`]
        """
        
        super(ListLifeCycleHooksResponse, self).__init__()

        self._lifecycle_hooks = None
        self.discriminator = None

        if lifecycle_hooks is not None:
            self.lifecycle_hooks = lifecycle_hooks

    @property
    def lifecycle_hooks(self):
        """Gets the lifecycle_hooks of this ListLifeCycleHooksResponse.

        生命周期挂钩列表。

        :return: The lifecycle_hooks of this ListLifeCycleHooksResponse.
        :rtype: list[:class:`huaweicloudsdkas.v1.LifecycleHookList`]
        """
        return self._lifecycle_hooks

    @lifecycle_hooks.setter
    def lifecycle_hooks(self, lifecycle_hooks):
        """Sets the lifecycle_hooks of this ListLifeCycleHooksResponse.

        生命周期挂钩列表。

        :param lifecycle_hooks: The lifecycle_hooks of this ListLifeCycleHooksResponse.
        :type lifecycle_hooks: list[:class:`huaweicloudsdkas.v1.LifecycleHookList`]
        """
        self._lifecycle_hooks = lifecycle_hooks

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
        if not isinstance(other, ListLifeCycleHooksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
