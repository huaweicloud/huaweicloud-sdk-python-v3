# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAccessKeysV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_keys': 'list[AccessKeyMetadata]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'access_keys': 'access_keys',
        'page_info': 'page_info'
    }

    def __init__(self, access_keys=None, page_info=None):
        r"""ListAccessKeysV5Response

        The model defined in huaweicloud sdk

        :param access_keys: 永久访问密钥列表。
        :type access_keys: list[:class:`huaweicloudsdkiam.v5.AccessKeyMetadata`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super(ListAccessKeysV5Response, self).__init__()

        self._access_keys = None
        self._page_info = None
        self.discriminator = None

        if access_keys is not None:
            self.access_keys = access_keys
        if page_info is not None:
            self.page_info = page_info

    @property
    def access_keys(self):
        r"""Gets the access_keys of this ListAccessKeysV5Response.

        永久访问密钥列表。

        :return: The access_keys of this ListAccessKeysV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.AccessKeyMetadata`]
        """
        return self._access_keys

    @access_keys.setter
    def access_keys(self, access_keys):
        r"""Sets the access_keys of this ListAccessKeysV5Response.

        永久访问密钥列表。

        :param access_keys: The access_keys of this ListAccessKeysV5Response.
        :type access_keys: list[:class:`huaweicloudsdkiam.v5.AccessKeyMetadata`]
        """
        self._access_keys = access_keys

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAccessKeysV5Response.

        :return: The page_info of this ListAccessKeysV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAccessKeysV5Response.

        :param page_info: The page_info of this ListAccessKeysV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAccessKeysV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
