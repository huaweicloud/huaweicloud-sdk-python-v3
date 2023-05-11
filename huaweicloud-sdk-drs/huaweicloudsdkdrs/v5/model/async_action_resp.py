# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncActionResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_id': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'query_id': 'query_id',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, query_id=None, id=None, name=None):
        """AsyncActionResp

        The model defined in huaweicloud sdk

        :param query_id: 异步操作任务响应查询ID。
        :type query_id: str
        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        """
        
        

        self._query_id = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.query_id = query_id
        self.id = id
        self.name = name

    @property
    def query_id(self):
        """Gets the query_id of this AsyncActionResp.

        异步操作任务响应查询ID。

        :return: The query_id of this AsyncActionResp.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this AsyncActionResp.

        异步操作任务响应查询ID。

        :param query_id: The query_id of this AsyncActionResp.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def id(self):
        """Gets the id of this AsyncActionResp.

        任务ID。

        :return: The id of this AsyncActionResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AsyncActionResp.

        任务ID。

        :param id: The id of this AsyncActionResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AsyncActionResp.

        任务名称。

        :return: The name of this AsyncActionResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AsyncActionResp.

        任务名称。

        :param name: The name of this AsyncActionResp.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AsyncActionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
