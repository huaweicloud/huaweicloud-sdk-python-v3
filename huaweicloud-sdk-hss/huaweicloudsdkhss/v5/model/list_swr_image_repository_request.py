# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSwrImageRepositoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'namespace': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'latest_version': 'bool',
        'offset': 'int',
        'limit': 'int',
        'image_type': 'str',
        'scan_status': 'str'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'namespace': 'namespace',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'latest_version': 'latest_version',
        'offset': 'offset',
        'limit': 'limit',
        'image_type': 'image_type',
        'scan_status': 'scan_status'
    }

    def __init__(self, region=None, enterprise_project_id=None, namespace=None, image_name=None, image_version=None, latest_version=None, offset=None, limit=None, image_type=None, scan_status=None):
        """ListSwrImageRepositoryRequest

        The model defined in huaweicloud sdk

        :param region: region id
        :type region: str
        :param enterprise_project_id: 租户企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param namespace: 组织名称
        :type namespace: str
        :param image_name: 镜像名称 id
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param latest_version: 仅关注最新版本镜像
        :type latest_version: bool
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        :param image_type: 镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库
        :type image_type: str
        :param scan_status: 扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大
        :type scan_status: str
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._namespace = None
        self._image_name = None
        self._image_version = None
        self._latest_version = None
        self._offset = None
        self._limit = None
        self._image_type = None
        self._scan_status = None
        self.discriminator = None

        self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if namespace is not None:
            self.namespace = namespace
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if latest_version is not None:
            self.latest_version = latest_version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.image_type = image_type
        if scan_status is not None:
            self.scan_status = scan_status

    @property
    def region(self):
        """Gets the region of this ListSwrImageRepositoryRequest.

        region id

        :return: The region of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListSwrImageRepositoryRequest.

        region id

        :param region: The region of this ListSwrImageRepositoryRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListSwrImageRepositoryRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListSwrImageRepositoryRequest.

        租户企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListSwrImageRepositoryRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def namespace(self):
        """Gets the namespace of this ListSwrImageRepositoryRequest.

        组织名称

        :return: The namespace of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListSwrImageRepositoryRequest.

        组织名称

        :param namespace: The namespace of this ListSwrImageRepositoryRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def image_name(self):
        """Gets the image_name of this ListSwrImageRepositoryRequest.

        镜像名称 id

        :return: The image_name of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ListSwrImageRepositoryRequest.

        镜像名称 id

        :param image_name: The image_name of this ListSwrImageRepositoryRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        """Gets the image_version of this ListSwrImageRepositoryRequest.

        镜像版本

        :return: The image_version of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this ListSwrImageRepositoryRequest.

        镜像版本

        :param image_version: The image_version of this ListSwrImageRepositoryRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def latest_version(self):
        """Gets the latest_version of this ListSwrImageRepositoryRequest.

        仅关注最新版本镜像

        :return: The latest_version of this ListSwrImageRepositoryRequest.
        :rtype: bool
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this ListSwrImageRepositoryRequest.

        仅关注最新版本镜像

        :param latest_version: The latest_version of this ListSwrImageRepositoryRequest.
        :type latest_version: bool
        """
        self._latest_version = latest_version

    @property
    def offset(self):
        """Gets the offset of this ListSwrImageRepositoryRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :return: The offset of this ListSwrImageRepositoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSwrImageRepositoryRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于或等于0，默认0

        :param offset: The offset of this ListSwrImageRepositoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSwrImageRepositoryRequest.

        每页显示个数

        :return: The limit of this ListSwrImageRepositoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSwrImageRepositoryRequest.

        每页显示个数

        :param limit: The limit of this ListSwrImageRepositoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def image_type(self):
        """Gets the image_type of this ListSwrImageRepositoryRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库

        :return: The image_type of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ListSwrImageRepositoryRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库

        :param image_type: The image_type of this ListSwrImageRepositoryRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def scan_status(self):
        """Gets the scan_status of this ListSwrImageRepositoryRequest.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :return: The scan_status of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this ListSwrImageRepositoryRequest.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大

        :param scan_status: The scan_status of this ListSwrImageRepositoryRequest.
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
        if not isinstance(other, ListSwrImageRepositoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
