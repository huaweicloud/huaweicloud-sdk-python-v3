# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAimMsgSignatureFileInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, file_id=None, offset=None, limit=None):
        """ShowAimMsgSignatureFileInfoRequest

        The model defined in huaweicloud sdk

        :param file_id: 营业执照/授权委托书文件ID。
        :type file_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: str
        :param limit: 每页显示的条目数量。
        :type limit: str
        """
        
        

        self._file_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.file_id = file_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def file_id(self):
        """Gets the file_id of this ShowAimMsgSignatureFileInfoRequest.

        营业执照/授权委托书文件ID。

        :return: The file_id of this ShowAimMsgSignatureFileInfoRequest.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ShowAimMsgSignatureFileInfoRequest.

        营业执照/授权委托书文件ID。

        :param file_id: The file_id of this ShowAimMsgSignatureFileInfoRequest.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def offset(self):
        """Gets the offset of this ShowAimMsgSignatureFileInfoRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this ShowAimMsgSignatureFileInfoRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowAimMsgSignatureFileInfoRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this ShowAimMsgSignatureFileInfoRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowAimMsgSignatureFileInfoRequest.

        每页显示的条目数量。

        :return: The limit of this ShowAimMsgSignatureFileInfoRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowAimMsgSignatureFileInfoRequest.

        每页显示的条目数量。

        :param limit: The limit of this ShowAimMsgSignatureFileInfoRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ShowAimMsgSignatureFileInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
