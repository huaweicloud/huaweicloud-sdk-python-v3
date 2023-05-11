# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_metadatas': 'list[VersionMetadata]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'version_metadatas': 'version_metadatas',
        'page_info': 'page_info'
    }

    def __init__(self, version_metadatas=None, page_info=None):
        """ListSecretVersionsResponse

        The model defined in huaweicloud sdk

        :param version_metadatas: version_metadata对象。
        :type version_metadatas: list[:class:`huaweicloudsdkcsms.v1.VersionMetadata`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcsms.v1.PageInfo`
        """
        
        super(ListSecretVersionsResponse, self).__init__()

        self._version_metadatas = None
        self._page_info = None
        self.discriminator = None

        if version_metadatas is not None:
            self.version_metadatas = version_metadatas
        if page_info is not None:
            self.page_info = page_info

    @property
    def version_metadatas(self):
        """Gets the version_metadatas of this ListSecretVersionsResponse.

        version_metadata对象。

        :return: The version_metadatas of this ListSecretVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.VersionMetadata`]
        """
        return self._version_metadatas

    @version_metadatas.setter
    def version_metadatas(self, version_metadatas):
        """Sets the version_metadatas of this ListSecretVersionsResponse.

        version_metadata对象。

        :param version_metadatas: The version_metadatas of this ListSecretVersionsResponse.
        :type version_metadatas: list[:class:`huaweicloudsdkcsms.v1.VersionMetadata`]
        """
        self._version_metadatas = version_metadatas

    @property
    def page_info(self):
        """Gets the page_info of this ListSecretVersionsResponse.

        :return: The page_info of this ListSecretVersionsResponse.
        :rtype: :class:`huaweicloudsdkcsms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListSecretVersionsResponse.

        :param page_info: The page_info of this ListSecretVersionsResponse.
        :type page_info: :class:`huaweicloudsdkcsms.v1.PageInfo`
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
        if not isinstance(other, ListSecretVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
