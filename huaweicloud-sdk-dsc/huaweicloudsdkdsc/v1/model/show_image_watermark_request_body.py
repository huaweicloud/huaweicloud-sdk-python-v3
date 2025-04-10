# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowImageWatermarkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file',
        'mark_len': 'str'
    }

    attribute_map = {
        'file': 'file',
        'mark_len': 'mark_len'
    }

    def __init__(self, file=None, mark_len=None):
        r"""ShowImageWatermarkRequestBody

        The model defined in huaweicloud sdk

        :param file: 待提取暗水印的图片文件。
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param mark_len: 指定待提取水印的长度，mark_len长度大于0，小于32。设置后可以提升水印提取性能
        :type mark_len: str
        """
        
        

        self._file = None
        self._mark_len = None
        self.discriminator = None

        self.file = file
        if mark_len is not None:
            self.mark_len = mark_len

    @property
    def file(self):
        r"""Gets the file of this ShowImageWatermarkRequestBody.

        待提取暗水印的图片文件。

        :return: The file of this ShowImageWatermarkRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ShowImageWatermarkRequestBody.

        待提取暗水印的图片文件。

        :param file: The file of this ShowImageWatermarkRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def mark_len(self):
        r"""Gets the mark_len of this ShowImageWatermarkRequestBody.

        指定待提取水印的长度，mark_len长度大于0，小于32。设置后可以提升水印提取性能

        :return: The mark_len of this ShowImageWatermarkRequestBody.
        :rtype: str
        """
        return self._mark_len

    @mark_len.setter
    def mark_len(self, mark_len):
        r"""Sets the mark_len of this ShowImageWatermarkRequestBody.

        指定待提取水印的长度，mark_len长度大于0，小于32。设置后可以提升水印提取性能

        :param mark_len: The mark_len of this ShowImageWatermarkRequestBody.
        :type mark_len: str
        """
        self._mark_len = mark_len

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
        if not isinstance(other, ShowImageWatermarkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
