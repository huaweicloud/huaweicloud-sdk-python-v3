# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterImageResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'image_version': 'str',
        'id': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_version': 'image_version',
        'id': 'id'
    }

    def __init__(self, image_name=None, image_version=None, id=None):
        r"""ClusterImageResponseInfo

        The model defined in huaweicloud sdk

        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param id: ID
        :type id: str
        """
        
        

        self._image_name = None
        self._image_version = None
        self._id = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if id is not None:
            self.id = id

    @property
    def image_name(self):
        r"""Gets the image_name of this ClusterImageResponseInfo.

        镜像名称

        :return: The image_name of this ClusterImageResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ClusterImageResponseInfo.

        镜像名称

        :param image_name: The image_name of this ClusterImageResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this ClusterImageResponseInfo.

        镜像版本

        :return: The image_version of this ClusterImageResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this ClusterImageResponseInfo.

        镜像版本

        :param image_version: The image_version of this ClusterImageResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def id(self):
        r"""Gets the id of this ClusterImageResponseInfo.

        ID

        :return: The id of this ClusterImageResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ClusterImageResponseInfo.

        ID

        :param id: The id of this ClusterImageResponseInfo.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ClusterImageResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
