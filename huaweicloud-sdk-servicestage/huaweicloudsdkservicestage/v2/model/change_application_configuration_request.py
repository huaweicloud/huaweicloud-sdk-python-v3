# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeApplicationConfigurationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'body': 'ApplicationConfigModify'
    }

    attribute_map = {
        'application_id': 'application_id',
        'body': 'body'
    }

    def __init__(self, application_id=None, body=None):
        """ChangeApplicationConfigurationRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用ID。
        :type application_id: str
        :param body: Body of the ChangeApplicationConfigurationRequest
        :type body: :class:`huaweicloudsdkservicestage.v2.ApplicationConfigModify`
        """
        
        

        self._application_id = None
        self._body = None
        self.discriminator = None

        self.application_id = application_id
        if body is not None:
            self.body = body

    @property
    def application_id(self):
        """Gets the application_id of this ChangeApplicationConfigurationRequest.

        应用ID。

        :return: The application_id of this ChangeApplicationConfigurationRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ChangeApplicationConfigurationRequest.

        应用ID。

        :param application_id: The application_id of this ChangeApplicationConfigurationRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def body(self):
        """Gets the body of this ChangeApplicationConfigurationRequest.


        :return: The body of this ChangeApplicationConfigurationRequest.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ApplicationConfigModify`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ChangeApplicationConfigurationRequest.


        :param body: The body of this ChangeApplicationConfigurationRequest.
        :type body: :class:`huaweicloudsdkservicestage.v2.ApplicationConfigModify`
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
        if not isinstance(other, ChangeApplicationConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
