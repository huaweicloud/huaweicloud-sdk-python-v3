# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceDatabasesForHtapRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'limit': 'str',
        'offset': 'str',
        'body': 'QueryDataBaseRequestV3'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, x_language=None, instance_id=None, limit=None, offset=None, body=None):
        r"""ShowInstanceDatabasesForHtapRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        :param instance_id: **参数解释**：  HTAP标准版实例ID，严格匹配UUID规则。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，且长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param limit: **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  100。
        :type limit: str
        :param offset: **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0。
        :type offset: str
        :param body: Body of the ShowInstanceDatabasesForHtapRequest
        :type body: :class:`huaweicloudsdkgaussdb.v3.QueryDataBaseRequestV3`
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self._body = None
        self.discriminator = None

        self.x_language = x_language
        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this ShowInstanceDatabasesForHtapRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowInstanceDatabasesForHtapRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  HTAP标准版实例ID，严格匹配UUID规则。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，且长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowInstanceDatabasesForHtapRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  HTAP标准版实例ID，严格匹配UUID规则。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，且长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowInstanceDatabasesForHtapRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  100。

        :return: The limit of this ShowInstanceDatabasesForHtapRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  查询记录数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  100。

        :param limit: The limit of this ShowInstanceDatabasesForHtapRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0。

        :return: The offset of this ShowInstanceDatabasesForHtapRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowInstanceDatabasesForHtapRequest.

        **参数解释**：  索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0。

        :param offset: The offset of this ShowInstanceDatabasesForHtapRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ShowInstanceDatabasesForHtapRequest.

        :return: The body of this ShowInstanceDatabasesForHtapRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.QueryDataBaseRequestV3`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowInstanceDatabasesForHtapRequest.

        :param body: The body of this ShowInstanceDatabasesForHtapRequest.
        :type body: :class:`huaweicloudsdkgaussdb.v3.QueryDataBaseRequestV3`
        """
        self._body = body

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
        if not isinstance(other, ShowInstanceDatabasesForHtapRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
