# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandardReqDataByNameAndId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verification_name': 'str',
        'verification_id': 'str',
        'face_image': 'str',
        'detail': 'bool',
        'crop': 'bool'
    }

    attribute_map = {
        'verification_name': 'verification_name',
        'verification_id': 'verification_id',
        'face_image': 'face_image',
        'detail': 'detail',
        'crop': 'crop'
    }

    def __init__(self, verification_name=None, verification_id=None, face_image=None, detail=None, crop=None):
        r"""StandardReqDataByNameAndId

        The model defined in huaweicloud sdk

        :param verification_name: 被验证人的姓名。
        :type verification_name: str
        :param verification_id: 被验证人的身份证号码。
        :type verification_id: str
        :param face_image: 现场人像图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。
        :type face_image: str
        :param detail: 响应参数similarity是否详细显示，默认为false。 - true表示响应中的similarity为0~1000的小数。 - false表示响应中的similarity为0~100的整数。
        :type detail: bool
        :param crop: 是否允许对入参face_image进行人脸检测及图片裁剪，默认为true，表示允许。
        :type crop: bool
        """
        
        

        self._verification_name = None
        self._verification_id = None
        self._face_image = None
        self._detail = None
        self._crop = None
        self.discriminator = None

        self.verification_name = verification_name
        self.verification_id = verification_id
        self.face_image = face_image
        if detail is not None:
            self.detail = detail
        if crop is not None:
            self.crop = crop

    @property
    def verification_name(self):
        r"""Gets the verification_name of this StandardReqDataByNameAndId.

        被验证人的姓名。

        :return: The verification_name of this StandardReqDataByNameAndId.
        :rtype: str
        """
        return self._verification_name

    @verification_name.setter
    def verification_name(self, verification_name):
        r"""Sets the verification_name of this StandardReqDataByNameAndId.

        被验证人的姓名。

        :param verification_name: The verification_name of this StandardReqDataByNameAndId.
        :type verification_name: str
        """
        self._verification_name = verification_name

    @property
    def verification_id(self):
        r"""Gets the verification_id of this StandardReqDataByNameAndId.

        被验证人的身份证号码。

        :return: The verification_id of this StandardReqDataByNameAndId.
        :rtype: str
        """
        return self._verification_id

    @verification_id.setter
    def verification_id(self, verification_id):
        r"""Sets the verification_id of this StandardReqDataByNameAndId.

        被验证人的身份证号码。

        :param verification_id: The verification_id of this StandardReqDataByNameAndId.
        :type verification_id: str
        """
        self._verification_id = verification_id

    @property
    def face_image(self):
        r"""Gets the face_image of this StandardReqDataByNameAndId.

        现场人像图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :return: The face_image of this StandardReqDataByNameAndId.
        :rtype: str
        """
        return self._face_image

    @face_image.setter
    def face_image(self, face_image):
        r"""Sets the face_image of this StandardReqDataByNameAndId.

        现场人像图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :param face_image: The face_image of this StandardReqDataByNameAndId.
        :type face_image: str
        """
        self._face_image = face_image

    @property
    def detail(self):
        r"""Gets the detail of this StandardReqDataByNameAndId.

        响应参数similarity是否详细显示，默认为false。 - true表示响应中的similarity为0~1000的小数。 - false表示响应中的similarity为0~100的整数。

        :return: The detail of this StandardReqDataByNameAndId.
        :rtype: bool
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this StandardReqDataByNameAndId.

        响应参数similarity是否详细显示，默认为false。 - true表示响应中的similarity为0~1000的小数。 - false表示响应中的similarity为0~100的整数。

        :param detail: The detail of this StandardReqDataByNameAndId.
        :type detail: bool
        """
        self._detail = detail

    @property
    def crop(self):
        r"""Gets the crop of this StandardReqDataByNameAndId.

        是否允许对入参face_image进行人脸检测及图片裁剪，默认为true，表示允许。

        :return: The crop of this StandardReqDataByNameAndId.
        :rtype: bool
        """
        return self._crop

    @crop.setter
    def crop(self, crop):
        r"""Sets the crop of this StandardReqDataByNameAndId.

        是否允许对入参face_image进行人脸检测及图片裁剪，默认为true，表示允许。

        :param crop: The crop of this StandardReqDataByNameAndId.
        :type crop: bool
        """
        self._crop = crop

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
        if not isinstance(other, StandardReqDataByNameAndId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
