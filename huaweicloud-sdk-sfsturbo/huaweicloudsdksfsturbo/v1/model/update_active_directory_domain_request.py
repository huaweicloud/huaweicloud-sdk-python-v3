# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateActiveDirectoryDomainRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'body': 'UpdateActiveDirectoryDomainRequestBody'
    }

    attribute_map = {
        'share_id': 'share_id',
        'body': 'body'
    }

    def __init__(self, share_id=None, body=None):
        r"""UpdateActiveDirectoryDomainRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统ID
        :type share_id: str
        :param body: Body of the UpdateActiveDirectoryDomainRequest
        :type body: :class:`huaweicloudsdksfsturbo.v1.UpdateActiveDirectoryDomainRequestBody`
        """
        
        

        self._share_id = None
        self._body = None
        self.discriminator = None

        self.share_id = share_id
        if body is not None:
            self.body = body

    @property
    def share_id(self):
        r"""Gets the share_id of this UpdateActiveDirectoryDomainRequest.

        文件系统ID

        :return: The share_id of this UpdateActiveDirectoryDomainRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this UpdateActiveDirectoryDomainRequest.

        文件系统ID

        :param share_id: The share_id of this UpdateActiveDirectoryDomainRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def body(self):
        r"""Gets the body of this UpdateActiveDirectoryDomainRequest.

        :return: The body of this UpdateActiveDirectoryDomainRequest.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.UpdateActiveDirectoryDomainRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateActiveDirectoryDomainRequest.

        :param body: The body of this UpdateActiveDirectoryDomainRequest.
        :type body: :class:`huaweicloudsdksfsturbo.v1.UpdateActiveDirectoryDomainRequestBody`
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
        if not isinstance(other, UpdateActiveDirectoryDomainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
