# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddOrModifyAttributeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cust_attr_name': 'str'
    }

    attribute_map = {
        'cust_attr_name': 'cust_attr_name'
    }

    def __init__(self, cust_attr_name=None):
        """AddOrModifyAttributeReq

        The model defined in huaweicloud sdk

        :param cust_attr_name: 自定义属性名称
        :type cust_attr_name: str
        """
        
        

        self._cust_attr_name = None
        self.discriminator = None

        self.cust_attr_name = cust_attr_name

    @property
    def cust_attr_name(self):
        """Gets the cust_attr_name of this AddOrModifyAttributeReq.

        自定义属性名称

        :return: The cust_attr_name of this AddOrModifyAttributeReq.
        :rtype: str
        """
        return self._cust_attr_name

    @cust_attr_name.setter
    def cust_attr_name(self, cust_attr_name):
        """Sets the cust_attr_name of this AddOrModifyAttributeReq.

        自定义属性名称

        :param cust_attr_name: The cust_attr_name of this AddOrModifyAttributeReq.
        :type cust_attr_name: str
        """
        self._cust_attr_name = cust_attr_name

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
        if not isinstance(other, AddOrModifyAttributeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
