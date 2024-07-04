# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageLocalInfo:

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
        'image_id': 'str',
        'image_digest': 'str',
        'image_version': 'str',
        'local_image_type': 'str',
        'scan_status': 'str',
        'image_size': 'int',
        'latest_update_time': 'int',
        'latest_scan_time': 'int',
        'vul_num': 'int',
        'unsafe_setting_num': 'int',
        'malicious_file_num': 'int',
        'host_num': 'int',
        'container_num': 'int',
        'component_num': 'int',
        'scan_failed_desc': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_id': 'image_id',
        'image_digest': 'image_digest',
        'image_version': 'image_version',
        'local_image_type': 'local_image_type',
        'scan_status': 'scan_status',
        'image_size': 'image_size',
        'latest_update_time': 'latest_update_time',
        'latest_scan_time': 'latest_scan_time',
        'vul_num': 'vul_num',
        'unsafe_setting_num': 'unsafe_setting_num',
        'malicious_file_num': 'malicious_file_num',
        'host_num': 'host_num',
        'container_num': 'container_num',
        'component_num': 'component_num',
        'scan_failed_desc': 'scan_failed_desc'
    }

    def __init__(self, image_name=None, image_id=None, image_digest=None, image_version=None, local_image_type=None, scan_status=None, image_size=None, latest_update_time=None, latest_scan_time=None, vul_num=None, unsafe_setting_num=None, malicious_file_num=None, host_num=None, container_num=None, component_num=None, scan_failed_desc=None):
        """ImageLocalInfo

        The model defined in huaweicloud sdk

        :param image_name: 镜像名称
        :type image_name: str
        :param image_id: 镜像ID
        :type image_id: str
        :param image_digest: 镜像digest
        :type image_digest: str
        :param image_version: 镜像版本
        :type image_version: str
        :param local_image_type: 本地镜像类型
        :type local_image_type: str
        :param scan_status: 扫描状态，包含如下：   - unscan：未扫描   - success：扫描完成   - scanning：正在扫描   - failed：扫描失败   - waiting：等待扫描
        :type scan_status: str
        :param image_size: 镜像大小，单位字节
        :type image_size: int
        :param latest_update_time: 镜像版本最后更新时间，时间单位毫秒（ms）
        :type latest_update_time: int
        :param latest_scan_time: 最近扫描时间，时间单位毫秒（ms）
        :type latest_scan_time: int
        :param vul_num: 漏洞个数
        :type vul_num: int
        :param unsafe_setting_num: 基线扫描未通过数
        :type unsafe_setting_num: int
        :param malicious_file_num: 恶意文件数
        :type malicious_file_num: int
        :param host_num: 关联主机数
        :type host_num: int
        :param container_num: 关联容器数
        :type container_num: int
        :param component_num: 关联组件数
        :type component_num: int
        :param scan_failed_desc: 扫描失败原因，包含如下10种。   - \&quot;unknown_error\&quot;:未知错误   - \&quot;failed_to_match_agent\&quot;:对应主机未开启容器版防护或agent离线   - \&quot;create_container_failed\&quot;:创建容器失败        - \&quot;get_container_info_failed\&quot;:获取容器信息失败   - \&quot;docker_offline\&quot;:docker引擎不在线   - \&quot;get_docker_root_failed\&quot;:获取容器根文件系统失败   - \&quot;image_not_exist_or_docker_api_fault\&quot;:镜像不存在或docker接口错误   - \&quot;huge_image\&quot;:超大镜像   - \&quot;docker_root_in_nfs\&quot;:容器根目录位于网络挂载   - \&quot;response_timed_out\&quot;:响应超时
        :type scan_failed_desc: str
        """
        
        

        self._image_name = None
        self._image_id = None
        self._image_digest = None
        self._image_version = None
        self._local_image_type = None
        self._scan_status = None
        self._image_size = None
        self._latest_update_time = None
        self._latest_scan_time = None
        self._vul_num = None
        self._unsafe_setting_num = None
        self._malicious_file_num = None
        self._host_num = None
        self._container_num = None
        self._component_num = None
        self._scan_failed_desc = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if image_id is not None:
            self.image_id = image_id
        if image_digest is not None:
            self.image_digest = image_digest
        if image_version is not None:
            self.image_version = image_version
        if local_image_type is not None:
            self.local_image_type = local_image_type
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
        if host_num is not None:
            self.host_num = host_num
        if container_num is not None:
            self.container_num = container_num
        if component_num is not None:
            self.component_num = component_num
        if scan_failed_desc is not None:
            self.scan_failed_desc = scan_failed_desc

    @property
    def image_name(self):
        """Gets the image_name of this ImageLocalInfo.

        镜像名称

        :return: The image_name of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ImageLocalInfo.

        镜像名称

        :param image_name: The image_name of this ImageLocalInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_id(self):
        """Gets the image_id of this ImageLocalInfo.

        镜像ID

        :return: The image_id of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ImageLocalInfo.

        镜像ID

        :param image_id: The image_id of this ImageLocalInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_digest(self):
        """Gets the image_digest of this ImageLocalInfo.

        镜像digest

        :return: The image_digest of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_digest

    @image_digest.setter
    def image_digest(self, image_digest):
        """Sets the image_digest of this ImageLocalInfo.

        镜像digest

        :param image_digest: The image_digest of this ImageLocalInfo.
        :type image_digest: str
        """
        self._image_digest = image_digest

    @property
    def image_version(self):
        """Gets the image_version of this ImageLocalInfo.

        镜像版本

        :return: The image_version of this ImageLocalInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this ImageLocalInfo.

        镜像版本

        :param image_version: The image_version of this ImageLocalInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def local_image_type(self):
        """Gets the local_image_type of this ImageLocalInfo.

        本地镜像类型

        :return: The local_image_type of this ImageLocalInfo.
        :rtype: str
        """
        return self._local_image_type

    @local_image_type.setter
    def local_image_type(self, local_image_type):
        """Sets the local_image_type of this ImageLocalInfo.

        本地镜像类型

        :param local_image_type: The local_image_type of this ImageLocalInfo.
        :type local_image_type: str
        """
        self._local_image_type = local_image_type

    @property
    def scan_status(self):
        """Gets the scan_status of this ImageLocalInfo.

        扫描状态，包含如下：   - unscan：未扫描   - success：扫描完成   - scanning：正在扫描   - failed：扫描失败   - waiting：等待扫描

        :return: The scan_status of this ImageLocalInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this ImageLocalInfo.

        扫描状态，包含如下：   - unscan：未扫描   - success：扫描完成   - scanning：正在扫描   - failed：扫描失败   - waiting：等待扫描

        :param scan_status: The scan_status of this ImageLocalInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def image_size(self):
        """Gets the image_size of this ImageLocalInfo.

        镜像大小，单位字节

        :return: The image_size of this ImageLocalInfo.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this ImageLocalInfo.

        镜像大小，单位字节

        :param image_size: The image_size of this ImageLocalInfo.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def latest_update_time(self):
        """Gets the latest_update_time of this ImageLocalInfo.

        镜像版本最后更新时间，时间单位毫秒（ms）

        :return: The latest_update_time of this ImageLocalInfo.
        :rtype: int
        """
        return self._latest_update_time

    @latest_update_time.setter
    def latest_update_time(self, latest_update_time):
        """Sets the latest_update_time of this ImageLocalInfo.

        镜像版本最后更新时间，时间单位毫秒（ms）

        :param latest_update_time: The latest_update_time of this ImageLocalInfo.
        :type latest_update_time: int
        """
        self._latest_update_time = latest_update_time

    @property
    def latest_scan_time(self):
        """Gets the latest_scan_time of this ImageLocalInfo.

        最近扫描时间，时间单位毫秒（ms）

        :return: The latest_scan_time of this ImageLocalInfo.
        :rtype: int
        """
        return self._latest_scan_time

    @latest_scan_time.setter
    def latest_scan_time(self, latest_scan_time):
        """Sets the latest_scan_time of this ImageLocalInfo.

        最近扫描时间，时间单位毫秒（ms）

        :param latest_scan_time: The latest_scan_time of this ImageLocalInfo.
        :type latest_scan_time: int
        """
        self._latest_scan_time = latest_scan_time

    @property
    def vul_num(self):
        """Gets the vul_num of this ImageLocalInfo.

        漏洞个数

        :return: The vul_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        """Sets the vul_num of this ImageLocalInfo.

        漏洞个数

        :param vul_num: The vul_num of this ImageLocalInfo.
        :type vul_num: int
        """
        self._vul_num = vul_num

    @property
    def unsafe_setting_num(self):
        """Gets the unsafe_setting_num of this ImageLocalInfo.

        基线扫描未通过数

        :return: The unsafe_setting_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._unsafe_setting_num

    @unsafe_setting_num.setter
    def unsafe_setting_num(self, unsafe_setting_num):
        """Sets the unsafe_setting_num of this ImageLocalInfo.

        基线扫描未通过数

        :param unsafe_setting_num: The unsafe_setting_num of this ImageLocalInfo.
        :type unsafe_setting_num: int
        """
        self._unsafe_setting_num = unsafe_setting_num

    @property
    def malicious_file_num(self):
        """Gets the malicious_file_num of this ImageLocalInfo.

        恶意文件数

        :return: The malicious_file_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._malicious_file_num

    @malicious_file_num.setter
    def malicious_file_num(self, malicious_file_num):
        """Sets the malicious_file_num of this ImageLocalInfo.

        恶意文件数

        :param malicious_file_num: The malicious_file_num of this ImageLocalInfo.
        :type malicious_file_num: int
        """
        self._malicious_file_num = malicious_file_num

    @property
    def host_num(self):
        """Gets the host_num of this ImageLocalInfo.

        关联主机数

        :return: The host_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        """Sets the host_num of this ImageLocalInfo.

        关联主机数

        :param host_num: The host_num of this ImageLocalInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def container_num(self):
        """Gets the container_num of this ImageLocalInfo.

        关联容器数

        :return: The container_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._container_num

    @container_num.setter
    def container_num(self, container_num):
        """Sets the container_num of this ImageLocalInfo.

        关联容器数

        :param container_num: The container_num of this ImageLocalInfo.
        :type container_num: int
        """
        self._container_num = container_num

    @property
    def component_num(self):
        """Gets the component_num of this ImageLocalInfo.

        关联组件数

        :return: The component_num of this ImageLocalInfo.
        :rtype: int
        """
        return self._component_num

    @component_num.setter
    def component_num(self, component_num):
        """Sets the component_num of this ImageLocalInfo.

        关联组件数

        :param component_num: The component_num of this ImageLocalInfo.
        :type component_num: int
        """
        self._component_num = component_num

    @property
    def scan_failed_desc(self):
        """Gets the scan_failed_desc of this ImageLocalInfo.

        扫描失败原因，包含如下10种。   - \"unknown_error\":未知错误   - \"failed_to_match_agent\":对应主机未开启容器版防护或agent离线   - \"create_container_failed\":创建容器失败        - \"get_container_info_failed\":获取容器信息失败   - \"docker_offline\":docker引擎不在线   - \"get_docker_root_failed\":获取容器根文件系统失败   - \"image_not_exist_or_docker_api_fault\":镜像不存在或docker接口错误   - \"huge_image\":超大镜像   - \"docker_root_in_nfs\":容器根目录位于网络挂载   - \"response_timed_out\":响应超时

        :return: The scan_failed_desc of this ImageLocalInfo.
        :rtype: str
        """
        return self._scan_failed_desc

    @scan_failed_desc.setter
    def scan_failed_desc(self, scan_failed_desc):
        """Sets the scan_failed_desc of this ImageLocalInfo.

        扫描失败原因，包含如下10种。   - \"unknown_error\":未知错误   - \"failed_to_match_agent\":对应主机未开启容器版防护或agent离线   - \"create_container_failed\":创建容器失败        - \"get_container_info_failed\":获取容器信息失败   - \"docker_offline\":docker引擎不在线   - \"get_docker_root_failed\":获取容器根文件系统失败   - \"image_not_exist_or_docker_api_fault\":镜像不存在或docker接口错误   - \"huge_image\":超大镜像   - \"docker_root_in_nfs\":容器根目录位于网络挂载   - \"response_timed_out\":响应超时

        :param scan_failed_desc: The scan_failed_desc of this ImageLocalInfo.
        :type scan_failed_desc: str
        """
        self._scan_failed_desc = scan_failed_desc

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
        if not isinstance(other, ImageLocalInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
