# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyVersionsV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'versions': 'list[PolicyVersion]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'versions': 'versions',
        'page_info': 'page_info'
    }

    def __init__(self, versions=None, page_info=None):
        r"""ListPolicyVersionsV5Response

        The model defined in huaweicloud sdk

        :param versions: 身份策略版本列表。
        :type versions: list[:class:`huaweicloudsdkiam.v5.PolicyVersion`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super(ListPolicyVersionsV5Response, self).__init__()

        self._versions = None
        self._page_info = None
        self.discriminator = None

        if versions is not None:
            self.versions = versions
        if page_info is not None:
            self.page_info = page_info

    @property
    def versions(self):
        r"""Gets the versions of this ListPolicyVersionsV5Response.

        身份策略版本列表。

        :return: The versions of this ListPolicyVersionsV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.PolicyVersion`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ListPolicyVersionsV5Response.

        身份策略版本列表。

        :param versions: The versions of this ListPolicyVersionsV5Response.
        :type versions: list[:class:`huaweicloudsdkiam.v5.PolicyVersion`]
        """
        self._versions = versions

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPolicyVersionsV5Response.

        :return: The page_info of this ListPolicyVersionsV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPolicyVersionsV5Response.

        :param page_info: The page_info of this ListPolicyVersionsV5Response.
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
        if not isinstance(other, ListPolicyVersionsV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
