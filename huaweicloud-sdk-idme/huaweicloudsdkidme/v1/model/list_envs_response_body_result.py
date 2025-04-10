# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvsResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'region_id': 'str',
        'env_id': 'str',
        'env_name': 'str',
        'env_status': 'str',
        'env_app_link_status': 'str',
        'env_app_link_status_msg': 'str',
        'endpoint': 'str',
        'job_id': 'str',
        'env_conf_info': 'str',
        'app_id': 'str',
        'app_version': 'str',
        'app_name_en': 'str',
        'app_name_cn': 'str',
        'enabled': 'bool',
        'expire_time': 'int',
        'last_deploy_time': 'int',
        'deploy_user_id': 'str',
        'charging_mode': 'str',
        'create_time': 'int',
        'resource_id': 'str',
        'deployable': 'bool',
        'uninstallable': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'region_id': 'region_id',
        'env_id': 'env_id',
        'env_name': 'env_name',
        'env_status': 'env_status',
        'env_app_link_status': 'env_app_link_status',
        'env_app_link_status_msg': 'env_app_link_status_msg',
        'endpoint': 'endpoint',
        'job_id': 'job_id',
        'env_conf_info': 'env_conf_info',
        'app_id': 'app_id',
        'app_version': 'app_version',
        'app_name_en': 'app_name_en',
        'app_name_cn': 'app_name_cn',
        'enabled': 'enabled',
        'expire_time': 'expire_time',
        'last_deploy_time': 'last_deploy_time',
        'deploy_user_id': 'deploy_user_id',
        'charging_mode': 'charging_mode',
        'create_time': 'create_time',
        'resource_id': 'resource_id',
        'deployable': 'deployable',
        'uninstallable': 'uninstallable'
    }

    def __init__(self, project_id=None, region_id=None, env_id=None, env_name=None, env_status=None, env_app_link_status=None, env_app_link_status_msg=None, endpoint=None, job_id=None, env_conf_info=None, app_id=None, app_version=None, app_name_en=None, app_name_cn=None, enabled=None, expire_time=None, last_deploy_time=None, deploy_user_id=None, charging_mode=None, create_time=None, resource_id=None, deployable=None, uninstallable=None):
        r"""ListEnvsResponseBodyResult

        The model defined in huaweicloud sdk

        :param project_id: 项目ID。
        :type project_id: str
        :param region_id: 区域ID。
        :type region_id: str
        :param env_id: 运行服务的ID。
        :type env_id: str
        :param env_name: 运行服务的名称。
        :type env_name: str
        :param env_status: 运行服务的状态。
        :type env_status: str
        :param env_app_link_status: 运行服务与应用间的状态。
        :type env_app_link_status: str
        :param env_app_link_status_msg: 运行服务与应用间的状态信息。
        :type env_app_link_status_msg: str
        :param endpoint: 访问方式。
        :type endpoint: str
        :param job_id: 创建运行服务的jobId。
        :type job_id: str
        :param env_conf_info: 运行服务的配置信息。
        :type env_conf_info: str
        :param app_id: 部署的应用ID。
        :type app_id: str
        :param app_version: 部署的应用版本。
        :type app_version: str
        :param app_name_en: 部署应用的英文名称。
        :type app_name_en: str
        :param app_name_cn: 部署应用的中文名称。
        :type app_name_cn: str
        :param enabled: 应用是否可用。 - 0：被认为是false。 - 非0：被认为是true。
        :type enabled: bool
        :param expire_time: 运行服务的过期时间。
        :type expire_time: int
        :param last_deploy_time: 最后部署时间。
        :type last_deploy_time: int
        :param deploy_user_id: 上次部署应用的IAM用户ID。
        :type deploy_user_id: str
        :param charging_mode: 计费模式。
        :type charging_mode: str
        :param create_time: 运行服务的创建时间。
        :type create_time: int
        :param resource_id: 绑定主资源ID。
        :type resource_id: str
        :param deployable: 是否支持部署。
        :type deployable: bool
        :param uninstallable: 是否支持卸载。
        :type uninstallable: bool
        """
        
        

        self._project_id = None
        self._region_id = None
        self._env_id = None
        self._env_name = None
        self._env_status = None
        self._env_app_link_status = None
        self._env_app_link_status_msg = None
        self._endpoint = None
        self._job_id = None
        self._env_conf_info = None
        self._app_id = None
        self._app_version = None
        self._app_name_en = None
        self._app_name_cn = None
        self._enabled = None
        self._expire_time = None
        self._last_deploy_time = None
        self._deploy_user_id = None
        self._charging_mode = None
        self._create_time = None
        self._resource_id = None
        self._deployable = None
        self._uninstallable = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if region_id is not None:
            self.region_id = region_id
        if env_id is not None:
            self.env_id = env_id
        if env_name is not None:
            self.env_name = env_name
        if env_status is not None:
            self.env_status = env_status
        if env_app_link_status is not None:
            self.env_app_link_status = env_app_link_status
        if env_app_link_status_msg is not None:
            self.env_app_link_status_msg = env_app_link_status_msg
        if endpoint is not None:
            self.endpoint = endpoint
        if job_id is not None:
            self.job_id = job_id
        if env_conf_info is not None:
            self.env_conf_info = env_conf_info
        if app_id is not None:
            self.app_id = app_id
        if app_version is not None:
            self.app_version = app_version
        if app_name_en is not None:
            self.app_name_en = app_name_en
        if app_name_cn is not None:
            self.app_name_cn = app_name_cn
        if enabled is not None:
            self.enabled = enabled
        if expire_time is not None:
            self.expire_time = expire_time
        if last_deploy_time is not None:
            self.last_deploy_time = last_deploy_time
        if deploy_user_id is not None:
            self.deploy_user_id = deploy_user_id
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if create_time is not None:
            self.create_time = create_time
        if resource_id is not None:
            self.resource_id = resource_id
        if deployable is not None:
            self.deployable = deployable
        if uninstallable is not None:
            self.uninstallable = uninstallable

    @property
    def project_id(self):
        r"""Gets the project_id of this ListEnvsResponseBodyResult.

        项目ID。

        :return: The project_id of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListEnvsResponseBodyResult.

        项目ID。

        :param project_id: The project_id of this ListEnvsResponseBodyResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListEnvsResponseBodyResult.

        区域ID。

        :return: The region_id of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListEnvsResponseBodyResult.

        区域ID。

        :param region_id: The region_id of this ListEnvsResponseBodyResult.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def env_id(self):
        r"""Gets the env_id of this ListEnvsResponseBodyResult.

        运行服务的ID。

        :return: The env_id of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ListEnvsResponseBodyResult.

        运行服务的ID。

        :param env_id: The env_id of this ListEnvsResponseBodyResult.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def env_name(self):
        r"""Gets the env_name of this ListEnvsResponseBodyResult.

        运行服务的名称。

        :return: The env_name of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this ListEnvsResponseBodyResult.

        运行服务的名称。

        :param env_name: The env_name of this ListEnvsResponseBodyResult.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def env_status(self):
        r"""Gets the env_status of this ListEnvsResponseBodyResult.

        运行服务的状态。

        :return: The env_status of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._env_status

    @env_status.setter
    def env_status(self, env_status):
        r"""Sets the env_status of this ListEnvsResponseBodyResult.

        运行服务的状态。

        :param env_status: The env_status of this ListEnvsResponseBodyResult.
        :type env_status: str
        """
        self._env_status = env_status

    @property
    def env_app_link_status(self):
        r"""Gets the env_app_link_status of this ListEnvsResponseBodyResult.

        运行服务与应用间的状态。

        :return: The env_app_link_status of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._env_app_link_status

    @env_app_link_status.setter
    def env_app_link_status(self, env_app_link_status):
        r"""Sets the env_app_link_status of this ListEnvsResponseBodyResult.

        运行服务与应用间的状态。

        :param env_app_link_status: The env_app_link_status of this ListEnvsResponseBodyResult.
        :type env_app_link_status: str
        """
        self._env_app_link_status = env_app_link_status

    @property
    def env_app_link_status_msg(self):
        r"""Gets the env_app_link_status_msg of this ListEnvsResponseBodyResult.

        运行服务与应用间的状态信息。

        :return: The env_app_link_status_msg of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._env_app_link_status_msg

    @env_app_link_status_msg.setter
    def env_app_link_status_msg(self, env_app_link_status_msg):
        r"""Sets the env_app_link_status_msg of this ListEnvsResponseBodyResult.

        运行服务与应用间的状态信息。

        :param env_app_link_status_msg: The env_app_link_status_msg of this ListEnvsResponseBodyResult.
        :type env_app_link_status_msg: str
        """
        self._env_app_link_status_msg = env_app_link_status_msg

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ListEnvsResponseBodyResult.

        访问方式。

        :return: The endpoint of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ListEnvsResponseBodyResult.

        访问方式。

        :param endpoint: The endpoint of this ListEnvsResponseBodyResult.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def job_id(self):
        r"""Gets the job_id of this ListEnvsResponseBodyResult.

        创建运行服务的jobId。

        :return: The job_id of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListEnvsResponseBodyResult.

        创建运行服务的jobId。

        :param job_id: The job_id of this ListEnvsResponseBodyResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def env_conf_info(self):
        r"""Gets the env_conf_info of this ListEnvsResponseBodyResult.

        运行服务的配置信息。

        :return: The env_conf_info of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._env_conf_info

    @env_conf_info.setter
    def env_conf_info(self, env_conf_info):
        r"""Sets the env_conf_info of this ListEnvsResponseBodyResult.

        运行服务的配置信息。

        :param env_conf_info: The env_conf_info of this ListEnvsResponseBodyResult.
        :type env_conf_info: str
        """
        self._env_conf_info = env_conf_info

    @property
    def app_id(self):
        r"""Gets the app_id of this ListEnvsResponseBodyResult.

        部署的应用ID。

        :return: The app_id of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListEnvsResponseBodyResult.

        部署的应用ID。

        :param app_id: The app_id of this ListEnvsResponseBodyResult.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_version(self):
        r"""Gets the app_version of this ListEnvsResponseBodyResult.

        部署的应用版本。

        :return: The app_version of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this ListEnvsResponseBodyResult.

        部署的应用版本。

        :param app_version: The app_version of this ListEnvsResponseBodyResult.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def app_name_en(self):
        r"""Gets the app_name_en of this ListEnvsResponseBodyResult.

        部署应用的英文名称。

        :return: The app_name_en of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._app_name_en

    @app_name_en.setter
    def app_name_en(self, app_name_en):
        r"""Sets the app_name_en of this ListEnvsResponseBodyResult.

        部署应用的英文名称。

        :param app_name_en: The app_name_en of this ListEnvsResponseBodyResult.
        :type app_name_en: str
        """
        self._app_name_en = app_name_en

    @property
    def app_name_cn(self):
        r"""Gets the app_name_cn of this ListEnvsResponseBodyResult.

        部署应用的中文名称。

        :return: The app_name_cn of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._app_name_cn

    @app_name_cn.setter
    def app_name_cn(self, app_name_cn):
        r"""Sets the app_name_cn of this ListEnvsResponseBodyResult.

        部署应用的中文名称。

        :param app_name_cn: The app_name_cn of this ListEnvsResponseBodyResult.
        :type app_name_cn: str
        """
        self._app_name_cn = app_name_cn

    @property
    def enabled(self):
        r"""Gets the enabled of this ListEnvsResponseBodyResult.

        应用是否可用。 - 0：被认为是false。 - 非0：被认为是true。

        :return: The enabled of this ListEnvsResponseBodyResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ListEnvsResponseBodyResult.

        应用是否可用。 - 0：被认为是false。 - 非0：被认为是true。

        :param enabled: The enabled of this ListEnvsResponseBodyResult.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ListEnvsResponseBodyResult.

        运行服务的过期时间。

        :return: The expire_time of this ListEnvsResponseBodyResult.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ListEnvsResponseBodyResult.

        运行服务的过期时间。

        :param expire_time: The expire_time of this ListEnvsResponseBodyResult.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def last_deploy_time(self):
        r"""Gets the last_deploy_time of this ListEnvsResponseBodyResult.

        最后部署时间。

        :return: The last_deploy_time of this ListEnvsResponseBodyResult.
        :rtype: int
        """
        return self._last_deploy_time

    @last_deploy_time.setter
    def last_deploy_time(self, last_deploy_time):
        r"""Sets the last_deploy_time of this ListEnvsResponseBodyResult.

        最后部署时间。

        :param last_deploy_time: The last_deploy_time of this ListEnvsResponseBodyResult.
        :type last_deploy_time: int
        """
        self._last_deploy_time = last_deploy_time

    @property
    def deploy_user_id(self):
        r"""Gets the deploy_user_id of this ListEnvsResponseBodyResult.

        上次部署应用的IAM用户ID。

        :return: The deploy_user_id of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._deploy_user_id

    @deploy_user_id.setter
    def deploy_user_id(self, deploy_user_id):
        r"""Sets the deploy_user_id of this ListEnvsResponseBodyResult.

        上次部署应用的IAM用户ID。

        :param deploy_user_id: The deploy_user_id of this ListEnvsResponseBodyResult.
        :type deploy_user_id: str
        """
        self._deploy_user_id = deploy_user_id

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListEnvsResponseBodyResult.

        计费模式。

        :return: The charging_mode of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListEnvsResponseBodyResult.

        计费模式。

        :param charging_mode: The charging_mode of this ListEnvsResponseBodyResult.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def create_time(self):
        r"""Gets the create_time of this ListEnvsResponseBodyResult.

        运行服务的创建时间。

        :return: The create_time of this ListEnvsResponseBodyResult.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListEnvsResponseBodyResult.

        运行服务的创建时间。

        :param create_time: The create_time of this ListEnvsResponseBodyResult.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListEnvsResponseBodyResult.

        绑定主资源ID。

        :return: The resource_id of this ListEnvsResponseBodyResult.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListEnvsResponseBodyResult.

        绑定主资源ID。

        :param resource_id: The resource_id of this ListEnvsResponseBodyResult.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def deployable(self):
        r"""Gets the deployable of this ListEnvsResponseBodyResult.

        是否支持部署。

        :return: The deployable of this ListEnvsResponseBodyResult.
        :rtype: bool
        """
        return self._deployable

    @deployable.setter
    def deployable(self, deployable):
        r"""Sets the deployable of this ListEnvsResponseBodyResult.

        是否支持部署。

        :param deployable: The deployable of this ListEnvsResponseBodyResult.
        :type deployable: bool
        """
        self._deployable = deployable

    @property
    def uninstallable(self):
        r"""Gets the uninstallable of this ListEnvsResponseBodyResult.

        是否支持卸载。

        :return: The uninstallable of this ListEnvsResponseBodyResult.
        :rtype: bool
        """
        return self._uninstallable

    @uninstallable.setter
    def uninstallable(self, uninstallable):
        r"""Sets the uninstallable of this ListEnvsResponseBodyResult.

        是否支持卸载。

        :param uninstallable: The uninstallable of this ListEnvsResponseBodyResult.
        :type uninstallable: bool
        """
        self._uninstallable = uninstallable

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
        if not isinstance(other, ListEnvsResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
