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
        'product_id': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'product_id': 'product_id'
    }

    def __init__(self, engine=None, product_id=None):
        r"""ListEngineProductsRequest

        The model defined in huaweicloud sdk

        :param engine: 消息引擎的类型。
        :type engine: str
        :param product_id: 产品ID。
        :type product_id: str
        """
        
        

        self._engine = None
        self._product_id = None
        self.discriminator = None

        self.engine = engine
        if product_id is not None:
            self.product_id = product_id

    @property
    def engine(self):
        r"""Gets the engine of this ListEngineProductsRequest.

        消息引擎的类型。

        :return: The engine of this ListEngineProductsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ListEngineProductsRequest.

        消息引擎的类型。

        :param engine: The engine of this ListEngineProductsRequest.
        :type engine: str
        """
        self._engine = engine

    @property
    def product_id(self):
        r"""Gets the product_id of this ListEngineProductsRequest.

        产品ID。

        :return: The product_id of this ListEngineProductsRequest.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListEngineProductsRequest.

        产品ID。

        :param product_id: The product_id of this ListEngineProductsRequest.
        :type product_id: str
        """
        self._product_id = product_id

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
