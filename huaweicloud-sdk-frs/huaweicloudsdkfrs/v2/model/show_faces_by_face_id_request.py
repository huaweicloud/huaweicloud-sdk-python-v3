# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFacesByFaceIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'face_set_name': 'str',
        'face_id': 'str'
    }

    attribute_map = {
        'face_set_name': 'face_set_name',
        'face_id': 'face_id'
    }

    def __init__(self, face_set_name=None, face_id=None):
        """ShowFacesByFaceIdRequest

        The model defined in huaweicloud sdk

        :param face_set_name: 人脸库名称。
        :type face_set_name: str
        :param face_id: 人脸ID。
        :type face_id: str
        """
        
        

        self._face_set_name = None
        self._face_id = None
        self.discriminator = None

        self.face_set_name = face_set_name
        self.face_id = face_id

    @property
    def face_set_name(self):
        """Gets the face_set_name of this ShowFacesByFaceIdRequest.

        人脸库名称。

        :return: The face_set_name of this ShowFacesByFaceIdRequest.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this ShowFacesByFaceIdRequest.

        人脸库名称。

        :param face_set_name: The face_set_name of this ShowFacesByFaceIdRequest.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def face_id(self):
        """Gets the face_id of this ShowFacesByFaceIdRequest.

        人脸ID。

        :return: The face_id of this ShowFacesByFaceIdRequest.
        :rtype: str
        """
        return self._face_id

    @face_id.setter
    def face_id(self, face_id):
        """Sets the face_id of this ShowFacesByFaceIdRequest.

        人脸ID。

        :param face_id: The face_id of this ShowFacesByFaceIdRequest.
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
        if not isinstance(other, ShowFacesByFaceIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
