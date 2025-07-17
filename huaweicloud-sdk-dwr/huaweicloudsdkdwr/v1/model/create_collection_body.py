# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCollectionBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'collection_name': 'str',
        'primary_field': 'PrimaryField',
        'fields': 'list[Field]',
        'description': 'str',
        'index_params': 'list[IndexParams]',
        'params': 'dict(str, object)'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'primary_field': 'primary_field',
        'fields': 'fields',
        'description': 'description',
        'index_params': 'index_params',
        'params': 'params'
    }

    def __init__(self, store_name=None, collection_name=None, primary_field=None, fields=None, description=None, index_params=None, params=None):
        r"""CreateCollectionBody

        The model defined in huaweicloud sdk

        :param store_name: **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type store_name: str
        :param collection_name: **参数解释：** collection名称。 **约束限制：** 可包含数字、字母和下划线 (_)。资源名称必须以字母或下划线 (_) 开头。最大长度支持255。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type collection_name: str
        :param primary_field: 
        :type primary_field: :class:`huaweicloudsdkdwr.v1.PrimaryField`
        :param fields: **参数解释：** 集合中通用字段，创建列的schema。 **约束限制：** 不涉及。
        :type fields: list[:class:`huaweicloudsdkdwr.v1.Field`]
        :param description: **参数解释：** 指定 Collection 的描述信息。 **约束限制：** 有效长度0-255字节。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type description: str
        :param index_params: **参数解释：** 索引的配置信息。 **约束限制：** 不涉及。
        :type index_params: list[:class:`huaweicloudsdkdwr.v1.IndexParams`]
        :param params: **参数解释：** collection常用参数。 **约束限制：** shards_num: 默认2，取值范围[1, 16] partitions_num: 默认4，取值范围[1, 1024]，若所有field的partition_key为false，则partitions_num固定为1。 max_length: 默认256，取值范围[1, 65535]，当primary_field.type为String时，指示String的最大长度。
        :type params: dict(str, object)
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._primary_field = None
        self._fields = None
        self._description = None
        self._index_params = None
        self._params = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        self.primary_field = primary_field
        self.fields = fields
        if description is not None:
            self.description = description
        if index_params is not None:
            self.index_params = index_params
        if params is not None:
            self.params = params

    @property
    def store_name(self):
        r"""Gets the store_name of this CreateCollectionBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The store_name of this CreateCollectionBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this CreateCollectionBody.

        **参数解释：** 知识仓实例名称，region内唯一。 **约束限制：** 长度范围为3到63个字符，支持小写字母、数字、中划线（-），第一个字符只能够是小写字母，中划线(-)不得出现在字符串末尾。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param store_name: The store_name of this CreateCollectionBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this CreateCollectionBody.

        **参数解释：** collection名称。 **约束限制：** 可包含数字、字母和下划线 (_)。资源名称必须以字母或下划线 (_) 开头。最大长度支持255。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The collection_name of this CreateCollectionBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this CreateCollectionBody.

        **参数解释：** collection名称。 **约束限制：** 可包含数字、字母和下划线 (_)。资源名称必须以字母或下划线 (_) 开头。最大长度支持255。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param collection_name: The collection_name of this CreateCollectionBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def primary_field(self):
        r"""Gets the primary_field of this CreateCollectionBody.

        :return: The primary_field of this CreateCollectionBody.
        :rtype: :class:`huaweicloudsdkdwr.v1.PrimaryField`
        """
        return self._primary_field

    @primary_field.setter
    def primary_field(self, primary_field):
        r"""Sets the primary_field of this CreateCollectionBody.

        :param primary_field: The primary_field of this CreateCollectionBody.
        :type primary_field: :class:`huaweicloudsdkdwr.v1.PrimaryField`
        """
        self._primary_field = primary_field

    @property
    def fields(self):
        r"""Gets the fields of this CreateCollectionBody.

        **参数解释：** 集合中通用字段，创建列的schema。 **约束限制：** 不涉及。

        :return: The fields of this CreateCollectionBody.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.Field`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this CreateCollectionBody.

        **参数解释：** 集合中通用字段，创建列的schema。 **约束限制：** 不涉及。

        :param fields: The fields of this CreateCollectionBody.
        :type fields: list[:class:`huaweicloudsdkdwr.v1.Field`]
        """
        self._fields = fields

    @property
    def description(self):
        r"""Gets the description of this CreateCollectionBody.

        **参数解释：** 指定 Collection 的描述信息。 **约束限制：** 有效长度0-255字节。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The description of this CreateCollectionBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCollectionBody.

        **参数解释：** 指定 Collection 的描述信息。 **约束限制：** 有效长度0-255字节。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param description: The description of this CreateCollectionBody.
        :type description: str
        """
        self._description = description

    @property
    def index_params(self):
        r"""Gets the index_params of this CreateCollectionBody.

        **参数解释：** 索引的配置信息。 **约束限制：** 不涉及。

        :return: The index_params of this CreateCollectionBody.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.IndexParams`]
        """
        return self._index_params

    @index_params.setter
    def index_params(self, index_params):
        r"""Sets the index_params of this CreateCollectionBody.

        **参数解释：** 索引的配置信息。 **约束限制：** 不涉及。

        :param index_params: The index_params of this CreateCollectionBody.
        :type index_params: list[:class:`huaweicloudsdkdwr.v1.IndexParams`]
        """
        self._index_params = index_params

    @property
    def params(self):
        r"""Gets the params of this CreateCollectionBody.

        **参数解释：** collection常用参数。 **约束限制：** shards_num: 默认2，取值范围[1, 16] partitions_num: 默认4，取值范围[1, 1024]，若所有field的partition_key为false，则partitions_num固定为1。 max_length: 默认256，取值范围[1, 65535]，当primary_field.type为String时，指示String的最大长度。

        :return: The params of this CreateCollectionBody.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this CreateCollectionBody.

        **参数解释：** collection常用参数。 **约束限制：** shards_num: 默认2，取值范围[1, 16] partitions_num: 默认4，取值范围[1, 1024]，若所有field的partition_key为false，则partitions_num固定为1。 max_length: 默认256，取值范围[1, 65535]，当primary_field.type为String时，指示String的最大长度。

        :param params: The params of this CreateCollectionBody.
        :type params: dict(str, object)
        """
        self._params = params

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
        if not isinstance(other, CreateCollectionBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
