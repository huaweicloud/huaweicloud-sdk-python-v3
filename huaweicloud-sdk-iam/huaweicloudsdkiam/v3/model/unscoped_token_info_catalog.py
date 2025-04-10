# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnscopedTokenInfoCatalog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'endpoints': 'list[UnscopedTokenInfoEndpoints]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'endpoints': 'endpoints'
    }

    def __init__(self, id=None, name=None, type=None, endpoints=None):
        r"""UnscopedTokenInfoCatalog

        The model defined in huaweicloud sdk

        :param id: 终端节点ID。
        :type id: str
        :param name: 服务名称。
        :type name: str
        :param type: 该接口所属服务。
        :type type: str
        :param endpoints: 
        :type endpoints: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoEndpoints`]
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._endpoints = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def id(self):
        r"""Gets the id of this UnscopedTokenInfoCatalog.

        终端节点ID。

        :return: The id of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UnscopedTokenInfoCatalog.

        终端节点ID。

        :param id: The id of this UnscopedTokenInfoCatalog.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UnscopedTokenInfoCatalog.

        服务名称。

        :return: The name of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UnscopedTokenInfoCatalog.

        服务名称。

        :param name: The name of this UnscopedTokenInfoCatalog.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this UnscopedTokenInfoCatalog.

        该接口所属服务。

        :return: The type of this UnscopedTokenInfoCatalog.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UnscopedTokenInfoCatalog.

        该接口所属服务。

        :param type: The type of this UnscopedTokenInfoCatalog.
        :type type: str
        """
        self._type = type

    @property
    def endpoints(self):
        r"""Gets the endpoints of this UnscopedTokenInfoCatalog.

        :return: The endpoints of this UnscopedTokenInfoCatalog.
        :rtype: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoEndpoints`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this UnscopedTokenInfoCatalog.

        :param endpoints: The endpoints of this UnscopedTokenInfoCatalog.
        :type endpoints: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoEndpoints`]
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
        if not isinstance(other, UnscopedTokenInfoCatalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
