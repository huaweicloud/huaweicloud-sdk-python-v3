# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbcProductInfoOrderChange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'resource_size': 'int',
        'resource_size_measure_id': 'int',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'resource_size': 'resource_size',
        'resource_size_measure_id': 'resource_size_measure_id',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, product_id=None, resource_size=None, resource_size_measure_id=None, resource_spec_code=None):
        r"""CbcProductInfoOrderChange

        The model defined in huaweicloud sdk

        :param product_id: 产品标识，通过订购询价接口获得，长度限制：1-64，只能由字母、数字、“_”、“-”组成。
        :type product_id: str
        :param resource_size: 资源容量大小，取值范围：10-10485760
        :type resource_size: int
        :param resource_size_measure_id: 资源容量度量标识，枚举值17：GB
        :type resource_size_measure_id: int
        :param resource_spec_code: 用户购买云服务产品的资源规格 Enum: [vault.backup.server.normal，vault.backup.turbo.normal, vault.backup.database.normal，vault.backup.volume.normal，vault.backup.rds.normal，vault.replication.server.normal，vault.hybrid.server.normal]
        :type resource_spec_code: str
        """
        
        

        self._product_id = None
        self._resource_size = None
        self._resource_size_measure_id = None
        self._resource_spec_code = None
        self.discriminator = None

        self.product_id = product_id
        self.resource_size = resource_size
        if resource_size_measure_id is not None:
            self.resource_size_measure_id = resource_size_measure_id
        self.resource_spec_code = resource_spec_code

    @property
    def product_id(self):
        r"""Gets the product_id of this CbcProductInfoOrderChange.

        产品标识，通过订购询价接口获得，长度限制：1-64，只能由字母、数字、“_”、“-”组成。

        :return: The product_id of this CbcProductInfoOrderChange.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CbcProductInfoOrderChange.

        产品标识，通过订购询价接口获得，长度限制：1-64，只能由字母、数字、“_”、“-”组成。

        :param product_id: The product_id of this CbcProductInfoOrderChange.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def resource_size(self):
        r"""Gets the resource_size of this CbcProductInfoOrderChange.

        资源容量大小，取值范围：10-10485760

        :return: The resource_size of this CbcProductInfoOrderChange.
        :rtype: int
        """
        return self._resource_size

    @resource_size.setter
    def resource_size(self, resource_size):
        r"""Sets the resource_size of this CbcProductInfoOrderChange.

        资源容量大小，取值范围：10-10485760

        :param resource_size: The resource_size of this CbcProductInfoOrderChange.
        :type resource_size: int
        """
        self._resource_size = resource_size

    @property
    def resource_size_measure_id(self):
        r"""Gets the resource_size_measure_id of this CbcProductInfoOrderChange.

        资源容量度量标识，枚举值17：GB

        :return: The resource_size_measure_id of this CbcProductInfoOrderChange.
        :rtype: int
        """
        return self._resource_size_measure_id

    @resource_size_measure_id.setter
    def resource_size_measure_id(self, resource_size_measure_id):
        r"""Sets the resource_size_measure_id of this CbcProductInfoOrderChange.

        资源容量度量标识，枚举值17：GB

        :param resource_size_measure_id: The resource_size_measure_id of this CbcProductInfoOrderChange.
        :type resource_size_measure_id: int
        """
        self._resource_size_measure_id = resource_size_measure_id

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this CbcProductInfoOrderChange.

        用户购买云服务产品的资源规格 Enum: [vault.backup.server.normal，vault.backup.turbo.normal, vault.backup.database.normal，vault.backup.volume.normal，vault.backup.rds.normal，vault.replication.server.normal，vault.hybrid.server.normal]

        :return: The resource_spec_code of this CbcProductInfoOrderChange.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this CbcProductInfoOrderChange.

        用户购买云服务产品的资源规格 Enum: [vault.backup.server.normal，vault.backup.turbo.normal, vault.backup.database.normal，vault.backup.volume.normal，vault.backup.rds.normal，vault.replication.server.normal，vault.hybrid.server.normal]

        :param resource_spec_code: The resource_spec_code of this CbcProductInfoOrderChange.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, CbcProductInfoOrderChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
