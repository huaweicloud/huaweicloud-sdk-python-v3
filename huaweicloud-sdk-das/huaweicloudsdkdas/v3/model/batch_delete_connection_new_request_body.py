# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteConnectionNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_all': 'bool',
        'connection_ids': 'list[ConnectionIdsItem]'
    }

    attribute_map = {
        'delete_all': 'delete_all',
        'connection_ids': 'connection_ids'
    }

    def __init__(self, delete_all=None, connection_ids=None):
        r"""BatchDeleteConnectionNewRequestBody

        The model defined in huaweicloud sdk

        :param delete_all: 是否删除所有连接
        :type delete_all: bool
        :param connection_ids: 连接ID列表
        :type connection_ids: list[:class:`huaweicloudsdkdas.v3.ConnectionIdsItem`]
        """
        
        

        self._delete_all = None
        self._connection_ids = None
        self.discriminator = None

        if delete_all is not None:
            self.delete_all = delete_all
        if connection_ids is not None:
            self.connection_ids = connection_ids

    @property
    def delete_all(self):
        r"""Gets the delete_all of this BatchDeleteConnectionNewRequestBody.

        是否删除所有连接

        :return: The delete_all of this BatchDeleteConnectionNewRequestBody.
        :rtype: bool
        """
        return self._delete_all

    @delete_all.setter
    def delete_all(self, delete_all):
        r"""Sets the delete_all of this BatchDeleteConnectionNewRequestBody.

        是否删除所有连接

        :param delete_all: The delete_all of this BatchDeleteConnectionNewRequestBody.
        :type delete_all: bool
        """
        self._delete_all = delete_all

    @property
    def connection_ids(self):
        r"""Gets the connection_ids of this BatchDeleteConnectionNewRequestBody.

        连接ID列表

        :return: The connection_ids of this BatchDeleteConnectionNewRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ConnectionIdsItem`]
        """
        return self._connection_ids

    @connection_ids.setter
    def connection_ids(self, connection_ids):
        r"""Sets the connection_ids of this BatchDeleteConnectionNewRequestBody.

        连接ID列表

        :param connection_ids: The connection_ids of this BatchDeleteConnectionNewRequestBody.
        :type connection_ids: list[:class:`huaweicloudsdkdas.v3.ConnectionIdsItem`]
        """
        self._connection_ids = connection_ids

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
        if not isinstance(other, BatchDeleteConnectionNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
