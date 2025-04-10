# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHooksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hooks': 'list[Hook]'
    }

    attribute_map = {
        'hooks': 'hooks'
    }

    def __init__(self, hooks=None):
        r"""ListHooksResponse

        The model defined in huaweicloud sdk

        :param hooks: hook列表。
        :type hooks: list[:class:`huaweicloudsdkservicestage.v2.Hook`]
        """
        
        super(ListHooksResponse, self).__init__()

        self._hooks = None
        self.discriminator = None

        if hooks is not None:
            self.hooks = hooks

    @property
    def hooks(self):
        r"""Gets the hooks of this ListHooksResponse.

        hook列表。

        :return: The hooks of this ListHooksResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.Hook`]
        """
        return self._hooks

    @hooks.setter
    def hooks(self, hooks):
        r"""Sets the hooks of this ListHooksResponse.

        hook列表。

        :param hooks: The hooks of this ListHooksResponse.
        :type hooks: list[:class:`huaweicloudsdkservicestage.v2.Hook`]
        """
        self._hooks = hooks

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
        if not isinstance(other, ListHooksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
