# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchConfigImageInfoSrlz:

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
        'name': 'str',
        'image_id': 'int',
        'image_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'image_id': 'image_id',
        'image_version': 'image_version'
    }

    def __init__(self, id=None, name=None, image_id=None, image_version=None):
        r"""BatchConfigImageInfoSrlz

        The model defined in huaweicloud sdk

        :param id: 项目id
        :type id: int
        :param name: 项目名称
        :type name: str
        :param image_id: 镜像id
        :type image_id: int
        :param image_version: 镜像版本
        :type image_version: str
        """
        
        

        self._id = None
        self._name = None
        self._image_id = None
        self._image_version = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.image_id = image_id
        self.image_version = image_version

    @property
    def id(self):
        r"""Gets the id of this BatchConfigImageInfoSrlz.

        项目id

        :return: The id of this BatchConfigImageInfoSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchConfigImageInfoSrlz.

        项目id

        :param id: The id of this BatchConfigImageInfoSrlz.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BatchConfigImageInfoSrlz.

        项目名称

        :return: The name of this BatchConfigImageInfoSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchConfigImageInfoSrlz.

        项目名称

        :param name: The name of this BatchConfigImageInfoSrlz.
        :type name: str
        """
        self._name = name

    @property
    def image_id(self):
        r"""Gets the image_id of this BatchConfigImageInfoSrlz.

        镜像id

        :return: The image_id of this BatchConfigImageInfoSrlz.
        :rtype: int
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this BatchConfigImageInfoSrlz.

        镜像id

        :param image_id: The image_id of this BatchConfigImageInfoSrlz.
        :type image_id: int
        """
        self._image_id = image_id

    @property
    def image_version(self):
        r"""Gets the image_version of this BatchConfigImageInfoSrlz.

        镜像版本

        :return: The image_version of this BatchConfigImageInfoSrlz.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this BatchConfigImageInfoSrlz.

        镜像版本

        :param image_version: The image_version of this BatchConfigImageInfoSrlz.
        :type image_version: str
        """
        self._image_version = image_version

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
        if not isinstance(other, BatchConfigImageInfoSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
