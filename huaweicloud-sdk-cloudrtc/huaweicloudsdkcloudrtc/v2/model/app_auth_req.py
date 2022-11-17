# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppAuthReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'expire': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'expire': 'expire'
    }

    def __init__(self, enable=None, expire=None):
        """AppAuthReq

        The model defined in huaweicloud sdk

        :param enable: 开启或关闭URL鉴权
        :type enable: bool
        :param expire: 有效期，当开启鉴权时必填。  取值范围：[60，2592000]，缺省为300。  单位：秒。 
        :type expire: int
        """
        
        

        self._enable = None
        self._expire = None
        self.discriminator = None

        self.enable = enable
        if expire is not None:
            self.expire = expire

    @property
    def enable(self):
        """Gets the enable of this AppAuthReq.

        开启或关闭URL鉴权

        :return: The enable of this AppAuthReq.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this AppAuthReq.

        开启或关闭URL鉴权

        :param enable: The enable of this AppAuthReq.
        :type enable: bool
        """
        self._enable = enable

    @property
    def expire(self):
        """Gets the expire of this AppAuthReq.

        有效期，当开启鉴权时必填。  取值范围：[60，2592000]，缺省为300。  单位：秒。 

        :return: The expire of this AppAuthReq.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        """Sets the expire of this AppAuthReq.

        有效期，当开启鉴权时必填。  取值范围：[60，2592000]，缺省为300。  单位：秒。 

        :param expire: The expire of this AppAuthReq.
        :type expire: int
        """
        self._expire = expire

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
        if not isinstance(other, AppAuthReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
