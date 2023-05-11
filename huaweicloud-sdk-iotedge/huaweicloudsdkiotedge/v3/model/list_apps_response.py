# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppsResponse(SdkResponse):

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
        'apps': 'list[QueryAppBriefResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'page_info': 'page_info',
        'apps': 'apps'
    }

    def __init__(self, count=None, page_info=None, apps=None):
        """ListAppsResponse

        The model defined in huaweicloud sdk

        :param count: 总记录数
        :type count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        :param apps: 每页记录数
        :type apps: list[:class:`huaweicloudsdkiotedge.v3.QueryAppBriefResponseDTO`]
        """
        
        super(ListAppsResponse, self).__init__()

        self._count = None
        self._page_info = None
        self._apps = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info
        if apps is not None:
            self.apps = apps

    @property
    def count(self):
        """Gets the count of this ListAppsResponse.

        总记录数

        :return: The count of this ListAppsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAppsResponse.

        总记录数

        :param count: The count of this ListAppsResponse.
        :type count: int
        """
        self._count = count

    @property
    def page_info(self):
        """Gets the page_info of this ListAppsResponse.

        :return: The page_info of this ListAppsResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAppsResponse.

        :param page_info: The page_info of this ListAppsResponse.
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        self._page_info = page_info

    @property
    def apps(self):
        """Gets the apps of this ListAppsResponse.

        每页记录数

        :return: The apps of this ListAppsResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.QueryAppBriefResponseDTO`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this ListAppsResponse.

        每页记录数

        :param apps: The apps of this ListAppsResponse.
        :type apps: list[:class:`huaweicloudsdkiotedge.v3.QueryAppBriefResponseDTO`]
        """
        self._apps = apps

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
        if not isinstance(other, ListAppsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
