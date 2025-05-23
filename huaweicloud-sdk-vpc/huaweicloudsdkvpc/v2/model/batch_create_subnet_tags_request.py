# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateSubnetTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'body': 'BatchCreateSubnetTagsRequestBody'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'body': 'body'
    }

    def __init__(self, subnet_id=None, body=None):
        r"""BatchCreateSubnetTagsRequest

        The model defined in huaweicloud sdk

        :param subnet_id: 子网ID
        :type subnet_id: str
        :param body: Body of the BatchCreateSubnetTagsRequest
        :type body: :class:`huaweicloudsdkvpc.v2.BatchCreateSubnetTagsRequestBody`
        """
        
        

        self._subnet_id = None
        self._body = None
        self.discriminator = None

        self.subnet_id = subnet_id
        if body is not None:
            self.body = body

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this BatchCreateSubnetTagsRequest.

        子网ID

        :return: The subnet_id of this BatchCreateSubnetTagsRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this BatchCreateSubnetTagsRequest.

        子网ID

        :param subnet_id: The subnet_id of this BatchCreateSubnetTagsRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateSubnetTagsRequest.

        :return: The body of this BatchCreateSubnetTagsRequest.
        :rtype: :class:`huaweicloudsdkvpc.v2.BatchCreateSubnetTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateSubnetTagsRequest.

        :param body: The body of this BatchCreateSubnetTagsRequest.
        :type body: :class:`huaweicloudsdkvpc.v2.BatchCreateSubnetTagsRequestBody`
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
        if not isinstance(other, BatchCreateSubnetTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
