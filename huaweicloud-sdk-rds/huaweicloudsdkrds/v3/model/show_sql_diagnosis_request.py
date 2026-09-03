# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlDiagnosisRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'x_language': 'str',
        'category': 'str',
        'subcategory': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'category': 'category',
        'subcategory': 'subcategory',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, x_language=None, category=None, subcategory=None, offset=None, limit=None):
        r"""ShowSqlDiagnosisRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn **默认取值**：  en-us。
        :type x_language: str
        :param category: **参数解释**：  实例诊断类型。  **约束限制**：  不涉及。  **取值范围**：  - disk (当前仅支持传入该项)  **默认取值**：  不涉及。
        :type category: str
        :param subcategory: **参数解释**：  sql诊断类型。  **约束限制**：  不涉及。  **取值范围**：  - time (执行耗时长) - temp (临时表类) - sort (排序类) - ddl (DDL类)  **默认取值**：  不涉及。
        :type subcategory: str
        :param offset: **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0
        :type offset: str
        :param limit: **参数解释**：  查询记录数。默认为10，最小值为1，最大值为100。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  10
        :type limit: str
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._category = None
        self._subcategory = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        self.category = category
        self.subcategory = subcategory
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSqlDiagnosisRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowSqlDiagnosisRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSqlDiagnosisRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowSqlDiagnosisRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowSqlDiagnosisRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn **默认取值**：  en-us。

        :return: The x_language of this ShowSqlDiagnosisRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowSqlDiagnosisRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn **默认取值**：  en-us。

        :param x_language: The x_language of this ShowSqlDiagnosisRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def category(self):
        r"""Gets the category of this ShowSqlDiagnosisRequest.

        **参数解释**：  实例诊断类型。  **约束限制**：  不涉及。  **取值范围**：  - disk (当前仅支持传入该项)  **默认取值**：  不涉及。

        :return: The category of this ShowSqlDiagnosisRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowSqlDiagnosisRequest.

        **参数解释**：  实例诊断类型。  **约束限制**：  不涉及。  **取值范围**：  - disk (当前仅支持传入该项)  **默认取值**：  不涉及。

        :param category: The category of this ShowSqlDiagnosisRequest.
        :type category: str
        """
        self._category = category

    @property
    def subcategory(self):
        r"""Gets the subcategory of this ShowSqlDiagnosisRequest.

        **参数解释**：  sql诊断类型。  **约束限制**：  不涉及。  **取值范围**：  - time (执行耗时长) - temp (临时表类) - sort (排序类) - ddl (DDL类)  **默认取值**：  不涉及。

        :return: The subcategory of this ShowSqlDiagnosisRequest.
        :rtype: str
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        r"""Sets the subcategory of this ShowSqlDiagnosisRequest.

        **参数解释**：  sql诊断类型。  **约束限制**：  不涉及。  **取值范围**：  - time (执行耗时长) - temp (临时表类) - sort (排序类) - ddl (DDL类)  **默认取值**：  不涉及。

        :param subcategory: The subcategory of this ShowSqlDiagnosisRequest.
        :type subcategory: str
        """
        self._subcategory = subcategory

    @property
    def offset(self):
        r"""Gets the offset of this ShowSqlDiagnosisRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0

        :return: The offset of this ShowSqlDiagnosisRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowSqlDiagnosisRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  0

        :param offset: The offset of this ShowSqlDiagnosisRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowSqlDiagnosisRequest.

        **参数解释**：  查询记录数。默认为10，最小值为1，最大值为100。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  10

        :return: The limit of this ShowSqlDiagnosisRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowSqlDiagnosisRequest.

        **参数解释**：  查询记录数。默认为10，最小值为1，最大值为100。  **约束限制**：  不涉及。  **取值范围**：  不涉及  **默认取值**：  10

        :param limit: The limit of this ShowSqlDiagnosisRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ShowSqlDiagnosisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
