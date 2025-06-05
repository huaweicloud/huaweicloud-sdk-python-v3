# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulhandleHistoryResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user_name': 'str',
        'type': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'handle_time': 'str',
        'status': 'str',
        'failed_reason': 'str',
        'description': 'str',
        'vul_id': 'str',
        'vul_name': 'str',
        'asset_value': 'str',
        'cve_list': 'list[VulCveInfo]',
        'app_name': 'str',
        'app_path': 'str',
        'app_version': 'str',
        'handle_type': 'str',
        'cluster_id': 'str',
        'container_name': 'str',
        'container_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_name': 'user_name',
        'type': 'type',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'handle_time': 'handle_time',
        'status': 'status',
        'failed_reason': 'failed_reason',
        'description': 'description',
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'asset_value': 'asset_value',
        'cve_list': 'cve_list',
        'app_name': 'app_name',
        'app_path': 'app_path',
        'app_version': 'app_version',
        'handle_type': 'handle_type',
        'cluster_id': 'cluster_id',
        'container_name': 'container_name',
        'container_id': 'container_id'
    }

    def __init__(self, id=None, user_name=None, type=None, host_id=None, host_name=None, public_ip=None, private_ip=None, handle_time=None, status=None, failed_reason=None, description=None, vul_id=None, vul_name=None, asset_value=None, cve_list=None, app_name=None, app_path=None, app_version=None, handle_type=None, cluster_id=None, container_name=None, container_id=None):
        r"""VulhandleHistoryResponseInfoDataList

        The model defined in huaweicloud sdk

        :param id: 历史记录唯一id
        :type id: str
        :param user_name: 用户名
        :type user_name: str
        :param type: 漏洞类型
        :type type: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param private_ip: 服务器私网IP
        :type private_ip: str
        :param handle_time: 处置时间
        :type handle_time: str
        :param status: 处置状态
        :type status: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        :param description: 备注
        :type description: str
        :param vul_id: 漏洞ID
        :type vul_id: str
        :param vul_name: 漏洞名称
        :type vul_name: str
        :param asset_value: 资产重要性
        :type asset_value: str
        :param cve_list: cve列表
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulCveInfo`]
        :param app_name: 软件名称
        :type app_name: str
        :param app_path: 应用软件路径
        :type app_path: str
        :param app_version: 软件版本
        :type app_version: str
        :param handle_type: 处置类型
        :type handle_type: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param container_name: 容器名称
        :type container_name: str
        :param container_id: 容器ID
        :type container_id: str
        """
        
        

        self._id = None
        self._user_name = None
        self._type = None
        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._handle_time = None
        self._status = None
        self._failed_reason = None
        self._description = None
        self._vul_id = None
        self._vul_name = None
        self._asset_value = None
        self._cve_list = None
        self._app_name = None
        self._app_path = None
        self._app_version = None
        self._handle_type = None
        self._cluster_id = None
        self._container_name = None
        self._container_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_name is not None:
            self.user_name = user_name
        if type is not None:
            self.type = type
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if handle_time is not None:
            self.handle_time = handle_time
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if description is not None:
            self.description = description
        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if asset_value is not None:
            self.asset_value = asset_value
        if cve_list is not None:
            self.cve_list = cve_list
        if app_name is not None:
            self.app_name = app_name
        if app_path is not None:
            self.app_path = app_path
        if app_version is not None:
            self.app_version = app_version
        if handle_type is not None:
            self.handle_type = handle_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id

    @property
    def id(self):
        r"""Gets the id of this VulhandleHistoryResponseInfoDataList.

        历史记录唯一id

        :return: The id of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VulhandleHistoryResponseInfoDataList.

        历史记录唯一id

        :param id: The id of this VulhandleHistoryResponseInfoDataList.
        :type id: str
        """
        self._id = id

    @property
    def user_name(self):
        r"""Gets the user_name of this VulhandleHistoryResponseInfoDataList.

        用户名

        :return: The user_name of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this VulhandleHistoryResponseInfoDataList.

        用户名

        :param user_name: The user_name of this VulhandleHistoryResponseInfoDataList.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def type(self):
        r"""Gets the type of this VulhandleHistoryResponseInfoDataList.

        漏洞类型

        :return: The type of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VulhandleHistoryResponseInfoDataList.

        漏洞类型

        :param type: The type of this VulhandleHistoryResponseInfoDataList.
        :type type: str
        """
        self._type = type

    @property
    def host_id(self):
        r"""Gets the host_id of this VulhandleHistoryResponseInfoDataList.

        服务器ID

        :return: The host_id of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulhandleHistoryResponseInfoDataList.

        服务器ID

        :param host_id: The host_id of this VulhandleHistoryResponseInfoDataList.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this VulhandleHistoryResponseInfoDataList.

        服务器名称

        :return: The host_name of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulhandleHistoryResponseInfoDataList.

        服务器名称

        :param host_name: The host_name of this VulhandleHistoryResponseInfoDataList.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulhandleHistoryResponseInfoDataList.

        服务器公网IP

        :return: The public_ip of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulhandleHistoryResponseInfoDataList.

        服务器公网IP

        :param public_ip: The public_ip of this VulhandleHistoryResponseInfoDataList.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulhandleHistoryResponseInfoDataList.

        服务器私网IP

        :return: The private_ip of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulhandleHistoryResponseInfoDataList.

        服务器私网IP

        :param private_ip: The private_ip of this VulhandleHistoryResponseInfoDataList.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def handle_time(self):
        r"""Gets the handle_time of this VulhandleHistoryResponseInfoDataList.

        处置时间

        :return: The handle_time of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._handle_time

    @handle_time.setter
    def handle_time(self, handle_time):
        r"""Sets the handle_time of this VulhandleHistoryResponseInfoDataList.

        处置时间

        :param handle_time: The handle_time of this VulhandleHistoryResponseInfoDataList.
        :type handle_time: str
        """
        self._handle_time = handle_time

    @property
    def status(self):
        r"""Gets the status of this VulhandleHistoryResponseInfoDataList.

        处置状态

        :return: The status of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulhandleHistoryResponseInfoDataList.

        处置状态

        :param status: The status of this VulhandleHistoryResponseInfoDataList.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this VulhandleHistoryResponseInfoDataList.

        失败原因

        :return: The failed_reason of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this VulhandleHistoryResponseInfoDataList.

        失败原因

        :param failed_reason: The failed_reason of this VulhandleHistoryResponseInfoDataList.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def description(self):
        r"""Gets the description of this VulhandleHistoryResponseInfoDataList.

        备注

        :return: The description of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VulhandleHistoryResponseInfoDataList.

        备注

        :param description: The description of this VulhandleHistoryResponseInfoDataList.
        :type description: str
        """
        self._description = description

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulhandleHistoryResponseInfoDataList.

        漏洞ID

        :return: The vul_id of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulhandleHistoryResponseInfoDataList.

        漏洞ID

        :param vul_id: The vul_id of this VulhandleHistoryResponseInfoDataList.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulhandleHistoryResponseInfoDataList.

        漏洞名称

        :return: The vul_name of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulhandleHistoryResponseInfoDataList.

        漏洞名称

        :param vul_name: The vul_name of this VulhandleHistoryResponseInfoDataList.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulhandleHistoryResponseInfoDataList.

        资产重要性

        :return: The asset_value of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulhandleHistoryResponseInfoDataList.

        资产重要性

        :param asset_value: The asset_value of this VulhandleHistoryResponseInfoDataList.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def cve_list(self):
        r"""Gets the cve_list of this VulhandleHistoryResponseInfoDataList.

        cve列表

        :return: The cve_list of this VulhandleHistoryResponseInfoDataList.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulCveInfo`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        r"""Sets the cve_list of this VulhandleHistoryResponseInfoDataList.

        cve列表

        :param cve_list: The cve_list of this VulhandleHistoryResponseInfoDataList.
        :type cve_list: list[:class:`huaweicloudsdkhss.v5.VulCveInfo`]
        """
        self._cve_list = cve_list

    @property
    def app_name(self):
        r"""Gets the app_name of this VulhandleHistoryResponseInfoDataList.

        软件名称

        :return: The app_name of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this VulhandleHistoryResponseInfoDataList.

        软件名称

        :param app_name: The app_name of this VulhandleHistoryResponseInfoDataList.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_path(self):
        r"""Gets the app_path of this VulhandleHistoryResponseInfoDataList.

        应用软件路径

        :return: The app_path of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this VulhandleHistoryResponseInfoDataList.

        应用软件路径

        :param app_path: The app_path of this VulhandleHistoryResponseInfoDataList.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def app_version(self):
        r"""Gets the app_version of this VulhandleHistoryResponseInfoDataList.

        软件版本

        :return: The app_version of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this VulhandleHistoryResponseInfoDataList.

        软件版本

        :param app_version: The app_version of this VulhandleHistoryResponseInfoDataList.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def handle_type(self):
        r"""Gets the handle_type of this VulhandleHistoryResponseInfoDataList.

        处置类型

        :return: The handle_type of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._handle_type

    @handle_type.setter
    def handle_type(self, handle_type):
        r"""Sets the handle_type of this VulhandleHistoryResponseInfoDataList.

        处置类型

        :param handle_type: The handle_type of this VulhandleHistoryResponseInfoDataList.
        :type handle_type: str
        """
        self._handle_type = handle_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this VulhandleHistoryResponseInfoDataList.

        集群ID

        :return: The cluster_id of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this VulhandleHistoryResponseInfoDataList.

        集群ID

        :param cluster_id: The cluster_id of this VulhandleHistoryResponseInfoDataList.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def container_name(self):
        r"""Gets the container_name of this VulhandleHistoryResponseInfoDataList.

        容器名称

        :return: The container_name of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this VulhandleHistoryResponseInfoDataList.

        容器名称

        :param container_name: The container_name of this VulhandleHistoryResponseInfoDataList.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this VulhandleHistoryResponseInfoDataList.

        容器ID

        :return: The container_id of this VulhandleHistoryResponseInfoDataList.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this VulhandleHistoryResponseInfoDataList.

        容器ID

        :param container_id: The container_id of this VulhandleHistoryResponseInfoDataList.
        :type container_id: str
        """
        self._container_id = container_id

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
        if not isinstance(other, VulhandleHistoryResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
