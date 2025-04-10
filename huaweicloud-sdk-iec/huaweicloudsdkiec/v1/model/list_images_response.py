# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'images': 'list[ImageList]',
        'total': 'int'
    }

    attribute_map = {
        'images': 'images',
        'total': 'total'
    }

    def __init__(self, images=None, total=None):
        r"""ListImagesResponse

        The model defined in huaweicloud sdk

        :param images: 查询返回的镜像列表。
        :type images: list[:class:`huaweicloudsdkiec.v1.ImageList`]
        :param total: 列表元素个数，分页查询时返回总数。
        :type total: int
        """
        
        super(ListImagesResponse, self).__init__()

        self._images = None
        self._total = None
        self.discriminator = None

        if images is not None:
            self.images = images
        if total is not None:
            self.total = total

    @property
    def images(self):
        r"""Gets the images of this ListImagesResponse.

        查询返回的镜像列表。

        :return: The images of this ListImagesResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.ImageList`]
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this ListImagesResponse.

        查询返回的镜像列表。

        :param images: The images of this ListImagesResponse.
        :type images: list[:class:`huaweicloudsdkiec.v1.ImageList`]
        """
        self._images = images

    @property
    def total(self):
        r"""Gets the total of this ListImagesResponse.

        列表元素个数，分页查询时返回总数。

        :return: The total of this ListImagesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListImagesResponse.

        列表元素个数，分页查询时返回总数。

        :param total: The total of this ListImagesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListImagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
