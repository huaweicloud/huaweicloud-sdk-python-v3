# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtlSpecification:

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
        'expire_after_seconds': 'int',
        'field_name': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'expire_after_seconds': 'expire_after_seconds',
        'field_name': 'field_name'
    }

    def __init__(self, enable=None, expire_after_seconds=None, field_name=None):
        r"""TtlSpecification

        The model defined in huaweicloud sdk

        :param enable: TTL开关
        :type enable: bool
        :param expire_after_seconds: 生存时间，以秒为单位
        :type expire_after_seconds: int
        :param field_name: 文档中记录TTL过期时间的字段名，字段值为UTC时间，单位秒
        :type field_name: str
        """
        
        

        self._enable = None
        self._expire_after_seconds = None
        self._field_name = None
        self.discriminator = None

        self.enable = enable
        if expire_after_seconds is not None:
            self.expire_after_seconds = expire_after_seconds
        if field_name is not None:
            self.field_name = field_name

    @property
    def enable(self):
        r"""Gets the enable of this TtlSpecification.

        TTL开关

        :return: The enable of this TtlSpecification.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this TtlSpecification.

        TTL开关

        :param enable: The enable of this TtlSpecification.
        :type enable: bool
        """
        self._enable = enable

    @property
    def expire_after_seconds(self):
        r"""Gets the expire_after_seconds of this TtlSpecification.

        生存时间，以秒为单位

        :return: The expire_after_seconds of this TtlSpecification.
        :rtype: int
        """
        return self._expire_after_seconds

    @expire_after_seconds.setter
    def expire_after_seconds(self, expire_after_seconds):
        r"""Sets the expire_after_seconds of this TtlSpecification.

        生存时间，以秒为单位

        :param expire_after_seconds: The expire_after_seconds of this TtlSpecification.
        :type expire_after_seconds: int
        """
        self._expire_after_seconds = expire_after_seconds

    @property
    def field_name(self):
        r"""Gets the field_name of this TtlSpecification.

        文档中记录TTL过期时间的字段名，字段值为UTC时间，单位秒

        :return: The field_name of this TtlSpecification.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this TtlSpecification.

        文档中记录TTL过期时间的字段名，字段值为UTC时间，单位秒

        :param field_name: The field_name of this TtlSpecification.
        :type field_name: str
        """
        self._field_name = field_name

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
        if not isinstance(other, TtlSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
