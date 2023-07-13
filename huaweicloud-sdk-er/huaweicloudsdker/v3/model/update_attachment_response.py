# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAttachmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachment': 'AttachmentResponse',
        'request_id': 'str'
    }

    attribute_map = {
        'attachment': 'attachment',
        'request_id': 'request_id'
    }

    def __init__(self, attachment=None, request_id=None):
        """UpdateAttachmentResponse

        The model defined in huaweicloud sdk

        :param attachment: 
        :type attachment: :class:`huaweicloudsdker.v3.AttachmentResponse`
        :param request_id: 请求id
        :type request_id: str
        """
        
        super(UpdateAttachmentResponse, self).__init__()

        self._attachment = None
        self._request_id = None
        self.discriminator = None

        if attachment is not None:
            self.attachment = attachment
        if request_id is not None:
            self.request_id = request_id

    @property
    def attachment(self):
        """Gets the attachment of this UpdateAttachmentResponse.

        :return: The attachment of this UpdateAttachmentResponse.
        :rtype: :class:`huaweicloudsdker.v3.AttachmentResponse`
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this UpdateAttachmentResponse.

        :param attachment: The attachment of this UpdateAttachmentResponse.
        :type attachment: :class:`huaweicloudsdker.v3.AttachmentResponse`
        """
        self._attachment = attachment

    @property
    def request_id(self):
        """Gets the request_id of this UpdateAttachmentResponse.

        请求id

        :return: The request_id of this UpdateAttachmentResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateAttachmentResponse.

        请求id

        :param request_id: The request_id of this UpdateAttachmentResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, UpdateAttachmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
