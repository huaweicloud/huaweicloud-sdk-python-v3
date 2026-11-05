# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageRemoveResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_id': 'str',
        'success': 'bool',
        'error_msg': 'str'
    }

    attribute_map = {
        'image_id': 'image_id',
        'success': 'success',
        'error_msg': 'error_msg'
    }

    def __init__(self, image_id=None, success=None, error_msg=None):
        r"""ImageRemoveResult

        The model defined in huaweicloud sdk

        :param image_id: 图片ID
        :type image_id: str
        :param success: 是否移除成功
        :type success: bool
        :param error_msg: 失败原因
        :type error_msg: str
        """
        
        

        self._image_id = None
        self._success = None
        self._error_msg = None
        self.discriminator = None

        if image_id is not None:
            self.image_id = image_id
        if success is not None:
            self.success = success
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def image_id(self):
        r"""Gets the image_id of this ImageRemoveResult.

        图片ID

        :return: The image_id of this ImageRemoveResult.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ImageRemoveResult.

        图片ID

        :param image_id: The image_id of this ImageRemoveResult.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def success(self):
        r"""Gets the success of this ImageRemoveResult.

        是否移除成功

        :return: The success of this ImageRemoveResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this ImageRemoveResult.

        是否移除成功

        :param success: The success of this ImageRemoveResult.
        :type success: bool
        """
        self._success = success

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ImageRemoveResult.

        失败原因

        :return: The error_msg of this ImageRemoveResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ImageRemoveResult.

        失败原因

        :param error_msg: The error_msg of this ImageRemoveResult.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ImageRemoveResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
