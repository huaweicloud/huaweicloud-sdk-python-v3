# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFaceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'external_fields': 'object',
        'external_image_id': 'str',
        'face_id': 'str'
    }

    attribute_map = {
        'external_fields': 'external_fields',
        'external_image_id': 'external_image_id',
        'face_id': 'face_id'
    }

    def __init__(self, external_fields=None, external_image_id=None, face_id=None):
        """UpdateFaceReq

        The model defined in huaweicloud sdk

        :param external_fields: Json字符串不校验重复性，自定义字段的key值长度范围为[1,36]，string类型的value长度范围为[1,256]，具体参见[[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)](tag:hc)。[[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)](tag:hk)。这里是待修改的参数，external_image_id和external_fields至少选一个。
        :type external_fields: object
        :param external_image_id: 用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。 这里是待修改的参数，external_image_id和external_fields至少选一个。
        :type external_image_id: str
        :param face_id: 人脸库ID，由系统内部生成的唯一ID。
        :type face_id: str
        """
        
        

        self._external_fields = None
        self._external_image_id = None
        self._face_id = None
        self.discriminator = None

        if external_fields is not None:
            self.external_fields = external_fields
        if external_image_id is not None:
            self.external_image_id = external_image_id
        self.face_id = face_id

    @property
    def external_fields(self):
        """Gets the external_fields of this UpdateFaceReq.

        Json字符串不校验重复性，自定义字段的key值长度范围为[1,36]，string类型的value长度范围为[1,256]，具体参见[[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)](tag:hc)。[[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)](tag:hk)。这里是待修改的参数，external_image_id和external_fields至少选一个。

        :return: The external_fields of this UpdateFaceReq.
        :rtype: object
        """
        return self._external_fields

    @external_fields.setter
    def external_fields(self, external_fields):
        """Sets the external_fields of this UpdateFaceReq.

        Json字符串不校验重复性，自定义字段的key值长度范围为[1,36]，string类型的value长度范围为[1,256]，具体参见[[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)](tag:hc)。[[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)](tag:hk)。这里是待修改的参数，external_image_id和external_fields至少选一个。

        :param external_fields: The external_fields of this UpdateFaceReq.
        :type external_fields: object
        """
        self._external_fields = external_fields

    @property
    def external_image_id(self):
        """Gets the external_image_id of this UpdateFaceReq.

        用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。 这里是待修改的参数，external_image_id和external_fields至少选一个。

        :return: The external_image_id of this UpdateFaceReq.
        :rtype: str
        """
        return self._external_image_id

    @external_image_id.setter
    def external_image_id(self, external_image_id):
        """Sets the external_image_id of this UpdateFaceReq.

        用户指定的图片外部ID，与当前图像绑定。用户没提供，系统会生成一个。该ID长度范围为1～36位，可以包含字母、数字、中划线或者下划线，不包含其他的特殊字符。 这里是待修改的参数，external_image_id和external_fields至少选一个。

        :param external_image_id: The external_image_id of this UpdateFaceReq.
        :type external_image_id: str
        """
        self._external_image_id = external_image_id

    @property
    def face_id(self):
        """Gets the face_id of this UpdateFaceReq.

        人脸库ID，由系统内部生成的唯一ID。

        :return: The face_id of this UpdateFaceReq.
        :rtype: str
        """
        return self._face_id

    @face_id.setter
    def face_id(self, face_id):
        """Sets the face_id of this UpdateFaceReq.

        人脸库ID，由系统内部生成的唯一ID。

        :param face_id: The face_id of this UpdateFaceReq.
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
        if not isinstance(other, UpdateFaceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
