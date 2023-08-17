# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunUpdateDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'body': 'UpdateParam'
    }

    attribute_map = {
        'service_name': 'service_name',
        'body': 'body'
    }

    def __init__(self, service_name=None, body=None):
        """RunUpdateDataRequest

        The model defined in huaweicloud sdk

        :param service_name: 服务实例的名称，用户创建服务实例时指定。
        :type service_name: str
        :param body: Body of the RunUpdateDataRequest
        :type body: :class:`huaweicloudsdkimagesearch.v2.UpdateParam`
        """
        
        

        self._service_name = None
        self._body = None
        self.discriminator = None

        self.service_name = service_name
        if body is not None:
            self.body = body

    @property
    def service_name(self):
        """Gets the service_name of this RunUpdateDataRequest.

        服务实例的名称，用户创建服务实例时指定。

        :return: The service_name of this RunUpdateDataRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this RunUpdateDataRequest.

        服务实例的名称，用户创建服务实例时指定。

        :param service_name: The service_name of this RunUpdateDataRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def body(self):
        """Gets the body of this RunUpdateDataRequest.

        :return: The body of this RunUpdateDataRequest.
        :rtype: :class:`huaweicloudsdkimagesearch.v2.UpdateParam`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this RunUpdateDataRequest.

        :param body: The body of this RunUpdateDataRequest.
        :type body: :class:`huaweicloudsdkimagesearch.v2.UpdateParam`
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
        if not isinstance(other, RunUpdateDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
