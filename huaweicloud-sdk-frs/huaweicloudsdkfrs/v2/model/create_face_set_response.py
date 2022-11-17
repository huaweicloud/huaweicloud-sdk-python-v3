# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFaceSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'face_set_info': 'FaceSetInfo'
    }

    attribute_map = {
        'face_set_info': 'face_set_info'
    }

    def __init__(self, face_set_info=None):
        """CreateFaceSetResponse

        The model defined in huaweicloud sdk

        :param face_set_info: 
        :type face_set_info: :class:`huaweicloudsdkfrs.v2.FaceSetInfo`
        """
        
        super(CreateFaceSetResponse, self).__init__()

        self._face_set_info = None
        self.discriminator = None

        if face_set_info is not None:
            self.face_set_info = face_set_info

    @property
    def face_set_info(self):
        """Gets the face_set_info of this CreateFaceSetResponse.

        :return: The face_set_info of this CreateFaceSetResponse.
        :rtype: :class:`huaweicloudsdkfrs.v2.FaceSetInfo`
        """
        return self._face_set_info

    @face_set_info.setter
    def face_set_info(self, face_set_info):
        """Sets the face_set_info of this CreateFaceSetResponse.

        :param face_set_info: The face_set_info of this CreateFaceSetResponse.
        :type face_set_info: :class:`huaweicloudsdkfrs.v2.FaceSetInfo`
        """
        self._face_set_info = face_set_info

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
        if not isinstance(other, CreateFaceSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
