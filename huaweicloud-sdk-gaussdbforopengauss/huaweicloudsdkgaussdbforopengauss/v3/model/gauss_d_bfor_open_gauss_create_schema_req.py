# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussCreateSchemaReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'owner': 'str'
    }

    attribute_map = {
        'name': 'name',
        'owner': 'owner'
    }

    def __init__(self, name=None, owner=None):
        """GaussDBforOpenGaussCreateSchemaReq

        The model defined in huaweicloud sdk

        :param name: schema名称。  schema名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB for OpenGauss模板库和已存在的schema重名。 GaussDB for OpenGauss模板库包括postgres， template0 ，template1。  已存在的schema包括public，information_schema。
        :type name: str
        :param owner: 数据库属主用户。  数据库属主名称在1到63个字符之间，不能以“pg”和数字开头，不能和系统用户名称相同。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。
        :type owner: str
        """
        
        

        self._name = None
        self._owner = None
        self.discriminator = None

        self.name = name
        self.owner = owner

    @property
    def name(self):
        """Gets the name of this GaussDBforOpenGaussCreateSchemaReq.

        schema名称。  schema名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB for OpenGauss模板库和已存在的schema重名。 GaussDB for OpenGauss模板库包括postgres， template0 ，template1。  已存在的schema包括public，information_schema。

        :return: The name of this GaussDBforOpenGaussCreateSchemaReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GaussDBforOpenGaussCreateSchemaReq.

        schema名称。  schema名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB for OpenGauss模板库和已存在的schema重名。 GaussDB for OpenGauss模板库包括postgres， template0 ，template1。  已存在的schema包括public，information_schema。

        :param name: The name of this GaussDBforOpenGaussCreateSchemaReq.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        """Gets the owner of this GaussDBforOpenGaussCreateSchemaReq.

        数据库属主用户。  数据库属主名称在1到63个字符之间，不能以“pg”和数字开头，不能和系统用户名称相同。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :return: The owner of this GaussDBforOpenGaussCreateSchemaReq.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GaussDBforOpenGaussCreateSchemaReq.

        数据库属主用户。  数据库属主名称在1到63个字符之间，不能以“pg”和数字开头，不能和系统用户名称相同。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :param owner: The owner of this GaussDBforOpenGaussCreateSchemaReq.
        :type owner: str
        """
        self._owner = owner

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
        if not isinstance(other, GaussDBforOpenGaussCreateSchemaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
