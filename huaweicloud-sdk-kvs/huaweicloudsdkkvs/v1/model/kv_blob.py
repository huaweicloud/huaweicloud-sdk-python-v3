# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KvBlob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary_key': 'dict',
        'xblob': 'bytes',
        'xattr': 'bytes'
    }

    attribute_map = {
        'primary_key': 'primary_key',
        'xblob': 'xblob',
        'xattr': 'xattr'
    }

    def __init__(self, primary_key=None, xblob=None, xattr=None):
        r"""KvBlob

        The model defined in huaweicloud sdk

        :param primary_key: 用户自定义的主键名及值。 &gt; 内容字段：主键字段名和值，组合索引多个元素。
        :type primary_key: dict
        :param xblob: 属性信息，最大2kb。
        :type xblob: :class:`huaweicloudsdkkvs.v1.bytes`
        :param xattr: 非结构化数据内容。
        :type xattr: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        
        

        self._primary_key = None
        self._xblob = None
        self._xattr = None
        self.discriminator = None

        self.primary_key = primary_key
        if xblob is not None:
            self.xblob = xblob
        if xattr is not None:
            self.xattr = xattr

    @property
    def primary_key(self):
        r"""Gets the primary_key of this KvBlob.

        用户自定义的主键名及值。 > 内容字段：主键字段名和值，组合索引多个元素。

        :return: The primary_key of this KvBlob.
        :rtype: dict
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        r"""Sets the primary_key of this KvBlob.

        用户自定义的主键名及值。 > 内容字段：主键字段名和值，组合索引多个元素。

        :param primary_key: The primary_key of this KvBlob.
        :type primary_key: dict
        """
        self._primary_key = primary_key

    @property
    def xblob(self):
        r"""Gets the xblob of this KvBlob.

        属性信息，最大2kb。

        :return: The xblob of this KvBlob.
        :rtype: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        return self._xblob

    @xblob.setter
    def xblob(self, xblob):
        r"""Sets the xblob of this KvBlob.

        属性信息，最大2kb。

        :param xblob: The xblob of this KvBlob.
        :type xblob: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        self._xblob = xblob

    @property
    def xattr(self):
        r"""Gets the xattr of this KvBlob.

        非结构化数据内容。

        :return: The xattr of this KvBlob.
        :rtype: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        return self._xattr

    @xattr.setter
    def xattr(self, xattr):
        r"""Sets the xattr of this KvBlob.

        非结构化数据内容。

        :param xattr: The xattr of this KvBlob.
        :type xattr: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        self._xattr = xattr

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
        if not isinstance(other, KvBlob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
