# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2TenantImagesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'sort_by': 'str',
        'order_by': 'str',
        'id': 'str',
        'category': 'str',
        'namespace': 'str',
        'name': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'order_by': 'order_by',
        'id': 'id',
        'category': 'category',
        'namespace': 'namespace',
        'name': 'name',
        'visibility': 'visibility'
    }

    def __init__(self, offset=None, limit=None, sort_by=None, order_by=None, id=None, category=None, namespace=None, name=None, visibility=None):
        r"""ListV2TenantImagesRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 
        :type limit: int
        :param sort_by: **参数解释**：指定排序字段。 **约束限制**：不涉及。 **取值范围**：   - CREATE_TIME：创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。   - UPDATE_TIME：更新时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **默认取值**：CREATE_TIME。
        :type sort_by: str
        :param order_by: **参数解释**：排序方式。 **约束限制**：不涉及。 **取值范围**：   - ASC：递增排序。   - DESC：递减排序。 **默认取值**：DESC。 
        :type order_by: str
        :param id: **参数解释**：镜像id检索。可通过[查询自定义镜像列表](ListV2TenantImages.xml)获取镜像ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type id: str
        :param category: **参数解释**：通过自定义镜像分类检索。 **约束限制**：不涉及。 **取值范围**：   - RAY_BASIC：基于Ray构建的自定义镜像。   - SPARK_JOB：基于SparkJob构建的自定义镜像。   - SPARK_SQL：基于SparkSql构建的自定义镜像。   - FLINK_JOB：基于FlinkJob构建的自定义镜像。   - AURA_JOB：基于AuraJobV2构建的自定义镜像。 **默认取值**：不涉及。 
        :type category: str
        :param namespace: **参数解释**：通过镜像组织搜索。 **约束限制**：不涉及。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度为0~64个字符。 **默认取值**：不涉及。 
        :type namespace: str
        :param name: **参数解释**：通过镜像名搜索。 **约束限制**：不涉及。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度为0~128个字符。 **默认取值**：不涉及。 
        :type name: str
        :param visibility: **参数解释**：可见性检索的参数。 **约束限制**：不涉及。 **取值范围**：   - PRIVATE：私有，用户自己创建的。   - PUBLIC：公共，查询所有公共的，包括其他用户创建的。   - ALL：所有的。 **默认取值**：默认为空，不填表示不限制。当前用户下包括PRIVATE和PUBLIC的，不包括其他用户创建的。 
        :type visibility: str
        """
        
        

        self._offset = None
        self._limit = None
        self._sort_by = None
        self._order_by = None
        self._id = None
        self._category = None
        self._namespace = None
        self._name = None
        self._visibility = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if order_by is not None:
            self.order_by = order_by
        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        if visibility is not None:
            self.visibility = visibility

    @property
    def offset(self):
        r"""Gets the offset of this ListV2TenantImagesRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListV2TenantImagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListV2TenantImagesRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListV2TenantImagesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListV2TenantImagesRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :return: The limit of this ListV2TenantImagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListV2TenantImagesRequest.

        **参数解释**：分页大小。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：100。 

        :param limit: The limit of this ListV2TenantImagesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListV2TenantImagesRequest.

        **参数解释**：指定排序字段。 **约束限制**：不涉及。 **取值范围**：   - CREATE_TIME：创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。   - UPDATE_TIME：更新时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **默认取值**：CREATE_TIME。

        :return: The sort_by of this ListV2TenantImagesRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListV2TenantImagesRequest.

        **参数解释**：指定排序字段。 **约束限制**：不涉及。 **取值范围**：   - CREATE_TIME：创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。   - UPDATE_TIME：更新时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **默认取值**：CREATE_TIME。

        :param sort_by: The sort_by of this ListV2TenantImagesRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order_by(self):
        r"""Gets the order_by of this ListV2TenantImagesRequest.

        **参数解释**：排序方式。 **约束限制**：不涉及。 **取值范围**：   - ASC：递增排序。   - DESC：递减排序。 **默认取值**：DESC。 

        :return: The order_by of this ListV2TenantImagesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListV2TenantImagesRequest.

        **参数解释**：排序方式。 **约束限制**：不涉及。 **取值范围**：   - ASC：递增排序。   - DESC：递减排序。 **默认取值**：DESC。 

        :param order_by: The order_by of this ListV2TenantImagesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def id(self):
        r"""Gets the id of this ListV2TenantImagesRequest.

        **参数解释**：镜像id检索。可通过[查询自定义镜像列表](ListV2TenantImages.xml)获取镜像ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The id of this ListV2TenantImagesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListV2TenantImagesRequest.

        **参数解释**：镜像id检索。可通过[查询自定义镜像列表](ListV2TenantImages.xml)获取镜像ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param id: The id of this ListV2TenantImagesRequest.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        r"""Gets the category of this ListV2TenantImagesRequest.

        **参数解释**：通过自定义镜像分类检索。 **约束限制**：不涉及。 **取值范围**：   - RAY_BASIC：基于Ray构建的自定义镜像。   - SPARK_JOB：基于SparkJob构建的自定义镜像。   - SPARK_SQL：基于SparkSql构建的自定义镜像。   - FLINK_JOB：基于FlinkJob构建的自定义镜像。   - AURA_JOB：基于AuraJobV2构建的自定义镜像。 **默认取值**：不涉及。 

        :return: The category of this ListV2TenantImagesRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListV2TenantImagesRequest.

        **参数解释**：通过自定义镜像分类检索。 **约束限制**：不涉及。 **取值范围**：   - RAY_BASIC：基于Ray构建的自定义镜像。   - SPARK_JOB：基于SparkJob构建的自定义镜像。   - SPARK_SQL：基于SparkSql构建的自定义镜像。   - FLINK_JOB：基于FlinkJob构建的自定义镜像。   - AURA_JOB：基于AuraJobV2构建的自定义镜像。 **默认取值**：不涉及。 

        :param category: The category of this ListV2TenantImagesRequest.
        :type category: str
        """
        self._category = category

    @property
    def namespace(self):
        r"""Gets the namespace of this ListV2TenantImagesRequest.

        **参数解释**：通过镜像组织搜索。 **约束限制**：不涉及。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度为0~64个字符。 **默认取值**：不涉及。 

        :return: The namespace of this ListV2TenantImagesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListV2TenantImagesRequest.

        **参数解释**：通过镜像组织搜索。 **约束限制**：不涉及。 **取值范围**：由英文字母、数字、中划线和下划线组成，长度为0~64个字符。 **默认取值**：不涉及。 

        :param namespace: The namespace of this ListV2TenantImagesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def name(self):
        r"""Gets the name of this ListV2TenantImagesRequest.

        **参数解释**：通过镜像名搜索。 **约束限制**：不涉及。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度为0~128个字符。 **默认取值**：不涉及。 

        :return: The name of this ListV2TenantImagesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListV2TenantImagesRequest.

        **参数解释**：通过镜像名搜索。 **约束限制**：不涉及。 **取值范围**：由中文字符、英文字母、数字、中划线和下划线组成，长度为0~128个字符。 **默认取值**：不涉及。 

        :param name: The name of this ListV2TenantImagesRequest.
        :type name: str
        """
        self._name = name

    @property
    def visibility(self):
        r"""Gets the visibility of this ListV2TenantImagesRequest.

        **参数解释**：可见性检索的参数。 **约束限制**：不涉及。 **取值范围**：   - PRIVATE：私有，用户自己创建的。   - PUBLIC：公共，查询所有公共的，包括其他用户创建的。   - ALL：所有的。 **默认取值**：默认为空，不填表示不限制。当前用户下包括PRIVATE和PUBLIC的，不包括其他用户创建的。 

        :return: The visibility of this ListV2TenantImagesRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ListV2TenantImagesRequest.

        **参数解释**：可见性检索的参数。 **约束限制**：不涉及。 **取值范围**：   - PRIVATE：私有，用户自己创建的。   - PUBLIC：公共，查询所有公共的，包括其他用户创建的。   - ALL：所有的。 **默认取值**：默认为空，不填表示不限制。当前用户下包括PRIVATE和PUBLIC的，不包括其他用户创建的。 

        :param visibility: The visibility of this ListV2TenantImagesRequest.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, ListV2TenantImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
