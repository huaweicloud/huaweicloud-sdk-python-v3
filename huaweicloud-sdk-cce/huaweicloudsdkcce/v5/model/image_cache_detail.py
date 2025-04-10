# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageCacheDetail:

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
        'id': 'str',
        'created_at': 'str',
        'images': 'list[str]',
        'image_cache_size': 'int',
        'retention_days': 'int',
        'building_config': 'ImageCacheBuildingConfig',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'created_at': 'created_at',
        'images': 'images',
        'image_cache_size': 'image_cache_size',
        'retention_days': 'retention_days',
        'building_config': 'building_config',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, name=None, id=None, created_at=None, images=None, image_cache_size=None, retention_days=None, building_config=None, status=None, message=None):
        r"""ImageCacheDetail

        The model defined in huaweicloud sdk

        :param name: 镜像缓存名称。
        :type name: str
        :param id: 镜像缓存ID。
        :type id: str
        :param created_at: 镜像缓存创建时间戳。
        :type created_at: str
        :param images: 镜像缓存中的容器镜像列表。
        :type images: list[str]
        :param image_cache_size: 镜像缓存后端对应的存储盘大小，单位GiB。
        :type image_cache_size: int
        :param retention_days: **参数解释：** 镜像缓存有效的天数,不设置或值为0表示永久有效。镜像缓存到达有效期后自动过期并删除。 **约束限制：** 不涉及 **取值范围：** [0-10000] **默认取值：** 0 
        :type retention_days: int
        :param building_config: 
        :type building_config: :class:`huaweicloudsdkcce.v5.ImageCacheBuildingConfig`
        :param status: **参数解释：** 镜像缓存的状态。 **约束限制：** 不涉及 **取值范围：** - Available： 可用状态，表示当前镜像缓存正常可用。 - Unavailable：不可用，表示镜像缓存状态异常或过期，不可使用。 - Creating：创建中，表示镜像缓存正在创建中。 - Deleting：删除中，表示镜像缓存正在删除中。 - Failed：创建失败，表示镜像缓存创建失败。 **默认取值：** 不涉及
        :type status: str
        :param message: 镜像缓存创建失败或异常的错误信息。
        :type message: str
        """
        
        

        self._name = None
        self._id = None
        self._created_at = None
        self._images = None
        self._image_cache_size = None
        self._retention_days = None
        self._building_config = None
        self._status = None
        self._message = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.created_at = created_at
        self.images = images
        self.image_cache_size = image_cache_size
        self.retention_days = retention_days
        self.building_config = building_config
        self.status = status
        if message is not None:
            self.message = message

    @property
    def name(self):
        r"""Gets the name of this ImageCacheDetail.

        镜像缓存名称。

        :return: The name of this ImageCacheDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageCacheDetail.

        镜像缓存名称。

        :param name: The name of this ImageCacheDetail.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ImageCacheDetail.

        镜像缓存ID。

        :return: The id of this ImageCacheDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImageCacheDetail.

        镜像缓存ID。

        :param id: The id of this ImageCacheDetail.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ImageCacheDetail.

        镜像缓存创建时间戳。

        :return: The created_at of this ImageCacheDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ImageCacheDetail.

        镜像缓存创建时间戳。

        :param created_at: The created_at of this ImageCacheDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def images(self):
        r"""Gets the images of this ImageCacheDetail.

        镜像缓存中的容器镜像列表。

        :return: The images of this ImageCacheDetail.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this ImageCacheDetail.

        镜像缓存中的容器镜像列表。

        :param images: The images of this ImageCacheDetail.
        :type images: list[str]
        """
        self._images = images

    @property
    def image_cache_size(self):
        r"""Gets the image_cache_size of this ImageCacheDetail.

        镜像缓存后端对应的存储盘大小，单位GiB。

        :return: The image_cache_size of this ImageCacheDetail.
        :rtype: int
        """
        return self._image_cache_size

    @image_cache_size.setter
    def image_cache_size(self, image_cache_size):
        r"""Sets the image_cache_size of this ImageCacheDetail.

        镜像缓存后端对应的存储盘大小，单位GiB。

        :param image_cache_size: The image_cache_size of this ImageCacheDetail.
        :type image_cache_size: int
        """
        self._image_cache_size = image_cache_size

    @property
    def retention_days(self):
        r"""Gets the retention_days of this ImageCacheDetail.

        **参数解释：** 镜像缓存有效的天数,不设置或值为0表示永久有效。镜像缓存到达有效期后自动过期并删除。 **约束限制：** 不涉及 **取值范围：** [0-10000] **默认取值：** 0 

        :return: The retention_days of this ImageCacheDetail.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this ImageCacheDetail.

        **参数解释：** 镜像缓存有效的天数,不设置或值为0表示永久有效。镜像缓存到达有效期后自动过期并删除。 **约束限制：** 不涉及 **取值范围：** [0-10000] **默认取值：** 0 

        :param retention_days: The retention_days of this ImageCacheDetail.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def building_config(self):
        r"""Gets the building_config of this ImageCacheDetail.

        :return: The building_config of this ImageCacheDetail.
        :rtype: :class:`huaweicloudsdkcce.v5.ImageCacheBuildingConfig`
        """
        return self._building_config

    @building_config.setter
    def building_config(self, building_config):
        r"""Sets the building_config of this ImageCacheDetail.

        :param building_config: The building_config of this ImageCacheDetail.
        :type building_config: :class:`huaweicloudsdkcce.v5.ImageCacheBuildingConfig`
        """
        self._building_config = building_config

    @property
    def status(self):
        r"""Gets the status of this ImageCacheDetail.

        **参数解释：** 镜像缓存的状态。 **约束限制：** 不涉及 **取值范围：** - Available： 可用状态，表示当前镜像缓存正常可用。 - Unavailable：不可用，表示镜像缓存状态异常或过期，不可使用。 - Creating：创建中，表示镜像缓存正在创建中。 - Deleting：删除中，表示镜像缓存正在删除中。 - Failed：创建失败，表示镜像缓存创建失败。 **默认取值：** 不涉及

        :return: The status of this ImageCacheDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ImageCacheDetail.

        **参数解释：** 镜像缓存的状态。 **约束限制：** 不涉及 **取值范围：** - Available： 可用状态，表示当前镜像缓存正常可用。 - Unavailable：不可用，表示镜像缓存状态异常或过期，不可使用。 - Creating：创建中，表示镜像缓存正在创建中。 - Deleting：删除中，表示镜像缓存正在删除中。 - Failed：创建失败，表示镜像缓存创建失败。 **默认取值：** 不涉及

        :param status: The status of this ImageCacheDetail.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ImageCacheDetail.

        镜像缓存创建失败或异常的错误信息。

        :return: The message of this ImageCacheDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ImageCacheDetail.

        镜像缓存创建失败或异常的错误信息。

        :param message: The message of this ImageCacheDetail.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ImageCacheDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
