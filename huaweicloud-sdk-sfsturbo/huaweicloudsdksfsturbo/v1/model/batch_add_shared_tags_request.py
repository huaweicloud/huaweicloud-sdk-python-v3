# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddSharedTagsRequest:

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
        'body': 'BatchAddSharedTagsRequestBody'
    }

    attribute_map = {
        'share_id': 'share_id',
        'body': 'body'
    }

    def __init__(self, share_id=None, body=None):
        """BatchAddSharedTagsRequest

        The model defined in huaweicloud sdk

        :param share_id: 共享ID
        :type share_id: str
        :param body: Body of the BatchAddSharedTagsRequest
        :type body: :class:`huaweicloudsdksfsturbo.v1.BatchAddSharedTagsRequestBody`
        """
        
        

        self._share_id = None
        self._body = None
        self.discriminator = None

        self.share_id = share_id
        if body is not None:
            self.body = body

    @property
    def share_id(self):
        """Gets the share_id of this BatchAddSharedTagsRequest.

        共享ID

        :return: The share_id of this BatchAddSharedTagsRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this BatchAddSharedTagsRequest.

        共享ID

        :param share_id: The share_id of this BatchAddSharedTagsRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def body(self):
        """Gets the body of this BatchAddSharedTagsRequest.

        :return: The body of this BatchAddSharedTagsRequest.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.BatchAddSharedTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchAddSharedTagsRequest.

        :param body: The body of this BatchAddSharedTagsRequest.
        :type body: :class:`huaweicloudsdksfsturbo.v1.BatchAddSharedTagsRequestBody`
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
        if not isinstance(other, BatchAddSharedTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
