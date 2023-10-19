# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'face_number': 'int',
        'face_set_id': 'str',
        'face_set_name': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'face_number': 'face_number',
        'face_set_id': 'face_set_id',
        'face_set_name': 'face_set_name',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, face_number=None, face_set_id=None, face_set_name=None, x_request_id=None):
        """UpdateFaceResponse

        The model defined in huaweicloud sdk

        :param face_number: 更新的人脸数量。 调用失败时无此字段。
        :type face_number: int
        :param face_set_id: 人脸库ID。 调用失败时无此字段。
        :type face_set_id: str
        :param face_set_name: 人脸库名称。 调用失败时无此字段。
        :type face_set_name: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateFaceResponse, self).__init__()

        self._face_number = None
        self._face_set_id = None
        self._face_set_name = None
        self._x_request_id = None
        self.discriminator = None

        if face_number is not None:
            self.face_number = face_number
        if face_set_id is not None:
            self.face_set_id = face_set_id
        if face_set_name is not None:
            self.face_set_name = face_set_name
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def face_number(self):
        """Gets the face_number of this UpdateFaceResponse.

        更新的人脸数量。 调用失败时无此字段。

        :return: The face_number of this UpdateFaceResponse.
        :rtype: int
        """
        return self._face_number

    @face_number.setter
    def face_number(self, face_number):
        """Sets the face_number of this UpdateFaceResponse.

        更新的人脸数量。 调用失败时无此字段。

        :param face_number: The face_number of this UpdateFaceResponse.
        :type face_number: int
        """
        self._face_number = face_number

    @property
    def face_set_id(self):
        """Gets the face_set_id of this UpdateFaceResponse.

        人脸库ID。 调用失败时无此字段。

        :return: The face_set_id of this UpdateFaceResponse.
        :rtype: str
        """
        return self._face_set_id

    @face_set_id.setter
    def face_set_id(self, face_set_id):
        """Sets the face_set_id of this UpdateFaceResponse.

        人脸库ID。 调用失败时无此字段。

        :param face_set_id: The face_set_id of this UpdateFaceResponse.
        :type face_set_id: str
        """
        self._face_set_id = face_set_id

    @property
    def face_set_name(self):
        """Gets the face_set_name of this UpdateFaceResponse.

        人脸库名称。 调用失败时无此字段。

        :return: The face_set_name of this UpdateFaceResponse.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this UpdateFaceResponse.

        人脸库名称。 调用失败时无此字段。

        :param face_set_name: The face_set_name of this UpdateFaceResponse.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateFaceResponse.

        :return: The x_request_id of this UpdateFaceResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateFaceResponse.

        :param x_request_id: The x_request_id of this UpdateFaceResponse.
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
        if not isinstance(other, UpdateFaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
