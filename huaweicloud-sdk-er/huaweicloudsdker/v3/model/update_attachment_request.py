# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAttachmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'attachment_id': 'str',
        'body': 'UpdateAttachmentRequestBody'
    }

    attribute_map = {
        'er_id': 'er_id',
        'attachment_id': 'attachment_id',
        'body': 'body'
    }

    def __init__(self, er_id=None, attachment_id=None, body=None):
        """UpdateAttachmentRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param attachment_id: 连接ID
        :type attachment_id: str
        :param body: Body of the UpdateAttachmentRequest
        :type body: :class:`huaweicloudsdker.v3.UpdateAttachmentRequestBody`
        """
        
        

        self._er_id = None
        self._attachment_id = None
        self._body = None
        self.discriminator = None

        self.er_id = er_id
        self.attachment_id = attachment_id
        if body is not None:
            self.body = body

    @property
    def er_id(self):
        """Gets the er_id of this UpdateAttachmentRequest.

        企业路由器实例ID

        :return: The er_id of this UpdateAttachmentRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this UpdateAttachmentRequest.

        企业路由器实例ID

        :param er_id: The er_id of this UpdateAttachmentRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def attachment_id(self):
        """Gets the attachment_id of this UpdateAttachmentRequest.

        连接ID

        :return: The attachment_id of this UpdateAttachmentRequest.
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this UpdateAttachmentRequest.

        连接ID

        :param attachment_id: The attachment_id of this UpdateAttachmentRequest.
        :type attachment_id: str
        """
        self._attachment_id = attachment_id

    @property
    def body(self):
        """Gets the body of this UpdateAttachmentRequest.


        :return: The body of this UpdateAttachmentRequest.
        :rtype: :class:`huaweicloudsdker.v3.UpdateAttachmentRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAttachmentRequest.


        :param body: The body of this UpdateAttachmentRequest.
        :type body: :class:`huaweicloudsdker.v3.UpdateAttachmentRequestBody`
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
        if not isinstance(other, UpdateAttachmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
