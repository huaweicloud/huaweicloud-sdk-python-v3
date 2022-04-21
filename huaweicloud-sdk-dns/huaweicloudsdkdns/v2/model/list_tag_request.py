# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'body': 'ListTagReq'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'body': 'body'
    }

    def __init__(self, resource_type=None, body=None):
        """ListTagRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源的类型：DNS-public_zone，DNS-private_zone，DNS-public_recordset，DNS-private_recordset，DNS-ptr_record。
        :type resource_type: str
        :param body: Body of the ListTagRequest
        :type body: :class:`huaweicloudsdkdns.v2.ListTagReq`
        """
        
        

        self._resource_type = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        """Gets the resource_type of this ListTagRequest.

        资源的类型：DNS-public_zone，DNS-private_zone，DNS-public_recordset，DNS-private_recordset，DNS-ptr_record。

        :return: The resource_type of this ListTagRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListTagRequest.

        资源的类型：DNS-public_zone，DNS-private_zone，DNS-public_recordset，DNS-private_recordset，DNS-ptr_record。

        :param resource_type: The resource_type of this ListTagRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def body(self):
        """Gets the body of this ListTagRequest.


        :return: The body of this ListTagRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.ListTagReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListTagRequest.


        :param body: The body of this ListTagRequest.
        :type body: :class:`huaweicloudsdkdns.v2.ListTagReq`
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
        if not isinstance(other, ListTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
