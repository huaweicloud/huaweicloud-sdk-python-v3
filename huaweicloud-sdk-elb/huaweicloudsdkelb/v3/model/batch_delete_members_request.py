# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'body': 'BatchDeleteMembersRequestBody'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'body': 'body'
    }

    def __init__(self, pool_id=None, body=None):
        """BatchDeleteMembersRequest

        The model defined in huaweicloud sdk

        :param pool_id: 后端服务器组ID。
        :type pool_id: str
        :param body: Body of the BatchDeleteMembersRequest
        :type body: :class:`huaweicloudsdkelb.v3.BatchDeleteMembersRequestBody`
        """
        
        

        self._pool_id = None
        self._body = None
        self.discriminator = None

        self.pool_id = pool_id
        if body is not None:
            self.body = body

    @property
    def pool_id(self):
        """Gets the pool_id of this BatchDeleteMembersRequest.

        后端服务器组ID。

        :return: The pool_id of this BatchDeleteMembersRequest.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this BatchDeleteMembersRequest.

        后端服务器组ID。

        :param pool_id: The pool_id of this BatchDeleteMembersRequest.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def body(self):
        """Gets the body of this BatchDeleteMembersRequest.

        :return: The body of this BatchDeleteMembersRequest.
        :rtype: :class:`huaweicloudsdkelb.v3.BatchDeleteMembersRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchDeleteMembersRequest.

        :param body: The body of this BatchDeleteMembersRequest.
        :type body: :class:`huaweicloudsdkelb.v3.BatchDeleteMembersRequestBody`
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
        if not isinstance(other, BatchDeleteMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
