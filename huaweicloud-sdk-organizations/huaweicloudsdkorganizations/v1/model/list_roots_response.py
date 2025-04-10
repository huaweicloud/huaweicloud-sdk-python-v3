# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRootsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'roots': 'list[RootDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'roots': 'roots',
        'page_info': 'page_info'
    }

    def __init__(self, roots=None, page_info=None):
        r"""ListRootsResponse

        The model defined in huaweicloud sdk

        :param roots: 在组织中定义的根列表。
        :type roots: list[:class:`huaweicloudsdkorganizations.v1.RootDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        
        super(ListRootsResponse, self).__init__()

        self._roots = None
        self._page_info = None
        self.discriminator = None

        if roots is not None:
            self.roots = roots
        if page_info is not None:
            self.page_info = page_info

    @property
    def roots(self):
        r"""Gets the roots of this ListRootsResponse.

        在组织中定义的根列表。

        :return: The roots of this ListRootsResponse.
        :rtype: list[:class:`huaweicloudsdkorganizations.v1.RootDto`]
        """
        return self._roots

    @roots.setter
    def roots(self, roots):
        r"""Sets the roots of this ListRootsResponse.

        在组织中定义的根列表。

        :param roots: The roots of this ListRootsResponse.
        :type roots: list[:class:`huaweicloudsdkorganizations.v1.RootDto`]
        """
        self._roots = roots

    @property
    def page_info(self):
        r"""Gets the page_info of this ListRootsResponse.

        :return: The page_info of this ListRootsResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListRootsResponse.

        :param page_info: The page_info of this ListRootsResponse.
        :type page_info: :class:`huaweicloudsdkorganizations.v1.PageInfoDto`
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
        if not isinstance(other, ListRootsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
