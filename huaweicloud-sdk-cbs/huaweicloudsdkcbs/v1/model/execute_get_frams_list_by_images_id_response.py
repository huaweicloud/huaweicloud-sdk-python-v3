# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteGetFramsListByImagesIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_frames': 'list[ImageFrame]',
        'total': 'int',
        'offset': 'int',
        'count': 'int'
    }

    attribute_map = {
        'image_frames': 'image_frames',
        'total': 'total',
        'offset': 'offset',
        'count': 'count'
    }

    def __init__(self, image_frames=None, total=None, offset=None, count=None):
        """ExecuteGetFramsListByImagesIdResponse

        The model defined in huaweicloud sdk

        :param image_frames: 播报框
        :type image_frames: list[:class:`huaweicloudsdkcbs.v1.ImageFrame`]
        :param total: 播报框总数
        :type total: int
        :param offset: 起始偏移量
        :type offset: int
        :param count: 本次查询数量
        :type count: int
        """
        
        super(ExecuteGetFramsListByImagesIdResponse, self).__init__()

        self._image_frames = None
        self._total = None
        self._offset = None
        self._count = None
        self.discriminator = None

        if image_frames is not None:
            self.image_frames = image_frames
        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count

    @property
    def image_frames(self):
        """Gets the image_frames of this ExecuteGetFramsListByImagesIdResponse.

        播报框

        :return: The image_frames of this ExecuteGetFramsListByImagesIdResponse.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.ImageFrame`]
        """
        return self._image_frames

    @image_frames.setter
    def image_frames(self, image_frames):
        """Sets the image_frames of this ExecuteGetFramsListByImagesIdResponse.

        播报框

        :param image_frames: The image_frames of this ExecuteGetFramsListByImagesIdResponse.
        :type image_frames: list[:class:`huaweicloudsdkcbs.v1.ImageFrame`]
        """
        self._image_frames = image_frames

    @property
    def total(self):
        """Gets the total of this ExecuteGetFramsListByImagesIdResponse.

        播报框总数

        :return: The total of this ExecuteGetFramsListByImagesIdResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ExecuteGetFramsListByImagesIdResponse.

        播报框总数

        :param total: The total of this ExecuteGetFramsListByImagesIdResponse.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        """Gets the offset of this ExecuteGetFramsListByImagesIdResponse.

        起始偏移量

        :return: The offset of this ExecuteGetFramsListByImagesIdResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ExecuteGetFramsListByImagesIdResponse.

        起始偏移量

        :param offset: The offset of this ExecuteGetFramsListByImagesIdResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        """Gets the count of this ExecuteGetFramsListByImagesIdResponse.

        本次查询数量

        :return: The count of this ExecuteGetFramsListByImagesIdResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ExecuteGetFramsListByImagesIdResponse.

        本次查询数量

        :param count: The count of this ExecuteGetFramsListByImagesIdResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ExecuteGetFramsListByImagesIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
