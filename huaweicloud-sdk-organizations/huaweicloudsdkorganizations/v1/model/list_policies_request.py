# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attached_entity_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'attached_entity_id': 'attached_entity_id',
        'limit': 'limit',
        'marker': 'marker',
        'x_language': 'X-Language'
    }

    def __init__(self, attached_entity_id=None, limit=None, marker=None, x_language=None):
        """ListPoliciesRequest

        The model defined in huaweicloud sdk

        :param attached_entity_id: 根、组织单元或帐号的唯一标识符（ID）。
        :type attached_entity_id: str
        :param limit: 页面中最大结果数量。
        :type limit: int
        :param marker: 分页标记。
        :type marker: str
        :param x_language: 选择接口返回的信息的语言
        :type x_language: str
        """
        
        

        self._attached_entity_id = None
        self._limit = None
        self._marker = None
        self._x_language = None
        self.discriminator = None

        if attached_entity_id is not None:
            self.attached_entity_id = attached_entity_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if x_language is not None:
            self.x_language = x_language

    @property
    def attached_entity_id(self):
        """Gets the attached_entity_id of this ListPoliciesRequest.

        根、组织单元或帐号的唯一标识符（ID）。

        :return: The attached_entity_id of this ListPoliciesRequest.
        :rtype: str
        """
        return self._attached_entity_id

    @attached_entity_id.setter
    def attached_entity_id(self, attached_entity_id):
        """Sets the attached_entity_id of this ListPoliciesRequest.

        根、组织单元或帐号的唯一标识符（ID）。

        :param attached_entity_id: The attached_entity_id of this ListPoliciesRequest.
        :type attached_entity_id: str
        """
        self._attached_entity_id = attached_entity_id

    @property
    def limit(self):
        """Gets the limit of this ListPoliciesRequest.

        页面中最大结果数量。

        :return: The limit of this ListPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPoliciesRequest.

        页面中最大结果数量。

        :param limit: The limit of this ListPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPoliciesRequest.

        分页标记。

        :return: The marker of this ListPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPoliciesRequest.

        分页标记。

        :param marker: The marker of this ListPoliciesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def x_language(self):
        """Gets the x_language of this ListPoliciesRequest.

        选择接口返回的信息的语言

        :return: The x_language of this ListPoliciesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListPoliciesRequest.

        选择接口返回的信息的语言

        :param x_language: The x_language of this ListPoliciesRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
