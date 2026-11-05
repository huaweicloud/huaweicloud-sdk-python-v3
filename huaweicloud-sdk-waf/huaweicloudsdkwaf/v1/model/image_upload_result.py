# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageUploadResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'image_id': 'str',
        'upload_url': 'str',
        'expire': 'int',
        'success': 'bool',
        'error_msg': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_id': 'image_id',
        'upload_url': 'upload_url',
        'expire': 'expire',
        'success': 'success',
        'error_msg': 'error_msg',
        'error_code': 'error_code'
    }

    def __init__(self, image_name=None, image_id=None, upload_url=None, expire=None, success=None, error_msg=None, error_code=None):
        r"""ImageUploadResult

        The model defined in huaweicloud sdk

        :param image_name: 图片名称（与请求项对应，保序返回）
        :type image_name: str
        :param image_id: 后端生成的图片ID（前端PUT后用此ID加入图库）；失败时为空
        :type image_id: str
        :param upload_url: OBS PUT预签名上传地址；失败时为空
        :type upload_url: str
        :param expire: 预签名过期时间（秒）；失败时为空
        :type expire: int
        :param success: 是否成功
        :type success: bool
        :param error_msg: 失败原因（如格式不支持/大小超限）
        :type error_msg: str
        :param error_code: 失败错误码（与error_msg配套，便于请求方按错误码处理）
        :type error_code: str
        """
        
        

        self._image_name = None
        self._image_id = None
        self._upload_url = None
        self._expire = None
        self._success = None
        self._error_msg = None
        self._error_code = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if image_id is not None:
            self.image_id = image_id
        if upload_url is not None:
            self.upload_url = upload_url
        if expire is not None:
            self.expire = expire
        if success is not None:
            self.success = success
        if error_msg is not None:
            self.error_msg = error_msg
        if error_code is not None:
            self.error_code = error_code

    @property
    def image_name(self):
        r"""Gets the image_name of this ImageUploadResult.

        图片名称（与请求项对应，保序返回）

        :return: The image_name of this ImageUploadResult.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ImageUploadResult.

        图片名称（与请求项对应，保序返回）

        :param image_name: The image_name of this ImageUploadResult.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageUploadResult.

        后端生成的图片ID（前端PUT后用此ID加入图库）；失败时为空

        :return: The image_id of this ImageUploadResult.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageUploadResult.

        后端生成的图片ID（前端PUT后用此ID加入图库）；失败时为空

        :param image_id: The image_id of this ImageUploadResult.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def upload_url(self):
        r"""Gets the upload_url of this ImageUploadResult.

        OBS PUT预签名上传地址；失败时为空

        :return: The upload_url of this ImageUploadResult.
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        r"""Sets the upload_url of this ImageUploadResult.

        OBS PUT预签名上传地址；失败时为空

        :param upload_url: The upload_url of this ImageUploadResult.
        :type upload_url: str
        """
        self._upload_url = upload_url

    @property
    def expire(self):
        r"""Gets the expire of this ImageUploadResult.

        预签名过期时间（秒）；失败时为空

        :return: The expire of this ImageUploadResult.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        r"""Sets the expire of this ImageUploadResult.

        预签名过期时间（秒）；失败时为空

        :param expire: The expire of this ImageUploadResult.
        :type expire: int
        """
        self._expire = expire

    @property
    def success(self):
        r"""Gets the success of this ImageUploadResult.

        是否成功

        :return: The success of this ImageUploadResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ImageUploadResult.

        是否成功

        :param success: The success of this ImageUploadResult.
        :type success: bool
        """
        self._success = success

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ImageUploadResult.

        失败原因（如格式不支持/大小超限）

        :return: The error_msg of this ImageUploadResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ImageUploadResult.

        失败原因（如格式不支持/大小超限）

        :param error_msg: The error_msg of this ImageUploadResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_code(self):
        r"""Gets the error_code of this ImageUploadResult.

        失败错误码（与error_msg配套，便于请求方按错误码处理）

        :return: The error_code of this ImageUploadResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ImageUploadResult.

        失败错误码（与error_msg配套，便于请求方按错误码处理）

        :param error_code: The error_code of this ImageUploadResult.
        :type error_code: str
        """
        self._error_code = error_code

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageUploadResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
