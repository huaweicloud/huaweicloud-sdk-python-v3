# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUploadFilesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_file_info': 'list[BatchUploadFilesResponseInfoSuccessFileInfo]',
        'fail_file_info': 'list[BatchUploadFilesResponseInfoFailFileInfo]'
    }

    attribute_map = {
        'success_file_info': 'success_file_info',
        'fail_file_info': 'fail_file_info'
    }

    def __init__(self, success_file_info=None, fail_file_info=None):
        r"""BatchUploadFilesResponse

        The model defined in huaweicloud sdk

        :param success_file_info: 上传成功的文件信息列表。
        :type success_file_info: list[:class:`huaweicloudsdkhss.v5.BatchUploadFilesResponseInfoSuccessFileInfo`]
        :param fail_file_info: 上传失败的文件信息列表。
        :type fail_file_info: list[:class:`huaweicloudsdkhss.v5.BatchUploadFilesResponseInfoFailFileInfo`]
        """
        
        super(BatchUploadFilesResponse, self).__init__()

        self._success_file_info = None
        self._fail_file_info = None
        self.discriminator = None

        if success_file_info is not None:
            self.success_file_info = success_file_info
        if fail_file_info is not None:
            self.fail_file_info = fail_file_info

    @property
    def success_file_info(self):
        r"""Gets the success_file_info of this BatchUploadFilesResponse.

        上传成功的文件信息列表。

        :return: The success_file_info of this BatchUploadFilesResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.BatchUploadFilesResponseInfoSuccessFileInfo`]
        """
        return self._success_file_info

    @success_file_info.setter
    def success_file_info(self, success_file_info):
        r"""Sets the success_file_info of this BatchUploadFilesResponse.

        上传成功的文件信息列表。

        :param success_file_info: The success_file_info of this BatchUploadFilesResponse.
        :type success_file_info: list[:class:`huaweicloudsdkhss.v5.BatchUploadFilesResponseInfoSuccessFileInfo`]
        """
        self._success_file_info = success_file_info

    @property
    def fail_file_info(self):
        r"""Gets the fail_file_info of this BatchUploadFilesResponse.

        上传失败的文件信息列表。

        :return: The fail_file_info of this BatchUploadFilesResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.BatchUploadFilesResponseInfoFailFileInfo`]
        """
        return self._fail_file_info

    @fail_file_info.setter
    def fail_file_info(self, fail_file_info):
        r"""Sets the fail_file_info of this BatchUploadFilesResponse.

        上传失败的文件信息列表。

        :param fail_file_info: The fail_file_info of this BatchUploadFilesResponse.
        :type fail_file_info: list[:class:`huaweicloudsdkhss.v5.BatchUploadFilesResponseInfoFailFileInfo`]
        """
        self._fail_file_info = fail_file_info

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
        if not isinstance(other, BatchUploadFilesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
