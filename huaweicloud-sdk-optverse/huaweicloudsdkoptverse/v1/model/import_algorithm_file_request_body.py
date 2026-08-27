# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportAlgorithmFileRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_update_time': 'float',
        'file': 'file'
    }

    attribute_map = {
        'last_update_time': 'last_update_time',
        'file': 'file'
    }

    def __init__(self, last_update_time=None, file=None):
        r"""ImportAlgorithmFileRequestBody

        The model defined in huaweicloud sdk

        :param last_update_time: **参数解释**： 算法最后更新时间，需要和算法的content_update_at字段一致。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type last_update_time: float
        :param file: **参数解释**： 待上传文件。 **约束限制**： 需要是合法的zip压缩包。 **取值范围**： 20MB以内 **默认取值**： 不涉及 
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._last_update_time = None
        self._file = None
        self.discriminator = None

        self.last_update_time = last_update_time
        self.file = file

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ImportAlgorithmFileRequestBody.

        **参数解释**： 算法最后更新时间，需要和算法的content_update_at字段一致。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The last_update_time of this ImportAlgorithmFileRequestBody.
        :rtype: float
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ImportAlgorithmFileRequestBody.

        **参数解释**： 算法最后更新时间，需要和算法的content_update_at字段一致。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param last_update_time: The last_update_time of this ImportAlgorithmFileRequestBody.
        :type last_update_time: float
        """
        self._last_update_time = last_update_time

    @property
    def file(self):
        r"""Gets the file of this ImportAlgorithmFileRequestBody.

        **参数解释**： 待上传文件。 **约束限制**： 需要是合法的zip压缩包。 **取值范围**： 20MB以内 **默认取值**： 不涉及 

        :return: The file of this ImportAlgorithmFileRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ImportAlgorithmFileRequestBody.

        **参数解释**： 待上传文件。 **约束限制**： 需要是合法的zip压缩包。 **取值范围**： 20MB以内 **默认取值**： 不涉及 

        :param file: The file of this ImportAlgorithmFileRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

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
        if not isinstance(other, ImportAlgorithmFileRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
