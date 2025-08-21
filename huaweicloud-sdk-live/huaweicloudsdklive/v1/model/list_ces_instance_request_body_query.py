# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCesInstanceRequestBodyQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dim_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'dim_name': 'dim_name',
        'id': 'id'
    }

    def __init__(self, dim_name=None, id=None):
        r"""ListCesInstanceRequestBodyQuery

        The model defined in huaweicloud sdk

        :param dim_name: 维度名称
        :type dim_name: str
        :param id: 维度id
        :type id: str
        """
        
        

        self._dim_name = None
        self._id = None
        self.discriminator = None

        self.dim_name = dim_name
        if id is not None:
            self.id = id

    @property
    def dim_name(self):
        r"""Gets the dim_name of this ListCesInstanceRequestBodyQuery.

        维度名称

        :return: The dim_name of this ListCesInstanceRequestBodyQuery.
        :rtype: str
        """
        return self._dim_name

    @dim_name.setter
    def dim_name(self, dim_name):
        r"""Sets the dim_name of this ListCesInstanceRequestBodyQuery.

        维度名称

        :param dim_name: The dim_name of this ListCesInstanceRequestBodyQuery.
        :type dim_name: str
        """
        self._dim_name = dim_name

    @property
    def id(self):
        r"""Gets the id of this ListCesInstanceRequestBodyQuery.

        维度id

        :return: The id of this ListCesInstanceRequestBodyQuery.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListCesInstanceRequestBodyQuery.

        维度id

        :param id: The id of this ListCesInstanceRequestBodyQuery.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ListCesInstanceRequestBodyQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
