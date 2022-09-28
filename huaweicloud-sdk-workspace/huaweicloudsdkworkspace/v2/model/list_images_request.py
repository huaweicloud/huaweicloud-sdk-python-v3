# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'os_type': 'str',
        'image_type': 'str',
        'platform': 'str',
        'architecture': 'str'
    }

    attribute_map = {
        'os_type': 'os_type',
        'image_type': 'image_type',
        'platform': 'platform',
        'architecture': 'architecture'
    }

    def __init__(self, os_type=None, image_type=None, platform=None, architecture=None):
        """ListImagesRequest

        The model defined in huaweicloud sdk

        :param os_type: 产品镜像的操作系统类型，如Windows。
        :type os_type: str
        :param image_type: 镜像类型。 -gold  公共镜像 -private  私有镜像
        :type image_type: str
        :param platform: 镜像系统类型,如Windows。
        :type platform: str
        :param architecture: 镜像架构：x86。
        :type architecture: str
        """
        
        

        self._os_type = None
        self._image_type = None
        self._platform = None
        self._architecture = None
        self.discriminator = None

        if os_type is not None:
            self.os_type = os_type
        if image_type is not None:
            self.image_type = image_type
        if platform is not None:
            self.platform = platform
        if architecture is not None:
            self.architecture = architecture

    @property
    def os_type(self):
        """Gets the os_type of this ListImagesRequest.

        产品镜像的操作系统类型，如Windows。

        :return: The os_type of this ListImagesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ListImagesRequest.

        产品镜像的操作系统类型，如Windows。

        :param os_type: The os_type of this ListImagesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def image_type(self):
        """Gets the image_type of this ListImagesRequest.

        镜像类型。 -gold  公共镜像 -private  私有镜像

        :return: The image_type of this ListImagesRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ListImagesRequest.

        镜像类型。 -gold  公共镜像 -private  私有镜像

        :param image_type: The image_type of this ListImagesRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def platform(self):
        """Gets the platform of this ListImagesRequest.

        镜像系统类型,如Windows。

        :return: The platform of this ListImagesRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ListImagesRequest.

        镜像系统类型,如Windows。

        :param platform: The platform of this ListImagesRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def architecture(self):
        """Gets the architecture of this ListImagesRequest.

        镜像架构：x86。

        :return: The architecture of this ListImagesRequest.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this ListImagesRequest.

        镜像架构：x86。

        :param architecture: The architecture of this ListImagesRequest.
        :type architecture: str
        """
        self._architecture = architecture

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
        if not isinstance(other, ListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
