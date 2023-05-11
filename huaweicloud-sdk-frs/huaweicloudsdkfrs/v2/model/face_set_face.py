# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FaceSetFace:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bounding_box': 'BoundingBox',
        'external_fields': 'object',
        'external_image_id': 'str',
        'face_id': 'str'
    }

    attribute_map = {
        'bounding_box': 'bounding_box',
        'external_fields': 'external_fields',
        'external_image_id': 'external_image_id',
        'face_id': 'face_id'
    }

    def __init__(self, bounding_box=None, external_fields=None, external_image_id=None, face_id=None):
        """FaceSetFace

        The model defined in huaweicloud sdk

        :param bounding_box: 
        :type bounding_box: :class:`huaweicloudsdkfrs.v2.BoundingBox`
        :param external_fields: 用户添加的额外字段。
        :type external_fields: object
        :param external_image_id: 人脸所在的外部图片ID。
        :type external_image_id: str
        :param face_id: 人脸ID，由系统内部生成的唯一ID。
        :type face_id: str
        """
        
        

        self._bounding_box = None
        self._external_fields = None
        self._external_image_id = None
        self._face_id = None
        self.discriminator = None

        self.bounding_box = bounding_box
        self.external_fields = external_fields
        self.external_image_id = external_image_id
        self.face_id = face_id

    @property
    def bounding_box(self):
        """Gets the bounding_box of this FaceSetFace.

        :return: The bounding_box of this FaceSetFace.
        :rtype: :class:`huaweicloudsdkfrs.v2.BoundingBox`
        """
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, bounding_box):
        """Sets the bounding_box of this FaceSetFace.

        :param bounding_box: The bounding_box of this FaceSetFace.
        :type bounding_box: :class:`huaweicloudsdkfrs.v2.BoundingBox`
        """
        self._bounding_box = bounding_box

    @property
    def external_fields(self):
        """Gets the external_fields of this FaceSetFace.

        用户添加的额外字段。

        :return: The external_fields of this FaceSetFace.
        :rtype: object
        """
        return self._external_fields

    @external_fields.setter
    def external_fields(self, external_fields):
        """Sets the external_fields of this FaceSetFace.

        用户添加的额外字段。

        :param external_fields: The external_fields of this FaceSetFace.
        :type external_fields: object
        """
        self._external_fields = external_fields

    @property
    def external_image_id(self):
        """Gets the external_image_id of this FaceSetFace.

        人脸所在的外部图片ID。

        :return: The external_image_id of this FaceSetFace.
        :rtype: str
        """
        return self._external_image_id

    @external_image_id.setter
    def external_image_id(self, external_image_id):
        """Sets the external_image_id of this FaceSetFace.

        人脸所在的外部图片ID。

        :param external_image_id: The external_image_id of this FaceSetFace.
        :type external_image_id: str
        """
        self._external_image_id = external_image_id

    @property
    def face_id(self):
        """Gets the face_id of this FaceSetFace.

        人脸ID，由系统内部生成的唯一ID。

        :return: The face_id of this FaceSetFace.
        :rtype: str
        """
        return self._face_id

    @face_id.setter
    def face_id(self, face_id):
        """Sets the face_id of this FaceSetFace.

        人脸ID，由系统内部生成的唯一ID。

        :param face_id: The face_id of this FaceSetFace.
        :type face_id: str
        """
        self._face_id = face_id

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
        if not isinstance(other, FaceSetFace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
