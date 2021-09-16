# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddFacesByBase64Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'face_set_id': 'str',
        'face_set_name': 'str',
        'faces': 'list[FaceSetFace]'
    }

    attribute_map = {
        'face_set_id': 'face_set_id',
        'face_set_name': 'face_set_name',
        'faces': 'faces'
    }

    def __init__(self, face_set_id=None, face_set_name=None, faces=None):
        """AddFacesByBase64Response - a model defined in huaweicloud sdk"""
        
        super(AddFacesByBase64Response, self).__init__()

        self._face_set_id = None
        self._face_set_name = None
        self._faces = None
        self.discriminator = None

        if face_set_id is not None:
            self.face_set_id = face_set_id
        if face_set_name is not None:
            self.face_set_name = face_set_name
        if faces is not None:
            self.faces = faces

    @property
    def face_set_id(self):
        """Gets the face_set_id of this AddFacesByBase64Response.

        人脸库ID。 调用失败时无此字段。

        :return: The face_set_id of this AddFacesByBase64Response.
        :rtype: str
        """
        return self._face_set_id

    @face_set_id.setter
    def face_set_id(self, face_set_id):
        """Sets the face_set_id of this AddFacesByBase64Response.

        人脸库ID。 调用失败时无此字段。

        :param face_set_id: The face_set_id of this AddFacesByBase64Response.
        :type: str
        """
        self._face_set_id = face_set_id

    @property
    def face_set_name(self):
        """Gets the face_set_name of this AddFacesByBase64Response.

        人脸库名称。 调用失败时无此字段。

        :return: The face_set_name of this AddFacesByBase64Response.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this AddFacesByBase64Response.

        人脸库名称。 调用失败时无此字段。

        :param face_set_name: The face_set_name of this AddFacesByBase64Response.
        :type: str
        """
        self._face_set_name = face_set_name

    @property
    def faces(self):
        """Gets the faces of this AddFacesByBase64Response.

        人脸库当中的人脸结构，详见[FaceSetFace](https://support.huaweicloud.com/api-face/face_02_0018.html)。 调用失败时无此字段。

        :return: The faces of this AddFacesByBase64Response.
        :rtype: list[FaceSetFace]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this AddFacesByBase64Response.

        人脸库当中的人脸结构，详见[FaceSetFace](https://support.huaweicloud.com/api-face/face_02_0018.html)。 调用失败时无此字段。

        :param faces: The faces of this AddFacesByBase64Response.
        :type: list[FaceSetFace]
        """
        self._faces = faces

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
        if not isinstance(other, AddFacesByBase64Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other