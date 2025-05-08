# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEngineProductsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'type': 'str',
        'product_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'engine': 'engine',
        'type': 'type',
        'product_id': 'product_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, engine=None, type=None, product_id=None, limit=None, offset=None):
        r"""ListEngineProductsRequest

        The model defined in huaweicloud sdk

        :param engine: **参数解释**： 消息引擎的类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type engine: str
        :param type: **参数解释**： 产品类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type type: str
        :param product_id: **参数解释**： 产品ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type product_id: str
        :param limit: **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。
        :type limit: int
        :param offset: **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。
        :type offset: int
        """
        
        

        self._engine = None
        self._type = None
        self._product_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.engine = engine
        self.type = type
        self.product_id = product_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def engine(self):
        r"""Gets the engine of this ListEngineProductsRequest.

        **参数解释**： 消息引擎的类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The engine of this ListEngineProductsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListEngineProductsRequest.

        **参数解释**： 消息引擎的类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param engine: The engine of this ListEngineProductsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def type(self):
        r"""Gets the type of this ListEngineProductsRequest.

        **参数解释**： 产品类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The type of this ListEngineProductsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListEngineProductsRequest.

        **参数解释**： 产品类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param type: The type of this ListEngineProductsRequest.
        :type type: str
        """
        self._type = type

    @property
    def product_id(self):
        r"""Gets the product_id of this ListEngineProductsRequest.

        **参数解释**： 产品ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The product_id of this ListEngineProductsRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListEngineProductsRequest.

        **参数解释**： 产品ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param product_id: The product_id of this ListEngineProductsRequest.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def limit(self):
        r"""Gets the limit of this ListEngineProductsRequest.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。

        :return: The limit of this ListEngineProductsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEngineProductsRequest.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 10。

        :param limit: The limit of this ListEngineProductsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListEngineProductsRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :return: The offset of this ListEngineProductsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEngineProductsRequest.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :param offset: The offset of this ListEngineProductsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListEngineProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
