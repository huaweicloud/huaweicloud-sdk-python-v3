# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataStoreDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_store_id': 'str',
        'data_store_group_id': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'data_store_id': 'data_store_id',
        'data_store_group_id': 'data_store_group_id',
        'product_id': 'product_id'
    }

    def __init__(self, data_store_id=None, data_store_group_id=None, product_id=None):
        """DataStoreDto

        The model defined in huaweicloud sdk

        :param data_store_id: 存储ID
        :type data_store_id: str
        :param data_store_group_id: 存储组ID
        :type data_store_group_id: str
        :param product_id: 产品ID
        :type product_id: str
        """
        
        

        self._data_store_id = None
        self._data_store_group_id = None
        self._product_id = None
        self.discriminator = None

        if data_store_id is not None:
            self.data_store_id = data_store_id
        if data_store_group_id is not None:
            self.data_store_group_id = data_store_group_id
        if product_id is not None:
            self.product_id = product_id

    @property
    def data_store_id(self):
        """Gets the data_store_id of this DataStoreDto.

        存储ID

        :return: The data_store_id of this DataStoreDto.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        """Sets the data_store_id of this DataStoreDto.

        存储ID

        :param data_store_id: The data_store_id of this DataStoreDto.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def data_store_group_id(self):
        """Gets the data_store_group_id of this DataStoreDto.

        存储组ID

        :return: The data_store_group_id of this DataStoreDto.
        :rtype: str
        """
        return self._data_store_group_id

    @data_store_group_id.setter
    def data_store_group_id(self, data_store_group_id):
        """Sets the data_store_group_id of this DataStoreDto.

        存储组ID

        :param data_store_group_id: The data_store_group_id of this DataStoreDto.
        :type data_store_group_id: str
        """
        self._data_store_group_id = data_store_group_id

    @property
    def product_id(self):
        """Gets the product_id of this DataStoreDto.

        产品ID

        :return: The product_id of this DataStoreDto.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DataStoreDto.

        产品ID

        :param product_id: The product_id of this DataStoreDto.
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
        if not isinstance(other, DataStoreDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
