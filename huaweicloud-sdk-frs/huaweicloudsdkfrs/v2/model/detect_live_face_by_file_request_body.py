# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectLiveFaceByFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_file': 'file'
    }

    attribute_map = {
        'image_file': 'image_file'
    }

    def __init__(self, image_file=None):
        r"""DetectLiveFaceByFileRequestBody

        The model defined in huaweicloud sdk

        :param image_file: 本地图片文件。上传文件时，请求格式为multipart。
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._image_file = None
        self.discriminator = None

        self.image_file = image_file

    @property
    def image_file(self):
        r"""Gets the image_file of this DetectLiveFaceByFileRequestBody.

        本地图片文件。上传文件时，请求格式为multipart。

        :return: The image_file of this DetectLiveFaceByFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        r"""Sets the image_file of this DetectLiveFaceByFileRequestBody.

        本地图片文件。上传文件时，请求格式为multipart。

        :param image_file: The image_file of this DetectLiveFaceByFileRequestBody.
        :type image_file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._image_file = image_file

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
        if not isinstance(other, DetectLiveFaceByFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
