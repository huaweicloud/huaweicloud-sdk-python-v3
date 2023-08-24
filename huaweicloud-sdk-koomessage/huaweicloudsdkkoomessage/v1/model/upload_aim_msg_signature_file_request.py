# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAimMsgSignatureFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_desc': 'str',
        'body': 'UploadAimMsgSignatureFileRequestBody'
    }

    attribute_map = {
        'file_desc': 'file_desc',
        'body': 'body'
    }

    def __init__(self, file_desc=None, body=None):
        """UploadAimMsgSignatureFileRequest

        The model defined in huaweicloud sdk

        :param file_desc: 文件描述。
        :type file_desc: str
        :param body: Body of the UploadAimMsgSignatureFileRequest
        :type body: :class:`huaweicloudsdkkoomessage.v1.UploadAimMsgSignatureFileRequestBody`
        """
        
        

        self._file_desc = None
        self._body = None
        self.discriminator = None

        if file_desc is not None:
            self.file_desc = file_desc
        if body is not None:
            self.body = body

    @property
    def file_desc(self):
        """Gets the file_desc of this UploadAimMsgSignatureFileRequest.

        文件描述。

        :return: The file_desc of this UploadAimMsgSignatureFileRequest.
        :rtype: str
        """
        return self._file_desc

    @file_desc.setter
    def file_desc(self, file_desc):
        """Sets the file_desc of this UploadAimMsgSignatureFileRequest.

        文件描述。

        :param file_desc: The file_desc of this UploadAimMsgSignatureFileRequest.
        :type file_desc: str
        """
        self._file_desc = file_desc

    @property
    def body(self):
        """Gets the body of this UploadAimMsgSignatureFileRequest.

        :return: The body of this UploadAimMsgSignatureFileRequest.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.UploadAimMsgSignatureFileRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadAimMsgSignatureFileRequest.

        :param body: The body of this UploadAimMsgSignatureFileRequest.
        :type body: :class:`huaweicloudsdkkoomessage.v1.UploadAimMsgSignatureFileRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UploadAimMsgSignatureFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
