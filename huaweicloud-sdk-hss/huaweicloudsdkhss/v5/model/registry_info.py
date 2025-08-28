# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegistryInfo:

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
        'registry_name': 'str',
        'registry_type': 'str',
        'api_version': 'str',
        'protocol': 'str',
        'registry_addr': 'str',
        'registry_username': 'str',
        'namespace': 'str',
        'connect_cluster_id': 'str',
        'get_scan_image_channel': 'str',
        'status': 'str',
        'fail_reason': 'str',
        'images_num': 'int',
        'latest_sync_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'registry_name': 'registry_name',
        'registry_type': 'registry_type',
        'api_version': 'api_version',
        'protocol': 'protocol',
        'registry_addr': 'registry_addr',
        'registry_username': 'registry_username',
        'namespace': 'namespace',
        'connect_cluster_id': 'connect_cluster_id',
        'get_scan_image_channel': 'get_scan_image_channel',
        'status': 'status',
        'fail_reason': 'fail_reason',
        'images_num': 'images_num',
        'latest_sync_time': 'latest_sync_time'
    }

    def __init__(self, id=None, registry_name=None, registry_type=None, api_version=None, protocol=None, registry_addr=None, registry_username=None, namespace=None, connect_cluster_id=None, get_scan_image_channel=None, status=None, fail_reason=None, images_num=None, latest_sync_time=None):
        r"""RegistryInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 镜像仓ID **取值范围**: 字符长度1-64位 
        :type id: str
        :param registry_name: **参数解释**: 仓库名称 **取值范围**: 字符长度1-128位 
        :type registry_name: str
        :param registry_type: **参数解释**: 镜像仓类型 **取值范围**: - Harbor harbor仓库 - Jfrog jfrog仓库 - SwrPrivate swr私有 - SwrShared  swr共享 - SwrEnterprise  swr企业 - Other  其他仓库 
        :type registry_type: str
        :param api_version: **参数解释**： 镜像仓接口版本 **取值范围**：   - V1：V1版本   - V2：V2版本 
        :type api_version: str
        :param protocol: **参数解释**： 协议类型 **取值范围**：   - http：http协议   - https：https协议 
        :type protocol: str
        :param registry_addr: **参数解释**： 镜像仓地址 **取值范围**： 字符长度1-256位 
        :type registry_addr: str
        :param registry_username: **参数解释**： 用于登录镜像仓的用户名。 **取值范围**： 字符长度1-128位 
        :type registry_username: str
        :param namespace: **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。get_scan_image_channel为Other时返回此值。 **取值范围**： 字符长度1-128位 
        :type namespace: str
        :param connect_cluster_id: **参数解释**： 承载集群id **取值范围**： 字符长度1-64位 
        :type connect_cluster_id: str
        :param get_scan_image_channel: **参数解释**： 获取扫描组件的方式 **取值范围**： - Swr：访问swr获取扫描组件 - Other：手动上传扫描组件到承载集群。 
        :type get_scan_image_channel: str
        :param status: **参数解释**： 接入状态 **取值范围**： - success：接入成功 - fail：接入异常 - accessing：接入中 
        :type status: str
        :param fail_reason: **参数解释**: 失败原因 **取值范围**: - CREATE_JOB_FAILED：集群接入状态异常，请检查集群接入状态。 - REQUEST_API_ERROR：网络不通，访问镜像仓失败。请检查承载集群是否能正常访问镜像仓 ，或前往三方镜像仓页面重新接入。 - SERVER_ERROR：系统内部错误，请稍后重试。 
        :type fail_reason: str
        :param images_num: **参数解释**： 镜像数量 **取值范围**： 0-20000 
        :type images_num: int
        :param latest_sync_time: **参数解释**： 最近同步时间，时间单位 毫秒（ms） **取值范围**： 0-9223372036854775807 
        :type latest_sync_time: int
        """
        
        

        self._id = None
        self._registry_name = None
        self._registry_type = None
        self._api_version = None
        self._protocol = None
        self._registry_addr = None
        self._registry_username = None
        self._namespace = None
        self._connect_cluster_id = None
        self._get_scan_image_channel = None
        self._status = None
        self._fail_reason = None
        self._images_num = None
        self._latest_sync_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if registry_name is not None:
            self.registry_name = registry_name
        if registry_type is not None:
            self.registry_type = registry_type
        if api_version is not None:
            self.api_version = api_version
        if protocol is not None:
            self.protocol = protocol
        if registry_addr is not None:
            self.registry_addr = registry_addr
        if registry_username is not None:
            self.registry_username = registry_username
        if namespace is not None:
            self.namespace = namespace
        if connect_cluster_id is not None:
            self.connect_cluster_id = connect_cluster_id
        if get_scan_image_channel is not None:
            self.get_scan_image_channel = get_scan_image_channel
        if status is not None:
            self.status = status
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if images_num is not None:
            self.images_num = images_num
        if latest_sync_time is not None:
            self.latest_sync_time = latest_sync_time

    @property
    def id(self):
        r"""Gets the id of this RegistryInfo.

        **参数解释**: 镜像仓ID **取值范围**: 字符长度1-64位 

        :return: The id of this RegistryInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RegistryInfo.

        **参数解释**: 镜像仓ID **取值范围**: 字符长度1-64位 

        :param id: The id of this RegistryInfo.
        :type id: str
        """
        self._id = id

    @property
    def registry_name(self):
        r"""Gets the registry_name of this RegistryInfo.

        **参数解释**: 仓库名称 **取值范围**: 字符长度1-128位 

        :return: The registry_name of this RegistryInfo.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this RegistryInfo.

        **参数解释**: 仓库名称 **取值范围**: 字符长度1-128位 

        :param registry_name: The registry_name of this RegistryInfo.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def registry_type(self):
        r"""Gets the registry_type of this RegistryInfo.

        **参数解释**: 镜像仓类型 **取值范围**: - Harbor harbor仓库 - Jfrog jfrog仓库 - SwrPrivate swr私有 - SwrShared  swr共享 - SwrEnterprise  swr企业 - Other  其他仓库 

        :return: The registry_type of this RegistryInfo.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this RegistryInfo.

        **参数解释**: 镜像仓类型 **取值范围**: - Harbor harbor仓库 - Jfrog jfrog仓库 - SwrPrivate swr私有 - SwrShared  swr共享 - SwrEnterprise  swr企业 - Other  其他仓库 

        :param registry_type: The registry_type of this RegistryInfo.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def api_version(self):
        r"""Gets the api_version of this RegistryInfo.

        **参数解释**： 镜像仓接口版本 **取值范围**：   - V1：V1版本   - V2：V2版本 

        :return: The api_version of this RegistryInfo.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this RegistryInfo.

        **参数解释**： 镜像仓接口版本 **取值范围**：   - V1：V1版本   - V2：V2版本 

        :param api_version: The api_version of this RegistryInfo.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def protocol(self):
        r"""Gets the protocol of this RegistryInfo.

        **参数解释**： 协议类型 **取值范围**：   - http：http协议   - https：https协议 

        :return: The protocol of this RegistryInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this RegistryInfo.

        **参数解释**： 协议类型 **取值范围**：   - http：http协议   - https：https协议 

        :param protocol: The protocol of this RegistryInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def registry_addr(self):
        r"""Gets the registry_addr of this RegistryInfo.

        **参数解释**： 镜像仓地址 **取值范围**： 字符长度1-256位 

        :return: The registry_addr of this RegistryInfo.
        :rtype: str
        """
        return self._registry_addr

    @registry_addr.setter
    def registry_addr(self, registry_addr):
        r"""Sets the registry_addr of this RegistryInfo.

        **参数解释**： 镜像仓地址 **取值范围**： 字符长度1-256位 

        :param registry_addr: The registry_addr of this RegistryInfo.
        :type registry_addr: str
        """
        self._registry_addr = registry_addr

    @property
    def registry_username(self):
        r"""Gets the registry_username of this RegistryInfo.

        **参数解释**： 用于登录镜像仓的用户名。 **取值范围**： 字符长度1-128位 

        :return: The registry_username of this RegistryInfo.
        :rtype: str
        """
        return self._registry_username

    @registry_username.setter
    def registry_username(self, registry_username):
        r"""Sets the registry_username of this RegistryInfo.

        **参数解释**： 用于登录镜像仓的用户名。 **取值范围**： 字符长度1-128位 

        :param registry_username: The registry_username of this RegistryInfo.
        :type registry_username: str
        """
        self._registry_username = registry_username

    @property
    def namespace(self):
        r"""Gets the namespace of this RegistryInfo.

        **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。get_scan_image_channel为Other时返回此值。 **取值范围**： 字符长度1-128位 

        :return: The namespace of this RegistryInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this RegistryInfo.

        **参数解释**： 镜像仓项目,用来指定扫描组件要上传到的镜像仓目录。get_scan_image_channel为Other时返回此值。 **取值范围**： 字符长度1-128位 

        :param namespace: The namespace of this RegistryInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def connect_cluster_id(self):
        r"""Gets the connect_cluster_id of this RegistryInfo.

        **参数解释**： 承载集群id **取值范围**： 字符长度1-64位 

        :return: The connect_cluster_id of this RegistryInfo.
        :rtype: str
        """
        return self._connect_cluster_id

    @connect_cluster_id.setter
    def connect_cluster_id(self, connect_cluster_id):
        r"""Sets the connect_cluster_id of this RegistryInfo.

        **参数解释**： 承载集群id **取值范围**： 字符长度1-64位 

        :param connect_cluster_id: The connect_cluster_id of this RegistryInfo.
        :type connect_cluster_id: str
        """
        self._connect_cluster_id = connect_cluster_id

    @property
    def get_scan_image_channel(self):
        r"""Gets the get_scan_image_channel of this RegistryInfo.

        **参数解释**： 获取扫描组件的方式 **取值范围**： - Swr：访问swr获取扫描组件 - Other：手动上传扫描组件到承载集群。 

        :return: The get_scan_image_channel of this RegistryInfo.
        :rtype: str
        """
        return self._get_scan_image_channel

    @get_scan_image_channel.setter
    def get_scan_image_channel(self, get_scan_image_channel):
        r"""Sets the get_scan_image_channel of this RegistryInfo.

        **参数解释**： 获取扫描组件的方式 **取值范围**： - Swr：访问swr获取扫描组件 - Other：手动上传扫描组件到承载集群。 

        :param get_scan_image_channel: The get_scan_image_channel of this RegistryInfo.
        :type get_scan_image_channel: str
        """
        self._get_scan_image_channel = get_scan_image_channel

    @property
    def status(self):
        r"""Gets the status of this RegistryInfo.

        **参数解释**： 接入状态 **取值范围**： - success：接入成功 - fail：接入异常 - accessing：接入中 

        :return: The status of this RegistryInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RegistryInfo.

        **参数解释**： 接入状态 **取值范围**： - success：接入成功 - fail：接入异常 - accessing：接入中 

        :param status: The status of this RegistryInfo.
        :type status: str
        """
        self._status = status

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this RegistryInfo.

        **参数解释**: 失败原因 **取值范围**: - CREATE_JOB_FAILED：集群接入状态异常，请检查集群接入状态。 - REQUEST_API_ERROR：网络不通，访问镜像仓失败。请检查承载集群是否能正常访问镜像仓 ，或前往三方镜像仓页面重新接入。 - SERVER_ERROR：系统内部错误，请稍后重试。 

        :return: The fail_reason of this RegistryInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this RegistryInfo.

        **参数解释**: 失败原因 **取值范围**: - CREATE_JOB_FAILED：集群接入状态异常，请检查集群接入状态。 - REQUEST_API_ERROR：网络不通，访问镜像仓失败。请检查承载集群是否能正常访问镜像仓 ，或前往三方镜像仓页面重新接入。 - SERVER_ERROR：系统内部错误，请稍后重试。 

        :param fail_reason: The fail_reason of this RegistryInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def images_num(self):
        r"""Gets the images_num of this RegistryInfo.

        **参数解释**： 镜像数量 **取值范围**： 0-20000 

        :return: The images_num of this RegistryInfo.
        :rtype: int
        """
        return self._images_num

    @images_num.setter
    def images_num(self, images_num):
        r"""Sets the images_num of this RegistryInfo.

        **参数解释**： 镜像数量 **取值范围**： 0-20000 

        :param images_num: The images_num of this RegistryInfo.
        :type images_num: int
        """
        self._images_num = images_num

    @property
    def latest_sync_time(self):
        r"""Gets the latest_sync_time of this RegistryInfo.

        **参数解释**： 最近同步时间，时间单位 毫秒（ms） **取值范围**： 0-9223372036854775807 

        :return: The latest_sync_time of this RegistryInfo.
        :rtype: int
        """
        return self._latest_sync_time

    @latest_sync_time.setter
    def latest_sync_time(self, latest_sync_time):
        r"""Sets the latest_sync_time of this RegistryInfo.

        **参数解释**： 最近同步时间，时间单位 毫秒（ms） **取值范围**： 0-9223372036854775807 

        :param latest_sync_time: The latest_sync_time of this RegistryInfo.
        :type latest_sync_time: int
        """
        self._latest_sync_time = latest_sync_time

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
        if not isinstance(other, RegistryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
