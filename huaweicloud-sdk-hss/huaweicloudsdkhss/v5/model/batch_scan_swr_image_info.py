# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchScanSwrImageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version'
    }

    def __init__(self, namespace=None, image_name=None, image_version=None):
        """BatchScanSwrImageInfo

        The model defined in huaweicloud sdk

        :param namespace: 命名空间
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        """
        
        

        self._namespace = None
        self._image_name = None
        self._image_version = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version

    @property
    def namespace(self):
        """Gets the namespace of this BatchScanSwrImageInfo.

        命名空间

        :return: The namespace of this BatchScanSwrImageInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this BatchScanSwrImageInfo.

        命名空间

        :param namespace: The namespace of this BatchScanSwrImageInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        """Gets the image_name of this BatchScanSwrImageInfo.

        镜像名称

        :return: The image_name of this BatchScanSwrImageInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this BatchScanSwrImageInfo.

        镜像名称

        :param image_name: The image_name of this BatchScanSwrImageInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        """Gets the image_version of this BatchScanSwrImageInfo.

        镜像版本

        :return: The image_version of this BatchScanSwrImageInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this BatchScanSwrImageInfo.

        镜像版本

        :param image_version: The image_version of this BatchScanSwrImageInfo.
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
        if not isinstance(other, BatchScanSwrImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
