# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_project_name': 'str',
        'image_name': 'str',
        'image_tag': 'str',
        'profile': 'Profile'
    }

    attribute_map = {
        'source_project_name': 'source_project_name',
        'image_name': 'image_name',
        'image_tag': 'image_tag',
        'profile': 'profile'
    }

    def __init__(self, source_project_name=None, image_name=None, image_tag=None, profile=None):
        """ImageInfo

        The model defined in huaweicloud sdk

        :param source_project_name: 源项目名
        :type source_project_name: str
        :param image_name: 镜像名
        :type image_name: str
        :param image_tag: 镜像tag名
        :type image_tag: str
        :param profile: 
        :type profile: :class:`huaweicloudsdkeihealth.v1.Profile`
        """
        
        

        self._source_project_name = None
        self._image_name = None
        self._image_tag = None
        self._profile = None
        self.discriminator = None

        if source_project_name is not None:
            self.source_project_name = source_project_name
        if image_name is not None:
            self.image_name = image_name
        if image_tag is not None:
            self.image_tag = image_tag
        if profile is not None:
            self.profile = profile

    @property
    def source_project_name(self):
        """Gets the source_project_name of this ImageInfo.

        源项目名

        :return: The source_project_name of this ImageInfo.
        :rtype: str
        """
        return self._source_project_name

    @source_project_name.setter
    def source_project_name(self, source_project_name):
        """Sets the source_project_name of this ImageInfo.

        源项目名

        :param source_project_name: The source_project_name of this ImageInfo.
        :type source_project_name: str
        """
        self._source_project_name = source_project_name

    @property
    def image_name(self):
        """Gets the image_name of this ImageInfo.

        镜像名

        :return: The image_name of this ImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ImageInfo.

        镜像名

        :param image_name: The image_name of this ImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_tag(self):
        """Gets the image_tag of this ImageInfo.

        镜像tag名

        :return: The image_tag of this ImageInfo.
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this ImageInfo.

        镜像tag名

        :param image_tag: The image_tag of this ImageInfo.
        :type image_tag: str
        """
        self._image_tag = image_tag

    @property
    def profile(self):
        """Gets the profile of this ImageInfo.

        :return: The profile of this ImageInfo.
        :rtype: :class:`huaweicloudsdkeihealth.v1.Profile`
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this ImageInfo.

        :param profile: The profile of this ImageInfo.
        :type profile: :class:`huaweicloudsdkeihealth.v1.Profile`
        """
        self._profile = profile

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
        if not isinstance(other, ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
