# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateImageCacheRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'images': 'list[str]',
        'image_cache_size': 'int',
        'retention_days': 'int',
        'building_config': 'ImageCacheBuildingConfig'
    }

    attribute_map = {
        'name': 'name',
        'images': 'images',
        'image_cache_size': 'image_cache_size',
        'retention_days': 'retention_days',
        'building_config': 'building_config'
    }

    def __init__(self, name=None, images=None, image_cache_size=None, retention_days=None, building_config=None):
        r"""CreateImageCacheRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 镜像缓存名称。 **约束限制：** 不涉及 **取值范围：** 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-128位，且不能以中划线(-)结尾。镜像缓存名称不可重复。 **默认取值：** 不涉及 
        :type name: str
        :param images: 镜像缓存中的容器镜像列表。
        :type images: list[str]
        :param image_cache_size: **参数解释：** 镜像缓存后端对应的存储盘大小，单位GiB。缓存对象为解压后的镜像文件，建议镜像缓存大小不低于该缓存中所有容器镜像大小总和的3倍。 **约束限制：** 不涉及 **取值范围：** [20-400] **默认取值：** 20 
        :type image_cache_size: int
        :param retention_days: **参数解释：** 镜像缓存有效的天数,不设置或值为0表示永久有效。镜像缓存到达有效期后自动过期并删除。 **约束限制：** 不涉及 **取值范围：** [0-10000] **默认取值：** 0 
        :type retention_days: int
        :param building_config: 
        :type building_config: :class:`huaweicloudsdkcce.v5.ImageCacheBuildingConfig`
        """
        
        

        self._name = None
        self._images = None
        self._image_cache_size = None
        self._retention_days = None
        self._building_config = None
        self.discriminator = None

        self.name = name
        self.images = images
        if image_cache_size is not None:
            self.image_cache_size = image_cache_size
        if retention_days is not None:
            self.retention_days = retention_days
        self.building_config = building_config

    @property
    def name(self):
        r"""Gets the name of this CreateImageCacheRequestBody.

        **参数解释：** 镜像缓存名称。 **约束限制：** 不涉及 **取值范围：** 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-128位，且不能以中划线(-)结尾。镜像缓存名称不可重复。 **默认取值：** 不涉及 

        :return: The name of this CreateImageCacheRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateImageCacheRequestBody.

        **参数解释：** 镜像缓存名称。 **约束限制：** 不涉及 **取值范围：** 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-128位，且不能以中划线(-)结尾。镜像缓存名称不可重复。 **默认取值：** 不涉及 

        :param name: The name of this CreateImageCacheRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def images(self):
        r"""Gets the images of this CreateImageCacheRequestBody.

        镜像缓存中的容器镜像列表。

        :return: The images of this CreateImageCacheRequestBody.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this CreateImageCacheRequestBody.

        镜像缓存中的容器镜像列表。

        :param images: The images of this CreateImageCacheRequestBody.
        :type images: list[str]
        """
        self._images = images

    @property
    def image_cache_size(self):
        r"""Gets the image_cache_size of this CreateImageCacheRequestBody.

        **参数解释：** 镜像缓存后端对应的存储盘大小，单位GiB。缓存对象为解压后的镜像文件，建议镜像缓存大小不低于该缓存中所有容器镜像大小总和的3倍。 **约束限制：** 不涉及 **取值范围：** [20-400] **默认取值：** 20 

        :return: The image_cache_size of this CreateImageCacheRequestBody.
        :rtype: int
        """
        return self._image_cache_size

    @image_cache_size.setter
    def image_cache_size(self, image_cache_size):
        r"""Sets the image_cache_size of this CreateImageCacheRequestBody.

        **参数解释：** 镜像缓存后端对应的存储盘大小，单位GiB。缓存对象为解压后的镜像文件，建议镜像缓存大小不低于该缓存中所有容器镜像大小总和的3倍。 **约束限制：** 不涉及 **取值范围：** [20-400] **默认取值：** 20 

        :param image_cache_size: The image_cache_size of this CreateImageCacheRequestBody.
        :type image_cache_size: int
        """
        self._image_cache_size = image_cache_size

    @property
    def retention_days(self):
        r"""Gets the retention_days of this CreateImageCacheRequestBody.

        **参数解释：** 镜像缓存有效的天数,不设置或值为0表示永久有效。镜像缓存到达有效期后自动过期并删除。 **约束限制：** 不涉及 **取值范围：** [0-10000] **默认取值：** 0 

        :return: The retention_days of this CreateImageCacheRequestBody.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this CreateImageCacheRequestBody.

        **参数解释：** 镜像缓存有效的天数,不设置或值为0表示永久有效。镜像缓存到达有效期后自动过期并删除。 **约束限制：** 不涉及 **取值范围：** [0-10000] **默认取值：** 0 

        :param retention_days: The retention_days of this CreateImageCacheRequestBody.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def building_config(self):
        r"""Gets the building_config of this CreateImageCacheRequestBody.

        :return: The building_config of this CreateImageCacheRequestBody.
        :rtype: :class:`huaweicloudsdkcce.v5.ImageCacheBuildingConfig`
        """
        return self._building_config

    @building_config.setter
    def building_config(self, building_config):
        r"""Sets the building_config of this CreateImageCacheRequestBody.

        :param building_config: The building_config of this CreateImageCacheRequestBody.
        :type building_config: :class:`huaweicloudsdkcce.v5.ImageCacheBuildingConfig`
        """
        self._building_config = building_config

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
        if not isinstance(other, CreateImageCacheRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
