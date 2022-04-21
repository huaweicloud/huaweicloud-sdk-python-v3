# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointWhiteRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'whitelist': 'list[str]',
        'enable_whitelist': 'bool'
    }

    attribute_map = {
        'whitelist': 'whitelist',
        'enable_whitelist': 'enable_whitelist'
    }

    def __init__(self, whitelist=None, enable_whitelist=None):
        """UpdateEndpointWhiteRequestBody

        The model defined in huaweicloud sdk

        :param whitelist: 更新或删除用于控制访问终端节点的白名单。此参数可以添加IPv4或CIDR： ● 当取值不为空时，表示将白名单更新为取值所示内容。 ● 当取值为空时，表示删除所有白名单。 默认为空列表。
        :type whitelist: list[str]
        :param enable_whitelist: 是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 默认值为false。
        :type enable_whitelist: bool
        """
        
        

        self._whitelist = None
        self._enable_whitelist = None
        self.discriminator = None

        if whitelist is not None:
            self.whitelist = whitelist
        if enable_whitelist is not None:
            self.enable_whitelist = enable_whitelist

    @property
    def whitelist(self):
        """Gets the whitelist of this UpdateEndpointWhiteRequestBody.

        更新或删除用于控制访问终端节点的白名单。此参数可以添加IPv4或CIDR： ● 当取值不为空时，表示将白名单更新为取值所示内容。 ● 当取值为空时，表示删除所有白名单。 默认为空列表。

        :return: The whitelist of this UpdateEndpointWhiteRequestBody.
        :rtype: list[str]
        """
        return self._whitelist

    @whitelist.setter
    def whitelist(self, whitelist):
        """Sets the whitelist of this UpdateEndpointWhiteRequestBody.

        更新或删除用于控制访问终端节点的白名单。此参数可以添加IPv4或CIDR： ● 当取值不为空时，表示将白名单更新为取值所示内容。 ● 当取值为空时，表示删除所有白名单。 默认为空列表。

        :param whitelist: The whitelist of this UpdateEndpointWhiteRequestBody.
        :type whitelist: list[str]
        """
        self._whitelist = whitelist

    @property
    def enable_whitelist(self):
        """Gets the enable_whitelist of this UpdateEndpointWhiteRequestBody.

        是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 默认值为false。

        :return: The enable_whitelist of this UpdateEndpointWhiteRequestBody.
        :rtype: bool
        """
        return self._enable_whitelist

    @enable_whitelist.setter
    def enable_whitelist(self, enable_whitelist):
        """Sets the enable_whitelist of this UpdateEndpointWhiteRequestBody.

        是否开启网络ACL隔离。 ● true：开启网络ACL隔离 ● false：不开启网络ACL隔离 默认值为false。

        :param enable_whitelist: The enable_whitelist of this UpdateEndpointWhiteRequestBody.
        :type enable_whitelist: bool
        """
        self._enable_whitelist = enable_whitelist

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
        if not isinstance(other, UpdateEndpointWhiteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
