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
        'scan_status': 'str',
        'instance_name': 'str',
        'image_size': 'int',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int',
        'has_malicious_file': 'bool',
        'has_unsafe_setting': 'bool',
        'has_vul': 'bool',
        'instance_id': 'str'
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
        'scan_status': 'scan_status',
        'instance_name': 'instance_name',
        'image_size': 'image_size',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time',
        'has_malicious_file': 'has_malicious_file',
        'has_unsafe_setting': 'has_unsafe_setting',
        'has_vul': 'has_vul',
        'instance_id': 'instance_id'
    }

    def __init__(self, region=None, enterprise_project_id=None, namespace=None, image_name=None, image_version=None, latest_version=None, offset=None, limit=None, image_type=None, scan_status=None, instance_name=None, image_size=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None, has_malicious_file=None, has_unsafe_setting=None, has_vul=None, instance_id=None):
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
        :param image_type: 镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像
        :type image_type: str
        :param scan_status: 扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - download_failed : 下载失败   - image_oversized : 镜像超大
        :type scan_status: str
        :param instance_name: 企业镜像实例名称
        :type instance_name: str
        :param image_size: 镜像大小
        :type image_size: int
        :param start_latest_update_time: 创建时间开始日期
        :type start_latest_update_time: int
        :param end_latest_update_time: 创建时间结束日期
        :type end_latest_update_time: int
        :param start_latest_scan_time: 最近一次扫描完成时间开始日期
        :type start_latest_scan_time: int
        :param end_latest_scan_time: 最近一次扫描完成时间结束日期
        :type end_latest_scan_time: int
        :param has_malicious_file: 是否存在恶意文件
        :type has_malicious_file: bool
        :param has_unsafe_setting: 是否存在基线检查
        :type has_unsafe_setting: bool
        :param has_vul: 是否存在软件漏洞
        :type has_vul: bool
        :param instance_id: 企业仓库实例ID，swr共享版无需使用该参数
        :type instance_id: str
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
        self._instance_name = None
        self._image_size = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self._has_malicious_file = None
        self._has_unsafe_setting = None
        self._has_vul = None
        self._instance_id = None
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
        if instance_name is not None:
            self.instance_name = instance_name
        if image_size is not None:
            self.image_size = image_size
        if start_latest_update_time is not None:
            self.start_latest_update_time = start_latest_update_time
        if end_latest_update_time is not None:
            self.end_latest_update_time = end_latest_update_time
        if start_latest_scan_time is not None:
            self.start_latest_scan_time = start_latest_scan_time
        if end_latest_scan_time is not None:
            self.end_latest_scan_time = end_latest_scan_time
        if has_malicious_file is not None:
            self.has_malicious_file = has_malicious_file
        if has_unsafe_setting is not None:
            self.has_unsafe_setting = has_unsafe_setting
        if has_vul is not None:
            self.has_vul = has_vul
        if instance_id is not None:
            self.instance_id = instance_id

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

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像

        :return: The image_type of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this ListSwrImageRepositoryRequest.

        镜像类型，包含如下:   - private_image : 私有镜像仓库   - shared_image : 共享镜像仓库   - local_image : 本地镜像   - instance_image : 企业镜像

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

    @property
    def instance_name(self):
        """Gets the instance_name of this ListSwrImageRepositoryRequest.

        企业镜像实例名称

        :return: The instance_name of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ListSwrImageRepositoryRequest.

        企业镜像实例名称

        :param instance_name: The instance_name of this ListSwrImageRepositoryRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def image_size(self):
        """Gets the image_size of this ListSwrImageRepositoryRequest.

        镜像大小

        :return: The image_size of this ListSwrImageRepositoryRequest.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this ListSwrImageRepositoryRequest.

        镜像大小

        :param image_size: The image_size of this ListSwrImageRepositoryRequest.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def start_latest_update_time(self):
        """Gets the start_latest_update_time of this ListSwrImageRepositoryRequest.

        创建时间开始日期

        :return: The start_latest_update_time of this ListSwrImageRepositoryRequest.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        """Sets the start_latest_update_time of this ListSwrImageRepositoryRequest.

        创建时间开始日期

        :param start_latest_update_time: The start_latest_update_time of this ListSwrImageRepositoryRequest.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        """Gets the end_latest_update_time of this ListSwrImageRepositoryRequest.

        创建时间结束日期

        :return: The end_latest_update_time of this ListSwrImageRepositoryRequest.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        """Sets the end_latest_update_time of this ListSwrImageRepositoryRequest.

        创建时间结束日期

        :param end_latest_update_time: The end_latest_update_time of this ListSwrImageRepositoryRequest.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        """Gets the start_latest_scan_time of this ListSwrImageRepositoryRequest.

        最近一次扫描完成时间开始日期

        :return: The start_latest_scan_time of this ListSwrImageRepositoryRequest.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        """Sets the start_latest_scan_time of this ListSwrImageRepositoryRequest.

        最近一次扫描完成时间开始日期

        :param start_latest_scan_time: The start_latest_scan_time of this ListSwrImageRepositoryRequest.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        """Gets the end_latest_scan_time of this ListSwrImageRepositoryRequest.

        最近一次扫描完成时间结束日期

        :return: The end_latest_scan_time of this ListSwrImageRepositoryRequest.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        """Sets the end_latest_scan_time of this ListSwrImageRepositoryRequest.

        最近一次扫描完成时间结束日期

        :param end_latest_scan_time: The end_latest_scan_time of this ListSwrImageRepositoryRequest.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

    @property
    def has_malicious_file(self):
        """Gets the has_malicious_file of this ListSwrImageRepositoryRequest.

        是否存在恶意文件

        :return: The has_malicious_file of this ListSwrImageRepositoryRequest.
        :rtype: bool
        """
        return self._has_malicious_file

    @has_malicious_file.setter
    def has_malicious_file(self, has_malicious_file):
        """Sets the has_malicious_file of this ListSwrImageRepositoryRequest.

        是否存在恶意文件

        :param has_malicious_file: The has_malicious_file of this ListSwrImageRepositoryRequest.
        :type has_malicious_file: bool
        """
        self._has_malicious_file = has_malicious_file

    @property
    def has_unsafe_setting(self):
        """Gets the has_unsafe_setting of this ListSwrImageRepositoryRequest.

        是否存在基线检查

        :return: The has_unsafe_setting of this ListSwrImageRepositoryRequest.
        :rtype: bool
        """
        return self._has_unsafe_setting

    @has_unsafe_setting.setter
    def has_unsafe_setting(self, has_unsafe_setting):
        """Sets the has_unsafe_setting of this ListSwrImageRepositoryRequest.

        是否存在基线检查

        :param has_unsafe_setting: The has_unsafe_setting of this ListSwrImageRepositoryRequest.
        :type has_unsafe_setting: bool
        """
        self._has_unsafe_setting = has_unsafe_setting

    @property
    def has_vul(self):
        """Gets the has_vul of this ListSwrImageRepositoryRequest.

        是否存在软件漏洞

        :return: The has_vul of this ListSwrImageRepositoryRequest.
        :rtype: bool
        """
        return self._has_vul

    @has_vul.setter
    def has_vul(self, has_vul):
        """Sets the has_vul of this ListSwrImageRepositoryRequest.

        是否存在软件漏洞

        :param has_vul: The has_vul of this ListSwrImageRepositoryRequest.
        :type has_vul: bool
        """
        self._has_vul = has_vul

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSwrImageRepositoryRequest.

        企业仓库实例ID，swr共享版无需使用该参数

        :return: The instance_id of this ListSwrImageRepositoryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSwrImageRepositoryRequest.

        企业仓库实例ID，swr共享版无需使用该参数

        :param instance_id: The instance_id of this ListSwrImageRepositoryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
