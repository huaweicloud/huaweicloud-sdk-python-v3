# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateImages:

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
        'image_type': 'str',
        'namespace': 'str',
        'image_digest': 'str',
        'scan_status': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'namespace': 'namespace',
        'image_digest': 'image_digest',
        'scan_status': 'scan_status'
    }

    def __init__(self, image_name=None, image_version=None, image_type=None, namespace=None, image_digest=None, scan_status=None):
        """AssociateImages

        The model defined in huaweicloud sdk

        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param image_type: 镜像类型
        :type image_type: str
        :param namespace: 命名空间
        :type namespace: str
        :param image_digest: 镜像digest
        :type image_digest: str
        :param scan_status: 扫描状态，包含如下2种。   - unscan ：未扫描。   - success ：扫描完成。   - scanning ：正在扫描。   - failed ：扫描失败。   - download_failed ：下载失败。   - image_oversized ：镜像超大。   - waiting_for_scan ：等待扫描。
        :type scan_status: str
        """
        
        

        self._image_name = None
        self._image_version = None
        self._image_type = None
        self._namespace = None
        self._image_digest = None
        self._scan_status = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if namespace is not None:
            self.namespace = namespace
        if image_digest is not None:
            self.image_digest = image_digest
        if scan_status is not None:
            self.scan_status = scan_status

    @property
    def image_name(self):
        """Gets the image_name of this AssociateImages.

        镜像名称

        :return: The image_name of this AssociateImages.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this AssociateImages.

        镜像名称

        :param image_name: The image_name of this AssociateImages.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        """Gets the image_version of this AssociateImages.

        镜像版本

        :return: The image_version of this AssociateImages.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this AssociateImages.

        镜像版本

        :param image_version: The image_version of this AssociateImages.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        """Gets the image_type of this AssociateImages.

        镜像类型

        :return: The image_type of this AssociateImages.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this AssociateImages.

        镜像类型

        :param image_type: The image_type of this AssociateImages.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def namespace(self):
        """Gets the namespace of this AssociateImages.

        命名空间

        :return: The namespace of this AssociateImages.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this AssociateImages.

        命名空间

        :param namespace: The namespace of this AssociateImages.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_digest(self):
        """Gets the image_digest of this AssociateImages.

        镜像digest

        :return: The image_digest of this AssociateImages.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        """Sets the image_digest of this AssociateImages.

        镜像digest

        :param image_digest: The image_digest of this AssociateImages.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def scan_status(self):
        """Gets the scan_status of this AssociateImages.

        扫描状态，包含如下2种。   - unscan ：未扫描。   - success ：扫描完成。   - scanning ：正在扫描。   - failed ：扫描失败。   - download_failed ：下载失败。   - image_oversized ：镜像超大。   - waiting_for_scan ：等待扫描。

        :return: The scan_status of this AssociateImages.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this AssociateImages.

        扫描状态，包含如下2种。   - unscan ：未扫描。   - success ：扫描完成。   - scanning ：正在扫描。   - failed ：扫描失败。   - download_failed ：下载失败。   - image_oversized ：镜像超大。   - waiting_for_scan ：等待扫描。

        :param scan_status: The scan_status of this AssociateImages.
        :type scan_status: str
        """
        self._scan_status = scan_status

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
        if not isinstance(other, AssociateImages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
