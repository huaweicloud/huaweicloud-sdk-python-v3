# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAttachmentRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file'
    }

    attribute_map = {
        'file': 'file'
    }

    def __init__(self, file=None):
        r"""CreateAttachmentRequestBody

        The model defined in huaweicloud sdk

        :param file: **参数解释：** 需要上传的文件，以表单的形式上传。 **约束限制：** 内容为二进制binary文本。支持文件类型：.jpg,.png,.docx,.txt,.pdf，且文本大小不超10M。 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        
        

        self._file = None
        self.discriminator = None

        self.file = file

    @property
    def file(self):
        r"""Gets the file of this CreateAttachmentRequestBody.

        **参数解释：** 需要上传的文件，以表单的形式上传。 **约束限制：** 内容为二进制binary文本。支持文件类型：.jpg,.png,.docx,.txt,.pdf，且文本大小不超10M。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The file of this CreateAttachmentRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this CreateAttachmentRequestBody.

        **参数解释：** 需要上传的文件，以表单的形式上传。 **约束限制：** 内容为二进制binary文本。支持文件类型：.jpg,.png,.docx,.txt,.pdf，且文本大小不超10M。 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param file: The file of this CreateAttachmentRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

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
        if not isinstance(other, CreateAttachmentRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
