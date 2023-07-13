# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareFaceByUrlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image1_face': 'CompareFace',
        'image2_face': 'CompareFace',
        'similarity': 'float'
    }

    attribute_map = {
        'image1_face': 'image1_face',
        'image2_face': 'image2_face',
        'similarity': 'similarity'
    }

    def __init__(self, image1_face=None, image2_face=None, similarity=None):
        """CompareFaceByUrlResponse

        The model defined in huaweicloud sdk

        :param image1_face: 
        :type image1_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        :param image2_face: 
        :type image2_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        :param similarity: 人脸相似度，1表示最大，0表示最小，值越大表示越相似。一般情况下超过0.93即可认为是同一个人。 调用失败时无此字段。
        :type similarity: float
        """
        
        super(CompareFaceByUrlResponse, self).__init__()

        self._image1_face = None
        self._image2_face = None
        self._similarity = None
        self.discriminator = None

        if image1_face is not None:
            self.image1_face = image1_face
        if image2_face is not None:
            self.image2_face = image2_face
        if similarity is not None:
            self.similarity = similarity

    @property
    def image1_face(self):
        """Gets the image1_face of this CompareFaceByUrlResponse.

        :return: The image1_face of this CompareFaceByUrlResponse.
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        return self._image1_face

    @image1_face.setter
    def image1_face(self, image1_face):
        """Sets the image1_face of this CompareFaceByUrlResponse.

        :param image1_face: The image1_face of this CompareFaceByUrlResponse.
        :type image1_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        self._image1_face = image1_face

    @property
    def image2_face(self):
        """Gets the image2_face of this CompareFaceByUrlResponse.

        :return: The image2_face of this CompareFaceByUrlResponse.
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        return self._image2_face

    @image2_face.setter
    def image2_face(self, image2_face):
        """Sets the image2_face of this CompareFaceByUrlResponse.

        :param image2_face: The image2_face of this CompareFaceByUrlResponse.
        :type image2_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        self._image2_face = image2_face

    @property
    def similarity(self):
        """Gets the similarity of this CompareFaceByUrlResponse.

        人脸相似度，1表示最大，0表示最小，值越大表示越相似。一般情况下超过0.93即可认为是同一个人。 调用失败时无此字段。

        :return: The similarity of this CompareFaceByUrlResponse.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this CompareFaceByUrlResponse.

        人脸相似度，1表示最大，0表示最小，值越大表示越相似。一般情况下超过0.93即可认为是同一个人。 调用失败时无此字段。

        :param similarity: The similarity of this CompareFaceByUrlResponse.
        :type similarity: float
        """
        self._similarity = similarity

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
        if not isinstance(other, CompareFaceByUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
