# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEdgeCloudRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, offset=None, limit=None, name=None, id=None):
        """ListEdgeCloudRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。 当前偏移量，默认为0。
        :type offset: int
        :param limit: 查询返回边缘业务列表当前页面的数量。 取值范围：0~1000。
        :type limit: int
        :param name: 边缘业务名称。
        :type name: str
        :param id: 边缘业务ID。
        :type id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def offset(self):
        """Gets the offset of this ListEdgeCloudRequest.

        偏移量。 当前偏移量，默认为0。

        :return: The offset of this ListEdgeCloudRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEdgeCloudRequest.

        偏移量。 当前偏移量，默认为0。

        :param offset: The offset of this ListEdgeCloudRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEdgeCloudRequest.

        查询返回边缘业务列表当前页面的数量。 取值范围：0~1000。

        :return: The limit of this ListEdgeCloudRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEdgeCloudRequest.

        查询返回边缘业务列表当前页面的数量。 取值范围：0~1000。

        :param limit: The limit of this ListEdgeCloudRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListEdgeCloudRequest.

        边缘业务名称。

        :return: The name of this ListEdgeCloudRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEdgeCloudRequest.

        边缘业务名称。

        :param name: The name of this ListEdgeCloudRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ListEdgeCloudRequest.

        边缘业务ID。

        :return: The id of this ListEdgeCloudRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListEdgeCloudRequest.

        边缘业务ID。

        :param id: The id of this ListEdgeCloudRequest.
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
        if not isinstance(other, ListEdgeCloudRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
