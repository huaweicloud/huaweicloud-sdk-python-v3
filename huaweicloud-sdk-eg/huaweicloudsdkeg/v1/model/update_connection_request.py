# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConnectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'body': 'ConnectionUpdateReq'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'body': 'body'
    }

    def __init__(self, connection_id=None, body=None):
        """UpdateConnectionRequest

        The model defined in huaweicloud sdk

        :param connection_id: 指定查询的目标连接ID
        :type connection_id: str
        :param body: Body of the UpdateConnectionRequest
        :type body: :class:`huaweicloudsdkeg.v1.ConnectionUpdateReq`
        """
        
        

        self._connection_id = None
        self._body = None
        self.discriminator = None

        self.connection_id = connection_id
        if body is not None:
            self.body = body

    @property
    def connection_id(self):
        """Gets the connection_id of this UpdateConnectionRequest.

        指定查询的目标连接ID

        :return: The connection_id of this UpdateConnectionRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this UpdateConnectionRequest.

        指定查询的目标连接ID

        :param connection_id: The connection_id of this UpdateConnectionRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def body(self):
        """Gets the body of this UpdateConnectionRequest.


        :return: The body of this UpdateConnectionRequest.
        :rtype: :class:`huaweicloudsdkeg.v1.ConnectionUpdateReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateConnectionRequest.


        :param body: The body of this UpdateConnectionRequest.
        :type body: :class:`huaweicloudsdkeg.v1.ConnectionUpdateReq`
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
        if not isinstance(other, UpdateConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
