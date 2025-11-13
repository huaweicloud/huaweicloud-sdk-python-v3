# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginBuiltInAccountRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str'
    }

    attribute_map = {
        'datastore_type': 'datastore_type'
    }

    def __init__(self, datastore_type=None):
        r"""LoginBuiltInAccountRequestBody

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库引擎，仅支持MySQL
        :type datastore_type: str
        """
        
        

        self._datastore_type = None
        self.discriminator = None

        self.datastore_type = datastore_type

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this LoginBuiltInAccountRequestBody.

        数据库引擎，仅支持MySQL

        :return: The datastore_type of this LoginBuiltInAccountRequestBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this LoginBuiltInAccountRequestBody.

        数据库引擎，仅支持MySQL

        :param datastore_type: The datastore_type of this LoginBuiltInAccountRequestBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginBuiltInAccountRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
