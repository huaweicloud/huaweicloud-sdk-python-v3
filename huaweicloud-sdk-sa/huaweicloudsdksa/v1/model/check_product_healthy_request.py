# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckProductHealthyRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'project_id': 'str',
        'body': 'ProductInfo'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'project_id': 'project_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, project_id=None, body=None):
        """CheckProductHealthyRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._project_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.project_id = project_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this CheckProductHealthyRequest.


        :return: The x_language of this CheckProductHealthyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this CheckProductHealthyRequest.


        :param x_language: The x_language of this CheckProductHealthyRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def project_id(self):
        """Gets the project_id of this CheckProductHealthyRequest.

        租户项目ID。

        :return: The project_id of this CheckProductHealthyRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CheckProductHealthyRequest.

        租户项目ID。

        :param project_id: The project_id of this CheckProductHealthyRequest.
        :type: str
        """
        self._project_id = project_id

    @property
    def body(self):
        """Gets the body of this CheckProductHealthyRequest.


        :return: The body of this CheckProductHealthyRequest.
        :rtype: ProductInfo
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CheckProductHealthyRequest.


        :param body: The body of this CheckProductHealthyRequest.
        :type: ProductInfo
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
        if not isinstance(other, CheckProductHealthyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other