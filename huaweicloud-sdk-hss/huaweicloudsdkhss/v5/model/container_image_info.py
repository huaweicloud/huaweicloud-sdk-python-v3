# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'create_time': 'create_time'
    }

    def __init__(self, image_id=None, image_name=None, image_version=None, create_time=None):
        r"""ContainerImageInfo

        The model defined in huaweicloud sdk

        :param image_id: 镜像唯一标识(虚拟)
        :type image_id: str
        :param image_name: 镜像名
        :type image_name: str
        :param image_version: 镜像版本号
        :type image_version: str
        :param create_time: 镜像创建时间(本地保存时间)
        :type create_time: int
        """
        
        

        self._image_id = None
        self._image_name = None
        self._image_version = None
        self._create_time = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if create_time is not None:
            self.create_time = create_time

    @property
    def image_id(self):
        r"""Gets the image_id of this ContainerImageInfo.

        镜像唯一标识(虚拟)

        :return: The image_id of this ContainerImageInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ContainerImageInfo.

        镜像唯一标识(虚拟)

        :param image_id: The image_id of this ContainerImageInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this ContainerImageInfo.

        镜像名

        :return: The image_name of this ContainerImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ContainerImageInfo.

        镜像名

        :param image_name: The image_name of this ContainerImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ContainerImageInfo.

        镜像版本号

        :return: The image_version of this ContainerImageInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ContainerImageInfo.

        镜像版本号

        :param image_version: The image_version of this ContainerImageInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def create_time(self):
        r"""Gets the create_time of this ContainerImageInfo.

        镜像创建时间(本地保存时间)

        :return: The create_time of this ContainerImageInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ContainerImageInfo.

        镜像创建时间(本地保存时间)

        :param create_time: The create_time of this ContainerImageInfo.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ContainerImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
