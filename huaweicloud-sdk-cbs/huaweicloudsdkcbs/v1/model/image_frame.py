# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageFrame:

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
        'frame_resolution_type': 'int',
        'id': 'str',
        'image_frame_position': 'LeftRightPosition',
        'image_position': 'LeftRightPosition',
        'resolution_type': 'int',
        'url': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'update_time': 'update_time',
        'frame_resolution_type': 'frame_resolution_type',
        'id': 'id',
        'image_frame_position': 'image_frame_position',
        'image_position': 'image_position',
        'resolution_type': 'resolution_type',
        'url': 'url'
    }

    def __init__(self, create_time=None, update_time=None, frame_resolution_type=None, id=None, image_frame_position=None, image_position=None, resolution_type=None, url=None):
        """ImageFrame

        The model defined in huaweicloud sdk

        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param frame_resolution_type: 0: 16/9 1: 4/3 2: 3/4
        :type frame_resolution_type: int
        :param id: 
        :type id: str
        :param image_frame_position: 
        :type image_frame_position: :class:`huaweicloudsdkcbs.v1.LeftRightPosition`
        :param image_position: 
        :type image_position: :class:`huaweicloudsdkcbs.v1.LeftRightPosition`
        :param resolution_type: 横版：0 竖版：1
        :type resolution_type: int
        :param url: 
        :type url: str
        """
        
        

        self._create_time = None
        self._update_time = None
        self._frame_resolution_type = None
        self._id = None
        self._image_frame_position = None
        self._image_position = None
        self._resolution_type = None
        self._url = None
        self.discriminator = None

        self.create_time = create_time
        self.update_time = update_time
        self.frame_resolution_type = frame_resolution_type
        self.id = id
        self.image_frame_position = image_frame_position
        self.image_position = image_position
        self.resolution_type = resolution_type
        self.url = url

    @property
    def create_time(self):
        """Gets the create_time of this ImageFrame.

        创建时间

        :return: The create_time of this ImageFrame.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ImageFrame.

        创建时间

        :param create_time: The create_time of this ImageFrame.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ImageFrame.

        更新时间

        :return: The update_time of this ImageFrame.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ImageFrame.

        更新时间

        :param update_time: The update_time of this ImageFrame.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def frame_resolution_type(self):
        """Gets the frame_resolution_type of this ImageFrame.

        0: 16/9 1: 4/3 2: 3/4

        :return: The frame_resolution_type of this ImageFrame.
        :rtype: int
        """
        return self._frame_resolution_type

    @frame_resolution_type.setter
    def frame_resolution_type(self, frame_resolution_type):
        """Sets the frame_resolution_type of this ImageFrame.

        0: 16/9 1: 4/3 2: 3/4

        :param frame_resolution_type: The frame_resolution_type of this ImageFrame.
        :type frame_resolution_type: int
        """
        self._frame_resolution_type = frame_resolution_type

    @property
    def id(self):
        """Gets the id of this ImageFrame.

        

        :return: The id of this ImageFrame.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageFrame.

        

        :param id: The id of this ImageFrame.
        :type id: str
        """
        self._id = id

    @property
    def image_frame_position(self):
        """Gets the image_frame_position of this ImageFrame.

        :return: The image_frame_position of this ImageFrame.
        :rtype: :class:`huaweicloudsdkcbs.v1.LeftRightPosition`
        """
        return self._image_frame_position

    @image_frame_position.setter
    def image_frame_position(self, image_frame_position):
        """Sets the image_frame_position of this ImageFrame.

        :param image_frame_position: The image_frame_position of this ImageFrame.
        :type image_frame_position: :class:`huaweicloudsdkcbs.v1.LeftRightPosition`
        """
        self._image_frame_position = image_frame_position

    @property
    def image_position(self):
        """Gets the image_position of this ImageFrame.

        :return: The image_position of this ImageFrame.
        :rtype: :class:`huaweicloudsdkcbs.v1.LeftRightPosition`
        """
        return self._image_position

    @image_position.setter
    def image_position(self, image_position):
        """Sets the image_position of this ImageFrame.

        :param image_position: The image_position of this ImageFrame.
        :type image_position: :class:`huaweicloudsdkcbs.v1.LeftRightPosition`
        """
        self._image_position = image_position

    @property
    def resolution_type(self):
        """Gets the resolution_type of this ImageFrame.

        横版：0 竖版：1

        :return: The resolution_type of this ImageFrame.
        :rtype: int
        """
        return self._resolution_type

    @resolution_type.setter
    def resolution_type(self, resolution_type):
        """Sets the resolution_type of this ImageFrame.

        横版：0 竖版：1

        :param resolution_type: The resolution_type of this ImageFrame.
        :type resolution_type: int
        """
        self._resolution_type = resolution_type

    @property
    def url(self):
        """Gets the url of this ImageFrame.

        

        :return: The url of this ImageFrame.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageFrame.

        

        :param url: The url of this ImageFrame.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ImageFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
