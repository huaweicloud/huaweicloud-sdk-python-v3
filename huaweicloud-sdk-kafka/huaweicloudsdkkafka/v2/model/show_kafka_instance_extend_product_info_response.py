# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaInstanceExtendProductInfoResponse(SdkResponse):

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
        'versions': 'list[str]',
        'products': 'list[ExtendProductInfoEntity]'
    }

    attribute_map = {
        'engine': 'engine',
        'versions': 'versions',
        'products': 'products'
    }

    def __init__(self, engine=None, versions=None, products=None):
        r"""ShowKafkaInstanceExtendProductInfoResponse

        The model defined in huaweicloud sdk

        :param engine: 消息引擎类型：kafka。
        :type engine: str
        :param versions: 消息引擎支持的版本。
        :type versions: list[str]
        :param products: 规格变更的产品信息。
        :type products: list[:class:`huaweicloudsdkkafka.v2.ExtendProductInfoEntity`]
        """
        
        super(ShowKafkaInstanceExtendProductInfoResponse, self).__init__()

        self._engine = None
        self._versions = None
        self._products = None
        self.discriminator = None

        if engine is not None:
            self.engine = engine
        if versions is not None:
            self.versions = versions
        if products is not None:
            self.products = products

    @property
    def engine(self):
        r"""Gets the engine of this ShowKafkaInstanceExtendProductInfoResponse.

        消息引擎类型：kafka。

        :return: The engine of this ShowKafkaInstanceExtendProductInfoResponse.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ShowKafkaInstanceExtendProductInfoResponse.

        消息引擎类型：kafka。

        :param engine: The engine of this ShowKafkaInstanceExtendProductInfoResponse.
        :type engine: str
        """
        self._engine = engine

    @property
    def versions(self):
        r"""Gets the versions of this ShowKafkaInstanceExtendProductInfoResponse.

        消息引擎支持的版本。

        :return: The versions of this ShowKafkaInstanceExtendProductInfoResponse.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this ShowKafkaInstanceExtendProductInfoResponse.

        消息引擎支持的版本。

        :param versions: The versions of this ShowKafkaInstanceExtendProductInfoResponse.
        :type versions: list[str]
        """
        self._versions = versions

    @property
    def products(self):
        r"""Gets the products of this ShowKafkaInstanceExtendProductInfoResponse.

        规格变更的产品信息。

        :return: The products of this ShowKafkaInstanceExtendProductInfoResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ExtendProductInfoEntity`]
        """
        return self._products

    @products.setter
    def products(self, products):
        r"""Sets the products of this ShowKafkaInstanceExtendProductInfoResponse.

        规格变更的产品信息。

        :param products: The products of this ShowKafkaInstanceExtendProductInfoResponse.
        :type products: list[:class:`huaweicloudsdkkafka.v2.ExtendProductInfoEntity`]
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
        if not isinstance(other, ShowKafkaInstanceExtendProductInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
