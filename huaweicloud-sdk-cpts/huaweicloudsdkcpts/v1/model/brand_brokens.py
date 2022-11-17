# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BrandBrokens:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rec_bytes': 'list[float]',
        'sent_bytes': 'list[float]'
    }

    attribute_map = {
        'rec_bytes': 'recBytes',
        'sent_bytes': 'sentBytes'
    }

    def __init__(self, rec_bytes=None, sent_bytes=None):
        """BrandBrokens

        The model defined in huaweicloud sdk

        :param rec_bytes: 接收字节数
        :type rec_bytes: list[float]
        :param sent_bytes: 发送字节数
        :type sent_bytes: list[float]
        """
        
        

        self._rec_bytes = None
        self._sent_bytes = None
        self.discriminator = None

        if rec_bytes is not None:
            self.rec_bytes = rec_bytes
        if sent_bytes is not None:
            self.sent_bytes = sent_bytes

    @property
    def rec_bytes(self):
        """Gets the rec_bytes of this BrandBrokens.

        接收字节数

        :return: The rec_bytes of this BrandBrokens.
        :rtype: list[float]
        """
        return self._rec_bytes

    @rec_bytes.setter
    def rec_bytes(self, rec_bytes):
        """Sets the rec_bytes of this BrandBrokens.

        接收字节数

        :param rec_bytes: The rec_bytes of this BrandBrokens.
        :type rec_bytes: list[float]
        """
        self._rec_bytes = rec_bytes

    @property
    def sent_bytes(self):
        """Gets the sent_bytes of this BrandBrokens.

        发送字节数

        :return: The sent_bytes of this BrandBrokens.
        :rtype: list[float]
        """
        return self._sent_bytes

    @sent_bytes.setter
    def sent_bytes(self, sent_bytes):
        """Sets the sent_bytes of this BrandBrokens.

        发送字节数

        :param sent_bytes: The sent_bytes of this BrandBrokens.
        :type sent_bytes: list[float]
        """
        self._sent_bytes = sent_bytes

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
        if not isinstance(other, BrandBrokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
