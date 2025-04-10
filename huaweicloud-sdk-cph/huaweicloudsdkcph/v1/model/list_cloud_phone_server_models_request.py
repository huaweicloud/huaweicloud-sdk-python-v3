# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhoneServerModelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_type': 'int'
    }

    attribute_map = {
        'product_type': 'product_type'
    }

    def __init__(self, product_type=None):
        r"""ListCloudPhoneServerModelsRequest

        The model defined in huaweicloud sdk

        :param product_type: 产品类型。 - 0：云手机 - 1：云手游
        :type product_type: int
        """
        
        

        self._product_type = None
        self.discriminator = None

        if product_type is not None:
            self.product_type = product_type

    @property
    def product_type(self):
        r"""Gets the product_type of this ListCloudPhoneServerModelsRequest.

        产品类型。 - 0：云手机 - 1：云手游

        :return: The product_type of this ListCloudPhoneServerModelsRequest.
        :rtype: int
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this ListCloudPhoneServerModelsRequest.

        产品类型。 - 0：云手机 - 1：云手游

        :param product_type: The product_type of this ListCloudPhoneServerModelsRequest.
        :type product_type: int
        """
        self._product_type = product_type

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
        if not isinstance(other, ListCloudPhoneServerModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
