# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUploadFilesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upload_type': 'str',
        'files': 'list[MultipartFile]'
    }

    attribute_map = {
        'upload_type': 'upload_type',
        'files': 'files'
    }

    def __init__(self, upload_type=None, files=None):
        r"""BatchUploadFilesRequestBody

        The model defined in huaweicloud sdk

        :param upload_type: **参数解释**: 上传文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件。如果所有文件上传成功，接口返回文件名称和文件ID列表，服务保存上传的文件。如果批量上传的文件中存在上传失败的文件，接口返回上传成功和失败的文件信息，所有文件都不会被服务保存。 - k8s_yaml：k8s yaml文件。如果所有文件上传成功，接口返回文件名称和文件ID列表，服务保存上传的文件。如果批量上传的文件中存在上传失败的文件，接口返回上传成功和失败的文件信息，所有文件都不会被服务保存。  **默认取值**: 不涉及 
        :type upload_type: str
        :param files: **参数解释**: 上传的文件，支持批量上传 **约束限制**: 上传文件需要与upload_type的类型对应 **取值范围**: 单文件支持最大1M，10个。  **默认取值**: 不涉及 
        :type files: list[:class:`huaweicloudsdkhss.v5.MultipartFile`]
        """
        
        

        self._upload_type = None
        self._files = None
        self.discriminator = None

        self.upload_type = upload_type
        self.files = files

    @property
    def upload_type(self):
        r"""Gets the upload_type of this BatchUploadFilesRequestBody.

        **参数解释**: 上传文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件。如果所有文件上传成功，接口返回文件名称和文件ID列表，服务保存上传的文件。如果批量上传的文件中存在上传失败的文件，接口返回上传成功和失败的文件信息，所有文件都不会被服务保存。 - k8s_yaml：k8s yaml文件。如果所有文件上传成功，接口返回文件名称和文件ID列表，服务保存上传的文件。如果批量上传的文件中存在上传失败的文件，接口返回上传成功和失败的文件信息，所有文件都不会被服务保存。  **默认取值**: 不涉及 

        :return: The upload_type of this BatchUploadFilesRequestBody.
        :rtype: str
        """
        return self._upload_type

    @upload_type.setter
    def upload_type(self, upload_type):
        r"""Sets the upload_type of this BatchUploadFilesRequestBody.

        **参数解释**: 上传文件类型 **约束限制**: 不涉及 **取值范围**: - dockerfile：Dockerfile文件。如果所有文件上传成功，接口返回文件名称和文件ID列表，服务保存上传的文件。如果批量上传的文件中存在上传失败的文件，接口返回上传成功和失败的文件信息，所有文件都不会被服务保存。 - k8s_yaml：k8s yaml文件。如果所有文件上传成功，接口返回文件名称和文件ID列表，服务保存上传的文件。如果批量上传的文件中存在上传失败的文件，接口返回上传成功和失败的文件信息，所有文件都不会被服务保存。  **默认取值**: 不涉及 

        :param upload_type: The upload_type of this BatchUploadFilesRequestBody.
        :type upload_type: str
        """
        self._upload_type = upload_type

    @property
    def files(self):
        r"""Gets the files of this BatchUploadFilesRequestBody.

        **参数解释**: 上传的文件，支持批量上传 **约束限制**: 上传文件需要与upload_type的类型对应 **取值范围**: 单文件支持最大1M，10个。  **默认取值**: 不涉及 

        :return: The files of this BatchUploadFilesRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.MultipartFile`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this BatchUploadFilesRequestBody.

        **参数解释**: 上传的文件，支持批量上传 **约束限制**: 上传文件需要与upload_type的类型对应 **取值范围**: 单文件支持最大1M，10个。  **默认取值**: 不涉及 

        :param files: The files of this BatchUploadFilesRequestBody.
        :type files: list[:class:`huaweicloudsdkhss.v5.MultipartFile`]
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
        if not isinstance(other, BatchUploadFilesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
