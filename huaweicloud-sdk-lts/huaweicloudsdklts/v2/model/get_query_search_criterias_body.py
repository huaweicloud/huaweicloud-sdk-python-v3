# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetQuerySearchCriteriasBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'criteria': 'str',
        'name': 'str',
        'id': 'str',
        'search_type': 'str'
    }

    attribute_map = {
        'criteria': 'criteria',
        'name': 'name',
        'id': 'id',
        'search_type': 'search_type'
    }

    def __init__(self, criteria=None, name=None, id=None, search_type=None):
        r"""GetQuerySearchCriteriasBody

        The model defined in huaweicloud sdk

        :param criteria: 快速查询字段
        :type criteria: str
        :param name: 快速查询名称
        :type name: str
        :param id: 快速查询id
        :type id: str
        :param search_type: 快速查询类型： 原始日志：ORIGINALLOG 可视化日志: VISUALIZATION
        :type search_type: str
        """
        
        

        self._criteria = None
        self._name = None
        self._id = None
        self._search_type = None
        self.discriminator = None

        if criteria is not None:
            self.criteria = criteria
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if search_type is not None:
            self.search_type = search_type

    @property
    def criteria(self):
        r"""Gets the criteria of this GetQuerySearchCriteriasBody.

        快速查询字段

        :return: The criteria of this GetQuerySearchCriteriasBody.
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        r"""Sets the criteria of this GetQuerySearchCriteriasBody.

        快速查询字段

        :param criteria: The criteria of this GetQuerySearchCriteriasBody.
        :type criteria: str
        """
        self._criteria = criteria

    @property
    def name(self):
        r"""Gets the name of this GetQuerySearchCriteriasBody.

        快速查询名称

        :return: The name of this GetQuerySearchCriteriasBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetQuerySearchCriteriasBody.

        快速查询名称

        :param name: The name of this GetQuerySearchCriteriasBody.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this GetQuerySearchCriteriasBody.

        快速查询id

        :return: The id of this GetQuerySearchCriteriasBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetQuerySearchCriteriasBody.

        快速查询id

        :param id: The id of this GetQuerySearchCriteriasBody.
        :type id: str
        """
        self._id = id

    @property
    def search_type(self):
        r"""Gets the search_type of this GetQuerySearchCriteriasBody.

        快速查询类型： 原始日志：ORIGINALLOG 可视化日志: VISUALIZATION

        :return: The search_type of this GetQuerySearchCriteriasBody.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this GetQuerySearchCriteriasBody.

        快速查询类型： 原始日志：ORIGINALLOG 可视化日志: VISUALIZATION

        :param search_type: The search_type of this GetQuerySearchCriteriasBody.
        :type search_type: str
        """
        self._search_type = search_type

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
        if not isinstance(other, GetQuerySearchCriteriasBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
