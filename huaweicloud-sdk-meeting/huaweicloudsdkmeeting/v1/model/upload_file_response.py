# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'image_moderation': 'ImageModerationResult'
    }

    attribute_map = {
        'file_id': 'fileId',
        'image_moderation': 'imageModeration'
    }

    def __init__(self, file_id=None, image_moderation=None):
        """UploadFileResponse

        The model defined in huaweicloud sdk

        :param file_id: 文件Id。
        :type file_id: str
        :param image_moderation: 
        :type image_moderation: :class:`huaweicloudsdkmeeting.v1.ImageModerationResult`
        """
        
        super(UploadFileResponse, self).__init__()

        self._file_id = None
        self._image_moderation = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if image_moderation is not None:
            self.image_moderation = image_moderation

    @property
    def file_id(self):
        """Gets the file_id of this UploadFileResponse.

        文件Id。

        :return: The file_id of this UploadFileResponse.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this UploadFileResponse.

        文件Id。

        :param file_id: The file_id of this UploadFileResponse.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def image_moderation(self):
        """Gets the image_moderation of this UploadFileResponse.

        :return: The image_moderation of this UploadFileResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ImageModerationResult`
        """
        return self._image_moderation

    @image_moderation.setter
    def image_moderation(self, image_moderation):
        """Sets the image_moderation of this UploadFileResponse.

        :param image_moderation: The image_moderation of this UploadFileResponse.
        :type image_moderation: :class:`huaweicloudsdkmeeting.v1.ImageModerationResult`
        """
        self._image_moderation = image_moderation

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
        if not isinstance(other, UploadFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
