# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBatchTaskFilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'files': 'list[BatchTaskFile]'
    }

    attribute_map = {
        'files': 'files'
    }

    def __init__(self, files=None):
        r"""ListBatchTaskFilesResponse

        The model defined in huaweicloud sdk

        :param files: 批量任务文件列表。
        :type files: list[:class:`huaweicloudsdkiotda.v5.BatchTaskFile`]
        """
        
        super(ListBatchTaskFilesResponse, self).__init__()

        self._files = None
        self.discriminator = None

        if files is not None:
            self.files = files

    @property
    def files(self):
        r"""Gets the files of this ListBatchTaskFilesResponse.

        批量任务文件列表。

        :return: The files of this ListBatchTaskFilesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.BatchTaskFile`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this ListBatchTaskFilesResponse.

        批量任务文件列表。

        :param files: The files of this ListBatchTaskFilesResponse.
        :type files: list[:class:`huaweicloudsdkiotda.v5.BatchTaskFile`]
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
        if not isinstance(other, ListBatchTaskFilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
