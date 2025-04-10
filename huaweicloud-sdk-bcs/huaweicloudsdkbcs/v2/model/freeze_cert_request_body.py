# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreezeCertRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file'
    }

    attribute_map = {
        'file': 'file'
    }

    def __init__(self, file=None):
        r"""FreezeCertRequestBody

        The model defined in huaweicloud sdk

        :param file: 生成证书的zip文件（每次只允许上传一个证书文件，文件大小不大于30K，后缀名为.zip文件）
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._file = None
        self.discriminator = None

        if file is not None:
            self.file = file

    @property
    def file(self):
        r"""Gets the file of this FreezeCertRequestBody.

        生成证书的zip文件（每次只允许上传一个证书文件，文件大小不大于30K，后缀名为.zip文件）

        :return: The file of this FreezeCertRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this FreezeCertRequestBody.

        生成证书的zip文件（每次只允许上传一个证书文件，文件大小不大于30K，后缀名为.zip文件）

        :param file: The file of this FreezeCertRequestBody.
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
        if not isinstance(other, FreezeCertRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
