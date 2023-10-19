# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFaceSetResponse(SdkResponse):

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
        'x_request_id': 'str'
    }

    attribute_map = {
        'face_set_name': 'face_set_name',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, face_set_name=None, x_request_id=None):
        """DeleteFaceSetResponse

        The model defined in huaweicloud sdk

        :param face_set_name: 人脸库名称。 调用失败时无此字段。
        :type face_set_name: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(DeleteFaceSetResponse, self).__init__()

        self._face_set_name = None
        self._x_request_id = None
        self.discriminator = None

        if face_set_name is not None:
            self.face_set_name = face_set_name
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def face_set_name(self):
        """Gets the face_set_name of this DeleteFaceSetResponse.

        人脸库名称。 调用失败时无此字段。

        :return: The face_set_name of this DeleteFaceSetResponse.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this DeleteFaceSetResponse.

        人脸库名称。 调用失败时无此字段。

        :param face_set_name: The face_set_name of this DeleteFaceSetResponse.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def x_request_id(self):
        """Gets the x_request_id of this DeleteFaceSetResponse.

        :return: The x_request_id of this DeleteFaceSetResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this DeleteFaceSetResponse.

        :param x_request_id: The x_request_id of this DeleteFaceSetResponse.
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
        if not isinstance(other, DeleteFaceSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
