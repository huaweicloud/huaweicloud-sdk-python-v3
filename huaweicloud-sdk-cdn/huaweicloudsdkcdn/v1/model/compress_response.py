# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompressResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compress_switch': 'int',
        'compress_rules': 'list[CompressRules]'
    }

    attribute_map = {
        'compress_switch': 'compress_switch',
        'compress_rules': 'compress_rules'
    }

    def __init__(self, compress_switch=None, compress_rules=None):
        """CompressResponse

        The model defined in huaweicloud sdk

        :param compress_switch: GZIP压缩开关。0关闭。1打开
        :type compress_switch: int
        :param compress_rules: GZIP压缩规则
        :type compress_rules: list[:class:`huaweicloudsdkcdn.v1.CompressRules`]
        """
        
        

        self._compress_switch = None
        self._compress_rules = None
        self.discriminator = None

        self.compress_switch = compress_switch
        if compress_rules is not None:
            self.compress_rules = compress_rules

    @property
    def compress_switch(self):
        """Gets the compress_switch of this CompressResponse.

        GZIP压缩开关。0关闭。1打开

        :return: The compress_switch of this CompressResponse.
        :rtype: int
        """
        return self._compress_switch

    @compress_switch.setter
    def compress_switch(self, compress_switch):
        """Sets the compress_switch of this CompressResponse.

        GZIP压缩开关。0关闭。1打开

        :param compress_switch: The compress_switch of this CompressResponse.
        :type compress_switch: int
        """
        self._compress_switch = compress_switch

    @property
    def compress_rules(self):
        """Gets the compress_rules of this CompressResponse.

        GZIP压缩规则

        :return: The compress_rules of this CompressResponse.
        :rtype: list[:class:`huaweicloudsdkcdn.v1.CompressRules`]
        """
        return self._compress_rules

    @compress_rules.setter
    def compress_rules(self, compress_rules):
        """Sets the compress_rules of this CompressResponse.

        GZIP压缩规则

        :param compress_rules: The compress_rules of this CompressResponse.
        :type compress_rules: list[:class:`huaweicloudsdkcdn.v1.CompressRules`]
        """
        self._compress_rules = compress_rules

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
        if not isinstance(other, CompressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
