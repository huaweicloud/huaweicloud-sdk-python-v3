# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPwdOneClickRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'body': 'ResetPasswordBody'
    }

    attribute_map = {
        'server_id': 'server_id',
        'body': 'body'
    }

    def __init__(self, server_id=None, body=None):
        """ResetPwdOneClickRequest

        The model defined in huaweicloud sdk

        :param server_id: 裸金属服务器ID。可以从裸金属服务器控制台查询，或者通过调用7.3.4-查询裸金属服务器列表（OpenStack原生）API获取。
        :type server_id: str
        :param body: Body of the ResetPwdOneClickRequest
        :type body: :class:`huaweicloudsdkbms.v1.ResetPasswordBody`
        """
        
        

        self._server_id = None
        self._body = None
        self.discriminator = None

        self.server_id = server_id
        if body is not None:
            self.body = body

    @property
    def server_id(self):
        """Gets the server_id of this ResetPwdOneClickRequest.

        裸金属服务器ID。可以从裸金属服务器控制台查询，或者通过调用7.3.4-查询裸金属服务器列表（OpenStack原生）API获取。

        :return: The server_id of this ResetPwdOneClickRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ResetPwdOneClickRequest.

        裸金属服务器ID。可以从裸金属服务器控制台查询，或者通过调用7.3.4-查询裸金属服务器列表（OpenStack原生）API获取。

        :param server_id: The server_id of this ResetPwdOneClickRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def body(self):
        """Gets the body of this ResetPwdOneClickRequest.


        :return: The body of this ResetPwdOneClickRequest.
        :rtype: :class:`huaweicloudsdkbms.v1.ResetPasswordBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ResetPwdOneClickRequest.


        :param body: The body of this ResetPwdOneClickRequest.
        :type body: :class:`huaweicloudsdkbms.v1.ResetPasswordBody`
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
        if not isinstance(other, ResetPwdOneClickRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
