# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStoredQueryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_id': 'str',
        'body': 'StoredQueryRequestBody'
    }

    attribute_map = {
        'query_id': 'query_id',
        'body': 'body'
    }

    def __init__(self, query_id=None, body=None):
        """UpdateStoredQueryRequest

        The model defined in huaweicloud sdk

        :param query_id: 查询ID
        :type query_id: str
        :param body: Body of the UpdateStoredQueryRequest
        :type body: :class:`huaweicloudsdkconfig.v1.StoredQueryRequestBody`
        """
        
        

        self._query_id = None
        self._body = None
        self.discriminator = None

        self.query_id = query_id
        if body is not None:
            self.body = body

    @property
    def query_id(self):
        """Gets the query_id of this UpdateStoredQueryRequest.

        查询ID

        :return: The query_id of this UpdateStoredQueryRequest.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this UpdateStoredQueryRequest.

        查询ID

        :param query_id: The query_id of this UpdateStoredQueryRequest.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def body(self):
        """Gets the body of this UpdateStoredQueryRequest.

        :return: The body of this UpdateStoredQueryRequest.
        :rtype: :class:`huaweicloudsdkconfig.v1.StoredQueryRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateStoredQueryRequest.

        :param body: The body of this UpdateStoredQueryRequest.
        :type body: :class:`huaweicloudsdkconfig.v1.StoredQueryRequestBody`
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
        if not isinstance(other, UpdateStoredQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
