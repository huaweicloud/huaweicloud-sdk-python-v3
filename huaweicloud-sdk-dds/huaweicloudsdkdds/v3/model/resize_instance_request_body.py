# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resize': 'ResizeInstanceOption',
        'is_auto_pay': 'bool'
    }

    attribute_map = {
        'resize': 'resize',
        'is_auto_pay': 'is_auto_pay'
    }

    def __init__(self, resize=None, is_auto_pay=None):
        """ResizeInstanceRequestBody

        The model defined in huaweicloud sdk

        :param resize: 
        :type resize: :class:`huaweicloudsdkdds.v3.ResizeInstanceOption`
        :param is_auto_pay: 变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - 对于降低规格场景，该字段无效。 - 对于扩大规格场景：   - true，表示自动从账户中支付。   - false，表示手动从账户中支付，默认为该方式。
        :type is_auto_pay: bool
        """
        
        

        self._resize = None
        self._is_auto_pay = None
        self.discriminator = None

        self.resize = resize
        if is_auto_pay is not None:
            self.is_auto_pay = is_auto_pay

    @property
    def resize(self):
        """Gets the resize of this ResizeInstanceRequestBody.

        :return: The resize of this ResizeInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkdds.v3.ResizeInstanceOption`
        """
        return self._resize

    @resize.setter
    def resize(self, resize):
        """Sets the resize of this ResizeInstanceRequestBody.

        :param resize: The resize of this ResizeInstanceRequestBody.
        :type resize: :class:`huaweicloudsdkdds.v3.ResizeInstanceOption`
        """
        self._resize = resize

    @property
    def is_auto_pay(self):
        """Gets the is_auto_pay of this ResizeInstanceRequestBody.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - 对于降低规格场景，该字段无效。 - 对于扩大规格场景：   - true，表示自动从账户中支付。   - false，表示手动从账户中支付，默认为该方式。

        :return: The is_auto_pay of this ResizeInstanceRequestBody.
        :rtype: bool
        """
        return self._is_auto_pay

    @is_auto_pay.setter
    def is_auto_pay(self, is_auto_pay):
        """Sets the is_auto_pay of this ResizeInstanceRequestBody.

        变更包年包月实例规格时可指定，表示是否自动从账户中支付，此字段不影响自动续订的支付方式。 - 对于降低规格场景，该字段无效。 - 对于扩大规格场景：   - true，表示自动从账户中支付。   - false，表示手动从账户中支付，默认为该方式。

        :param is_auto_pay: The is_auto_pay of this ResizeInstanceRequestBody.
        :type is_auto_pay: bool
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
        if not isinstance(other, ResizeInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
