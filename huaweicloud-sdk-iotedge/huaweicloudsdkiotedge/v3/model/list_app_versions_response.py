# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'page_info': 'PageInfoDTO',
        'app_versions': 'list[QueryAppVersionResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'page_info': 'page_info',
        'app_versions': 'app_versions'
    }

    def __init__(self, count=None, page_info=None, app_versions=None):
        r"""ListAppVersionsResponse

        The model defined in huaweicloud sdk

        :param count: 总记录数
        :type count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        :param app_versions: 每页记录数
        :type app_versions: list[:class:`huaweicloudsdkiotedge.v3.QueryAppVersionResponseDTO`]
        """
        
        super(ListAppVersionsResponse, self).__init__()

        self._count = None
        self._page_info = None
        self._app_versions = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info
        if app_versions is not None:
            self.app_versions = app_versions

    @property
    def count(self):
        r"""Gets the count of this ListAppVersionsResponse.

        总记录数

        :return: The count of this ListAppVersionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAppVersionsResponse.

        总记录数

        :param count: The count of this ListAppVersionsResponse.
        :type count: int
        """
        self._count = count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAppVersionsResponse.

        :return: The page_info of this ListAppVersionsResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAppVersionsResponse.

        :param page_info: The page_info of this ListAppVersionsResponse.
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        self._page_info = page_info

    @property
    def app_versions(self):
        r"""Gets the app_versions of this ListAppVersionsResponse.

        每页记录数

        :return: The app_versions of this ListAppVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.QueryAppVersionResponseDTO`]
        """
        return self._app_versions

    @app_versions.setter
    def app_versions(self, app_versions):
        r"""Sets the app_versions of this ListAppVersionsResponse.

        每页记录数

        :param app_versions: The app_versions of this ListAppVersionsResponse.
        :type app_versions: list[:class:`huaweicloudsdkiotedge.v3.QueryAppVersionResponseDTO`]
        """
        self._app_versions = app_versions

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
        if not isinstance(other, ListAppVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
