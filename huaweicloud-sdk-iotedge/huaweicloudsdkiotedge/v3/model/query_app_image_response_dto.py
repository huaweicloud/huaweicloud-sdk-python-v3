# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAppImageResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_namespace': 'str',
        'name': 'str',
        'tag': 'str',
        'digest': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'image_namespace': 'image_namespace',
        'name': 'name',
        'tag': 'tag',
        'digest': 'digest',
        'create_time': 'create_time'
    }

    def __init__(self, image_namespace=None, name=None, tag=None, digest=None, create_time=None):
        r"""QueryAppImageResponseDTO

        The model defined in huaweicloud sdk

        :param image_namespace: 镜像组织
        :type image_namespace: str
        :param name: 镜像仓库名称
        :type name: str
        :param tag: 镜像tag
        :type tag: str
        :param digest: 镜像摘要
        :type digest: str
        :param create_time: 创建时间
        :type create_time: str
        """
        
        

        self._image_namespace = None
        self._name = None
        self._tag = None
        self._digest = None
        self._create_time = None
        self.discriminator = None

        if image_namespace is not None:
            self.image_namespace = image_namespace
        if name is not None:
            self.name = name
        if tag is not None:
            self.tag = tag
        if digest is not None:
            self.digest = digest
        if create_time is not None:
            self.create_time = create_time

    @property
    def image_namespace(self):
        r"""Gets the image_namespace of this QueryAppImageResponseDTO.

        镜像组织

        :return: The image_namespace of this QueryAppImageResponseDTO.
        :rtype: str
        """
        return self._image_namespace

    @image_namespace.setter
    def image_namespace(self, image_namespace):
        r"""Sets the image_namespace of this QueryAppImageResponseDTO.

        镜像组织

        :param image_namespace: The image_namespace of this QueryAppImageResponseDTO.
        :type image_namespace: str
        """
        self._image_namespace = image_namespace

    @property
    def name(self):
        r"""Gets the name of this QueryAppImageResponseDTO.

        镜像仓库名称

        :return: The name of this QueryAppImageResponseDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryAppImageResponseDTO.

        镜像仓库名称

        :param name: The name of this QueryAppImageResponseDTO.
        :type name: str
        """
        self._name = name

    @property
    def tag(self):
        r"""Gets the tag of this QueryAppImageResponseDTO.

        镜像tag

        :return: The tag of this QueryAppImageResponseDTO.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this QueryAppImageResponseDTO.

        镜像tag

        :param tag: The tag of this QueryAppImageResponseDTO.
        :type tag: str
        """
        self._tag = tag

    @property
    def digest(self):
        r"""Gets the digest of this QueryAppImageResponseDTO.

        镜像摘要

        :return: The digest of this QueryAppImageResponseDTO.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this QueryAppImageResponseDTO.

        镜像摘要

        :param digest: The digest of this QueryAppImageResponseDTO.
        :type digest: str
        """
        self._digest = digest

    @property
    def create_time(self):
        r"""Gets the create_time of this QueryAppImageResponseDTO.

        创建时间

        :return: The create_time of this QueryAppImageResponseDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QueryAppImageResponseDTO.

        创建时间

        :param create_time: The create_time of this QueryAppImageResponseDTO.
        :type create_time: str
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
        if not isinstance(other, QueryAppImageResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
