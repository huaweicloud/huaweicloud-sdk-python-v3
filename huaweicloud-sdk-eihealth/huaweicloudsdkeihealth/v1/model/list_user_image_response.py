# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserImageResponse(SdkResponse):

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
        'images': 'list[ImageDetailRsp]'
    }

    attribute_map = {
        'count': 'count',
        'images': 'images'
    }

    def __init__(self, count=None, images=None):
        r"""ListUserImageResponse

        The model defined in huaweicloud sdk

        :param count: 镜像总数
        :type count: int
        :param images: 镜像详情列表
        :type images: list[:class:`huaweicloudsdkeihealth.v1.ImageDetailRsp`]
        """
        
        super(ListUserImageResponse, self).__init__()

        self._count = None
        self._images = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if images is not None:
            self.images = images

    @property
    def count(self):
        r"""Gets the count of this ListUserImageResponse.

        镜像总数

        :return: The count of this ListUserImageResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListUserImageResponse.

        镜像总数

        :param count: The count of this ListUserImageResponse.
        :type count: int
        """
        self._count = count

    @property
    def images(self):
        r"""Gets the images of this ListUserImageResponse.

        镜像详情列表

        :return: The images of this ListUserImageResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ImageDetailRsp`]
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this ListUserImageResponse.

        镜像详情列表

        :param images: The images of this ListUserImageResponse.
        :type images: list[:class:`huaweicloudsdkeihealth.v1.ImageDetailRsp`]
        """
        self._images = images

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
        if not isinstance(other, ListUserImageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
