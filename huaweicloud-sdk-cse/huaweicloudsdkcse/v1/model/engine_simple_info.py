# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineSimpleInfo:

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
        'name': 'str',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'type': 'str',
        'description': 'str',
        'flavor': 'str',
        'payment': 'str',
        'auth_type': 'str',
        'status': 'str',
        'external_address': 'str',
        'service_endpoint': 'dict(str, EntrypointItem)',
        'public_address': 'str',
        'public_service_endpoint': 'dict(str, EntrypointItem)',
        'total_instance': 'int',
        'used_instance': 'int',
        'available_instance': 'int',
        'version': 'str',
        'latest_version': 'str',
        'create_time': 'int',
        'due_to': 'int',
        'latest_job_id': 'int',
        'engine_additional_actions': 'list[str]',
        'spec_type': 'str',
        'reference': 'EngineReference'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'enterprise_project_id': 'enterpriseProjectId',
        'enterprise_project_name': 'enterpriseProjectName',
        'type': 'type',
        'description': 'description',
        'flavor': 'flavor',
        'payment': 'payment',
        'auth_type': 'authType',
        'status': 'status',
        'external_address': 'externalAddress',
        'service_endpoint': 'serviceEndpoint',
        'public_address': 'publicAddress',
        'public_service_endpoint': 'publicServiceEndpoint',
        'total_instance': 'totalInstance',
        'used_instance': 'usedInstance',
        'available_instance': 'availableInstance',
        'version': 'version',
        'latest_version': 'latestVersion',
        'create_time': 'createTime',
        'due_to': 'dueTo',
        'latest_job_id': 'latestJobId',
        'engine_additional_actions': 'engineAdditionalActions',
        'spec_type': 'specType',
        'reference': 'reference'
    }

    def __init__(self, id=None, name=None, enterprise_project_id=None, enterprise_project_name=None, type=None, description=None, flavor=None, payment=None, auth_type=None, status=None, external_address=None, service_endpoint=None, public_address=None, public_service_endpoint=None, total_instance=None, used_instance=None, available_instance=None, version=None, latest_version=None, create_time=None, due_to=None, latest_job_id=None, engine_additional_actions=None, spec_type=None, reference=None):
        r"""EngineSimpleInfo

        The model defined in huaweicloud sdk

        :param id: 微服务引擎的ID
        :type id: str
        :param name: 引擎的名称
        :type name: str
        :param enterprise_project_id: 微服务引擎所属企业项目ID
        :type enterprise_project_id: str
        :param enterprise_project_name: 微服务引擎所属企业项目名称
        :type enterprise_project_name: str
        :param type: 微服务引擎的类型，CSE为专享版引擎，CSE_Share表示为专业版引擎
        :type type: str
        :param description: 微服务引擎的描述
        :type description: str
        :param flavor: 微服务引擎的规格
        :type flavor: str
        :param payment: 微服务引擎的计费方式，0表示包周期，1表示按需，2表示免费
        :type payment: str
        :param auth_type: 微服务引擎的认证方式，RBAC/NONE
        :type auth_type: str
        :param status: 微服务引擎当前的状态
        :type status: str
        :param external_address: 微服务引擎暴露的IP地址
        :type external_address: str
        :param service_endpoint: 微服务引擎组件的访问地址。
        :type service_endpoint: dict(str, EntrypointItem)
        :param public_address: 微服务引擎的公网IP地址
        :type public_address: str
        :param public_service_endpoint: 微服务引擎的公网接入地址
        :type public_service_endpoint: dict(str, EntrypointItem)
        :param total_instance: 微服务引擎可支持的实例总数
        :type total_instance: int
        :param used_instance: 已使用的实例总数
        :type used_instance: int
        :param available_instance: 可用实例总数
        :type available_instance: int
        :param version: 微服务引擎当前版本
        :type version: str
        :param latest_version: 微服务引擎最新版本
        :type latest_version: str
        :param create_time: 微服务引擎创建时间
        :type create_time: int
        :param due_to: 微服务引擎到期时间
        :type due_to: int
        :param latest_job_id: 微服务引擎最近的任务ID
        :type latest_job_id: int
        :param engine_additional_actions: 微服务引擎允许的附加操作
        :type engine_additional_actions: list[str]
        :param spec_type: 微服务引擎应用部署类型
        :type spec_type: str
        :param reference: 
        :type reference: :class:`huaweicloudsdkcse.v1.EngineReference`
        """
        
        

        self._id = None
        self._name = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._type = None
        self._description = None
        self._flavor = None
        self._payment = None
        self._auth_type = None
        self._status = None
        self._external_address = None
        self._service_endpoint = None
        self._public_address = None
        self._public_service_endpoint = None
        self._total_instance = None
        self._used_instance = None
        self._available_instance = None
        self._version = None
        self._latest_version = None
        self._create_time = None
        self._due_to = None
        self._latest_job_id = None
        self._engine_additional_actions = None
        self._spec_type = None
        self._reference = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if flavor is not None:
            self.flavor = flavor
        if payment is not None:
            self.payment = payment
        if auth_type is not None:
            self.auth_type = auth_type
        if status is not None:
            self.status = status
        if external_address is not None:
            self.external_address = external_address
        if service_endpoint is not None:
            self.service_endpoint = service_endpoint
        if public_address is not None:
            self.public_address = public_address
        if public_service_endpoint is not None:
            self.public_service_endpoint = public_service_endpoint
        if total_instance is not None:
            self.total_instance = total_instance
        if used_instance is not None:
            self.used_instance = used_instance
        if available_instance is not None:
            self.available_instance = available_instance
        if version is not None:
            self.version = version
        if latest_version is not None:
            self.latest_version = latest_version
        if create_time is not None:
            self.create_time = create_time
        if due_to is not None:
            self.due_to = due_to
        if latest_job_id is not None:
            self.latest_job_id = latest_job_id
        if engine_additional_actions is not None:
            self.engine_additional_actions = engine_additional_actions
        if spec_type is not None:
            self.spec_type = spec_type
        if reference is not None:
            self.reference = reference

    @property
    def id(self):
        r"""Gets the id of this EngineSimpleInfo.

        微服务引擎的ID

        :return: The id of this EngineSimpleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EngineSimpleInfo.

        微服务引擎的ID

        :param id: The id of this EngineSimpleInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EngineSimpleInfo.

        引擎的名称

        :return: The name of this EngineSimpleInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EngineSimpleInfo.

        引擎的名称

        :param name: The name of this EngineSimpleInfo.
        :type name: str
        """
        self._name = name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this EngineSimpleInfo.

        微服务引擎所属企业项目ID

        :return: The enterprise_project_id of this EngineSimpleInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this EngineSimpleInfo.

        微服务引擎所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this EngineSimpleInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        r"""Gets the enterprise_project_name of this EngineSimpleInfo.

        微服务引擎所属企业项目名称

        :return: The enterprise_project_name of this EngineSimpleInfo.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        r"""Sets the enterprise_project_name of this EngineSimpleInfo.

        微服务引擎所属企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this EngineSimpleInfo.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def type(self):
        r"""Gets the type of this EngineSimpleInfo.

        微服务引擎的类型，CSE为专享版引擎，CSE_Share表示为专业版引擎

        :return: The type of this EngineSimpleInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EngineSimpleInfo.

        微服务引擎的类型，CSE为专享版引擎，CSE_Share表示为专业版引擎

        :param type: The type of this EngineSimpleInfo.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this EngineSimpleInfo.

        微服务引擎的描述

        :return: The description of this EngineSimpleInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EngineSimpleInfo.

        微服务引擎的描述

        :param description: The description of this EngineSimpleInfo.
        :type description: str
        """
        self._description = description

    @property
    def flavor(self):
        r"""Gets the flavor of this EngineSimpleInfo.

        微服务引擎的规格

        :return: The flavor of this EngineSimpleInfo.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this EngineSimpleInfo.

        微服务引擎的规格

        :param flavor: The flavor of this EngineSimpleInfo.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def payment(self):
        r"""Gets the payment of this EngineSimpleInfo.

        微服务引擎的计费方式，0表示包周期，1表示按需，2表示免费

        :return: The payment of this EngineSimpleInfo.
        :rtype: str
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        r"""Sets the payment of this EngineSimpleInfo.

        微服务引擎的计费方式，0表示包周期，1表示按需，2表示免费

        :param payment: The payment of this EngineSimpleInfo.
        :type payment: str
        """
        self._payment = payment

    @property
    def auth_type(self):
        r"""Gets the auth_type of this EngineSimpleInfo.

        微服务引擎的认证方式，RBAC/NONE

        :return: The auth_type of this EngineSimpleInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this EngineSimpleInfo.

        微服务引擎的认证方式，RBAC/NONE

        :param auth_type: The auth_type of this EngineSimpleInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def status(self):
        r"""Gets the status of this EngineSimpleInfo.

        微服务引擎当前的状态

        :return: The status of this EngineSimpleInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EngineSimpleInfo.

        微服务引擎当前的状态

        :param status: The status of this EngineSimpleInfo.
        :type status: str
        """
        self._status = status

    @property
    def external_address(self):
        r"""Gets the external_address of this EngineSimpleInfo.

        微服务引擎暴露的IP地址

        :return: The external_address of this EngineSimpleInfo.
        :rtype: str
        """
        return self._external_address

    @external_address.setter
    def external_address(self, external_address):
        r"""Sets the external_address of this EngineSimpleInfo.

        微服务引擎暴露的IP地址

        :param external_address: The external_address of this EngineSimpleInfo.
        :type external_address: str
        """
        self._external_address = external_address

    @property
    def service_endpoint(self):
        r"""Gets the service_endpoint of this EngineSimpleInfo.

        微服务引擎组件的访问地址。

        :return: The service_endpoint of this EngineSimpleInfo.
        :rtype: dict(str, EntrypointItem)
        """
        return self._service_endpoint

    @service_endpoint.setter
    def service_endpoint(self, service_endpoint):
        r"""Sets the service_endpoint of this EngineSimpleInfo.

        微服务引擎组件的访问地址。

        :param service_endpoint: The service_endpoint of this EngineSimpleInfo.
        :type service_endpoint: dict(str, EntrypointItem)
        """
        self._service_endpoint = service_endpoint

    @property
    def public_address(self):
        r"""Gets the public_address of this EngineSimpleInfo.

        微服务引擎的公网IP地址

        :return: The public_address of this EngineSimpleInfo.
        :rtype: str
        """
        return self._public_address

    @public_address.setter
    def public_address(self, public_address):
        r"""Sets the public_address of this EngineSimpleInfo.

        微服务引擎的公网IP地址

        :param public_address: The public_address of this EngineSimpleInfo.
        :type public_address: str
        """
        self._public_address = public_address

    @property
    def public_service_endpoint(self):
        r"""Gets the public_service_endpoint of this EngineSimpleInfo.

        微服务引擎的公网接入地址

        :return: The public_service_endpoint of this EngineSimpleInfo.
        :rtype: dict(str, EntrypointItem)
        """
        return self._public_service_endpoint

    @public_service_endpoint.setter
    def public_service_endpoint(self, public_service_endpoint):
        r"""Sets the public_service_endpoint of this EngineSimpleInfo.

        微服务引擎的公网接入地址

        :param public_service_endpoint: The public_service_endpoint of this EngineSimpleInfo.
        :type public_service_endpoint: dict(str, EntrypointItem)
        """
        self._public_service_endpoint = public_service_endpoint

    @property
    def total_instance(self):
        r"""Gets the total_instance of this EngineSimpleInfo.

        微服务引擎可支持的实例总数

        :return: The total_instance of this EngineSimpleInfo.
        :rtype: int
        """
        return self._total_instance

    @total_instance.setter
    def total_instance(self, total_instance):
        r"""Sets the total_instance of this EngineSimpleInfo.

        微服务引擎可支持的实例总数

        :param total_instance: The total_instance of this EngineSimpleInfo.
        :type total_instance: int
        """
        self._total_instance = total_instance

    @property
    def used_instance(self):
        r"""Gets the used_instance of this EngineSimpleInfo.

        已使用的实例总数

        :return: The used_instance of this EngineSimpleInfo.
        :rtype: int
        """
        return self._used_instance

    @used_instance.setter
    def used_instance(self, used_instance):
        r"""Sets the used_instance of this EngineSimpleInfo.

        已使用的实例总数

        :param used_instance: The used_instance of this EngineSimpleInfo.
        :type used_instance: int
        """
        self._used_instance = used_instance

    @property
    def available_instance(self):
        r"""Gets the available_instance of this EngineSimpleInfo.

        可用实例总数

        :return: The available_instance of this EngineSimpleInfo.
        :rtype: int
        """
        return self._available_instance

    @available_instance.setter
    def available_instance(self, available_instance):
        r"""Sets the available_instance of this EngineSimpleInfo.

        可用实例总数

        :param available_instance: The available_instance of this EngineSimpleInfo.
        :type available_instance: int
        """
        self._available_instance = available_instance

    @property
    def version(self):
        r"""Gets the version of this EngineSimpleInfo.

        微服务引擎当前版本

        :return: The version of this EngineSimpleInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this EngineSimpleInfo.

        微服务引擎当前版本

        :param version: The version of this EngineSimpleInfo.
        :type version: str
        """
        self._version = version

    @property
    def latest_version(self):
        r"""Gets the latest_version of this EngineSimpleInfo.

        微服务引擎最新版本

        :return: The latest_version of this EngineSimpleInfo.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this EngineSimpleInfo.

        微服务引擎最新版本

        :param latest_version: The latest_version of this EngineSimpleInfo.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def create_time(self):
        r"""Gets the create_time of this EngineSimpleInfo.

        微服务引擎创建时间

        :return: The create_time of this EngineSimpleInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this EngineSimpleInfo.

        微服务引擎创建时间

        :param create_time: The create_time of this EngineSimpleInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def due_to(self):
        r"""Gets the due_to of this EngineSimpleInfo.

        微服务引擎到期时间

        :return: The due_to of this EngineSimpleInfo.
        :rtype: int
        """
        return self._due_to

    @due_to.setter
    def due_to(self, due_to):
        r"""Sets the due_to of this EngineSimpleInfo.

        微服务引擎到期时间

        :param due_to: The due_to of this EngineSimpleInfo.
        :type due_to: int
        """
        self._due_to = due_to

    @property
    def latest_job_id(self):
        r"""Gets the latest_job_id of this EngineSimpleInfo.

        微服务引擎最近的任务ID

        :return: The latest_job_id of this EngineSimpleInfo.
        :rtype: int
        """
        return self._latest_job_id

    @latest_job_id.setter
    def latest_job_id(self, latest_job_id):
        r"""Sets the latest_job_id of this EngineSimpleInfo.

        微服务引擎最近的任务ID

        :param latest_job_id: The latest_job_id of this EngineSimpleInfo.
        :type latest_job_id: int
        """
        self._latest_job_id = latest_job_id

    @property
    def engine_additional_actions(self):
        r"""Gets the engine_additional_actions of this EngineSimpleInfo.

        微服务引擎允许的附加操作

        :return: The engine_additional_actions of this EngineSimpleInfo.
        :rtype: list[str]
        """
        return self._engine_additional_actions

    @engine_additional_actions.setter
    def engine_additional_actions(self, engine_additional_actions):
        r"""Sets the engine_additional_actions of this EngineSimpleInfo.

        微服务引擎允许的附加操作

        :param engine_additional_actions: The engine_additional_actions of this EngineSimpleInfo.
        :type engine_additional_actions: list[str]
        """
        self._engine_additional_actions = engine_additional_actions

    @property
    def spec_type(self):
        r"""Gets the spec_type of this EngineSimpleInfo.

        微服务引擎应用部署类型

        :return: The spec_type of this EngineSimpleInfo.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        r"""Sets the spec_type of this EngineSimpleInfo.

        微服务引擎应用部署类型

        :param spec_type: The spec_type of this EngineSimpleInfo.
        :type spec_type: str
        """
        self._spec_type = spec_type

    @property
    def reference(self):
        r"""Gets the reference of this EngineSimpleInfo.

        :return: The reference of this EngineSimpleInfo.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineReference`
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        r"""Sets the reference of this EngineSimpleInfo.

        :param reference: The reference of this EngineSimpleInfo.
        :type reference: :class:`huaweicloudsdkcse.v1.EngineReference`
        """
        self._reference = reference

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
        if not isinstance(other, EngineSimpleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
