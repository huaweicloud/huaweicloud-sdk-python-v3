# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataStoresRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'data_store_id': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'data_store_id': 'data_store_id',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, group_id=None, data_store_id=None, name=None, offset=None, limit=None):
        """ListDataStoresRequest

        The model defined in huaweicloud sdk

        :param group_id: 存储组 ID
        :type group_id: str
        :param data_store_id: 存储 ID
        :type data_store_id: str
        :param name: 存储名称
        :type name: str
        :param offset: 页码
        :type offset: int
        :param limit: 返回条数限制
        :type limit: int
        """
        
        

        self._group_id = None
        self._data_store_id = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if data_store_id is not None:
            self.data_store_id = data_store_id
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def group_id(self):
        """Gets the group_id of this ListDataStoresRequest.

        存储组 ID

        :return: The group_id of this ListDataStoresRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListDataStoresRequest.

        存储组 ID

        :param group_id: The group_id of this ListDataStoresRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def data_store_id(self):
        """Gets the data_store_id of this ListDataStoresRequest.

        存储 ID

        :return: The data_store_id of this ListDataStoresRequest.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        """Sets the data_store_id of this ListDataStoresRequest.

        存储 ID

        :param data_store_id: The data_store_id of this ListDataStoresRequest.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def name(self):
        """Gets the name of this ListDataStoresRequest.

        存储名称

        :return: The name of this ListDataStoresRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDataStoresRequest.

        存储名称

        :param name: The name of this ListDataStoresRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListDataStoresRequest.

        页码

        :return: The offset of this ListDataStoresRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDataStoresRequest.

        页码

        :param offset: The offset of this ListDataStoresRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDataStoresRequest.

        返回条数限制

        :return: The limit of this ListDataStoresRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDataStoresRequest.

        返回条数限制

        :param limit: The limit of this ListDataStoresRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDataStoresRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
