# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeResourceInEnvironmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'environment_id': 'str',
        'body': 'EnvironmentResourceModify'
    }

    attribute_map = {
        'environment_id': 'environment_id',
        'body': 'body'
    }

    def __init__(self, environment_id=None, body=None):
        """ChangeResourceInEnvironmentRequest

        The model defined in huaweicloud sdk

        :param environment_id: 环境ID。
        :type environment_id: str
        :param body: Body of the ChangeResourceInEnvironmentRequest
        :type body: :class:`huaweicloudsdkservicestage.v2.EnvironmentResourceModify`
        """
        
        

        self._environment_id = None
        self._body = None
        self.discriminator = None

        self.environment_id = environment_id
        if body is not None:
            self.body = body

    @property
    def environment_id(self):
        """Gets the environment_id of this ChangeResourceInEnvironmentRequest.

        环境ID。

        :return: The environment_id of this ChangeResourceInEnvironmentRequest.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this ChangeResourceInEnvironmentRequest.

        环境ID。

        :param environment_id: The environment_id of this ChangeResourceInEnvironmentRequest.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def body(self):
        """Gets the body of this ChangeResourceInEnvironmentRequest.


        :return: The body of this ChangeResourceInEnvironmentRequest.
        :rtype: :class:`huaweicloudsdkservicestage.v2.EnvironmentResourceModify`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ChangeResourceInEnvironmentRequest.


        :param body: The body of this ChangeResourceInEnvironmentRequest.
        :type body: :class:`huaweicloudsdkservicestage.v2.EnvironmentResourceModify`
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
        if not isinstance(other, ChangeResourceInEnvironmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
