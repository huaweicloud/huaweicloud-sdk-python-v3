# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceCompareUrlReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image1_url': 'str',
        'image2_url': 'str'
    }

    attribute_map = {
        'image1_url': 'image1_url',
        'image2_url': 'image2_url'
    }

    def __init__(self, image1_url=None, image2_url=None):
        r"""FaceCompareUrlReq

        The model defined in huaweicloud sdk

        :param image1_url: [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。与image1_file、image1_base64三选一](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。与image1_file、image1_base64三选一](tag:hk)
        :type image1_url: str
        :param image2_url: [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。与image2_file、image2_base64三选一](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。与image2_file、image2_base64三选一](tag:hk)
        :type image2_url: str
        """
        
        

        self._image1_url = None
        self._image2_url = None
        self.discriminator = None

        self.image1_url = image1_url
        self.image2_url = image2_url

    @property
    def image1_url(self):
        r"""Gets the image1_url of this FaceCompareUrlReq.

        [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。与image1_file、image1_base64三选一](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。与image1_file、image1_base64三选一](tag:hk)

        :return: The image1_url of this FaceCompareUrlReq.
        :rtype: str
        """
        return self._image1_url

    @image1_url.setter
    def image1_url(self, image1_url):
        r"""Sets the image1_url of this FaceCompareUrlReq.

        [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。与image1_file、image1_base64三选一](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。与image1_file、image1_base64三选一](tag:hk)

        :param image1_url: The image1_url of this FaceCompareUrlReq.
        :type image1_url: str
        """
        self._image1_url = image1_url

    @property
    def image2_url(self):
        r"""Gets the image2_url of this FaceCompareUrlReq.

        [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。与image2_file、image2_base64三选一](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。与image2_file、image2_base64三选一](tag:hk)

        :return: The image2_url of this FaceCompareUrlReq.
        :rtype: str
        """
        return self._image2_url

    @image2_url.setter
    def image2_url(self, image2_url):
        r"""Sets the image2_url of this FaceCompareUrlReq.

        [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/api-face/face_02_0006.html)。与image2_file、image2_base64三选一](tag:hc) [图片的URL路径，目前仅支持华为云上OBS的URL，且人脸识别服务有权限读取该OBS桶的数据。开通读取权限的操作请参见[服务授权](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0006.html)。与image2_file、image2_base64三选一](tag:hk)

        :param image2_url: The image2_url of this FaceCompareUrlReq.
        :type image2_url: str
        """
        self._image2_url = image2_url

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
        if not isinstance(other, FaceCompareUrlReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
