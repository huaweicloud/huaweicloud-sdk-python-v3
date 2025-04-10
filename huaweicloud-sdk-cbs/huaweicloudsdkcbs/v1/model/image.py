# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Image:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'update_time': 'str',
        'id': 'str',
        'image_frame': 'ImageFrame',
        'image_url': 'str',
        'name': 'str',
        'type': 'int',
        'resolution_type': 'int'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'id': 'id',
        'image_frame': 'image_frame',
        'image_url': 'image_url',
        'name': 'name',
        'type': 'type',
        'resolution_type': 'resolution_type'
    }

    def __init__(self, create_time=None, update_time=None, id=None, image_frame=None, image_url=None, name=None, type=None, resolution_type=None):
        r"""Image

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param id: 
        :type id: str
        :param image_frame: 
        :type image_frame: :class:`huaweicloudsdkcbs.v1.ImageFrame`
        :param image_url: 图片的obs路径
        :type image_url: str
        :param name: 
        :type name: str
        :param type: 0：背景图 1：图标 2：系统背景
        :type type: int
        :param resolution_type: 横竖屏模式。0：横版1：竖版
        :type resolution_type: int
        """
        
        

        self._create_time = None
        self._update_time = None
        self._id = None
        self._image_frame = None
        self._image_url = None
        self._name = None
        self._type = None
        self._resolution_type = None
        self.discriminator = None

        self.create_time = create_time
        self.update_time = update_time
        self.id = id
        if image_frame is not None:
            self.image_frame = image_frame
        self.image_url = image_url
        self.name = name
        self.type = type
        if resolution_type is not None:
            self.resolution_type = resolution_type

    @property
    def create_time(self):
        r"""Gets the create_time of this Image.

        创建时间

        :return: The create_time of this Image.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Image.

        创建时间

        :param create_time: The create_time of this Image.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Image.

        更新时间

        :return: The update_time of this Image.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Image.

        更新时间

        :param update_time: The update_time of this Image.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this Image.

        :return: The id of this Image.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Image.

        :param id: The id of this Image.
        :type id: str
        """
        self._id = id

    @property
    def image_frame(self):
        r"""Gets the image_frame of this Image.

        :return: The image_frame of this Image.
        :rtype: :class:`huaweicloudsdkcbs.v1.ImageFrame`
        """
        return self._image_frame

    @image_frame.setter
    def image_frame(self, image_frame):
        r"""Sets the image_frame of this Image.

        :param image_frame: The image_frame of this Image.
        :type image_frame: :class:`huaweicloudsdkcbs.v1.ImageFrame`
        """
        self._image_frame = image_frame

    @property
    def image_url(self):
        r"""Gets the image_url of this Image.

        图片的obs路径

        :return: The image_url of this Image.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        r"""Sets the image_url of this Image.

        图片的obs路径

        :param image_url: The image_url of this Image.
        :type image_url: str
        """
        self._image_url = image_url

    @property
    def name(self):
        r"""Gets the name of this Image.

        :return: The name of this Image.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Image.

        :param name: The name of this Image.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this Image.

        0：背景图 1：图标 2：系统背景

        :return: The type of this Image.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Image.

        0：背景图 1：图标 2：系统背景

        :param type: The type of this Image.
        :type type: int
        """
        self._type = type

    @property
    def resolution_type(self):
        r"""Gets the resolution_type of this Image.

        横竖屏模式。0：横版1：竖版

        :return: The resolution_type of this Image.
        :rtype: int
        """
        return self._resolution_type

    @resolution_type.setter
    def resolution_type(self, resolution_type):
        r"""Sets the resolution_type of this Image.

        横竖屏模式。0：横版1：竖版

        :param resolution_type: The resolution_type of this Image.
        :type resolution_type: int
        """
        self._resolution_type = resolution_type

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
        if not isinstance(other, Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
