# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuthorizingAppsV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auths': 'list[ApiAuthRelations]'
    }

    attribute_map = {
        'auths': 'auths'
    }

    def __init__(self, auths=None):
        r"""CreateAuthorizingAppsV2Response

        The model defined in huaweicloud sdk

        :param auths: API与APP的授权关系列表
        :type auths: list[:class:`huaweicloudsdkapig.v2.ApiAuthRelations`]
        """
        
        super(CreateAuthorizingAppsV2Response, self).__init__()

        self._auths = None
        self.discriminator = None

        if auths is not None:
            self.auths = auths

    @property
    def auths(self):
        r"""Gets the auths of this CreateAuthorizingAppsV2Response.

        API与APP的授权关系列表

        :return: The auths of this CreateAuthorizingAppsV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ApiAuthRelations`]
        """
        return self._auths

    @auths.setter
    def auths(self, auths):
        r"""Sets the auths of this CreateAuthorizingAppsV2Response.

        API与APP的授权关系列表

        :param auths: The auths of this CreateAuthorizingAppsV2Response.
        :type auths: list[:class:`huaweicloudsdkapig.v2.ApiAuthRelations`]
        """
        self._auths = auths

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
        if not isinstance(other, CreateAuthorizingAppsV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
