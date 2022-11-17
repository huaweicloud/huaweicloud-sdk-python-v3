# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEngineResponse(SdkResponse):

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
        'description': 'str',
        'auth_type': 'str',
        'flavor': 'str',
        'payment': 'str',
        'version': 'str',
        'latest_version': 'str',
        'status': 'str',
        'be_default': 'bool',
        'create_user': 'str',
        'create_time': 'int',
        'cce_spec': 'Spec',
        'external_entrypoint': 'EngineExternalEntrypoint',
        'reference': 'EngineReference',
        'latest_job_id': 'int',
        'enterprise_project_id': 'str',
        'enterprise_project_name': 'str',
        'engine_additional_actions': 'list[str]',
        'spec_type': 'str',
        'type': 'str',
        'project_id': 'str',
        'vm_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'auth_type': 'auth_type',
        'flavor': 'flavor',
        'payment': 'payment',
        'version': 'version',
        'latest_version': 'latest_version',
        'status': 'status',
        'be_default': 'be_default',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'cce_spec': 'cce_spec',
        'external_entrypoint': 'external_entrypoint',
        'reference': 'reference',
        'latest_job_id': 'latest_job_id',
        'enterprise_project_id': 'enterprise_project_id',
        'enterprise_project_name': 'enterprise_project_name',
        'engine_additional_actions': 'engine_additional_actions',
        'spec_type': 'spec_type',
        'type': 'type',
        'project_id': 'project_id',
        'vm_ids': 'vm_ids'
    }

    def __init__(self, id=None, name=None, description=None, auth_type=None, flavor=None, payment=None, version=None, latest_version=None, status=None, be_default=None, create_user=None, create_time=None, cce_spec=None, external_entrypoint=None, reference=None, latest_job_id=None, enterprise_project_id=None, enterprise_project_name=None, engine_additional_actions=None, spec_type=None, type=None, project_id=None, vm_ids=None):
        """ShowEngineResponse

        The model defined in huaweicloud sdk

        :param id: 微服务引擎专享版ID
        :type id: str
        :param name: 微服务引擎专享版名称
        :type name: str
        :param description: 微服务引擎专享版描述
        :type description: str
        :param auth_type: 微服务引擎专享版认证类型
        :type auth_type: str
        :param flavor: 微服务引擎专享版规格
        :type flavor: str
        :param payment: 微服务引擎专享版计费方式
        :type payment: str
        :param version: 微服务引擎专享版当前版本
        :type version: str
        :param latest_version: 微服务引擎专享版最新版本
        :type latest_version: str
        :param status: 微服务引擎专享版状态
        :type status: str
        :param be_default: engine 是否是默认引擎
        :type be_default: bool
        :param create_user: 微服务引擎专享版创建者
        :type create_user: str
        :param create_time: 微服务引擎专享版创建时间
        :type create_time: int
        :param cce_spec: 
        :type cce_spec: :class:`huaweicloudsdkcse.v1.Spec`
        :param external_entrypoint: 
        :type external_entrypoint: :class:`huaweicloudsdkcse.v1.EngineExternalEntrypoint`
        :param reference: 
        :type reference: :class:`huaweicloudsdkcse.v1.EngineReference`
        :param latest_job_id: 微服务引擎专享版最近的任务ID
        :type latest_job_id: int
        :param enterprise_project_id: 微服务引擎专享版所属企业项目ID
        :type enterprise_project_id: str
        :param enterprise_project_name: 微服务引擎专享版所属企业项目名称
        :type enterprise_project_name: str
        :param engine_additional_actions: 微服务引擎专享版允许的附加操作
        :type engine_additional_actions: list[str]
        :param spec_type: 微服务引擎专享版应用部署类型
        :type spec_type: str
        :param type: 微服务引擎类型，CSE表示专享版，CSE_Share表示专业版
        :type type: str
        :param project_id: 微服务引擎专享版所属项目ID
        :type project_id: str
        :param vm_ids: 当前引擎在资源租户侧使用的虚拟机 id 列表
        :type vm_ids: list[str]
        """
        
        super(ShowEngineResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._auth_type = None
        self._flavor = None
        self._payment = None
        self._version = None
        self._latest_version = None
        self._status = None
        self._be_default = None
        self._create_user = None
        self._create_time = None
        self._cce_spec = None
        self._external_entrypoint = None
        self._reference = None
        self._latest_job_id = None
        self._enterprise_project_id = None
        self._enterprise_project_name = None
        self._engine_additional_actions = None
        self._spec_type = None
        self._type = None
        self._project_id = None
        self._vm_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if auth_type is not None:
            self.auth_type = auth_type
        if flavor is not None:
            self.flavor = flavor
        if payment is not None:
            self.payment = payment
        if version is not None:
            self.version = version
        if latest_version is not None:
            self.latest_version = latest_version
        if status is not None:
            self.status = status
        if be_default is not None:
            self.be_default = be_default
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if cce_spec is not None:
            self.cce_spec = cce_spec
        if external_entrypoint is not None:
            self.external_entrypoint = external_entrypoint
        if reference is not None:
            self.reference = reference
        if latest_job_id is not None:
            self.latest_job_id = latest_job_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if enterprise_project_name is not None:
            self.enterprise_project_name = enterprise_project_name
        if engine_additional_actions is not None:
            self.engine_additional_actions = engine_additional_actions
        if spec_type is not None:
            self.spec_type = spec_type
        if type is not None:
            self.type = type
        if project_id is not None:
            self.project_id = project_id
        if vm_ids is not None:
            self.vm_ids = vm_ids

    @property
    def id(self):
        """Gets the id of this ShowEngineResponse.

        微服务引擎专享版ID

        :return: The id of this ShowEngineResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowEngineResponse.

        微服务引擎专享版ID

        :param id: The id of this ShowEngineResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowEngineResponse.

        微服务引擎专享版名称

        :return: The name of this ShowEngineResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowEngineResponse.

        微服务引擎专享版名称

        :param name: The name of this ShowEngineResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowEngineResponse.

        微服务引擎专享版描述

        :return: The description of this ShowEngineResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowEngineResponse.

        微服务引擎专享版描述

        :param description: The description of this ShowEngineResponse.
        :type description: str
        """
        self._description = description

    @property
    def auth_type(self):
        """Gets the auth_type of this ShowEngineResponse.

        微服务引擎专享版认证类型

        :return: The auth_type of this ShowEngineResponse.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ShowEngineResponse.

        微服务引擎专享版认证类型

        :param auth_type: The auth_type of this ShowEngineResponse.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def flavor(self):
        """Gets the flavor of this ShowEngineResponse.

        微服务引擎专享版规格

        :return: The flavor of this ShowEngineResponse.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ShowEngineResponse.

        微服务引擎专享版规格

        :param flavor: The flavor of this ShowEngineResponse.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def payment(self):
        """Gets the payment of this ShowEngineResponse.

        微服务引擎专享版计费方式

        :return: The payment of this ShowEngineResponse.
        :rtype: str
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ShowEngineResponse.

        微服务引擎专享版计费方式

        :param payment: The payment of this ShowEngineResponse.
        :type payment: str
        """
        self._payment = payment

    @property
    def version(self):
        """Gets the version of this ShowEngineResponse.

        微服务引擎专享版当前版本

        :return: The version of this ShowEngineResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowEngineResponse.

        微服务引擎专享版当前版本

        :param version: The version of this ShowEngineResponse.
        :type version: str
        """
        self._version = version

    @property
    def latest_version(self):
        """Gets the latest_version of this ShowEngineResponse.

        微服务引擎专享版最新版本

        :return: The latest_version of this ShowEngineResponse.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this ShowEngineResponse.

        微服务引擎专享版最新版本

        :param latest_version: The latest_version of this ShowEngineResponse.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def status(self):
        """Gets the status of this ShowEngineResponse.

        微服务引擎专享版状态

        :return: The status of this ShowEngineResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowEngineResponse.

        微服务引擎专享版状态

        :param status: The status of this ShowEngineResponse.
        :type status: str
        """
        self._status = status

    @property
    def be_default(self):
        """Gets the be_default of this ShowEngineResponse.

        engine 是否是默认引擎

        :return: The be_default of this ShowEngineResponse.
        :rtype: bool
        """
        return self._be_default

    @be_default.setter
    def be_default(self, be_default):
        """Sets the be_default of this ShowEngineResponse.

        engine 是否是默认引擎

        :param be_default: The be_default of this ShowEngineResponse.
        :type be_default: bool
        """
        self._be_default = be_default

    @property
    def create_user(self):
        """Gets the create_user of this ShowEngineResponse.

        微服务引擎专享版创建者

        :return: The create_user of this ShowEngineResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ShowEngineResponse.

        微服务引擎专享版创建者

        :param create_user: The create_user of this ShowEngineResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        """Gets the create_time of this ShowEngineResponse.

        微服务引擎专享版创建时间

        :return: The create_time of this ShowEngineResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowEngineResponse.

        微服务引擎专享版创建时间

        :param create_time: The create_time of this ShowEngineResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def cce_spec(self):
        """Gets the cce_spec of this ShowEngineResponse.

        :return: The cce_spec of this ShowEngineResponse.
        :rtype: :class:`huaweicloudsdkcse.v1.Spec`
        """
        return self._cce_spec

    @cce_spec.setter
    def cce_spec(self, cce_spec):
        """Sets the cce_spec of this ShowEngineResponse.

        :param cce_spec: The cce_spec of this ShowEngineResponse.
        :type cce_spec: :class:`huaweicloudsdkcse.v1.Spec`
        """
        self._cce_spec = cce_spec

    @property
    def external_entrypoint(self):
        """Gets the external_entrypoint of this ShowEngineResponse.

        :return: The external_entrypoint of this ShowEngineResponse.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineExternalEntrypoint`
        """
        return self._external_entrypoint

    @external_entrypoint.setter
    def external_entrypoint(self, external_entrypoint):
        """Sets the external_entrypoint of this ShowEngineResponse.

        :param external_entrypoint: The external_entrypoint of this ShowEngineResponse.
        :type external_entrypoint: :class:`huaweicloudsdkcse.v1.EngineExternalEntrypoint`
        """
        self._external_entrypoint = external_entrypoint

    @property
    def reference(self):
        """Gets the reference of this ShowEngineResponse.

        :return: The reference of this ShowEngineResponse.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineReference`
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ShowEngineResponse.

        :param reference: The reference of this ShowEngineResponse.
        :type reference: :class:`huaweicloudsdkcse.v1.EngineReference`
        """
        self._reference = reference

    @property
    def latest_job_id(self):
        """Gets the latest_job_id of this ShowEngineResponse.

        微服务引擎专享版最近的任务ID

        :return: The latest_job_id of this ShowEngineResponse.
        :rtype: int
        """
        return self._latest_job_id

    @latest_job_id.setter
    def latest_job_id(self, latest_job_id):
        """Sets the latest_job_id of this ShowEngineResponse.

        微服务引擎专享版最近的任务ID

        :param latest_job_id: The latest_job_id of this ShowEngineResponse.
        :type latest_job_id: int
        """
        self._latest_job_id = latest_job_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowEngineResponse.

        微服务引擎专享版所属企业项目ID

        :return: The enterprise_project_id of this ShowEngineResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowEngineResponse.

        微服务引擎专享版所属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowEngineResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enterprise_project_name(self):
        """Gets the enterprise_project_name of this ShowEngineResponse.

        微服务引擎专享版所属企业项目名称

        :return: The enterprise_project_name of this ShowEngineResponse.
        :rtype: str
        """
        return self._enterprise_project_name

    @enterprise_project_name.setter
    def enterprise_project_name(self, enterprise_project_name):
        """Sets the enterprise_project_name of this ShowEngineResponse.

        微服务引擎专享版所属企业项目名称

        :param enterprise_project_name: The enterprise_project_name of this ShowEngineResponse.
        :type enterprise_project_name: str
        """
        self._enterprise_project_name = enterprise_project_name

    @property
    def engine_additional_actions(self):
        """Gets the engine_additional_actions of this ShowEngineResponse.

        微服务引擎专享版允许的附加操作

        :return: The engine_additional_actions of this ShowEngineResponse.
        :rtype: list[str]
        """
        return self._engine_additional_actions

    @engine_additional_actions.setter
    def engine_additional_actions(self, engine_additional_actions):
        """Sets the engine_additional_actions of this ShowEngineResponse.

        微服务引擎专享版允许的附加操作

        :param engine_additional_actions: The engine_additional_actions of this ShowEngineResponse.
        :type engine_additional_actions: list[str]
        """
        self._engine_additional_actions = engine_additional_actions

    @property
    def spec_type(self):
        """Gets the spec_type of this ShowEngineResponse.

        微服务引擎专享版应用部署类型

        :return: The spec_type of this ShowEngineResponse.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        """Sets the spec_type of this ShowEngineResponse.

        微服务引擎专享版应用部署类型

        :param spec_type: The spec_type of this ShowEngineResponse.
        :type spec_type: str
        """
        self._spec_type = spec_type

    @property
    def type(self):
        """Gets the type of this ShowEngineResponse.

        微服务引擎类型，CSE表示专享版，CSE_Share表示专业版

        :return: The type of this ShowEngineResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowEngineResponse.

        微服务引擎类型，CSE表示专享版，CSE_Share表示专业版

        :param type: The type of this ShowEngineResponse.
        :type type: str
        """
        self._type = type

    @property
    def project_id(self):
        """Gets the project_id of this ShowEngineResponse.

        微服务引擎专享版所属项目ID

        :return: The project_id of this ShowEngineResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowEngineResponse.

        微服务引擎专享版所属项目ID

        :param project_id: The project_id of this ShowEngineResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def vm_ids(self):
        """Gets the vm_ids of this ShowEngineResponse.

        当前引擎在资源租户侧使用的虚拟机 id 列表

        :return: The vm_ids of this ShowEngineResponse.
        :rtype: list[str]
        """
        return self._vm_ids

    @vm_ids.setter
    def vm_ids(self, vm_ids):
        """Sets the vm_ids of this ShowEngineResponse.

        当前引擎在资源租户侧使用的虚拟机 id 列表

        :param vm_ids: The vm_ids of this ShowEngineResponse.
        :type vm_ids: list[str]
        """
        self._vm_ids = vm_ids

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
        if not isinstance(other, ShowEngineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
