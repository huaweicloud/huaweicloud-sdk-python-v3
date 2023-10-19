# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchFaceByFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'faces': 'list[SearchFace]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'faces': 'faces',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, faces=None, x_request_id=None):
        """SearchFaceByFileResponse

        The model defined in huaweicloud sdk

        :param faces: [查找的人脸集合，详见[SearchFace](https://support.huaweicloud.com/api-face/face_02_0019.html)。调用失败时无此字段。](tag:hc) [查找的人脸集合，详见[SearchFace](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0019.html)。调用失败时无此字段。](tag:hk)
        :type faces: list[:class:`huaweicloudsdkfrs.v2.SearchFace`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(SearchFaceByFileResponse, self).__init__()

        self._faces = None
        self._x_request_id = None
        self.discriminator = None

        if faces is not None:
            self.faces = faces
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def faces(self):
        """Gets the faces of this SearchFaceByFileResponse.

        [查找的人脸集合，详见[SearchFace](https://support.huaweicloud.com/api-face/face_02_0019.html)。调用失败时无此字段。](tag:hc) [查找的人脸集合，详见[SearchFace](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0019.html)。调用失败时无此字段。](tag:hk)

        :return: The faces of this SearchFaceByFileResponse.
        :rtype: list[:class:`huaweicloudsdkfrs.v2.SearchFace`]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this SearchFaceByFileResponse.

        [查找的人脸集合，详见[SearchFace](https://support.huaweicloud.com/api-face/face_02_0019.html)。调用失败时无此字段。](tag:hc) [查找的人脸集合，详见[SearchFace](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0019.html)。调用失败时无此字段。](tag:hk)

        :param faces: The faces of this SearchFaceByFileResponse.
        :type faces: list[:class:`huaweicloudsdkfrs.v2.SearchFace`]
        """
        self._faces = faces

    @property
    def x_request_id(self):
        """Gets the x_request_id of this SearchFaceByFileResponse.

        :return: The x_request_id of this SearchFaceByFileResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this SearchFaceByFileResponse.

        :param x_request_id: The x_request_id of this SearchFaceByFileResponse.
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
        if not isinstance(other, SearchFaceByFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
