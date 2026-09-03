# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseObjectsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'object',
        'total': 'int',
        'object_type': 'str'
    }

    attribute_map = {
        'data': 'data',
        'total': 'total',
        'object_type': 'object_type'
    }

    def __init__(self, data=None, total=None, object_type=None):
        r"""ListDatabaseObjectsResponse

        The model defined in huaweicloud sdk

        :param data: 数据库对象信息列表
        :type data: object
        :param total: 列表大小
        :type total: int
        :param object_type: 对象类型
        :type object_type: str
        """
        
        super().__init__()

        self._data = None
        self._total = None
        self._object_type = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total is not None:
            self.total = total
        if object_type is not None:
            self.object_type = object_type

    @property
    def data(self):
        r"""Gets the data of this ListDatabaseObjectsResponse.

        数据库对象信息列表

        :return: The data of this ListDatabaseObjectsResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListDatabaseObjectsResponse.

        数据库对象信息列表

        :param data: The data of this ListDatabaseObjectsResponse.
        :type data: object
        """
        self._data = data

    @property
    def total(self):
        r"""Gets the total of this ListDatabaseObjectsResponse.

        列表大小

        :return: The total of this ListDatabaseObjectsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDatabaseObjectsResponse.

        列表大小

        :param total: The total of this ListDatabaseObjectsResponse.
        :type total: int
        """
        self._total = total

    @property
    def object_type(self):
        r"""Gets the object_type of this ListDatabaseObjectsResponse.

        对象类型

        :return: The object_type of this ListDatabaseObjectsResponse.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListDatabaseObjectsResponse.

        对象类型

        :param object_type: The object_type of this ListDatabaseObjectsResponse.
        :type object_type: str
        """
        self._object_type = object_type

    def to_dict(self):
        import warnings
        warnings.warn("ListDatabaseObjectsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListDatabaseObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
