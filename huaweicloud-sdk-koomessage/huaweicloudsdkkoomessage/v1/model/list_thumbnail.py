# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListThumbnail:

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
        'is_primary': 'int',
        'file_name': 'str',
        'aim_resource_id': 'str',
        'obs_object_key': 'str',
        'image_rate': 'str',
        'is_auto_gen': 'int',
        'description': 'str',
        'obs_bucket_name': 'str',
        'domain_id': 'str',
        'size': 'int',
        'obs_file_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'is_primary': 'is_primary',
        'file_name': 'file_name',
        'aim_resource_id': 'aim_resource_id',
        'obs_object_key': 'obs_object_key',
        'image_rate': 'image_rate',
        'is_auto_gen': 'is_auto_gen',
        'description': 'description',
        'obs_bucket_name': 'obs_bucket_name',
        'domain_id': 'domain_id',
        'size': 'size',
        'obs_file_url': 'obs_file_url'
    }

    def __init__(self, id=None, created_at=None, is_primary=None, file_name=None, aim_resource_id=None, obs_object_key=None, image_rate=None, is_auto_gen=None, description=None, obs_bucket_name=None, domain_id=None, size=None, obs_file_url=None):
        r"""ListThumbnail

        The model defined in huaweicloud sdk

        :param id: 视频封面图ID。
        :type id: str
        :param created_at: 创建时间。
        :type created_at: str
        :param is_primary: 是否作为视频素材封面。 - 0：否 - 1：是 
        :type is_primary: int
        :param file_name: 文件名称。
        :type file_name: str
        :param aim_resource_id: 资源ID。
        :type aim_resource_id: str
        :param obs_object_key: 从OBS返回的文件Key。
        :type obs_object_key: str
        :param image_rate: 图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 - threeToFour：指3:4比例 
        :type image_rate: str
        :param is_auto_gen: 视频封面图是否自动从系统生成。 - 0：系统自动生成 - 1：上传自定义 
        :type is_auto_gen: int
        :param description: 视频封面图的详细描述。
        :type description: str
        :param obs_bucket_name: OBS桶名称。
        :type obs_bucket_name: str
        :param domain_id: 租户ID。
        :type domain_id: str
        :param size: 素材所占空间大小。
        :type size: int
        :param obs_file_url: 文件访问路径。
        :type obs_file_url: str
        """
        
        

        self._id = None
        self._created_at = None
        self._is_primary = None
        self._file_name = None
        self._aim_resource_id = None
        self._obs_object_key = None
        self._image_rate = None
        self._is_auto_gen = None
        self._description = None
        self._obs_bucket_name = None
        self._domain_id = None
        self._size = None
        self._obs_file_url = None
        self.discriminator = None

        self.id = id
        self.created_at = created_at
        self.is_primary = is_primary
        self.file_name = file_name
        self.aim_resource_id = aim_resource_id
        self.obs_object_key = obs_object_key
        if image_rate is not None:
            self.image_rate = image_rate
        if is_auto_gen is not None:
            self.is_auto_gen = is_auto_gen
        if description is not None:
            self.description = description
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if domain_id is not None:
            self.domain_id = domain_id
        if size is not None:
            self.size = size
        if obs_file_url is not None:
            self.obs_file_url = obs_file_url

    @property
    def id(self):
        r"""Gets the id of this ListThumbnail.

        视频封面图ID。

        :return: The id of this ListThumbnail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListThumbnail.

        视频封面图ID。

        :param id: The id of this ListThumbnail.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ListThumbnail.

        创建时间。

        :return: The created_at of this ListThumbnail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ListThumbnail.

        创建时间。

        :param created_at: The created_at of this ListThumbnail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def is_primary(self):
        r"""Gets the is_primary of this ListThumbnail.

        是否作为视频素材封面。 - 0：否 - 1：是 

        :return: The is_primary of this ListThumbnail.
        :rtype: int
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        r"""Sets the is_primary of this ListThumbnail.

        是否作为视频素材封面。 - 0：否 - 1：是 

        :param is_primary: The is_primary of this ListThumbnail.
        :type is_primary: int
        """
        self._is_primary = is_primary

    @property
    def file_name(self):
        r"""Gets the file_name of this ListThumbnail.

        文件名称。

        :return: The file_name of this ListThumbnail.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListThumbnail.

        文件名称。

        :param file_name: The file_name of this ListThumbnail.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def aim_resource_id(self):
        r"""Gets the aim_resource_id of this ListThumbnail.

        资源ID。

        :return: The aim_resource_id of this ListThumbnail.
        :rtype: str
        """
        return self._aim_resource_id

    @aim_resource_id.setter
    def aim_resource_id(self, aim_resource_id):
        r"""Sets the aim_resource_id of this ListThumbnail.

        资源ID。

        :param aim_resource_id: The aim_resource_id of this ListThumbnail.
        :type aim_resource_id: str
        """
        self._aim_resource_id = aim_resource_id

    @property
    def obs_object_key(self):
        r"""Gets the obs_object_key of this ListThumbnail.

        从OBS返回的文件Key。

        :return: The obs_object_key of this ListThumbnail.
        :rtype: str
        """
        return self._obs_object_key

    @obs_object_key.setter
    def obs_object_key(self, obs_object_key):
        r"""Sets the obs_object_key of this ListThumbnail.

        从OBS返回的文件Key。

        :param obs_object_key: The obs_object_key of this ListThumbnail.
        :type obs_object_key: str
        """
        self._obs_object_key = obs_object_key

    @property
    def image_rate(self):
        r"""Gets the image_rate of this ListThumbnail.

        图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 - threeToFour：指3:4比例 

        :return: The image_rate of this ListThumbnail.
        :rtype: str
        """
        return self._image_rate

    @image_rate.setter
    def image_rate(self, image_rate):
        r"""Sets the image_rate of this ListThumbnail.

        图像比例。 - oneToOne：指1:1比例 - sixteenToNine：指16:9比例 - threeToOne：指3:1比例 - fortyEightToSixtyFive：指48:65比例 - twentyOneToNine：指21:9比例 - threeToFour：指3:4比例 

        :param image_rate: The image_rate of this ListThumbnail.
        :type image_rate: str
        """
        self._image_rate = image_rate

    @property
    def is_auto_gen(self):
        r"""Gets the is_auto_gen of this ListThumbnail.

        视频封面图是否自动从系统生成。 - 0：系统自动生成 - 1：上传自定义 

        :return: The is_auto_gen of this ListThumbnail.
        :rtype: int
        """
        return self._is_auto_gen

    @is_auto_gen.setter
    def is_auto_gen(self, is_auto_gen):
        r"""Sets the is_auto_gen of this ListThumbnail.

        视频封面图是否自动从系统生成。 - 0：系统自动生成 - 1：上传自定义 

        :param is_auto_gen: The is_auto_gen of this ListThumbnail.
        :type is_auto_gen: int
        """
        self._is_auto_gen = is_auto_gen

    @property
    def description(self):
        r"""Gets the description of this ListThumbnail.

        视频封面图的详细描述。

        :return: The description of this ListThumbnail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListThumbnail.

        视频封面图的详细描述。

        :param description: The description of this ListThumbnail.
        :type description: str
        """
        self._description = description

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this ListThumbnail.

        OBS桶名称。

        :return: The obs_bucket_name of this ListThumbnail.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this ListThumbnail.

        OBS桶名称。

        :param obs_bucket_name: The obs_bucket_name of this ListThumbnail.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListThumbnail.

        租户ID。

        :return: The domain_id of this ListThumbnail.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListThumbnail.

        租户ID。

        :param domain_id: The domain_id of this ListThumbnail.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def size(self):
        r"""Gets the size of this ListThumbnail.

        素材所占空间大小。

        :return: The size of this ListThumbnail.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListThumbnail.

        素材所占空间大小。

        :param size: The size of this ListThumbnail.
        :type size: int
        """
        self._size = size

    @property
    def obs_file_url(self):
        r"""Gets the obs_file_url of this ListThumbnail.

        文件访问路径。

        :return: The obs_file_url of this ListThumbnail.
        :rtype: str
        """
        return self._obs_file_url

    @obs_file_url.setter
    def obs_file_url(self, obs_file_url):
        r"""Sets the obs_file_url of this ListThumbnail.

        文件访问路径。

        :param obs_file_url: The obs_file_url of this ListThumbnail.
        :type obs_file_url: str
        """
        self._obs_file_url = obs_file_url

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
        if not isinstance(other, ListThumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
