# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadProductsRequest:

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
        'product_ids': 'list[int]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'product_ids': 'product_ids'
    }

    def __init__(self, instance_id=None, product_ids=None):
        """DownloadProductsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param product_ids: 待导出产品ID列表
        :type product_ids: list[int]
        """
        
        

        self._instance_id = None
        self._product_ids = None
        self.discriminator = None

        self.instance_id = instance_id
        if product_ids is not None:
            self.product_ids = product_ids

    @property
    def instance_id(self):
        """Gets the instance_id of this DownloadProductsRequest.

        实例ID

        :return: The instance_id of this DownloadProductsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DownloadProductsRequest.

        实例ID

        :param instance_id: The instance_id of this DownloadProductsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def product_ids(self):
        """Gets the product_ids of this DownloadProductsRequest.

        待导出产品ID列表

        :return: The product_ids of this DownloadProductsRequest.
        :rtype: list[int]
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """Sets the product_ids of this DownloadProductsRequest.

        待导出产品ID列表

        :param product_ids: The product_ids of this DownloadProductsRequest.
        :type product_ids: list[int]
        """
        self._product_ids = product_ids

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
        if not isinstance(other, DownloadProductsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
