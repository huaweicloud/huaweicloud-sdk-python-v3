# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateImageRepositoryInfo:

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
        'namespace': 'str',
        'image_name': 'str',
        'image_id': 'str',
        'image_digest': 'str',
        'image_version': 'str',
        'image_type': 'str',
        'latest_version': 'bool',
        'scan_status': 'str',
        'image_size': 'int',
        'latest_update_time': 'int',
        'latest_scan_time': 'int',
        'vul_num': 'int',
        'unsafe_setting_num': 'int',
        'malicious_file_num': 'int',
        'domain_name': 'str',
        'shared_status': 'str',
        'scannable': 'bool',
        'association_images': 'list[AssociateImages]'
    }

    attribute_map = {
        'id': 'id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_id': 'image_id',
        'image_digest': 'image_digest',
        'image_version': 'image_version',
        'image_type': 'image_type',
        'latest_version': 'latest_version',
        'scan_status': 'scan_status',
        'image_size': 'image_size',
        'latest_update_time': 'latest_update_time',
        'latest_scan_time': 'latest_scan_time',
        'vul_num': 'vul_num',
        'unsafe_setting_num': 'unsafe_setting_num',
        'malicious_file_num': 'malicious_file_num',
        'domain_name': 'domain_name',
        'shared_status': 'shared_status',
        'scannable': 'scannable',
        'association_images': 'association_images'
    }

    def __init__(self, id=None, namespace=None, image_name=None, image_id=None, image_digest=None, image_version=None, image_type=None, latest_version=None, scan_status=None, image_size=None, latest_update_time=None, latest_scan_time=None, vul_num=None, unsafe_setting_num=None, malicious_file_num=None, domain_name=None, shared_status=None, scannable=None, association_images=None):
        """PrivateImageRepositoryInfo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param namespace: 命名空间
        :type namespace: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_id: 镜像id
        :type image_id: str
        :param image_digest: 镜像digest
        :type image_digest: str
        :param image_version: 镜像版本
        :type image_version: str
        :param image_type: 镜像类型，包含如下2种。   - private_image ：私有镜像。   - shared_image ：共享镜像。
        :type image_type: str
        :param latest_version: 是否是最新版本
        :type latest_version: bool
        :param scan_status: 扫描状态，包含如下2种。   - unscan ：未扫描。   - success ：扫描完成。   - scanning ：正在扫描。   - failed ：扫描失败。   - download_failed ：下载失败。   - image_oversized ：镜像超大。   - waiting_for_scan ：等待扫描。
        :type scan_status: str
        :param image_size: 镜像大小
        :type image_size: int
        :param latest_update_time: 镜像版本最后更新时间
        :type latest_update_time: int
        :param latest_scan_time: 最近扫描时间
        :type latest_scan_time: int
        :param vul_num: 漏洞个数
        :type vul_num: int
        :param unsafe_setting_num: 基线扫描未通过数
        :type unsafe_setting_num: int
        :param malicious_file_num: 恶意文件数
        :type malicious_file_num: int
        :param domain_name: 拥有者（共享镜像参数）
        :type domain_name: str
        :param shared_status: 共享镜像状态，包含如下2种。   - expired ：已过期。   - effective ：有效。
        :type shared_status: str
        :param scannable: 是否可扫描
        :type scannable: bool
        :param association_images: 多架构关联镜像信息
        :type association_images: list[:class:`huaweicloudsdkhss.v5.AssociateImages`]
        """
        
        

        self._id = None
        self._namespace = None
        self._image_name = None
        self._image_id = None
        self._image_digest = None
        self._image_version = None
        self._image_type = None
        self._latest_version = None
        self._scan_status = None
        self._image_size = None
        self._latest_update_time = None
        self._latest_scan_time = None
        self._vul_num = None
        self._unsafe_setting_num = None
        self._malicious_file_num = None
        self._domain_name = None
        self._shared_status = None
        self._scannable = None
        self._association_images = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_id is not None:
            self.image_id = image_id
        if image_digest is not None:
            self.image_digest = image_digest
        if image_version is not None:
            self.image_version = image_version
        if image_type is not None:
            self.image_type = image_type
        if latest_version is not None:
            self.latest_version = latest_version
        if scan_status is not None:
            self.scan_status = scan_status
        if image_size is not None:
            self.image_size = image_size
        if latest_update_time is not None:
            self.latest_update_time = latest_update_time
        if latest_scan_time is not None:
            self.latest_scan_time = latest_scan_time
        if vul_num is not None:
            self.vul_num = vul_num
        if unsafe_setting_num is not None:
            self.unsafe_setting_num = unsafe_setting_num
        if malicious_file_num is not None:
            self.malicious_file_num = malicious_file_num
        if domain_name is not None:
            self.domain_name = domain_name
        if shared_status is not None:
            self.shared_status = shared_status
        if scannable is not None:
            self.scannable = scannable
        if association_images is not None:
            self.association_images = association_images

    @property
    def id(self):
        """Gets the id of this PrivateImageRepositoryInfo.

        id

        :return: The id of this PrivateImageRepositoryInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivateImageRepositoryInfo.

        id

        :param id: The id of this PrivateImageRepositoryInfo.
        :type id: int
        """
        self._id = id

    @property
    def namespace(self):
        """Gets the namespace of this PrivateImageRepositoryInfo.

        命名空间

        :return: The namespace of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this PrivateImageRepositoryInfo.

        命名空间

        :param namespace: The namespace of this PrivateImageRepositoryInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        """Gets the image_name of this PrivateImageRepositoryInfo.

        镜像名称

        :return: The image_name of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this PrivateImageRepositoryInfo.

        镜像名称

        :param image_name: The image_name of this PrivateImageRepositoryInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_id(self):
        """Gets the image_id of this PrivateImageRepositoryInfo.

        镜像id

        :return: The image_id of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this PrivateImageRepositoryInfo.

        镜像id

        :param image_id: The image_id of this PrivateImageRepositoryInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_digest(self):
        """Gets the image_digest of this PrivateImageRepositoryInfo.

        镜像digest

        :return: The image_digest of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        """Sets the image_digest of this PrivateImageRepositoryInfo.

        镜像digest

        :param image_digest: The image_digest of this PrivateImageRepositoryInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_version(self):
        """Gets the image_version of this PrivateImageRepositoryInfo.

        镜像版本

        :return: The image_version of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this PrivateImageRepositoryInfo.

        镜像版本

        :param image_version: The image_version of this PrivateImageRepositoryInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def image_type(self):
        """Gets the image_type of this PrivateImageRepositoryInfo.

        镜像类型，包含如下2种。   - private_image ：私有镜像。   - shared_image ：共享镜像。

        :return: The image_type of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this PrivateImageRepositoryInfo.

        镜像类型，包含如下2种。   - private_image ：私有镜像。   - shared_image ：共享镜像。

        :param image_type: The image_type of this PrivateImageRepositoryInfo.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def latest_version(self):
        """Gets the latest_version of this PrivateImageRepositoryInfo.

        是否是最新版本

        :return: The latest_version of this PrivateImageRepositoryInfo.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this PrivateImageRepositoryInfo.

        是否是最新版本

        :param latest_version: The latest_version of this PrivateImageRepositoryInfo.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def scan_status(self):
        """Gets the scan_status of this PrivateImageRepositoryInfo.

        扫描状态，包含如下2种。   - unscan ：未扫描。   - success ：扫描完成。   - scanning ：正在扫描。   - failed ：扫描失败。   - download_failed ：下载失败。   - image_oversized ：镜像超大。   - waiting_for_scan ：等待扫描。

        :return: The scan_status of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this PrivateImageRepositoryInfo.

        扫描状态，包含如下2种。   - unscan ：未扫描。   - success ：扫描完成。   - scanning ：正在扫描。   - failed ：扫描失败。   - download_failed ：下载失败。   - image_oversized ：镜像超大。   - waiting_for_scan ：等待扫描。

        :param scan_status: The scan_status of this PrivateImageRepositoryInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def image_size(self):
        """Gets the image_size of this PrivateImageRepositoryInfo.

        镜像大小

        :return: The image_size of this PrivateImageRepositoryInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this PrivateImageRepositoryInfo.

        镜像大小

        :param image_size: The image_size of this PrivateImageRepositoryInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def latest_update_time(self):
        """Gets the latest_update_time of this PrivateImageRepositoryInfo.

        镜像版本最后更新时间

        :return: The latest_update_time of this PrivateImageRepositoryInfo.
        :rtype: int
        """
        return self._latest_update_time

    @latest_update_time.setter
    def latest_update_time(self, latest_update_time):
        """Sets the latest_update_time of this PrivateImageRepositoryInfo.

        镜像版本最后更新时间

        :param latest_update_time: The latest_update_time of this PrivateImageRepositoryInfo.
        :type latest_update_time: int
        """
        self._latest_update_time = latest_update_time

    @property
    def latest_scan_time(self):
        """Gets the latest_scan_time of this PrivateImageRepositoryInfo.

        最近扫描时间

        :return: The latest_scan_time of this PrivateImageRepositoryInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        """Sets the latest_scan_time of this PrivateImageRepositoryInfo.

        最近扫描时间

        :param latest_scan_time: The latest_scan_time of this PrivateImageRepositoryInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def vul_num(self):
        """Gets the vul_num of this PrivateImageRepositoryInfo.

        漏洞个数

        :return: The vul_num of this PrivateImageRepositoryInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        """Sets the vul_num of this PrivateImageRepositoryInfo.

        漏洞个数

        :param vul_num: The vul_num of this PrivateImageRepositoryInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def unsafe_setting_num(self):
        """Gets the unsafe_setting_num of this PrivateImageRepositoryInfo.

        基线扫描未通过数

        :return: The unsafe_setting_num of this PrivateImageRepositoryInfo.
        :rtype: int
        """
        return self._unsafe_setting_num

    @unsafe_setting_num.setter
    def unsafe_setting_num(self, unsafe_setting_num):
        """Sets the unsafe_setting_num of this PrivateImageRepositoryInfo.

        基线扫描未通过数

        :param unsafe_setting_num: The unsafe_setting_num of this PrivateImageRepositoryInfo.
        :type unsafe_setting_num: int
        """
        self._unsafe_setting_num = unsafe_setting_num

    @property
    def malicious_file_num(self):
        """Gets the malicious_file_num of this PrivateImageRepositoryInfo.

        恶意文件数

        :return: The malicious_file_num of this PrivateImageRepositoryInfo.
        :rtype: int
        """
        return self._malicious_file_num

    @malicious_file_num.setter
    def malicious_file_num(self, malicious_file_num):
        """Sets the malicious_file_num of this PrivateImageRepositoryInfo.

        恶意文件数

        :param malicious_file_num: The malicious_file_num of this PrivateImageRepositoryInfo.
        :type malicious_file_num: int
        """
        self._malicious_file_num = malicious_file_num

    @property
    def domain_name(self):
        """Gets the domain_name of this PrivateImageRepositoryInfo.

        拥有者（共享镜像参数）

        :return: The domain_name of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this PrivateImageRepositoryInfo.

        拥有者（共享镜像参数）

        :param domain_name: The domain_name of this PrivateImageRepositoryInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def shared_status(self):
        """Gets the shared_status of this PrivateImageRepositoryInfo.

        共享镜像状态，包含如下2种。   - expired ：已过期。   - effective ：有效。

        :return: The shared_status of this PrivateImageRepositoryInfo.
        :rtype: str
        """
        return self._shared_status

    @shared_status.setter
    def shared_status(self, shared_status):
        """Sets the shared_status of this PrivateImageRepositoryInfo.

        共享镜像状态，包含如下2种。   - expired ：已过期。   - effective ：有效。

        :param shared_status: The shared_status of this PrivateImageRepositoryInfo.
        :type shared_status: str
        """
        self._shared_status = shared_status

    @property
    def scannable(self):
        """Gets the scannable of this PrivateImageRepositoryInfo.

        是否可扫描

        :return: The scannable of this PrivateImageRepositoryInfo.
        :rtype: bool
        """
        return self._scannable

    @scannable.setter
    def scannable(self, scannable):
        """Sets the scannable of this PrivateImageRepositoryInfo.

        是否可扫描

        :param scannable: The scannable of this PrivateImageRepositoryInfo.
        :type scannable: bool
        """
        self._scannable = scannable

    @property
    def association_images(self):
        """Gets the association_images of this PrivateImageRepositoryInfo.

        多架构关联镜像信息

        :return: The association_images of this PrivateImageRepositoryInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AssociateImages`]
        """
        return self._association_images

    @association_images.setter
    def association_images(self, association_images):
        """Sets the association_images of this PrivateImageRepositoryInfo.

        多架构关联镜像信息

        :param association_images: The association_images of this PrivateImageRepositoryInfo.
        :type association_images: list[:class:`huaweicloudsdkhss.v5.AssociateImages`]
        """
        self._association_images = association_images

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
        if not isinstance(other, PrivateImageRepositoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
