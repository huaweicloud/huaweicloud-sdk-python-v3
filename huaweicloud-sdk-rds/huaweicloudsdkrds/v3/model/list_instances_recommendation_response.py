# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesRecommendationResponse(SdkResponse):

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
        'recommended_products': 'list[RecommendedProduct]'
    }

    attribute_map = {
        'engine': 'engine',
        'recommended_products': 'recommended_products'
    }

    def __init__(self, engine=None, recommended_products=None):
        """ListInstancesRecommendationResponse

        The model defined in huaweicloud sdk

        :param engine: 引擎类型
        :type engine: str
        :param recommended_products: 推荐商品信息
        :type recommended_products: list[:class:`huaweicloudsdkrds.v3.RecommendedProduct`]
        """
        
        super(ListInstancesRecommendationResponse, self).__init__()

        self._engine = None
        self._recommended_products = None
        self.discriminator = None

        if engine is not None:
            self.engine = engine
        if recommended_products is not None:
            self.recommended_products = recommended_products

    @property
    def engine(self):
        """Gets the engine of this ListInstancesRecommendationResponse.

        引擎类型

        :return: The engine of this ListInstancesRecommendationResponse.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListInstancesRecommendationResponse.

        引擎类型

        :param engine: The engine of this ListInstancesRecommendationResponse.
        :type engine: str
        """
        self._engine = engine

    @property
    def recommended_products(self):
        """Gets the recommended_products of this ListInstancesRecommendationResponse.

        推荐商品信息

        :return: The recommended_products of this ListInstancesRecommendationResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.RecommendedProduct`]
        """
        return self._recommended_products

    @recommended_products.setter
    def recommended_products(self, recommended_products):
        """Sets the recommended_products of this ListInstancesRecommendationResponse.

        推荐商品信息

        :param recommended_products: The recommended_products of this ListInstancesRecommendationResponse.
        :type recommended_products: list[:class:`huaweicloudsdkrds.v3.RecommendedProduct`]
        """
        self._recommended_products = recommended_products

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
        if not isinstance(other, ListInstancesRecommendationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
