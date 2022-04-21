# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeGaussMySqlInstanceSpecificationRequest:

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
        'instance_id': 'str',
        'body': 'MysqlChangeSpecificationRequest'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, x_language=None, instance_id=None, body=None):
        """ChangeGaussMySqlInstanceSpecificationRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param body: Body of the ChangeGaussMySqlInstanceSpecificationRequest
        :type body: :class:`huaweicloudsdkgaussdb.v3.MysqlChangeSpecificationRequest`
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        """Gets the x_language of this ChangeGaussMySqlInstanceSpecificationRequest.

        语言

        :return: The x_language of this ChangeGaussMySqlInstanceSpecificationRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ChangeGaussMySqlInstanceSpecificationRequest.

        语言

        :param x_language: The x_language of this ChangeGaussMySqlInstanceSpecificationRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ChangeGaussMySqlInstanceSpecificationRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ChangeGaussMySqlInstanceSpecificationRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ChangeGaussMySqlInstanceSpecificationRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ChangeGaussMySqlInstanceSpecificationRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        """Gets the body of this ChangeGaussMySqlInstanceSpecificationRequest.


        :return: The body of this ChangeGaussMySqlInstanceSpecificationRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlChangeSpecificationRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ChangeGaussMySqlInstanceSpecificationRequest.


        :param body: The body of this ChangeGaussMySqlInstanceSpecificationRequest.
        :type body: :class:`huaweicloudsdkgaussdb.v3.MysqlChangeSpecificationRequest`
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
        if not isinstance(other, ChangeGaussMySqlInstanceSpecificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
