# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentUploadingAddress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'int',
        'uploading_url': 'str'
    }

    attribute_map = {
        'number': 'number',
        'uploading_url': 'uploading_url'
    }

    def __init__(self, number=None, uploading_url=None):
        r"""AttachmentUploadingAddress

        The model defined in huaweicloud sdk

        :param number: 序号
        :type number: int
        :param uploading_url: 上传url
        :type uploading_url: str
        """
        
        

        self._number = None
        self._uploading_url = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if uploading_url is not None:
            self.uploading_url = uploading_url

    @property
    def number(self):
        r"""Gets the number of this AttachmentUploadingAddress.

        序号

        :return: The number of this AttachmentUploadingAddress.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this AttachmentUploadingAddress.

        序号

        :param number: The number of this AttachmentUploadingAddress.
        :type number: int
        """
        self._number = number

    @property
    def uploading_url(self):
        r"""Gets the uploading_url of this AttachmentUploadingAddress.

        上传url

        :return: The uploading_url of this AttachmentUploadingAddress.
        :rtype: str
        """
        return self._uploading_url

    @uploading_url.setter
    def uploading_url(self, uploading_url):
        r"""Sets the uploading_url of this AttachmentUploadingAddress.

        上传url

        :param uploading_url: The uploading_url of this AttachmentUploadingAddress.
        :type uploading_url: str
        """
        self._uploading_url = uploading_url

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
        if not isinstance(other, AttachmentUploadingAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
