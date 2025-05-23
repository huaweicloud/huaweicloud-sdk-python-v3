# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateTaskStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_suit_id': 'int',
        'body': 'BatchUpdateTaskStatusRequestBody'
    }

    attribute_map = {
        'test_suit_id': 'test_suit_id',
        'body': 'body'
    }

    def __init__(self, test_suit_id=None, body=None):
        r"""BatchUpdateTaskStatusRequest

        The model defined in huaweicloud sdk

        :param test_suit_id: 工程id
        :type test_suit_id: int
        :param body: Body of the BatchUpdateTaskStatusRequest
        :type body: :class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusRequestBody`
        """
        
        

        self._test_suit_id = None
        self._body = None
        self.discriminator = None

        self.test_suit_id = test_suit_id
        if body is not None:
            self.body = body

    @property
    def test_suit_id(self):
        r"""Gets the test_suit_id of this BatchUpdateTaskStatusRequest.

        工程id

        :return: The test_suit_id of this BatchUpdateTaskStatusRequest.
        :rtype: int
        """
        return self._test_suit_id

    @test_suit_id.setter
    def test_suit_id(self, test_suit_id):
        r"""Sets the test_suit_id of this BatchUpdateTaskStatusRequest.

        工程id

        :param test_suit_id: The test_suit_id of this BatchUpdateTaskStatusRequest.
        :type test_suit_id: int
        """
        self._test_suit_id = test_suit_id

    @property
    def body(self):
        r"""Gets the body of this BatchUpdateTaskStatusRequest.

        :return: The body of this BatchUpdateTaskStatusRequest.
        :rtype: :class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchUpdateTaskStatusRequest.

        :param body: The body of this BatchUpdateTaskStatusRequest.
        :type body: :class:`huaweicloudsdkcpts.v1.BatchUpdateTaskStatusRequestBody`
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
        if not isinstance(other, BatchUpdateTaskStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
