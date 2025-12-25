# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDataclassTypeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_delete': 'bool',
        'ids': 'list[str]'
    }

    attribute_map = {
        'is_delete': 'is_delete',
        'ids': 'ids'
    }

    def __init__(self, is_delete=None, ids=None):
        r"""DeleteDataclassTypeRequestBody

        The model defined in huaweicloud sdk

        :param is_delete: 是否删除，true删除，false不删除
        :type is_delete: bool
        :param ids: 删除ids
        :type ids: list[str]
        """
        
        

        self._is_delete = None
        self._ids = None
        self.discriminator = None

        self.is_delete = is_delete
        self.ids = ids

    @property
    def is_delete(self):
        r"""Gets the is_delete of this DeleteDataclassTypeRequestBody.

        是否删除，true删除，false不删除

        :return: The is_delete of this DeleteDataclassTypeRequestBody.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        r"""Sets the is_delete of this DeleteDataclassTypeRequestBody.

        是否删除，true删除，false不删除

        :param is_delete: The is_delete of this DeleteDataclassTypeRequestBody.
        :type is_delete: bool
        """
        self._is_delete = is_delete

    @property
    def ids(self):
        r"""Gets the ids of this DeleteDataclassTypeRequestBody.

        删除ids

        :return: The ids of this DeleteDataclassTypeRequestBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this DeleteDataclassTypeRequestBody.

        删除ids

        :param ids: The ids of this DeleteDataclassTypeRequestBody.
        :type ids: list[str]
        """
        self._ids = ids

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
        if not isinstance(other, DeleteDataclassTypeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
