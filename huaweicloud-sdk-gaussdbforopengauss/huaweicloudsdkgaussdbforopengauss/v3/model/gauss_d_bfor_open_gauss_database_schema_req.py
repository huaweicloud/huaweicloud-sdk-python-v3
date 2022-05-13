# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBforOpenGaussDatabaseSchemaReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'schemas': 'list[GaussDBforOpenGaussCreateSchemaReq]'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schemas': 'schemas'
    }

    def __init__(self, db_name=None, schemas=None):
        """GaussDBforOpenGaussDatabaseSchemaReq

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。  数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB for OpenGauss模板库重名。  GaussDB for OpenGauss模板库包括postgres， template0 ，template1。
        :type db_name: str
        :param schemas: 每个元素都是与数据库相关联的schmea信息。单次请求最多支持20个元素。
        :type schemas: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussCreateSchemaReq`]
        """
        
        

        self._db_name = None
        self._schemas = None
        self.discriminator = None

        self.db_name = db_name
        self.schemas = schemas

    @property
    def db_name(self):
        """Gets the db_name of this GaussDBforOpenGaussDatabaseSchemaReq.

        数据库名称。  数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB for OpenGauss模板库重名。  GaussDB for OpenGauss模板库包括postgres， template0 ，template1。

        :return: The db_name of this GaussDBforOpenGaussDatabaseSchemaReq.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this GaussDBforOpenGaussDatabaseSchemaReq.

        数据库名称。  数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和GaussDB for OpenGauss模板库重名。  GaussDB for OpenGauss模板库包括postgres， template0 ，template1。

        :param db_name: The db_name of this GaussDBforOpenGaussDatabaseSchemaReq.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schemas(self):
        """Gets the schemas of this GaussDBforOpenGaussDatabaseSchemaReq.

        每个元素都是与数据库相关联的schmea信息。单次请求最多支持20个元素。

        :return: The schemas of this GaussDBforOpenGaussDatabaseSchemaReq.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussCreateSchemaReq`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this GaussDBforOpenGaussDatabaseSchemaReq.

        每个元素都是与数据库相关联的schmea信息。单次请求最多支持20个元素。

        :param schemas: The schemas of this GaussDBforOpenGaussDatabaseSchemaReq.
        :type schemas: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBforOpenGaussCreateSchemaReq`]
        """
        self._schemas = schemas

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
        if not isinstance(other, GaussDBforOpenGaussDatabaseSchemaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
