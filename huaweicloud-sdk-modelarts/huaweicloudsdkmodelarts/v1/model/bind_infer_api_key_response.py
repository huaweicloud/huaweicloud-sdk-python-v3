# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindInferApiKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'name': 'str',
        'description': 'str',
        'create_time': 'str',
        'scope': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'services': 'list[ServiceIdName]',
        'workspace_id': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'scope': 'scope',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'services': 'services',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, key_id=None, name=None, description=None, create_time=None, scope=None, domain_id=None, project_id=None, services=None, workspace_id=None):
        r"""BindInferApiKeyResponse

        The model defined in huaweicloud sdk

        :param key_id: **参数解释：** api-key的ID，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的api-key，其中id字段即为api-key的ID。 **取值范围：** UUID格式。
        :type key_id: str
        :param name: **参数解释：** api-key的名称，在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **取值范围：** 支持1-64个字符，可以包含字母、汉字、数字、连字符和下划线。
        :type name: str
        :param description: **参数解释：** api-key的描述，在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **取值范围：** 支持1-256个字符，可以包含字母、汉字、数字、连字符和下划线。
        :type description: str
        :param create_time: **参数解释：** api-key的创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。
        :type create_time: str
        :param scope: **参数解释：** api-key生效范围。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。
        :type scope: str
        :param domain_id: **参数解释：** 用户domain ID。获取方法请参见[获取账号名和账号ID](modelarts_03_0148.xml)。 **取值范围：** 账号ID。
        :type domain_id: str
        :param project_id: **参数解释：** [用户项目ID](tag:hws,hws_hk,fcs,fcs_super)[资源空间ID](tag:hcs,hcs_sm)。获取方法请参见[[获取项目ID和名称](tag:hws,hws_hk,fcs,fcs_super)[获取资源空间ID和名称](tag:hcs,hcs_sm)](modelarts_03_0147.xml)。 **取值范围：** 账号的项目ID。
        :type project_id: str
        :param services: **参数解释：** 绑定此api-key的在线服务列表。
        :type services: list[:class:`huaweicloudsdkmodelarts.v1.ServiceIdName`]
        :param workspace_id: **参数解释：** 工作空间ID。 **取值范围：** 工作空间ID。
        :type workspace_id: str
        """
        
        super().__init__()

        self._key_id = None
        self._name = None
        self._description = None
        self._create_time = None
        self._scope = None
        self._domain_id = None
        self._project_id = None
        self._services = None
        self._workspace_id = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if scope is not None:
            self.scope = scope
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if services is not None:
            self.services = services
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def key_id(self):
        r"""Gets the key_id of this BindInferApiKeyResponse.

        **参数解释：** api-key的ID，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的api-key，其中id字段即为api-key的ID。 **取值范围：** UUID格式。

        :return: The key_id of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this BindInferApiKeyResponse.

        **参数解释：** api-key的ID，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的api-key，其中id字段即为api-key的ID。 **取值范围：** UUID格式。

        :param key_id: The key_id of this BindInferApiKeyResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def name(self):
        r"""Gets the name of this BindInferApiKeyResponse.

        **参数解释：** api-key的名称，在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **取值范围：** 支持1-64个字符，可以包含字母、汉字、数字、连字符和下划线。

        :return: The name of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BindInferApiKeyResponse.

        **参数解释：** api-key的名称，在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **取值范围：** 支持1-64个字符，可以包含字母、汉字、数字、连字符和下划线。

        :param name: The name of this BindInferApiKeyResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this BindInferApiKeyResponse.

        **参数解释：** api-key的描述，在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **取值范围：** 支持1-256个字符，可以包含字母、汉字、数字、连字符和下划线。

        :return: The description of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BindInferApiKeyResponse.

        **参数解释：** api-key的描述，在[创建API_KEY](CreateInferApiKey.xml)时自定义。 **取值范围：** 支持1-256个字符，可以包含字母、汉字、数字、连字符和下划线。

        :param description: The description of this BindInferApiKeyResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this BindInferApiKeyResponse.

        **参数解释：** api-key的创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。

        :return: The create_time of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BindInferApiKeyResponse.

        **参数解释：** api-key的创建时间，根据创建时的当前时间自动生成。 **取值范围：** 毫秒级时间戳，13位数字，如1609459200000。

        :param create_time: The create_time of this BindInferApiKeyResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def scope(self):
        r"""Gets the scope of this BindInferApiKeyResponse.

        **参数解释：** api-key生效范围。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。

        :return: The scope of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this BindInferApiKeyResponse.

        **参数解释：** api-key生效范围。 **取值范围：** - USER：表示生效范围为用户级别，可以访问该用户创建的所有在线服务。 - SERVICE：表示生效范围为单个服务，可以访问绑定该api-key的在线服务。

        :param scope: The scope of this BindInferApiKeyResponse.
        :type scope: str
        """
        self._scope = scope

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BindInferApiKeyResponse.

        **参数解释：** 用户domain ID。获取方法请参见[获取账号名和账号ID](modelarts_03_0148.xml)。 **取值范围：** 账号ID。

        :return: The domain_id of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BindInferApiKeyResponse.

        **参数解释：** 用户domain ID。获取方法请参见[获取账号名和账号ID](modelarts_03_0148.xml)。 **取值范围：** 账号ID。

        :param domain_id: The domain_id of this BindInferApiKeyResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this BindInferApiKeyResponse.

        **参数解释：** [用户项目ID](tag:hws,hws_hk,fcs,fcs_super)[资源空间ID](tag:hcs,hcs_sm)。获取方法请参见[[获取项目ID和名称](tag:hws,hws_hk,fcs,fcs_super)[获取资源空间ID和名称](tag:hcs,hcs_sm)](modelarts_03_0147.xml)。 **取值范围：** 账号的项目ID。

        :return: The project_id of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BindInferApiKeyResponse.

        **参数解释：** [用户项目ID](tag:hws,hws_hk,fcs,fcs_super)[资源空间ID](tag:hcs,hcs_sm)。获取方法请参见[[获取项目ID和名称](tag:hws,hws_hk,fcs,fcs_super)[获取资源空间ID和名称](tag:hcs,hcs_sm)](modelarts_03_0147.xml)。 **取值范围：** 账号的项目ID。

        :param project_id: The project_id of this BindInferApiKeyResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def services(self):
        r"""Gets the services of this BindInferApiKeyResponse.

        **参数解释：** 绑定此api-key的在线服务列表。

        :return: The services of this BindInferApiKeyResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServiceIdName`]
        """
        return self._services

    @services.setter
    def services(self, services):
        r"""Sets the services of this BindInferApiKeyResponse.

        **参数解释：** 绑定此api-key的在线服务列表。

        :param services: The services of this BindInferApiKeyResponse.
        :type services: list[:class:`huaweicloudsdkmodelarts.v1.ServiceIdName`]
        """
        self._services = services

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this BindInferApiKeyResponse.

        **参数解释：** 工作空间ID。 **取值范围：** 工作空间ID。

        :return: The workspace_id of this BindInferApiKeyResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this BindInferApiKeyResponse.

        **参数解释：** 工作空间ID。 **取值范围：** 工作空间ID。

        :param workspace_id: The workspace_id of this BindInferApiKeyResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    def to_dict(self):
        import warnings
        warnings.warn("BindInferApiKeyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BindInferApiKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
