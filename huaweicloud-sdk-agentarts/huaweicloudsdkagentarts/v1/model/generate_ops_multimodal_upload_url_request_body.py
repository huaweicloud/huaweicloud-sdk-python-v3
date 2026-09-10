# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateOpsMultimodalUploadUrlRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_suffix': 'str',
        'file_hash': 'str'
    }

    attribute_map = {
        'file_suffix': 'file_suffix',
        'file_hash': 'file_hash'
    }

    def __init__(self, file_suffix=None, file_hash=None):
        r"""GenerateOpsMultimodalUploadUrlRequestBody

        The model defined in huaweicloud sdk

        :param file_suffix: **参数解释：** 文件后缀名，用于生成OBS对象名。 **约束限制：** 必须为枚举值之一。 **取值范围：** 由英文字母及点(.)组成的字符串，长度为0~20个字符。 **默认取值：** 不涉及。
        :type file_suffix: str
        :param file_hash: **参数解释：** 文件的SHA256哈希值，用于OBS上传校验。 **约束限制：** 必须为有效的SHA256哈希值。 **取值范围：** 64位十六进制字符串。 **默认取值：** 不涉及。
        :type file_hash: str
        """
        
        

        self._file_suffix = None
        self._file_hash = None
        self.discriminator = None

        self.file_suffix = file_suffix
        self.file_hash = file_hash

    @property
    def file_suffix(self):
        r"""Gets the file_suffix of this GenerateOpsMultimodalUploadUrlRequestBody.

        **参数解释：** 文件后缀名，用于生成OBS对象名。 **约束限制：** 必须为枚举值之一。 **取值范围：** 由英文字母及点(.)组成的字符串，长度为0~20个字符。 **默认取值：** 不涉及。

        :return: The file_suffix of this GenerateOpsMultimodalUploadUrlRequestBody.
        :rtype: str
        """
        return self._file_suffix

    @file_suffix.setter
    def file_suffix(self, file_suffix):
        r"""Sets the file_suffix of this GenerateOpsMultimodalUploadUrlRequestBody.

        **参数解释：** 文件后缀名，用于生成OBS对象名。 **约束限制：** 必须为枚举值之一。 **取值范围：** 由英文字母及点(.)组成的字符串，长度为0~20个字符。 **默认取值：** 不涉及。

        :param file_suffix: The file_suffix of this GenerateOpsMultimodalUploadUrlRequestBody.
        :type file_suffix: str
        """
        self._file_suffix = file_suffix

    @property
    def file_hash(self):
        r"""Gets the file_hash of this GenerateOpsMultimodalUploadUrlRequestBody.

        **参数解释：** 文件的SHA256哈希值，用于OBS上传校验。 **约束限制：** 必须为有效的SHA256哈希值。 **取值范围：** 64位十六进制字符串。 **默认取值：** 不涉及。

        :return: The file_hash of this GenerateOpsMultimodalUploadUrlRequestBody.
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):
        r"""Sets the file_hash of this GenerateOpsMultimodalUploadUrlRequestBody.

        **参数解释：** 文件的SHA256哈希值，用于OBS上传校验。 **约束限制：** 必须为有效的SHA256哈希值。 **取值范围：** 64位十六进制字符串。 **默认取值：** 不涉及。

        :param file_hash: The file_hash of this GenerateOpsMultimodalUploadUrlRequestBody.
        :type file_hash: str
        """
        self._file_hash = file_hash

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
        if not isinstance(other, GenerateOpsMultimodalUploadUrlRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
