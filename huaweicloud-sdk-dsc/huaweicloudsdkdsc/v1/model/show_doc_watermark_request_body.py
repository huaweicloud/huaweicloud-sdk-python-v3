# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDocWatermarkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'doc_type': 'str',
        'file_password': 'str',
        'file': 'file'
    }

    attribute_map = {
        'doc_type': 'doc_type',
        'file_password': 'file_password',
        'file': 'file'
    }

    def __init__(self, doc_type=None, file_password=None, file=None):
        """ShowDocWatermarkRequestBody

        The model defined in huaweicloud sdk

        :param doc_type: 待提取水印的文档类型
        :type doc_type: str
        :param file_password: 解密文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。
        :type file_password: str
        :param file: 上传要提取水印的文档
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._doc_type = None
        self._file_password = None
        self._file = None
        self.discriminator = None

        self.doc_type = doc_type
        if file_password is not None:
            self.file_password = file_password
        self.file = file

    @property
    def doc_type(self):
        """Gets the doc_type of this ShowDocWatermarkRequestBody.

        待提取水印的文档类型

        :return: The doc_type of this ShowDocWatermarkRequestBody.
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this ShowDocWatermarkRequestBody.

        待提取水印的文档类型

        :param doc_type: The doc_type of this ShowDocWatermarkRequestBody.
        :type doc_type: str
        """
        self._doc_type = doc_type

    @property
    def file_password(self):
        """Gets the file_password of this ShowDocWatermarkRequestBody.

        解密文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :return: The file_password of this ShowDocWatermarkRequestBody.
        :rtype: str
        """
        return self._file_password

    @file_password.setter
    def file_password(self, file_password):
        """Sets the file_password of this ShowDocWatermarkRequestBody.

        解密文件的密码， 最大支持长度256。如果Office文档有读密码或域控的权限密码，请输入读密码，或者有读权限的域控密码。

        :param file_password: The file_password of this ShowDocWatermarkRequestBody.
        :type file_password: str
        """
        self._file_password = file_password

    @property
    def file(self):
        """Gets the file of this ShowDocWatermarkRequestBody.

        上传要提取水印的文档

        :return: The file of this ShowDocWatermarkRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ShowDocWatermarkRequestBody.

        上传要提取水印的文档

        :param file: The file of this ShowDocWatermarkRequestBody.
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
        if not isinstance(other, ShowDocWatermarkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
