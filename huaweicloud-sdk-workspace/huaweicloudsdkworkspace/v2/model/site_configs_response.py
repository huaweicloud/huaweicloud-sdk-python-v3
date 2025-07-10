# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteConfigsResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'site_id': 'str',
        'site_type': 'str',
        'site_name': 'str',
        'status': 'str',
        'access_status': 'str',
        'config_status': 'str',
        'infrastructure_security_group': 'SecurityGroup',
        'desktop_security_group': 'SecurityGroup',
        'availability_zones': 'list[str]',
        'job_id': 'str',
        'progress': 'str',
        'fail_code': 'int',
        'fail_reason': 'str',
        'network_config': 'NetworkConfig',
        'access_config': 'AccessConfig',
        'closable': 'bool'
    }

    attribute_map = {
        'site_id': 'site_id',
        'site_type': 'site_type',
        'site_name': 'site_name',
        'status': 'status',
        'access_status': 'access_status',
        'config_status': 'config_status',
        'infrastructure_security_group': 'infrastructure_security_group',
        'desktop_security_group': 'desktop_security_group',
        'availability_zones': 'availability_zones',
        'job_id': 'job_id',
        'progress': 'progress',
        'fail_code': 'fail_code',
        'fail_reason': 'fail_reason',
        'network_config': 'network_config',
        'access_config': 'access_config',
        'closable': 'closable'
    }

    def __init__(self, site_id=None, site_type=None, site_name=None, status=None, access_status=None, config_status=None, infrastructure_security_group=None, desktop_security_group=None, availability_zones=None, job_id=None, progress=None, fail_code=None, fail_reason=None, network_config=None, access_config=None, closable=None):
        r"""SiteConfigsResponse

        The model defined in huaweicloud sdk

        :param site_id: 站点id。
        :type site_id: str
        :param site_type: 配置状态。 - CENTER： 中心初始化 - IES： 边缘初始化
        :type site_type: str
        :param site_name: 站点名称。
        :type site_name: str
        :param status: 云办公服务的状态。 - PREPARING：准备初始化服务 - SUBSCRIBING：初始化服务中 - SUBSCRIBED：已初始化服务 - SUBSCRIPTION_FAILED：初始化服务失败 - DEREGISTERING：清理资源中 - DEREGISTRATION_FAILED：清理资源失败 - RECYCLING：清理资源中。 - RECYCLED：清理资源成功。 - RECYCLE_FAILED：清理资源失败。 - CLOSED：已销户未初始化服务
        :type status: str
        :param access_status: 互联网和专线切换任务的状态。 - init： 初始化 - 开通服务后的初始状态 - available： 可用 - 执行过任务且成功后恢复的正常状态 - internetOpening： 开启中 - 开通互联网接入开启中 - dedicatedOpening： 开启中 - 开通专线接入开启中 - internetOpenFailed： 开启失败 - 开通互联网接入开启失败 - dedicatedOpenFailed： 开启失败 - 开通专线接入开启失败 - openSuccess： 开启成功 - 开通互联网接入成功 - internetClosing： 关闭中 - 关闭互联网接入关闭中 - dedicatedClosing： 关闭中 - 关闭专线接入关闭中 - internetCloseFailed： 关闭失败 - 关闭互联网接入方式失败 - dedicatedCloseFailed： 关闭失败 - 关闭专线接入方式失败 - closeSuccess： 关闭成功 - 关闭接入方式成功 - internetAccessPortModifying： 互联网接入端口修改中 - internetAccessPortModifyFailed: 端口修改失败
        :type access_status: str
        :param config_status: 配置状态。 - \&quot;0\&quot;： 开通服务成功，且对接AD成功 - \&quot;1\&quot;： 开通服务成功，但AD配置失败 - \&quot;2\&quot;： 开通服务成功，但AD配置失败后存在其他错误 - \&quot;3\&quot;： 开通服务成功，AD未开启对接
        :type config_status: str
        :param infrastructure_security_group: 
        :type infrastructure_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        :param desktop_security_group: 
        :type desktop_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        :param availability_zones: 开通服务资源使用的可用分区。
        :type availability_zones: list[str]
        :param job_id: 开通服务或取消服务的任务ID。
        :type job_id: str
        :param progress: 初始化服务或清理资源的进度，格式为100%。
        :type progress: str
        :param fail_code: 失败错误码。
        :type fail_code: int
        :param fail_reason: 失败原因。
        :type fail_reason: str
        :param network_config: 
        :type network_config: :class:`huaweicloudsdkworkspace.v2.NetworkConfig`
        :param access_config: 
        :type access_config: :class:`huaweicloudsdkworkspace.v2.AccessConfig`
        :param closable: 是否可以取消服务。
        :type closable: bool
        """
        
        

        self._site_id = None
        self._site_type = None
        self._site_name = None
        self._status = None
        self._access_status = None
        self._config_status = None
        self._infrastructure_security_group = None
        self._desktop_security_group = None
        self._availability_zones = None
        self._job_id = None
        self._progress = None
        self._fail_code = None
        self._fail_reason = None
        self._network_config = None
        self._access_config = None
        self._closable = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if site_type is not None:
            self.site_type = site_type
        if site_name is not None:
            self.site_name = site_name
        if status is not None:
            self.status = status
        if access_status is not None:
            self.access_status = access_status
        if config_status is not None:
            self.config_status = config_status
        if infrastructure_security_group is not None:
            self.infrastructure_security_group = infrastructure_security_group
        if desktop_security_group is not None:
            self.desktop_security_group = desktop_security_group
        if availability_zones is not None:
            self.availability_zones = availability_zones
        if job_id is not None:
            self.job_id = job_id
        if progress is not None:
            self.progress = progress
        if fail_code is not None:
            self.fail_code = fail_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if network_config is not None:
            self.network_config = network_config
        if access_config is not None:
            self.access_config = access_config
        if closable is not None:
            self.closable = closable

    @property
    def site_id(self):
        r"""Gets the site_id of this SiteConfigsResponse.

        站点id。

        :return: The site_id of this SiteConfigsResponse.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        r"""Sets the site_id of this SiteConfigsResponse.

        站点id。

        :param site_id: The site_id of this SiteConfigsResponse.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def site_type(self):
        r"""Gets the site_type of this SiteConfigsResponse.

        配置状态。 - CENTER： 中心初始化 - IES： 边缘初始化

        :return: The site_type of this SiteConfigsResponse.
        :rtype: str
        """
        return self._site_type

    @site_type.setter
    def site_type(self, site_type):
        r"""Sets the site_type of this SiteConfigsResponse.

        配置状态。 - CENTER： 中心初始化 - IES： 边缘初始化

        :param site_type: The site_type of this SiteConfigsResponse.
        :type site_type: str
        """
        self._site_type = site_type

    @property
    def site_name(self):
        r"""Gets the site_name of this SiteConfigsResponse.

        站点名称。

        :return: The site_name of this SiteConfigsResponse.
        :rtype: str
        """
        return self._site_name

    @site_name.setter
    def site_name(self, site_name):
        r"""Sets the site_name of this SiteConfigsResponse.

        站点名称。

        :param site_name: The site_name of this SiteConfigsResponse.
        :type site_name: str
        """
        self._site_name = site_name

    @property
    def status(self):
        r"""Gets the status of this SiteConfigsResponse.

        云办公服务的状态。 - PREPARING：准备初始化服务 - SUBSCRIBING：初始化服务中 - SUBSCRIBED：已初始化服务 - SUBSCRIPTION_FAILED：初始化服务失败 - DEREGISTERING：清理资源中 - DEREGISTRATION_FAILED：清理资源失败 - RECYCLING：清理资源中。 - RECYCLED：清理资源成功。 - RECYCLE_FAILED：清理资源失败。 - CLOSED：已销户未初始化服务

        :return: The status of this SiteConfigsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SiteConfigsResponse.

        云办公服务的状态。 - PREPARING：准备初始化服务 - SUBSCRIBING：初始化服务中 - SUBSCRIBED：已初始化服务 - SUBSCRIPTION_FAILED：初始化服务失败 - DEREGISTERING：清理资源中 - DEREGISTRATION_FAILED：清理资源失败 - RECYCLING：清理资源中。 - RECYCLED：清理资源成功。 - RECYCLE_FAILED：清理资源失败。 - CLOSED：已销户未初始化服务

        :param status: The status of this SiteConfigsResponse.
        :type status: str
        """
        self._status = status

    @property
    def access_status(self):
        r"""Gets the access_status of this SiteConfigsResponse.

        互联网和专线切换任务的状态。 - init： 初始化 - 开通服务后的初始状态 - available： 可用 - 执行过任务且成功后恢复的正常状态 - internetOpening： 开启中 - 开通互联网接入开启中 - dedicatedOpening： 开启中 - 开通专线接入开启中 - internetOpenFailed： 开启失败 - 开通互联网接入开启失败 - dedicatedOpenFailed： 开启失败 - 开通专线接入开启失败 - openSuccess： 开启成功 - 开通互联网接入成功 - internetClosing： 关闭中 - 关闭互联网接入关闭中 - dedicatedClosing： 关闭中 - 关闭专线接入关闭中 - internetCloseFailed： 关闭失败 - 关闭互联网接入方式失败 - dedicatedCloseFailed： 关闭失败 - 关闭专线接入方式失败 - closeSuccess： 关闭成功 - 关闭接入方式成功 - internetAccessPortModifying： 互联网接入端口修改中 - internetAccessPortModifyFailed: 端口修改失败

        :return: The access_status of this SiteConfigsResponse.
        :rtype: str
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this SiteConfigsResponse.

        互联网和专线切换任务的状态。 - init： 初始化 - 开通服务后的初始状态 - available： 可用 - 执行过任务且成功后恢复的正常状态 - internetOpening： 开启中 - 开通互联网接入开启中 - dedicatedOpening： 开启中 - 开通专线接入开启中 - internetOpenFailed： 开启失败 - 开通互联网接入开启失败 - dedicatedOpenFailed： 开启失败 - 开通专线接入开启失败 - openSuccess： 开启成功 - 开通互联网接入成功 - internetClosing： 关闭中 - 关闭互联网接入关闭中 - dedicatedClosing： 关闭中 - 关闭专线接入关闭中 - internetCloseFailed： 关闭失败 - 关闭互联网接入方式失败 - dedicatedCloseFailed： 关闭失败 - 关闭专线接入方式失败 - closeSuccess： 关闭成功 - 关闭接入方式成功 - internetAccessPortModifying： 互联网接入端口修改中 - internetAccessPortModifyFailed: 端口修改失败

        :param access_status: The access_status of this SiteConfigsResponse.
        :type access_status: str
        """
        self._access_status = access_status

    @property
    def config_status(self):
        r"""Gets the config_status of this SiteConfigsResponse.

        配置状态。 - \"0\"： 开通服务成功，且对接AD成功 - \"1\"： 开通服务成功，但AD配置失败 - \"2\"： 开通服务成功，但AD配置失败后存在其他错误 - \"3\"： 开通服务成功，AD未开启对接

        :return: The config_status of this SiteConfigsResponse.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this SiteConfigsResponse.

        配置状态。 - \"0\"： 开通服务成功，且对接AD成功 - \"1\"： 开通服务成功，但AD配置失败 - \"2\"： 开通服务成功，但AD配置失败后存在其他错误 - \"3\"： 开通服务成功，AD未开启对接

        :param config_status: The config_status of this SiteConfigsResponse.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def infrastructure_security_group(self):
        r"""Gets the infrastructure_security_group of this SiteConfigsResponse.

        :return: The infrastructure_security_group of this SiteConfigsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        return self._infrastructure_security_group

    @infrastructure_security_group.setter
    def infrastructure_security_group(self, infrastructure_security_group):
        r"""Sets the infrastructure_security_group of this SiteConfigsResponse.

        :param infrastructure_security_group: The infrastructure_security_group of this SiteConfigsResponse.
        :type infrastructure_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        self._infrastructure_security_group = infrastructure_security_group

    @property
    def desktop_security_group(self):
        r"""Gets the desktop_security_group of this SiteConfigsResponse.

        :return: The desktop_security_group of this SiteConfigsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        return self._desktop_security_group

    @desktop_security_group.setter
    def desktop_security_group(self, desktop_security_group):
        r"""Sets the desktop_security_group of this SiteConfigsResponse.

        :param desktop_security_group: The desktop_security_group of this SiteConfigsResponse.
        :type desktop_security_group: :class:`huaweicloudsdkworkspace.v2.SecurityGroup`
        """
        self._desktop_security_group = desktop_security_group

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this SiteConfigsResponse.

        开通服务资源使用的可用分区。

        :return: The availability_zones of this SiteConfigsResponse.
        :rtype: list[str]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this SiteConfigsResponse.

        开通服务资源使用的可用分区。

        :param availability_zones: The availability_zones of this SiteConfigsResponse.
        :type availability_zones: list[str]
        """
        self._availability_zones = availability_zones

    @property
    def job_id(self):
        r"""Gets the job_id of this SiteConfigsResponse.

        开通服务或取消服务的任务ID。

        :return: The job_id of this SiteConfigsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SiteConfigsResponse.

        开通服务或取消服务的任务ID。

        :param job_id: The job_id of this SiteConfigsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def progress(self):
        r"""Gets the progress of this SiteConfigsResponse.

        初始化服务或清理资源的进度，格式为100%。

        :return: The progress of this SiteConfigsResponse.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this SiteConfigsResponse.

        初始化服务或清理资源的进度，格式为100%。

        :param progress: The progress of this SiteConfigsResponse.
        :type progress: str
        """
        self._progress = progress

    @property
    def fail_code(self):
        r"""Gets the fail_code of this SiteConfigsResponse.

        失败错误码。

        :return: The fail_code of this SiteConfigsResponse.
        :rtype: int
        """
        return self._fail_code

    @fail_code.setter
    def fail_code(self, fail_code):
        r"""Sets the fail_code of this SiteConfigsResponse.

        失败错误码。

        :param fail_code: The fail_code of this SiteConfigsResponse.
        :type fail_code: int
        """
        self._fail_code = fail_code

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this SiteConfigsResponse.

        失败原因。

        :return: The fail_reason of this SiteConfigsResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this SiteConfigsResponse.

        失败原因。

        :param fail_reason: The fail_reason of this SiteConfigsResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def network_config(self):
        r"""Gets the network_config of this SiteConfigsResponse.

        :return: The network_config of this SiteConfigsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.NetworkConfig`
        """
        return self._network_config

    @network_config.setter
    def network_config(self, network_config):
        r"""Sets the network_config of this SiteConfigsResponse.

        :param network_config: The network_config of this SiteConfigsResponse.
        :type network_config: :class:`huaweicloudsdkworkspace.v2.NetworkConfig`
        """
        self._network_config = network_config

    @property
    def access_config(self):
        r"""Gets the access_config of this SiteConfigsResponse.

        :return: The access_config of this SiteConfigsResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.AccessConfig`
        """
        return self._access_config

    @access_config.setter
    def access_config(self, access_config):
        r"""Sets the access_config of this SiteConfigsResponse.

        :param access_config: The access_config of this SiteConfigsResponse.
        :type access_config: :class:`huaweicloudsdkworkspace.v2.AccessConfig`
        """
        self._access_config = access_config

    @property
    def closable(self):
        r"""Gets the closable of this SiteConfigsResponse.

        是否可以取消服务。

        :return: The closable of this SiteConfigsResponse.
        :rtype: bool
        """
        return self._closable

    @closable.setter
    def closable(self, closable):
        r"""Sets the closable of this SiteConfigsResponse.

        是否可以取消服务。

        :param closable: The closable of this SiteConfigsResponse.
        :type closable: bool
        """
        self._closable = closable

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
        if not isinstance(other, SiteConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
