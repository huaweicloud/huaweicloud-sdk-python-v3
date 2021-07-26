# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBcsMetricRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'body': 'ListBcsMetricRequestBody'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'body': 'body'
    }

    def __init__(self, blockchain_id=None, body=None):
        """ListBcsMetricRequest - a model defined in huaweicloud sdk"""
        
        

        self._blockchain_id = None
        self._body = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        if body is not None:
            self.body = body

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this ListBcsMetricRequest.

        区块链服务id,当前不支持IEF实例

        :return: The blockchain_id of this ListBcsMetricRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this ListBcsMetricRequest.

        区块链服务id,当前不支持IEF实例

        :param blockchain_id: The blockchain_id of this ListBcsMetricRequest.
        :type: str
        """
        self._blockchain_id = blockchain_id

    @property
    def body(self):
        """Gets the body of this ListBcsMetricRequest.


        :return: The body of this ListBcsMetricRequest.
        :rtype: ListBcsMetricRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListBcsMetricRequest.


        :param body: The body of this ListBcsMetricRequest.
        :type: ListBcsMetricRequestBody
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListBcsMetricRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
