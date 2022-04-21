# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TokenCatalog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'endpoints': 'list[TokenCatalogEndpoint]'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'endpoints': 'endpoints'
    }

    def __init__(self, type=None, id=None, name=None, endpoints=None):
        """TokenCatalog

        The model defined in huaweicloud sdk

        :param type: 该接口所属服务。
        :type type: str
        :param id: 服务ID。
        :type id: str
        :param name: 服务名称。
        :type name: str
        :param endpoints: 终端节点。
        :type endpoints: list[:class:`huaweicloudsdkiam.v3.TokenCatalogEndpoint`]
        """
        
        

        self._type = None
        self._id = None
        self._name = None
        self._endpoints = None
        self.discriminator = None

        self.type = type
        self.id = id
        self.name = name
        self.endpoints = endpoints

    @property
    def type(self):
        """Gets the type of this TokenCatalog.

        该接口所属服务。

        :return: The type of this TokenCatalog.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TokenCatalog.

        该接口所属服务。

        :param type: The type of this TokenCatalog.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this TokenCatalog.

        服务ID。

        :return: The id of this TokenCatalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TokenCatalog.

        服务ID。

        :param id: The id of this TokenCatalog.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TokenCatalog.

        服务名称。

        :return: The name of this TokenCatalog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenCatalog.

        服务名称。

        :param name: The name of this TokenCatalog.
        :type name: str
        """
        self._name = name

    @property
    def endpoints(self):
        """Gets the endpoints of this TokenCatalog.

        终端节点。

        :return: The endpoints of this TokenCatalog.
        :rtype: list[:class:`huaweicloudsdkiam.v3.TokenCatalogEndpoint`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this TokenCatalog.

        终端节点。

        :param endpoints: The endpoints of this TokenCatalog.
        :type endpoints: list[:class:`huaweicloudsdkiam.v3.TokenCatalogEndpoint`]
        """
        self._endpoints = endpoints

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
        if not isinstance(other, TokenCatalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
