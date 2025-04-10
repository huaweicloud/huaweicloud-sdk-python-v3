# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppImageResponse(SdkResponse):

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
        'app_images': 'list[QueryAppImageResponseDTO]'
    }

    attribute_map = {
        'count': 'count',
        'page_info': 'page_info',
        'app_images': 'app_images'
    }

    def __init__(self, count=None, page_info=None, app_images=None):
        r"""ListAppImageResponse

        The model defined in huaweicloud sdk

        :param count: 总记录数
        :type count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        :param app_images: 每页记录数
        :type app_images: list[:class:`huaweicloudsdkiotedge.v3.QueryAppImageResponseDTO`]
        """
        
        super(ListAppImageResponse, self).__init__()

        self._count = None
        self._page_info = None
        self._app_images = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if page_info is not None:
            self.page_info = page_info
        if app_images is not None:
            self.app_images = app_images

    @property
    def count(self):
        r"""Gets the count of this ListAppImageResponse.

        总记录数

        :return: The count of this ListAppImageResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAppImageResponse.

        总记录数

        :param count: The count of this ListAppImageResponse.
        :type count: int
        """
        self._count = count

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAppImageResponse.

        :return: The page_info of this ListAppImageResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAppImageResponse.

        :param page_info: The page_info of this ListAppImageResponse.
        :type page_info: :class:`huaweicloudsdkiotedge.v3.PageInfoDTO`
        """
        self._page_info = page_info

    @property
    def app_images(self):
        r"""Gets the app_images of this ListAppImageResponse.

        每页记录数

        :return: The app_images of this ListAppImageResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v3.QueryAppImageResponseDTO`]
        """
        return self._app_images

    @app_images.setter
    def app_images(self, app_images):
        r"""Sets the app_images of this ListAppImageResponse.

        每页记录数

        :param app_images: The app_images of this ListAppImageResponse.
        :type app_images: list[:class:`huaweicloudsdkiotedge.v3.QueryAppImageResponseDTO`]
        """
        self._app_images = app_images

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
        if not isinstance(other, ListAppImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
