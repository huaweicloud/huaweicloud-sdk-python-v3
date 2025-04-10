# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareFaceByBase64Response(SdkResponse):

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
        'similarity': 'float',
        'x_request_id': 'str'
    }

    attribute_map = {
        'image1_face': 'image1_face',
        'image2_face': 'image2_face',
        'similarity': 'similarity',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, image1_face=None, image2_face=None, similarity=None, x_request_id=None):
        r"""CompareFaceByBase64Response

        The model defined in huaweicloud sdk

        :param image1_face: 
        :type image1_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        :param image2_face: 
        :type image2_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        :param similarity: 人脸相似度，1表示最大，0表示最小，值越大表示越相似。一般情况下超过0.93即可认为是同一个人。 调用失败时无此字段。
        :type similarity: float
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CompareFaceByBase64Response, self).__init__()

        self._image1_face = None
        self._image2_face = None
        self._similarity = None
        self._x_request_id = None
        self.discriminator = None

        if image1_face is not None:
            self.image1_face = image1_face
        if image2_face is not None:
            self.image2_face = image2_face
        if similarity is not None:
            self.similarity = similarity
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def image1_face(self):
        r"""Gets the image1_face of this CompareFaceByBase64Response.

        :return: The image1_face of this CompareFaceByBase64Response.
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        return self._image1_face

    @image1_face.setter
    def image1_face(self, image1_face):
        r"""Sets the image1_face of this CompareFaceByBase64Response.

        :param image1_face: The image1_face of this CompareFaceByBase64Response.
        :type image1_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        self._image1_face = image1_face

    @property
    def image2_face(self):
        r"""Gets the image2_face of this CompareFaceByBase64Response.

        :return: The image2_face of this CompareFaceByBase64Response.
        :rtype: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        return self._image2_face

    @image2_face.setter
    def image2_face(self, image2_face):
        r"""Sets the image2_face of this CompareFaceByBase64Response.

        :param image2_face: The image2_face of this CompareFaceByBase64Response.
        :type image2_face: :class:`huaweicloudsdkfrs.v2.CompareFace`
        """
        self._image2_face = image2_face

    @property
    def similarity(self):
        r"""Gets the similarity of this CompareFaceByBase64Response.

        人脸相似度，1表示最大，0表示最小，值越大表示越相似。一般情况下超过0.93即可认为是同一个人。 调用失败时无此字段。

        :return: The similarity of this CompareFaceByBase64Response.
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        r"""Sets the similarity of this CompareFaceByBase64Response.

        人脸相似度，1表示最大，0表示最小，值越大表示越相似。一般情况下超过0.93即可认为是同一个人。 调用失败时无此字段。

        :param similarity: The similarity of this CompareFaceByBase64Response.
        :type similarity: float
        """
        self._similarity = similarity

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CompareFaceByBase64Response.

        :return: The x_request_id of this CompareFaceByBase64Response.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CompareFaceByBase64Response.

        :param x_request_id: The x_request_id of this CompareFaceByBase64Response.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CompareFaceByBase64Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
