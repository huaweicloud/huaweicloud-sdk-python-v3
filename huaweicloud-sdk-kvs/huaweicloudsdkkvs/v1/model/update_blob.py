# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBlob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'xattr': 'bytes',
        'offset': 'int',
        'len': 'int',
        'blob_data': 'bytes'
    }

    attribute_map = {
        'xattr': 'xattr',
        'offset': 'offset',
        'len': 'len',
        'blob_data': 'blob_data'
    }

    def __init__(self, xattr=None, offset=None, len=None, blob_data=None):
        r"""UpdateBlob

        The model defined in huaweicloud sdk

        :param xattr: 属性信息。
        :type xattr: :class:`huaweicloudsdkkvs.v1.bytes`
        :param offset: value部分的偏移位置。 &gt; - 超过value当前size无效 &gt; - \&quot;offset\&quot;与\&quot;len\&quot;与\&quot;blob_data\&quot; 要么都带，要么都不带。
        :type offset: int
        :param len: 更新内容长度。
        :type len: int
        :param blob_data: 二进制内容。
        :type blob_data: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        
        

        self._xattr = None
        self._offset = None
        self._len = None
        self._blob_data = None
        self.discriminator = None

        if xattr is not None:
            self.xattr = xattr
        if offset is not None:
            self.offset = offset
        if len is not None:
            self.len = len
        if blob_data is not None:
            self.blob_data = blob_data

    @property
    def xattr(self):
        r"""Gets the xattr of this UpdateBlob.

        属性信息。

        :return: The xattr of this UpdateBlob.
        :rtype: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        return self._xattr

    @xattr.setter
    def xattr(self, xattr):
        r"""Sets the xattr of this UpdateBlob.

        属性信息。

        :param xattr: The xattr of this UpdateBlob.
        :type xattr: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        self._xattr = xattr

    @property
    def offset(self):
        r"""Gets the offset of this UpdateBlob.

        value部分的偏移位置。 > - 超过value当前size无效 > - \"offset\"与\"len\"与\"blob_data\" 要么都带，要么都不带。

        :return: The offset of this UpdateBlob.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this UpdateBlob.

        value部分的偏移位置。 > - 超过value当前size无效 > - \"offset\"与\"len\"与\"blob_data\" 要么都带，要么都不带。

        :param offset: The offset of this UpdateBlob.
        :type offset: int
        """
        self._offset = offset

    @property
    def len(self):
        r"""Gets the len of this UpdateBlob.

        更新内容长度。

        :return: The len of this UpdateBlob.
        :rtype: int
        """
        return self._len

    @len.setter
    def len(self, len):
        r"""Sets the len of this UpdateBlob.

        更新内容长度。

        :param len: The len of this UpdateBlob.
        :type len: int
        """
        self._len = len

    @property
    def blob_data(self):
        r"""Gets the blob_data of this UpdateBlob.

        二进制内容。

        :return: The blob_data of this UpdateBlob.
        :rtype: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        return self._blob_data

    @blob_data.setter
    def blob_data(self, blob_data):
        r"""Sets the blob_data of this UpdateBlob.

        二进制内容。

        :param blob_data: The blob_data of this UpdateBlob.
        :type blob_data: :class:`huaweicloudsdkkvs.v1.bytes`
        """
        self._blob_data = blob_data

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
        if not isinstance(other, UpdateBlob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
