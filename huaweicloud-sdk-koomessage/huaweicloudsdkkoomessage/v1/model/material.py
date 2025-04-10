# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Material:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'created_at': 'str',
        'resource_type': 'str',
        'file_name': 'str',
        'aim_resource_id': 'str',
        'obs_object_key': 'str',
        'obs_file_url': 'str',
        'image_rate': 'str',
        'description': 'str',
        'thumbnail': 'Thumbnail'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'resource_type': 'resource_type',
        'file_name': 'file_name',
        'aim_resource_id': 'aim_resource_id',
        'obs_object_key': 'obs_object_key',
        'obs_file_url': 'obs_file_url',
        'image_rate': 'image_rate',
        'description': 'description',
        'thumbnail': 'thumbnail'
    }

    def __init__(self, id=None, created_at=None, resource_type=None, file_name=None, aim_resource_id=None, obs_object_key=None, obs_file_url=None, image_rate=None, description=None, thumbnail=None):
        r"""Material

        The model defined in huaweicloud sdk

        :param id: 素材ID。
        :type id: str
        :param created_at: 创建时间。
        :type created_at: str
        :param resource_type: 资源类型。 - image：表示图片 - video：表示视频 - thumbnail：表示缩略图 
        :type resource_type: str
        :param file_name: 文件名称。
        :type file_name: str
        :param aim_resource_id: 资源ID。
        :type aim_resource_id: str
        :param obs_object_key: 从OBS返回的文件Key。
        :type obs_object_key: str
        :param obs_file_url: 文件访问路径。
        :type obs_file_url: str
        :param image_rate: 图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 
        :type image_rate: str
        :param description: 素材详细描述。
        :type description: str
        :param thumbnail: 
        :type thumbnail: :class:`huaweicloudsdkkoomessage.v1.Thumbnail`
        """
        
        

        self._id = None
        self._created_at = None
        self._resource_type = None
        self._file_name = None
        self._aim_resource_id = None
        self._obs_object_key = None
        self._obs_file_url = None
        self._image_rate = None
        self._description = None
        self._thumbnail = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        self.resource_type = resource_type
        self.file_name = file_name
        self.aim_resource_id = aim_resource_id
        self.obs_object_key = obs_object_key
        if obs_file_url is not None:
            self.obs_file_url = obs_file_url
        if image_rate is not None:
            self.image_rate = image_rate
        if description is not None:
            self.description = description
        if thumbnail is not None:
            self.thumbnail = thumbnail

    @property
    def id(self):
        r"""Gets the id of this Material.

        素材ID。

        :return: The id of this Material.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Material.

        素材ID。

        :param id: The id of this Material.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this Material.

        创建时间。

        :return: The created_at of this Material.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Material.

        创建时间。

        :param created_at: The created_at of this Material.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def resource_type(self):
        r"""Gets the resource_type of this Material.

        资源类型。 - image：表示图片 - video：表示视频 - thumbnail：表示缩略图 

        :return: The resource_type of this Material.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this Material.

        资源类型。 - image：表示图片 - video：表示视频 - thumbnail：表示缩略图 

        :param resource_type: The resource_type of this Material.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def file_name(self):
        r"""Gets the file_name of this Material.

        文件名称。

        :return: The file_name of this Material.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this Material.

        文件名称。

        :param file_name: The file_name of this Material.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def aim_resource_id(self):
        r"""Gets the aim_resource_id of this Material.

        资源ID。

        :return: The aim_resource_id of this Material.
        :rtype: str
        """
        return self._aim_resource_id

    @aim_resource_id.setter
    def aim_resource_id(self, aim_resource_id):
        r"""Sets the aim_resource_id of this Material.

        资源ID。

        :param aim_resource_id: The aim_resource_id of this Material.
        :type aim_resource_id: str
        """
        self._aim_resource_id = aim_resource_id

    @property
    def obs_object_key(self):
        r"""Gets the obs_object_key of this Material.

        从OBS返回的文件Key。

        :return: The obs_object_key of this Material.
        :rtype: str
        """
        return self._obs_object_key

    @obs_object_key.setter
    def obs_object_key(self, obs_object_key):
        r"""Sets the obs_object_key of this Material.

        从OBS返回的文件Key。

        :param obs_object_key: The obs_object_key of this Material.
        :type obs_object_key: str
        """
        self._obs_object_key = obs_object_key

    @property
    def obs_file_url(self):
        r"""Gets the obs_file_url of this Material.

        文件访问路径。

        :return: The obs_file_url of this Material.
        :rtype: str
        """
        return self._obs_file_url

    @obs_file_url.setter
    def obs_file_url(self, obs_file_url):
        r"""Sets the obs_file_url of this Material.

        文件访问路径。

        :param obs_file_url: The obs_file_url of this Material.
        :type obs_file_url: str
        """
        self._obs_file_url = obs_file_url

    @property
    def image_rate(self):
        r"""Gets the image_rate of this Material.

        图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 

        :return: The image_rate of this Material.
        :rtype: str
        """
        return self._image_rate

    @image_rate.setter
    def image_rate(self, image_rate):
        r"""Sets the image_rate of this Material.

        图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 

        :param image_rate: The image_rate of this Material.
        :type image_rate: str
        """
        self._image_rate = image_rate

    @property
    def description(self):
        r"""Gets the description of this Material.

        素材详细描述。

        :return: The description of this Material.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Material.

        素材详细描述。

        :param description: The description of this Material.
        :type description: str
        """
        self._description = description

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this Material.

        :return: The thumbnail of this Material.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Thumbnail`
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this Material.

        :param thumbnail: The thumbnail of this Material.
        :type thumbnail: :class:`huaweicloudsdkkoomessage.v1.Thumbnail`
        """
        self._thumbnail = thumbnail

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
        if not isinstance(other, Material):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
