# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LocalImageInfo:

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
        'image_digest': 'str',
        'image_name': 'str',
        'image_version': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'image_digest': 'image_digest',
        'image_name': 'image_name',
        'image_version': 'image_version'
    }

    def __init__(self, image_id=None, image_digest=None, image_name=None, image_version=None):
        r"""LocalImageInfo

        The model defined in huaweicloud sdk

        :param image_id: 镜像id
        :type image_id: str
        :param image_digest: 镜像摘要
        :type image_digest: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        """
        
        

        self._image_id = None
        self._image_digest = None
        self._image_name = None
        self._image_version = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if image_digest is not None:
            self.image_digest = image_digest
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version

    @property
    def image_id(self):
        r"""Gets the image_id of this LocalImageInfo.

        镜像id

        :return: The image_id of this LocalImageInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this LocalImageInfo.

        镜像id

        :param image_id: The image_id of this LocalImageInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_digest(self):
        r"""Gets the image_digest of this LocalImageInfo.

        镜像摘要

        :return: The image_digest of this LocalImageInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        r"""Sets the image_digest of this LocalImageInfo.

        镜像摘要

        :param image_digest: The image_digest of this LocalImageInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_name(self):
        r"""Gets the image_name of this LocalImageInfo.

        镜像名称

        :return: The image_name of this LocalImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this LocalImageInfo.

        镜像名称

        :param image_name: The image_name of this LocalImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this LocalImageInfo.

        镜像版本

        :return: The image_version of this LocalImageInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this LocalImageInfo.

        镜像版本

        :param image_version: The image_version of this LocalImageInfo.
        :type image_version: str
        """
        self._image_version = image_version

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LocalImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
