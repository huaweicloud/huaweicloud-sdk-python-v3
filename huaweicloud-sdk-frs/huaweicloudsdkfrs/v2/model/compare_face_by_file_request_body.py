# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareFaceByFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image1_file': 'file',
        'image2_file': 'file'
    }

    attribute_map = {
        'image1_file': 'image1_file',
        'image2_file': 'image2_file'
    }

    def __init__(self, image1_file=None, image2_file=None):
        r"""CompareFaceByFileRequestBody

        The model defined in huaweicloud sdk

        :param image1_file: 本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。
        :type image1_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param image2_file: 本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。
        :type image2_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._image1_file = None
        self._image2_file = None
        self.discriminator = None

        self.image1_file = image1_file
        self.image2_file = image2_file

    @property
    def image1_file(self):
        r"""Gets the image1_file of this CompareFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。

        :return: The image1_file of this CompareFaceByFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._image1_file

    @image1_file.setter
    def image1_file(self, image1_file):
        r"""Sets the image1_file of this CompareFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。

        :param image1_file: The image1_file of this CompareFaceByFileRequestBody.
        :type image1_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._image1_file = image1_file

    @property
    def image2_file(self):
        r"""Gets the image2_file of this CompareFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。

        :return: The image2_file of this CompareFaceByFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._image2_file

    @image2_file.setter
    def image2_file(self, image2_file):
        r"""Sets the image2_file of this CompareFaceByFileRequestBody.

        本地图片文件，图片不能超过8MB。上传文件时，请求格式为multipart。

        :param image2_file: The image2_file of this CompareFaceByFileRequestBody.
        :type image2_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._image2_file = image2_file

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
        if not isinstance(other, CompareFaceByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
