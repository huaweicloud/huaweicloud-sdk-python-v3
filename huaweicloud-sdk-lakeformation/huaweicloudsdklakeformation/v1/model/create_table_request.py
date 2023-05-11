# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTableRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'catalog_name': 'str',
        'database_name': 'str',
        'body': 'TableInput'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'body': 'body'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, body=None):
        """CreateTableRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例Id
        :type instance_id: str
        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param body: Body of the CreateTableRequest
        :type body: :class:`huaweicloudsdklakeformation.v1.TableInput`
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateTableRequest.

        实例Id

        :return: The instance_id of this CreateTableRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateTableRequest.

        实例Id

        :param instance_id: The instance_id of this CreateTableRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        """Gets the catalog_name of this CreateTableRequest.

        catalog名字

        :return: The catalog_name of this CreateTableRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this CreateTableRequest.

        catalog名字

        :param catalog_name: The catalog_name of this CreateTableRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this CreateTableRequest.

        数据库名字

        :return: The database_name of this CreateTableRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this CreateTableRequest.

        数据库名字

        :param database_name: The database_name of this CreateTableRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def body(self):
        """Gets the body of this CreateTableRequest.

        :return: The body of this CreateTableRequest.
        :rtype: :class:`huaweicloudsdklakeformation.v1.TableInput`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateTableRequest.

        :param body: The body of this CreateTableRequest.
        :type body: :class:`huaweicloudsdklakeformation.v1.TableInput`
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
        if not isinstance(other, CreateTableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
