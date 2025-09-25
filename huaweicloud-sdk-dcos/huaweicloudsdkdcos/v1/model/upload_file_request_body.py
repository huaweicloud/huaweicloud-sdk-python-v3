# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scene_code': 'str',
        'file_name': 'str',
        'file': 'file'
    }

    attribute_map = {
        'scene_code': 'scene_code',
        'file_name': 'file_name',
        'file': 'file'
    }

    def __init__(self, scene_code=None, file_name=None, file=None):
        r"""UploadFileRequestBody

        The model defined in huaweicloud sdk

        :param scene_code: 文件上传场景,如服务单附件上传:order
        :type scene_code: str
        :param file_name: 文件名称,用户上传服务单附件的文件名
        :type file_name: str
        :param file: 文件,用户上传的服务单附件
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._scene_code = None
        self._file_name = None
        self._file = None
        self.discriminator = None

        self.scene_code = scene_code
        self.file_name = file_name
        self.file = file

    @property
    def scene_code(self):
        r"""Gets the scene_code of this UploadFileRequestBody.

        文件上传场景,如服务单附件上传:order

        :return: The scene_code of this UploadFileRequestBody.
        :rtype: str
        """
        return self._scene_code

    @scene_code.setter
    def scene_code(self, scene_code):
        r"""Sets the scene_code of this UploadFileRequestBody.

        文件上传场景,如服务单附件上传:order

        :param scene_code: The scene_code of this UploadFileRequestBody.
        :type scene_code: str
        """
        self._scene_code = scene_code

    @property
    def file_name(self):
        r"""Gets the file_name of this UploadFileRequestBody.

        文件名称,用户上传服务单附件的文件名

        :return: The file_name of this UploadFileRequestBody.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this UploadFileRequestBody.

        文件名称,用户上传服务单附件的文件名

        :param file_name: The file_name of this UploadFileRequestBody.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file(self):
        r"""Gets the file of this UploadFileRequestBody.

        文件,用户上传的服务单附件

        :return: The file of this UploadFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this UploadFileRequestBody.

        文件,用户上传的服务单附件

        :param file: The file of this UploadFileRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

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
        if not isinstance(other, UploadFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
