# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAttachmentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_type': 'str',
        'upload_file': 'file'
    }

    attribute_map = {
        'file_type': 'fileType',
        'upload_file': 'uploadFile'
    }

    def __init__(self, file_type=None, upload_file=None):
        r"""UploadAttachmentRequestBody

        The model defined in huaweicloud sdk

        :param file_type: 固定枚举，当前仅支持user_task/用户任务
        :type file_type: str
        :param upload_file: 导入的流程文件
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._file_type = None
        self._upload_file = None
        self.discriminator = None

        if file_type is not None:
            self.file_type = file_type
        self.upload_file = upload_file

    @property
    def file_type(self):
        r"""Gets the file_type of this UploadAttachmentRequestBody.

        固定枚举，当前仅支持user_task/用户任务

        :return: The file_type of this UploadAttachmentRequestBody.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this UploadAttachmentRequestBody.

        固定枚举，当前仅支持user_task/用户任务

        :param file_type: The file_type of this UploadAttachmentRequestBody.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def upload_file(self):
        r"""Gets the upload_file of this UploadAttachmentRequestBody.

        导入的流程文件

        :return: The upload_file of this UploadAttachmentRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._upload_file

    @upload_file.setter
    def upload_file(self, upload_file):
        r"""Sets the upload_file of this UploadAttachmentRequestBody.

        导入的流程文件

        :param upload_file: The upload_file of this UploadAttachmentRequestBody.
        :type upload_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._upload_file = upload_file

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UploadAttachmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
