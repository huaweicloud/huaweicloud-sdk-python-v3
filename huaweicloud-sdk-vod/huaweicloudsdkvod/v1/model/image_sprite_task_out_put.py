# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageSpriteTaskOutPut:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_info': 'ObsInfo',
        'height': 'int',
        'width': 'int',
        'sprite_image_list': 'list[str]'
    }

    attribute_map = {
        'obs_info': 'obs_info',
        'height': 'height',
        'width': 'width',
        'sprite_image_list': 'sprite_image_list'
    }

    def __init__(self, obs_info=None, height=None, width=None, sprite_image_list=None):
        r"""ImageSpriteTaskOutPut

        The model defined in huaweicloud sdk

        :param obs_info: 
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param height: 雪碧图的高度
        :type height: int
        :param width: 雪碧图的宽度
        :type width: int
        :param sprite_image_list: 雪碧图对象列表
        :type sprite_image_list: list[str]
        """
        
        

        self._obs_info = None
        self._height = None
        self._width = None
        self._sprite_image_list = None
        self.discriminator = None

        if obs_info is not None:
            self.obs_info = obs_info
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if sprite_image_list is not None:
            self.sprite_image_list = sprite_image_list

    @property
    def obs_info(self):
        r"""Gets the obs_info of this ImageSpriteTaskOutPut.

        :return: The obs_info of this ImageSpriteTaskOutPut.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._obs_info

    @obs_info.setter
    def obs_info(self, obs_info):
        r"""Sets the obs_info of this ImageSpriteTaskOutPut.

        :param obs_info: The obs_info of this ImageSpriteTaskOutPut.
        :type obs_info: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._obs_info = obs_info

    @property
    def height(self):
        r"""Gets the height of this ImageSpriteTaskOutPut.

        雪碧图的高度

        :return: The height of this ImageSpriteTaskOutPut.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this ImageSpriteTaskOutPut.

        雪碧图的高度

        :param height: The height of this ImageSpriteTaskOutPut.
        :type height: int
        """
        self._height = height

    @property
    def width(self):
        r"""Gets the width of this ImageSpriteTaskOutPut.

        雪碧图的宽度

        :return: The width of this ImageSpriteTaskOutPut.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this ImageSpriteTaskOutPut.

        雪碧图的宽度

        :param width: The width of this ImageSpriteTaskOutPut.
        :type width: int
        """
        self._width = width

    @property
    def sprite_image_list(self):
        r"""Gets the sprite_image_list of this ImageSpriteTaskOutPut.

        雪碧图对象列表

        :return: The sprite_image_list of this ImageSpriteTaskOutPut.
        :rtype: list[str]
        """
        return self._sprite_image_list

    @sprite_image_list.setter
    def sprite_image_list(self, sprite_image_list):
        r"""Sets the sprite_image_list of this ImageSpriteTaskOutPut.

        雪碧图对象列表

        :param sprite_image_list: The sprite_image_list of this ImageSpriteTaskOutPut.
        :type sprite_image_list: list[str]
        """
        self._sprite_image_list = sprite_image_list

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
        if not isinstance(other, ImageSpriteTaskOutPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
