# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReferResources:

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
        'type': 'ResourceType',
        'refer_alias': 'str',
        'parameters': 'object'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'refer_alias': 'refer_alias',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, type=None, refer_alias=None, parameters=None):
        r"""ReferResources

        The model defined in huaweicloud sdk

        :param id: 资源ID。
        :type id: str
        :param type: 
        :type type: :class:`huaweicloudsdkservicestage.v2.ResourceType`
        :param refer_alias: 应用别名，dcs时才提供，支持“distributed_session”、“distributed_cache”、“distributed_session, distributed_cache”，  默认值是“distributed_session, distributed_cache”。 
        :type refer_alias: str
        :param parameters: 引用资源参数。
        :type parameters: object
        """
        
        

        self._id = None
        self._type = None
        self._refer_alias = None
        self._parameters = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if refer_alias is not None:
            self.refer_alias = refer_alias
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        r"""Gets the id of this ReferResources.

        资源ID。

        :return: The id of this ReferResources.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReferResources.

        资源ID。

        :param id: The id of this ReferResources.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ReferResources.

        :return: The type of this ReferResources.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ResourceType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ReferResources.

        :param type: The type of this ReferResources.
        :type type: :class:`huaweicloudsdkservicestage.v2.ResourceType`
        """
        self._type = type

    @property
    def refer_alias(self):
        r"""Gets the refer_alias of this ReferResources.

        应用别名，dcs时才提供，支持“distributed_session”、“distributed_cache”、“distributed_session, distributed_cache”，  默认值是“distributed_session, distributed_cache”。 

        :return: The refer_alias of this ReferResources.
        :rtype: str
        """
        return self._refer_alias

    @refer_alias.setter
    def refer_alias(self, refer_alias):
        r"""Sets the refer_alias of this ReferResources.

        应用别名，dcs时才提供，支持“distributed_session”、“distributed_cache”、“distributed_session, distributed_cache”，  默认值是“distributed_session, distributed_cache”。 

        :param refer_alias: The refer_alias of this ReferResources.
        :type refer_alias: str
        """
        self._refer_alias = refer_alias

    @property
    def parameters(self):
        r"""Gets the parameters of this ReferResources.

        引用资源参数。

        :return: The parameters of this ReferResources.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ReferResources.

        引用资源参数。

        :param parameters: The parameters of this ReferResources.
        :type parameters: object
        """
        self._parameters = parameters

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
        if not isinstance(other, ReferResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
