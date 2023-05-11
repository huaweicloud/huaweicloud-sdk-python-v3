# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadExtensionFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'official': 'str',
        'body': 'UploadExtensionFileRequestBody'
    }

    attribute_map = {
        'official': 'official',
        'body': 'body'
    }

    def __init__(self, official=None, body=None):
        """UploadExtensionFileRequest

        The model defined in huaweicloud sdk

        :param official: 插件类型。目前只支持CodeArtsIDEOnline
        :type official: str
        :param body: Body of the UploadExtensionFileRequest
        :type body: :class:`huaweicloudsdkcloudide.v2.UploadExtensionFileRequestBody`
        """
        
        

        self._official = None
        self._body = None
        self.discriminator = None

        self.official = official
        if body is not None:
            self.body = body

    @property
    def official(self):
        """Gets the official of this UploadExtensionFileRequest.

        插件类型。目前只支持CodeArtsIDEOnline

        :return: The official of this UploadExtensionFileRequest.
        :rtype: str
        """
        return self._official

    @official.setter
    def official(self, official):
        """Sets the official of this UploadExtensionFileRequest.

        插件类型。目前只支持CodeArtsIDEOnline

        :param official: The official of this UploadExtensionFileRequest.
        :type official: str
        """
        self._official = official

    @property
    def body(self):
        """Gets the body of this UploadExtensionFileRequest.

        :return: The body of this UploadExtensionFileRequest.
        :rtype: :class:`huaweicloudsdkcloudide.v2.UploadExtensionFileRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadExtensionFileRequest.

        :param body: The body of this UploadExtensionFileRequest.
        :type body: :class:`huaweicloudsdkcloudide.v2.UploadExtensionFileRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UploadExtensionFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
