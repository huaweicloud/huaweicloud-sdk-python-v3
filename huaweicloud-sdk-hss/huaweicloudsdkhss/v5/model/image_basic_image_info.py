# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageBasicImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_name': 'str',
        'os_version': 'str',
        'layer_digest': 'str'
    }

    attribute_map = {
        'os_name': 'os_name',
        'os_version': 'os_version',
        'layer_digest': 'layer_digest'
    }

    def __init__(self, os_name=None, os_version=None, layer_digest=None):
        r"""ImageBasicImageInfo

        The model defined in huaweicloud sdk

        :param os_name: 基础镜像的系统名称
        :type os_name: str
        :param os_version: 基础镜像的系统版本
        :type os_version: str
        :param layer_digest: 基础镜像的层digest
        :type layer_digest: str
        """
        
        

        self._os_name = None
        self._os_version = None
        self._layer_digest = None
        self.discriminator = None

        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if layer_digest is not None:
            self.layer_digest = layer_digest

    @property
    def os_name(self):
        r"""Gets the os_name of this ImageBasicImageInfo.

        基础镜像的系统名称

        :return: The os_name of this ImageBasicImageInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ImageBasicImageInfo.

        基础镜像的系统名称

        :param os_name: The os_name of this ImageBasicImageInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this ImageBasicImageInfo.

        基础镜像的系统版本

        :return: The os_version of this ImageBasicImageInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ImageBasicImageInfo.

        基础镜像的系统版本

        :param os_version: The os_version of this ImageBasicImageInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def layer_digest(self):
        r"""Gets the layer_digest of this ImageBasicImageInfo.

        基础镜像的层digest

        :return: The layer_digest of this ImageBasicImageInfo.
        :rtype: str
        """
        return self._layer_digest

    @layer_digest.setter
    def layer_digest(self, layer_digest):
        r"""Sets the layer_digest of this ImageBasicImageInfo.

        基础镜像的层digest

        :param layer_digest: The layer_digest of this ImageBasicImageInfo.
        :type layer_digest: str
        """
        self._layer_digest = layer_digest

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
        if not isinstance(other, ImageBasicImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
