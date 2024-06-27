# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteTestCasesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_async': 'bool',
        'body': 'DeleteTestCaseInfo'
    }

    attribute_map = {
        'is_async': 'is_async',
        'body': 'body'
    }

    def __init__(self, is_async=None, body=None):
        """BatchDeleteTestCasesRequest

        The model defined in huaweicloud sdk

        :param is_async: 是否异步
        :type is_async: bool
        :param body: Body of the BatchDeleteTestCasesRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.DeleteTestCaseInfo`
        """
        
        

        self._is_async = None
        self._body = None
        self.discriminator = None

        if is_async is not None:
            self.is_async = is_async
        if body is not None:
            self.body = body

    @property
    def is_async(self):
        """Gets the is_async of this BatchDeleteTestCasesRequest.

        是否异步

        :return: The is_async of this BatchDeleteTestCasesRequest.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        """Sets the is_async of this BatchDeleteTestCasesRequest.

        是否异步

        :param is_async: The is_async of this BatchDeleteTestCasesRequest.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def body(self):
        """Gets the body of this BatchDeleteTestCasesRequest.

        :return: The body of this BatchDeleteTestCasesRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.DeleteTestCaseInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchDeleteTestCasesRequest.

        :param body: The body of this BatchDeleteTestCasesRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.DeleteTestCaseInfo`
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
        if not isinstance(other, BatchDeleteTestCasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
