# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageWisedesignCombineBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'x': 'int',
        'y': 'int',
        'w': 'int',
        'h': 'int',
        'flipx': 'bool',
        'flipy': 'bool',
        'rotate': 'int',
        'opacity': 'float',
        'image_base64': 'str',
        'image_url': 'str',
        'backgroundattrs': 'ImageWisedesignCombineBodyBackgroundattrs'
    }

    attribute_map = {
        'id': 'id',
        'x': 'x',
        'y': 'y',
        'w': 'w',
        'h': 'h',
        'flipx': 'flipx',
        'flipy': 'flipy',
        'rotate': 'rotate',
        'opacity': 'opacity',
        'image_base64': 'image_base64',
        'image_url': 'image_url',
        'backgroundattrs': 'backgroundattrs'
    }

    def __init__(self, id=None, x=None, y=None, w=None, h=None, flipx=None, flipy=None, rotate=None, opacity=None, image_base64=None, image_url=None, backgroundattrs=None):
        """ImageWisedesignCombineBody

        The model defined in huaweicloud sdk

        :param id: 图层标识，范围5个图层以内, 0 代表背景层
        :type id: int
        :param x: 图层左上角的横坐标位置，单位为px，默认为0
        :type x: int
        :param y: 图层左上角的纵坐标位置，单位为px，默认为0
        :type y: int
        :param w: 图层宽度，单位为px，默认为上传图片的宽度
        :type w: int
        :param h: 图层高度，单位为px，默认为上传图片的高度
        :type h: int
        :param flipx: 是否水平翻转，默认值为false
        :type flipx: bool
        :param flipy: 是否垂直翻转，默认值为false
        :type flipy: bool
        :param rotate: 图层旋转角度，范围[-180, +180]，默认为0
        :type rotate: int
        :param opacity: 图层透明度，范围[0, 1]，默认为1
        :type opacity: float
        :param image_base64: 非背景图的图像数据，base64编码，要求base64编码最长边最大3000px，支持JPG/PNG/BMP/JPEG格式
        :type image_base64: str
        :param image_url: 与image_base64二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  &gt; - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 &gt; - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 &gt; - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。
        :type image_url: str
        :param backgroundattrs: 
        :type backgroundattrs: :class:`huaweicloudsdkimage.v2.ImageWisedesignCombineBodyBackgroundattrs`
        """
        
        

        self._id = None
        self._x = None
        self._y = None
        self._w = None
        self._h = None
        self._flipx = None
        self._flipy = None
        self._rotate = None
        self._opacity = None
        self._image_base64 = None
        self._image_url = None
        self._backgroundattrs = None
        self.discriminator = None

        self.id = id
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if w is not None:
            self.w = w
        if h is not None:
            self.h = h
        if flipx is not None:
            self.flipx = flipx
        if flipy is not None:
            self.flipy = flipy
        if rotate is not None:
            self.rotate = rotate
        if opacity is not None:
            self.opacity = opacity
        if image_base64 is not None:
            self.image_base64 = image_base64
        if image_url is not None:
            self.image_url = image_url
        if backgroundattrs is not None:
            self.backgroundattrs = backgroundattrs

    @property
    def id(self):
        """Gets the id of this ImageWisedesignCombineBody.

        图层标识，范围5个图层以内, 0 代表背景层

        :return: The id of this ImageWisedesignCombineBody.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageWisedesignCombineBody.

        图层标识，范围5个图层以内, 0 代表背景层

        :param id: The id of this ImageWisedesignCombineBody.
        :type id: int
        """
        self._id = id

    @property
    def x(self):
        """Gets the x of this ImageWisedesignCombineBody.

        图层左上角的横坐标位置，单位为px，默认为0

        :return: The x of this ImageWisedesignCombineBody.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this ImageWisedesignCombineBody.

        图层左上角的横坐标位置，单位为px，默认为0

        :param x: The x of this ImageWisedesignCombineBody.
        :type x: int
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this ImageWisedesignCombineBody.

        图层左上角的纵坐标位置，单位为px，默认为0

        :return: The y of this ImageWisedesignCombineBody.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this ImageWisedesignCombineBody.

        图层左上角的纵坐标位置，单位为px，默认为0

        :param y: The y of this ImageWisedesignCombineBody.
        :type y: int
        """
        self._y = y

    @property
    def w(self):
        """Gets the w of this ImageWisedesignCombineBody.

        图层宽度，单位为px，默认为上传图片的宽度

        :return: The w of this ImageWisedesignCombineBody.
        :rtype: int
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this ImageWisedesignCombineBody.

        图层宽度，单位为px，默认为上传图片的宽度

        :param w: The w of this ImageWisedesignCombineBody.
        :type w: int
        """
        self._w = w

    @property
    def h(self):
        """Gets the h of this ImageWisedesignCombineBody.

        图层高度，单位为px，默认为上传图片的高度

        :return: The h of this ImageWisedesignCombineBody.
        :rtype: int
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this ImageWisedesignCombineBody.

        图层高度，单位为px，默认为上传图片的高度

        :param h: The h of this ImageWisedesignCombineBody.
        :type h: int
        """
        self._h = h

    @property
    def flipx(self):
        """Gets the flipx of this ImageWisedesignCombineBody.

        是否水平翻转，默认值为false

        :return: The flipx of this ImageWisedesignCombineBody.
        :rtype: bool
        """
        return self._flipx

    @flipx.setter
    def flipx(self, flipx):
        """Sets the flipx of this ImageWisedesignCombineBody.

        是否水平翻转，默认值为false

        :param flipx: The flipx of this ImageWisedesignCombineBody.
        :type flipx: bool
        """
        self._flipx = flipx

    @property
    def flipy(self):
        """Gets the flipy of this ImageWisedesignCombineBody.

        是否垂直翻转，默认值为false

        :return: The flipy of this ImageWisedesignCombineBody.
        :rtype: bool
        """
        return self._flipy

    @flipy.setter
    def flipy(self, flipy):
        """Sets the flipy of this ImageWisedesignCombineBody.

        是否垂直翻转，默认值为false

        :param flipy: The flipy of this ImageWisedesignCombineBody.
        :type flipy: bool
        """
        self._flipy = flipy

    @property
    def rotate(self):
        """Gets the rotate of this ImageWisedesignCombineBody.

        图层旋转角度，范围[-180, +180]，默认为0

        :return: The rotate of this ImageWisedesignCombineBody.
        :rtype: int
        """
        return self._rotate

    @rotate.setter
    def rotate(self, rotate):
        """Sets the rotate of this ImageWisedesignCombineBody.

        图层旋转角度，范围[-180, +180]，默认为0

        :param rotate: The rotate of this ImageWisedesignCombineBody.
        :type rotate: int
        """
        self._rotate = rotate

    @property
    def opacity(self):
        """Gets the opacity of this ImageWisedesignCombineBody.

        图层透明度，范围[0, 1]，默认为1

        :return: The opacity of this ImageWisedesignCombineBody.
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this ImageWisedesignCombineBody.

        图层透明度，范围[0, 1]，默认为1

        :param opacity: The opacity of this ImageWisedesignCombineBody.
        :type opacity: float
        """
        self._opacity = opacity

    @property
    def image_base64(self):
        """Gets the image_base64 of this ImageWisedesignCombineBody.

        非背景图的图像数据，base64编码，要求base64编码最长边最大3000px，支持JPG/PNG/BMP/JPEG格式

        :return: The image_base64 of this ImageWisedesignCombineBody.
        :rtype: str
        """
        return self._image_base64

    @image_base64.setter
    def image_base64(self, image_base64):
        """Sets the image_base64 of this ImageWisedesignCombineBody.

        非背景图的图像数据，base64编码，要求base64编码最长边最大3000px，支持JPG/PNG/BMP/JPEG格式

        :param image_base64: The image_base64 of this ImageWisedesignCombineBody.
        :type image_base64: str
        """
        self._image_base64 = image_base64

    @property
    def image_url(self):
        """Gets the image_url of this ImageWisedesignCombineBody.

        与image_base64二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  > - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 > - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 > - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。

        :return: The image_url of this ImageWisedesignCombineBody.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this ImageWisedesignCombineBody.

        与image_base64二选一  图片的URL路径，目前支持：  - 公网HTTP/HTTPS URL  - 华为云OBS提供的URL，使用OBS数据需要进行授权。包括对服务授权、临时授权、匿名公开授权。详请参见[[配置OBS服务的访问权限](https://support.huaweicloud.com/api-moderation/moderation_03_0020.html)](tag:hc)[[配置OBS服务的访问权限](https://support.huaweicloud.com/intl/zh-cn/api-moderation/moderation_03_0020.html)](tag:hk)。  > - 接口响应时间依赖于图片的下载时间，如果图片下载时间过长，会返回接口调用失败。 > - 请保证被检测图片所在的存储服务稳定可靠，建议您使用华为云OBS存储。 > - lmage不支持跨区域OBS，OBS的区域需要和服务保持一致。

        :param image_url: The image_url of this ImageWisedesignCombineBody.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def backgroundattrs(self):
        """Gets the backgroundattrs of this ImageWisedesignCombineBody.

        :return: The backgroundattrs of this ImageWisedesignCombineBody.
        :rtype: :class:`huaweicloudsdkimage.v2.ImageWisedesignCombineBodyBackgroundattrs`
        """
        return self._backgroundattrs

    @backgroundattrs.setter
    def backgroundattrs(self, backgroundattrs):
        """Sets the backgroundattrs of this ImageWisedesignCombineBody.

        :param backgroundattrs: The backgroundattrs of this ImageWisedesignCombineBody.
        :type backgroundattrs: :class:`huaweicloudsdkimage.v2.ImageWisedesignCombineBodyBackgroundattrs`
        """
        self._backgroundattrs = backgroundattrs

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
        if not isinstance(other, ImageWisedesignCombineBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
