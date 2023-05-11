# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqDataByIdCardImage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idcard_image1': 'str',
        'idcard_image2': 'str',
        'face_image': 'str'
    }

    attribute_map = {
        'idcard_image1': 'idcard_image1',
        'idcard_image2': 'idcard_image2',
        'face_image': 'face_image'
    }

    def __init__(self, idcard_image1=None, idcard_image2=None, face_image=None):
        """ReqDataByIdCardImage

        The model defined in huaweicloud sdk

        :param idcard_image1: 身份证人像面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。
        :type idcard_image1: str
        :param idcard_image2: 身份证国徽面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。
        :type idcard_image2: str
        :param face_image: 现场人像图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。
        :type face_image: str
        """
        
        

        self._idcard_image1 = None
        self._idcard_image2 = None
        self._face_image = None
        self.discriminator = None

        self.idcard_image1 = idcard_image1
        if idcard_image2 is not None:
            self.idcard_image2 = idcard_image2
        self.face_image = face_image

    @property
    def idcard_image1(self):
        """Gets the idcard_image1 of this ReqDataByIdCardImage.

        身份证人像面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :return: The idcard_image1 of this ReqDataByIdCardImage.
        :rtype: str
        """
        return self._idcard_image1

    @idcard_image1.setter
    def idcard_image1(self, idcard_image1):
        """Sets the idcard_image1 of this ReqDataByIdCardImage.

        身份证人像面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :param idcard_image1: The idcard_image1 of this ReqDataByIdCardImage.
        :type idcard_image1: str
        """
        self._idcard_image1 = idcard_image1

    @property
    def idcard_image2(self):
        """Gets the idcard_image2 of this ReqDataByIdCardImage.

        身份证国徽面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :return: The idcard_image2 of this ReqDataByIdCardImage.
        :rtype: str
        """
        return self._idcard_image2

    @idcard_image2.setter
    def idcard_image2(self, idcard_image2):
        """Sets the idcard_image2 of this ReqDataByIdCardImage.

        身份证国徽面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :param idcard_image2: The idcard_image2 of this ReqDataByIdCardImage.
        :type idcard_image2: str
        """
        self._idcard_image2 = idcard_image2

    @property
    def face_image(self):
        """Gets the face_image of this ReqDataByIdCardImage.

        现场人像图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :return: The face_image of this ReqDataByIdCardImage.
        :rtype: str
        """
        return self._face_image

    @face_image.setter
    def face_image(self, face_image):
        """Sets the face_image of this ReqDataByIdCardImage.

        现场人像图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :param face_image: The face_image of this ReqDataByIdCardImage.
        :type face_image: str
        """
        self._face_image = face_image

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
        if not isinstance(other, ReqDataByIdCardImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
