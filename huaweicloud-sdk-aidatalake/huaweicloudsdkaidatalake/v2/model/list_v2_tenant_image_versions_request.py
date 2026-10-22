# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2TenantImageVersionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'version': 'str',
        'type': 'str',
        'architectures': 'str',
        'workspace_id': 'str',
        'endpoint_id': 'str',
        'sort_by': 'str',
        'order_by': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'limit': 'limit',
        'offset': 'offset',
        'version': 'version',
        'type': 'type',
        'architectures': 'architectures',
        'workspace_id': 'workspace_id',
        'endpoint_id': 'endpoint_id',
        'sort_by': 'sort_by',
        'order_by': 'order_by',
        'tenant_id': 'tenantId'
    }

    def __init__(self, image_id=None, limit=None, offset=None, version=None, type=None, architectures=None, workspace_id=None, endpoint_id=None, sort_by=None, order_by=None, tenant_id=None):
        r"""ListV2TenantImageVersionsRequest

        The model defined in huaweicloud sdk

        :param image_id: **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type image_id: str
        :param limit: **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 
        :type limit: int
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param version: **参数解释**：镜像版本名称（TAG）。 **约束限制**：不涉及。 **取值范围**：长度为2~32的英文字符、数字、中划线、点和下划线的组合。 **默认取值**：不涉及。
        :type version: str
        :param type: **参数解释**：镜像版本类型。 **约束限制**：不涉及。 **取值范围**：   - STABLE：稳定版本。   - RECOMMEND：推荐版本。   - BETA：测试版本。 **默认取值**：不涉及 
        :type type: str
        :param architectures: **参数解释**：镜像架构，多个架构用逗号分隔。 **约束限制**：不涉及。 **取值范围**：   - x86_64：x86架构。   - aarch64：ARM架构。 **默认取值**：不涉及 
        :type architectures: str
        :param workspace_id: **参数解释**：工作空间ID，用于查询过滤工作空间支持的镜像版本。可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type workspace_id: str
        :param endpoint_id: **参数解释**：端点ID，用于查询过滤端点支持的镜像版本。可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type endpoint_id: str
        :param sort_by: **参数解释**：指定排序字段。 **约束限制**：不涉及。 **取值范围**：   - CREATE_TIME：创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。   - UPDATE_TIME：更新时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **默认取值**：CREATE_TIME。
        :type sort_by: str
        :param order_by: **参数解释**：排序方式。 **约束限制**：不涉及。 **取值范围**：   - ASC：递增排序。   - DESC：递减排序。 **默认取值**：DESC。 
        :type order_by: str
        :param tenant_id: **参数解释**：租户ID，用于标识租户。可通过IAM服务或控制台获取租户ID。获取方式请参见[获取账号、IAM用户、项目、用户组、委托的名称和ID](iam_01_0023.xml)。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type tenant_id: str
        """
        
        

        self._image_id = None
        self._limit = None
        self._offset = None
        self._version = None
        self._type = None
        self._architectures = None
        self._workspace_id = None
        self._endpoint_id = None
        self._sort_by = None
        self._order_by = None
        self._tenant_id = None
        self.discriminator = None

        self.image_id = image_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if version is not None:
            self.version = version
        if type is not None:
            self.type = type
        if architectures is not None:
            self.architectures = architectures
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if sort_by is not None:
            self.sort_by = sort_by
        if order_by is not None:
            self.order_by = order_by
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def image_id(self):
        r"""Gets the image_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The image_id of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像ID。可通过[查询自定义镜像列表]获取镜像ID(ListV2TenantImages.xml)。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param image_id: The image_id of this ListV2TenantImageVersionsRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def limit(self):
        r"""Gets the limit of this ListV2TenantImageVersionsRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :return: The limit of this ListV2TenantImageVersionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2TenantImageVersionsRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :param limit: The limit of this ListV2TenantImageVersionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListV2TenantImageVersionsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2TenantImageVersionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2TenantImageVersionsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2TenantImageVersionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def version(self):
        r"""Gets the version of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像版本名称（TAG）。 **约束限制**：不涉及。 **取值范围**：长度为2~32的英文字符、数字、中划线、点和下划线的组合。 **默认取值**：不涉及。

        :return: The version of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像版本名称（TAG）。 **约束限制**：不涉及。 **取值范围**：长度为2~32的英文字符、数字、中划线、点和下划线的组合。 **默认取值**：不涉及。

        :param version: The version of this ListV2TenantImageVersionsRequest.
        :type version: str
        """
        self._version = version

    @property
    def type(self):
        r"""Gets the type of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像版本类型。 **约束限制**：不涉及。 **取值范围**：   - STABLE：稳定版本。   - RECOMMEND：推荐版本。   - BETA：测试版本。 **默认取值**：不涉及 

        :return: The type of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像版本类型。 **约束限制**：不涉及。 **取值范围**：   - STABLE：稳定版本。   - RECOMMEND：推荐版本。   - BETA：测试版本。 **默认取值**：不涉及 

        :param type: The type of this ListV2TenantImageVersionsRequest.
        :type type: str
        """
        self._type = type

    @property
    def architectures(self):
        r"""Gets the architectures of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像架构，多个架构用逗号分隔。 **约束限制**：不涉及。 **取值范围**：   - x86_64：x86架构。   - aarch64：ARM架构。 **默认取值**：不涉及 

        :return: The architectures of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._architectures

    @architectures.setter
    def architectures(self, architectures):
        r"""Sets the architectures of this ListV2TenantImageVersionsRequest.

        **参数解释**：镜像架构，多个架构用逗号分隔。 **约束限制**：不涉及。 **取值范围**：   - x86_64：x86架构。   - aarch64：ARM架构。 **默认取值**：不涉及 

        :param architectures: The architectures of this ListV2TenantImageVersionsRequest.
        :type architectures: str
        """
        self._architectures = architectures

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：工作空间ID，用于查询过滤工作空间支持的镜像版本。可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The workspace_id of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：工作空间ID，用于查询过滤工作空间支持的镜像版本。可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param workspace_id: The workspace_id of this ListV2TenantImageVersionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：端点ID，用于查询过滤端点支持的镜像版本。可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The endpoint_id of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：端点ID，用于查询过滤端点支持的镜像版本。可通过[查询端点列表](ListV2Endpoints.xml)获取端点ID。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param endpoint_id: The endpoint_id of this ListV2TenantImageVersionsRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListV2TenantImageVersionsRequest.

        **参数解释**：指定排序字段。 **约束限制**：不涉及。 **取值范围**：   - CREATE_TIME：创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。   - UPDATE_TIME：更新时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **默认取值**：CREATE_TIME。

        :return: The sort_by of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListV2TenantImageVersionsRequest.

        **参数解释**：指定排序字段。 **约束限制**：不涉及。 **取值范围**：   - CREATE_TIME：创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。   - UPDATE_TIME：更新时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **默认取值**：CREATE_TIME。

        :param sort_by: The sort_by of this ListV2TenantImageVersionsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order_by(self):
        r"""Gets the order_by of this ListV2TenantImageVersionsRequest.

        **参数解释**：排序方式。 **约束限制**：不涉及。 **取值范围**：   - ASC：递增排序。   - DESC：递减排序。 **默认取值**：DESC。 

        :return: The order_by of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListV2TenantImageVersionsRequest.

        **参数解释**：排序方式。 **约束限制**：不涉及。 **取值范围**：   - ASC：递增排序。   - DESC：递减排序。 **默认取值**：DESC。 

        :param order_by: The order_by of this ListV2TenantImageVersionsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：租户ID，用于标识租户。可通过IAM服务或控制台获取租户ID。获取方式请参见[获取账号、IAM用户、项目、用户组、委托的名称和ID](iam_01_0023.xml)。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The tenant_id of this ListV2TenantImageVersionsRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ListV2TenantImageVersionsRequest.

        **参数解释**：租户ID，用于标识租户。可通过IAM服务或控制台获取租户ID。获取方式请参见[获取账号、IAM用户、项目、用户组、委托的名称和ID](iam_01_0023.xml)。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param tenant_id: The tenant_id of this ListV2TenantImageVersionsRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    def to_dict(self):
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
        if not isinstance(other, ListV2TenantImageVersionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
