# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEngineProductsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'float',
        'next_offset': 'int',
        'previous_offset': 'int',
        'engine': 'str',
        'versions': 'list[str]',
        'products': 'list[ProductEntity]'
    }

    attribute_map = {
        'total': 'total',
        'next_offset': 'next_offset',
        'previous_offset': 'previous_offset',
        'engine': 'engine',
        'versions': 'versions',
        'products': 'products'
    }

    def __init__(self, total=None, next_offset=None, previous_offset=None, engine=None, versions=None, products=None):
        r"""ListEngineProductsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**： 总数。 **取值范围**： 大于等于0。
        :type total: float
        :param next_offset: **参数解释**： 下个分页的offset。 **取值范围**： 大于等于0。
        :type next_offset: int
        :param previous_offset: **参数解释**： 上个分页的offset。 **取值范围**： 大于等于0。
        :type previous_offset: int
        :param engine: **参数解释**： 引擎类型。 **取值范围**： 不涉及。
        :type engine: str
        :param versions: **参数解释**： 支持的版本。
        :type versions: list[str]
        :param products: **参数解释**： 产品详情列表。
        :type products: list[:class:`huaweicloudsdkrocketmq.v2.ProductEntity`]
        """
        
        super(ListEngineProductsResponse, self).__init__()

        self._total = None
        self._next_offset = None
        self._previous_offset = None
        self._engine = None
        self._versions = None
        self._products = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if next_offset is not None:
            self.next_offset = next_offset
        if previous_offset is not None:
            self.previous_offset = previous_offset
        if engine is not None:
            self.engine = engine
        if versions is not None:
            self.versions = versions
        if products is not None:
            self.products = products

    @property
    def total(self):
        r"""Gets the total of this ListEngineProductsResponse.

        **参数解释**： 总数。 **取值范围**： 大于等于0。

        :return: The total of this ListEngineProductsResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListEngineProductsResponse.

        **参数解释**： 总数。 **取值范围**： 大于等于0。

        :param total: The total of this ListEngineProductsResponse.
        :type total: float
        """
        self._total = total

    @property
    def next_offset(self):
        r"""Gets the next_offset of this ListEngineProductsResponse.

        **参数解释**： 下个分页的offset。 **取值范围**： 大于等于0。

        :return: The next_offset of this ListEngineProductsResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        r"""Sets the next_offset of this ListEngineProductsResponse.

        **参数解释**： 下个分页的offset。 **取值范围**： 大于等于0。

        :param next_offset: The next_offset of this ListEngineProductsResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def previous_offset(self):
        r"""Gets the previous_offset of this ListEngineProductsResponse.

        **参数解释**： 上个分页的offset。 **取值范围**： 大于等于0。

        :return: The previous_offset of this ListEngineProductsResponse.
        :rtype: int
        """
        return self._previous_offset

    @previous_offset.setter
    def previous_offset(self, previous_offset):
        r"""Sets the previous_offset of this ListEngineProductsResponse.

        **参数解释**： 上个分页的offset。 **取值范围**： 大于等于0。

        :param previous_offset: The previous_offset of this ListEngineProductsResponse.
        :type previous_offset: int
        """
        self._previous_offset = previous_offset

    @property
    def engine(self):
        r"""Gets the engine of this ListEngineProductsResponse.

        **参数解释**： 引擎类型。 **取值范围**： 不涉及。

        :return: The engine of this ListEngineProductsResponse.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListEngineProductsResponse.

        **参数解释**： 引擎类型。 **取值范围**： 不涉及。

        :param engine: The engine of this ListEngineProductsResponse.
        :type engine: str
        """
        self._engine = engine

    @property
    def versions(self):
        r"""Gets the versions of this ListEngineProductsResponse.

        **参数解释**： 支持的版本。

        :return: The versions of this ListEngineProductsResponse.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ListEngineProductsResponse.

        **参数解释**： 支持的版本。

        :param versions: The versions of this ListEngineProductsResponse.
        :type versions: list[str]
        """
        self._versions = versions

    @property
    def products(self):
        r"""Gets the products of this ListEngineProductsResponse.

        **参数解释**： 产品详情列表。

        :return: The products of this ListEngineProductsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ProductEntity`]
        """
        return self._products

    @products.setter
    def products(self, products):
        r"""Sets the products of this ListEngineProductsResponse.

        **参数解释**： 产品详情列表。

        :param products: The products of this ListEngineProductsResponse.
        :type products: list[:class:`huaweicloudsdkrocketmq.v2.ProductEntity`]
        """
        self._products = products

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
        if not isinstance(other, ListEngineProductsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
