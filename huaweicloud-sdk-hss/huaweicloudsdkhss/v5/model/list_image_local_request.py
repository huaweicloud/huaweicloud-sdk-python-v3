# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageLocalRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'offset': 'int',
        'limit': 'int',
        'scan_status': 'str',
        'local_image_type': 'str',
        'image_size': 'int',
        'start_latest_update_time': 'int',
        'end_latest_update_time': 'int',
        'start_latest_scan_time': 'int',
        'end_latest_scan_time': 'int',
        'has_vul': 'bool',
        'host_name': 'str',
        'host_id': 'str',
        'host_ip': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'pod_id': 'str',
        'pod_name': 'str',
        'app_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'offset': 'offset',
        'limit': 'limit',
        'scan_status': 'scan_status',
        'local_image_type': 'local_image_type',
        'image_size': 'image_size',
        'start_latest_update_time': 'start_latest_update_time',
        'end_latest_update_time': 'end_latest_update_time',
        'start_latest_scan_time': 'start_latest_scan_time',
        'end_latest_scan_time': 'end_latest_scan_time',
        'has_vul': 'has_vul',
        'host_name': 'host_name',
        'host_id': 'host_id',
        'host_ip': 'host_ip',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'pod_id': 'pod_id',
        'pod_name': 'pod_name',
        'app_name': 'app_name'
    }

    def __init__(self, enterprise_project_id=None, image_name=None, image_version=None, offset=None, limit=None, scan_status=None, local_image_type=None, image_size=None, start_latest_update_time=None, end_latest_update_time=None, start_latest_scan_time=None, end_latest_scan_time=None, has_vul=None, host_name=None, host_id=None, host_ip=None, container_id=None, container_name=None, pod_id=None, pod_name=None, app_name=None):
        """ListImageLocalRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param image_name: 镜像名称
        :type image_name: str
        :param image_version: 镜像版本
        :type image_version: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示数量
        :type limit: int
        :param scan_status: 扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - waiting_for_scan : 等待扫描
        :type scan_status: str
        :param local_image_type: 镜像类型，包含如下:  - other_image : 非SWR镜像  - swr_image : SWR镜像
        :type local_image_type: str
        :param image_size: 镜像大小，单位字节
        :type image_size: int
        :param start_latest_update_time: 最近更新时间搜索开始日期，时间单位 毫秒（ms）
        :type start_latest_update_time: int
        :param end_latest_update_time: 最近更新时间搜索结束日期，时间单位 毫秒（ms）
        :type end_latest_update_time: int
        :param start_latest_scan_time: 最近一次扫描完成时间搜索开始日期，时间单位 毫秒（ms）
        :type start_latest_scan_time: int
        :param end_latest_scan_time: 最近一次扫描完成时间搜索结束日期，时间单位 毫秒（ms）
        :type end_latest_scan_time: int
        :param has_vul: 是否存在软件漏洞
        :type has_vul: bool
        :param host_name: 本地镜像所关联服务器的名称
        :type host_name: str
        :param host_id: 本地镜像所关联服务器的ID
        :type host_id: str
        :param host_ip: 本地镜像所关联服务器的IP（公网或私网）
        :type host_ip: str
        :param container_id: 本地镜像所关联容器的ID
        :type container_id: str
        :param container_name: 本地镜像所关联容器的名称
        :type container_name: str
        :param pod_id: 本地镜像所关联Pod的ID
        :type pod_id: str
        :param pod_name: 本地镜像所关联Pod的名称
        :type pod_name: str
        :param app_name: 本地镜像所关联软件的名称
        :type app_name: str
        """
        
        

        self._enterprise_project_id = None
        self._image_name = None
        self._image_version = None
        self._offset = None
        self._limit = None
        self._scan_status = None
        self._local_image_type = None
        self._image_size = None
        self._start_latest_update_time = None
        self._end_latest_update_time = None
        self._start_latest_scan_time = None
        self._end_latest_scan_time = None
        self._has_vul = None
        self._host_name = None
        self._host_id = None
        self._host_ip = None
        self._container_id = None
        self._container_name = None
        self._pod_id = None
        self._pod_name = None
        self._app_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if scan_status is not None:
            self.scan_status = scan_status
        if local_image_type is not None:
            self.local_image_type = local_image_type
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
        if has_vul is not None:
            self.has_vul = has_vul
        if host_name is not None:
            self.host_name = host_name
        if host_id is not None:
            self.host_id = host_id
        if host_ip is not None:
            self.host_ip = host_ip
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name
        if app_name is not None:
            self.app_name = app_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListImageLocalRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListImageLocalRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListImageLocalRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def image_name(self):
        """Gets the image_name of this ListImageLocalRequest.

        镜像名称

        :return: The image_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ListImageLocalRequest.

        镜像名称

        :param image_name: The image_name of this ListImageLocalRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        """Gets the image_version of this ListImageLocalRequest.

        镜像版本

        :return: The image_version of this ListImageLocalRequest.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this ListImageLocalRequest.

        镜像版本

        :param image_version: The image_version of this ListImageLocalRequest.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def offset(self):
        """Gets the offset of this ListImageLocalRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListImageLocalRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListImageLocalRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListImageLocalRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListImageLocalRequest.

        每页显示数量

        :return: The limit of this ListImageLocalRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListImageLocalRequest.

        每页显示数量

        :param limit: The limit of this ListImageLocalRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def scan_status(self):
        """Gets the scan_status of this ListImageLocalRequest.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - waiting_for_scan : 等待扫描

        :return: The scan_status of this ListImageLocalRequest.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this ListImageLocalRequest.

        扫描状态，包含如下:   - unscan : 未扫描   - success : 扫描完成   - scanning : 扫描中   - failed : 扫描失败   - waiting_for_scan : 等待扫描

        :param scan_status: The scan_status of this ListImageLocalRequest.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def local_image_type(self):
        """Gets the local_image_type of this ListImageLocalRequest.

        镜像类型，包含如下:  - other_image : 非SWR镜像  - swr_image : SWR镜像

        :return: The local_image_type of this ListImageLocalRequest.
        :rtype: str
        """
        return self._local_image_type

    @local_image_type.setter
    def local_image_type(self, local_image_type):
        """Sets the local_image_type of this ListImageLocalRequest.

        镜像类型，包含如下:  - other_image : 非SWR镜像  - swr_image : SWR镜像

        :param local_image_type: The local_image_type of this ListImageLocalRequest.
        :type local_image_type: str
        """
        self._local_image_type = local_image_type

    @property
    def image_size(self):
        """Gets the image_size of this ListImageLocalRequest.

        镜像大小，单位字节

        :return: The image_size of this ListImageLocalRequest.
        :rtype: int
        """
        return self._image_size

    @image_size.setter
    def image_size(self, image_size):
        """Sets the image_size of this ListImageLocalRequest.

        镜像大小，单位字节

        :param image_size: The image_size of this ListImageLocalRequest.
        :type image_size: int
        """
        self._image_size = image_size

    @property
    def start_latest_update_time(self):
        """Gets the start_latest_update_time of this ListImageLocalRequest.

        最近更新时间搜索开始日期，时间单位 毫秒（ms）

        :return: The start_latest_update_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._start_latest_update_time

    @start_latest_update_time.setter
    def start_latest_update_time(self, start_latest_update_time):
        """Sets the start_latest_update_time of this ListImageLocalRequest.

        最近更新时间搜索开始日期，时间单位 毫秒（ms）

        :param start_latest_update_time: The start_latest_update_time of this ListImageLocalRequest.
        :type start_latest_update_time: int
        """
        self._start_latest_update_time = start_latest_update_time

    @property
    def end_latest_update_time(self):
        """Gets the end_latest_update_time of this ListImageLocalRequest.

        最近更新时间搜索结束日期，时间单位 毫秒（ms）

        :return: The end_latest_update_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._end_latest_update_time

    @end_latest_update_time.setter
    def end_latest_update_time(self, end_latest_update_time):
        """Sets the end_latest_update_time of this ListImageLocalRequest.

        最近更新时间搜索结束日期，时间单位 毫秒（ms）

        :param end_latest_update_time: The end_latest_update_time of this ListImageLocalRequest.
        :type end_latest_update_time: int
        """
        self._end_latest_update_time = end_latest_update_time

    @property
    def start_latest_scan_time(self):
        """Gets the start_latest_scan_time of this ListImageLocalRequest.

        最近一次扫描完成时间搜索开始日期，时间单位 毫秒（ms）

        :return: The start_latest_scan_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._start_latest_scan_time

    @start_latest_scan_time.setter
    def start_latest_scan_time(self, start_latest_scan_time):
        """Sets the start_latest_scan_time of this ListImageLocalRequest.

        最近一次扫描完成时间搜索开始日期，时间单位 毫秒（ms）

        :param start_latest_scan_time: The start_latest_scan_time of this ListImageLocalRequest.
        :type start_latest_scan_time: int
        """
        self._start_latest_scan_time = start_latest_scan_time

    @property
    def end_latest_scan_time(self):
        """Gets the end_latest_scan_time of this ListImageLocalRequest.

        最近一次扫描完成时间搜索结束日期，时间单位 毫秒（ms）

        :return: The end_latest_scan_time of this ListImageLocalRequest.
        :rtype: int
        """
        return self._end_latest_scan_time

    @end_latest_scan_time.setter
    def end_latest_scan_time(self, end_latest_scan_time):
        """Sets the end_latest_scan_time of this ListImageLocalRequest.

        最近一次扫描完成时间搜索结束日期，时间单位 毫秒（ms）

        :param end_latest_scan_time: The end_latest_scan_time of this ListImageLocalRequest.
        :type end_latest_scan_time: int
        """
        self._end_latest_scan_time = end_latest_scan_time

    @property
    def has_vul(self):
        """Gets the has_vul of this ListImageLocalRequest.

        是否存在软件漏洞

        :return: The has_vul of this ListImageLocalRequest.
        :rtype: bool
        """
        return self._has_vul

    @has_vul.setter
    def has_vul(self, has_vul):
        """Sets the has_vul of this ListImageLocalRequest.

        是否存在软件漏洞

        :param has_vul: The has_vul of this ListImageLocalRequest.
        :type has_vul: bool
        """
        self._has_vul = has_vul

    @property
    def host_name(self):
        """Gets the host_name of this ListImageLocalRequest.

        本地镜像所关联服务器的名称

        :return: The host_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ListImageLocalRequest.

        本地镜像所关联服务器的名称

        :param host_name: The host_name of this ListImageLocalRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_id(self):
        """Gets the host_id of this ListImageLocalRequest.

        本地镜像所关联服务器的ID

        :return: The host_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ListImageLocalRequest.

        本地镜像所关联服务器的ID

        :param host_id: The host_id of this ListImageLocalRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_ip(self):
        """Gets the host_ip of this ListImageLocalRequest.

        本地镜像所关联服务器的IP（公网或私网）

        :return: The host_ip of this ListImageLocalRequest.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ListImageLocalRequest.

        本地镜像所关联服务器的IP（公网或私网）

        :param host_ip: The host_ip of this ListImageLocalRequest.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def container_id(self):
        """Gets the container_id of this ListImageLocalRequest.

        本地镜像所关联容器的ID

        :return: The container_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        """Sets the container_id of this ListImageLocalRequest.

        本地镜像所关联容器的ID

        :param container_id: The container_id of this ListImageLocalRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        """Gets the container_name of this ListImageLocalRequest.

        本地镜像所关联容器的名称

        :return: The container_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this ListImageLocalRequest.

        本地镜像所关联容器的名称

        :param container_name: The container_name of this ListImageLocalRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_id(self):
        """Gets the pod_id of this ListImageLocalRequest.

        本地镜像所关联Pod的ID

        :return: The pod_id of this ListImageLocalRequest.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        """Sets the pod_id of this ListImageLocalRequest.

        本地镜像所关联Pod的ID

        :param pod_id: The pod_id of this ListImageLocalRequest.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        """Gets the pod_name of this ListImageLocalRequest.

        本地镜像所关联Pod的名称

        :return: The pod_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this ListImageLocalRequest.

        本地镜像所关联Pod的名称

        :param pod_name: The pod_name of this ListImageLocalRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def app_name(self):
        """Gets the app_name of this ListImageLocalRequest.

        本地镜像所关联软件的名称

        :return: The app_name of this ListImageLocalRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListImageLocalRequest.

        本地镜像所关联软件的名称

        :param app_name: The app_name of this ListImageLocalRequest.
        :type app_name: str
        """
        self._app_name = app_name

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
        if not isinstance(other, ListImageLocalRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
