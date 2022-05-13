# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectFaceByUrlIntlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'faces': 'list[DetectFace]'
    }

    attribute_map = {
        'faces': 'faces'
    }

    def __init__(self, faces=None):
        """DetectFaceByUrlIntlResponse

        The model defined in huaweicloud sdk

        :param faces: 检测到的人脸。 调用失败时无此字段。
        :type faces: list[:class:`huaweicloudsdkfrs.v2.DetectFace`]
        """
        
        super(DetectFaceByUrlIntlResponse, self).__init__()

        self._faces = None
        self.discriminator = None

        if faces is not None:
            self.faces = faces

    @property
    def faces(self):
        """Gets the faces of this DetectFaceByUrlIntlResponse.

        检测到的人脸。 调用失败时无此字段。

        :return: The faces of this DetectFaceByUrlIntlResponse.
        :rtype: list[:class:`huaweicloudsdkfrs.v2.DetectFace`]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this DetectFaceByUrlIntlResponse.

        检测到的人脸。 调用失败时无此字段。

        :param faces: The faces of this DetectFaceByUrlIntlResponse.
        :type faces: list[:class:`huaweicloudsdkfrs.v2.DetectFace`]
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
        if not isinstance(other, DetectFaceByUrlIntlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
