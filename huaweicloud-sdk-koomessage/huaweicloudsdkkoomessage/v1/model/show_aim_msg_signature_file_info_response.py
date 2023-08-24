# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAimMsgSignatureFileInfoResponse(SdkResponse):

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
        'file_name': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'file_name': 'file_name'
    }

    def __init__(self, file_id=None, file_name=None):
        """ShowAimMsgSignatureFileInfoResponse

        The model defined in huaweicloud sdk

        :param file_id: 文件ID。
        :type file_id: str
        :param file_name: 文件名称。
        :type file_name: str
        """
        
        super(ShowAimMsgSignatureFileInfoResponse, self).__init__()

        self._file_id = None
        self._file_name = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if file_name is not None:
            self.file_name = file_name

    @property
    def file_id(self):
        """Gets the file_id of this ShowAimMsgSignatureFileInfoResponse.

        文件ID。

        :return: The file_id of this ShowAimMsgSignatureFileInfoResponse.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this ShowAimMsgSignatureFileInfoResponse.

        文件ID。

        :param file_id: The file_id of this ShowAimMsgSignatureFileInfoResponse.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def file_name(self):
        """Gets the file_name of this ShowAimMsgSignatureFileInfoResponse.

        文件名称。

        :return: The file_name of this ShowAimMsgSignatureFileInfoResponse.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ShowAimMsgSignatureFileInfoResponse.

        文件名称。

        :param file_name: The file_name of this ShowAimMsgSignatureFileInfoResponse.
        :type file_name: str
        """
        self._file_name = file_name

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
        if not isinstance(other, ShowAimMsgSignatureFileInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
