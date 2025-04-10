# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachPluginToApiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attached_plugins': 'list[PluginApiAttachInfo]'
    }

    attribute_map = {
        'attached_plugins': 'attached_plugins'
    }

    def __init__(self, attached_plugins=None):
        r"""AttachPluginToApiResponse

        The model defined in huaweicloud sdk

        :param attached_plugins: 绑定插件信息列表。
        :type attached_plugins: list[:class:`huaweicloudsdkroma.v2.PluginApiAttachInfo`]
        """
        
        super(AttachPluginToApiResponse, self).__init__()

        self._attached_plugins = None
        self.discriminator = None

        if attached_plugins is not None:
            self.attached_plugins = attached_plugins

    @property
    def attached_plugins(self):
        r"""Gets the attached_plugins of this AttachPluginToApiResponse.

        绑定插件信息列表。

        :return: The attached_plugins of this AttachPluginToApiResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.PluginApiAttachInfo`]
        """
        return self._attached_plugins

    @attached_plugins.setter
    def attached_plugins(self, attached_plugins):
        r"""Sets the attached_plugins of this AttachPluginToApiResponse.

        绑定插件信息列表。

        :param attached_plugins: The attached_plugins of this AttachPluginToApiResponse.
        :type attached_plugins: list[:class:`huaweicloudsdkroma.v2.PluginApiAttachInfo`]
        """
        self._attached_plugins = attached_plugins

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
        if not isinstance(other, AttachPluginToApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
