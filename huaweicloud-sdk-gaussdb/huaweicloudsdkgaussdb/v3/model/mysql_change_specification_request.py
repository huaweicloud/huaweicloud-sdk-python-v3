# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlChangeSpecificationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resize_flavor': 'MysqlResizeFlavor',
        'is_auto_pay': 'str'
    }

    attribute_map = {
        'resize_flavor': 'resize_flavor',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, resize_flavor=None, is_auto_pay=None):
        """MysqlChangeSpecificationRequest

        The model defined in huaweicloud sdk

        :param resize_flavor: 
        :type resize_flavor: :class:`huaweicloudsdkgaussdb.v3.MysqlResizeFlavor`
        :param is_auto_pay: 变更包周期实例规格时可指定，表示是否自动从客户的账户中支付。true，为自动支付，默认该方式。false，为手动支付。
        :type is_auto_pay: str
        """
        
        

        self._resize_flavor = None
        self._is_auto_pay = None
        self.discriminator = None

        self.resize_flavor = resize_flavor
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def resize_flavor(self):
        """Gets the resize_flavor of this MysqlChangeSpecificationRequest.


        :return: The resize_flavor of this MysqlChangeSpecificationRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlResizeFlavor`
        """
        return self._resize_flavor

    @resize_flavor.setter
    def resize_flavor(self, resize_flavor):
        """Sets the resize_flavor of this MysqlChangeSpecificationRequest.


        :param resize_flavor: The resize_flavor of this MysqlChangeSpecificationRequest.
        :type resize_flavor: :class:`huaweicloudsdkgaussdb.v3.MysqlResizeFlavor`
        """
        self._resize_flavor = resize_flavor

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this MysqlChangeSpecificationRequest.

        变更包周期实例规格时可指定，表示是否自动从客户的账户中支付。true，为自动支付，默认该方式。false，为手动支付。

        :return: The is_auto_pay of this MysqlChangeSpecificationRequest.
        :rtype: str
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this MysqlChangeSpecificationRequest.

        变更包周期实例规格时可指定，表示是否自动从客户的账户中支付。true，为自动支付，默认该方式。false，为手动支付。

        :param is_auto_pay: The is_auto_pay of this MysqlChangeSpecificationRequest.
        :type is_auto_pay: str
        """
        self._is_auto_pay = is_auto_pay

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
        if not isinstance(other, MysqlChangeSpecificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
