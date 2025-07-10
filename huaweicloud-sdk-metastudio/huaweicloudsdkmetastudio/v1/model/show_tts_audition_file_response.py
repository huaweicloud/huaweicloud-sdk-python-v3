# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTtsAuditionFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_file_complete': 'bool',
        'message': 'str',
        'files': 'list[AuditionFile]'
    }

    attribute_map = {
        'is_file_complete': 'is_file_complete',
        'message': 'message',
        'files': 'files'
    }

    def __init__(self, is_file_complete=None, message=None, files=None):
        r"""ShowTtsAuditionFileResponse

        The model defined in huaweicloud sdk

        :param is_file_complete: 试听文件是否已生成完成。该标记为false时，应该每隔5秒再次调用本接口获取试听文件。当存在该参数时，将会返回以下message和files两个字段信息
        :type is_file_complete: bool
        :param message: 异常信息。
        :type message: str
        :param files: 试听文件列表。
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.AuditionFile`]
        """
        
        super(ShowTtsAuditionFileResponse, self).__init__()

        self._is_file_complete = None
        self._message = None
        self._files = None
        self.discriminator = None

        if is_file_complete is not None:
            self.is_file_complete = is_file_complete
        if message is not None:
            self.message = message
        if files is not None:
            self.files = files

    @property
    def is_file_complete(self):
        r"""Gets the is_file_complete of this ShowTtsAuditionFileResponse.

        试听文件是否已生成完成。该标记为false时，应该每隔5秒再次调用本接口获取试听文件。当存在该参数时，将会返回以下message和files两个字段信息

        :return: The is_file_complete of this ShowTtsAuditionFileResponse.
        :rtype: bool
        """
        return self._is_file_complete

    @is_file_complete.setter
    def is_file_complete(self, is_file_complete):
        r"""Sets the is_file_complete of this ShowTtsAuditionFileResponse.

        试听文件是否已生成完成。该标记为false时，应该每隔5秒再次调用本接口获取试听文件。当存在该参数时，将会返回以下message和files两个字段信息

        :param is_file_complete: The is_file_complete of this ShowTtsAuditionFileResponse.
        :type is_file_complete: bool
        """
        self._is_file_complete = is_file_complete

    @property
    def message(self):
        r"""Gets the message of this ShowTtsAuditionFileResponse.

        异常信息。

        :return: The message of this ShowTtsAuditionFileResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowTtsAuditionFileResponse.

        异常信息。

        :param message: The message of this ShowTtsAuditionFileResponse.
        :type message: str
        """
        self._message = message

    @property
    def files(self):
        r"""Gets the files of this ShowTtsAuditionFileResponse.

        试听文件列表。

        :return: The files of this ShowTtsAuditionFileResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.AuditionFile`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this ShowTtsAuditionFileResponse.

        试听文件列表。

        :param files: The files of this ShowTtsAuditionFileResponse.
        :type files: list[:class:`huaweicloudsdkmetastudio.v1.AuditionFile`]
        """
        self._files = files

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
        if not isinstance(other, ShowTtsAuditionFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
