# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSearchCriteriasBody:

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
        'eps_id': 'str',
        'name': 'str',
        'search_type': 'str'
    }

    attribute_map = {
        'criteria': 'criteria',
        'eps_id': 'eps_id',
        'name': 'name',
        'search_type': 'search_type'
    }

    def __init__(self, criteria=None, eps_id=None, name=None, search_type=None):
        r"""CreateSearchCriteriasBody

        The model defined in huaweicloud sdk

        :param criteria: 快速查询字段
        :type criteria: str
        :param eps_id: 企业项目id
        :type eps_id: str
        :param name: 创建快速查询名称
        :type name: str
        :param search_type: 查询类型 原始日志：ORIGINALLOG 可视化日志: VISUALIZATION
        :type search_type: str
        """
        
        

        self._criteria = None
        self._eps_id = None
        self._name = None
        self._search_type = None
        self.discriminator = None

        self.criteria = criteria
        if eps_id is not None:
            self.eps_id = eps_id
        self.name = name
        self.search_type = search_type

    @property
    def criteria(self):
        r"""Gets the criteria of this CreateSearchCriteriasBody.

        快速查询字段

        :return: The criteria of this CreateSearchCriteriasBody.
        :rtype: str
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        r"""Sets the criteria of this CreateSearchCriteriasBody.

        快速查询字段

        :param criteria: The criteria of this CreateSearchCriteriasBody.
        :type criteria: str
        """
        self._criteria = criteria

    @property
    def eps_id(self):
        r"""Gets the eps_id of this CreateSearchCriteriasBody.

        企业项目id

        :return: The eps_id of this CreateSearchCriteriasBody.
        :rtype: str
        """
        return self._eps_id

    @eps_id.setter
    def eps_id(self, eps_id):
        r"""Sets the eps_id of this CreateSearchCriteriasBody.

        企业项目id

        :param eps_id: The eps_id of this CreateSearchCriteriasBody.
        :type eps_id: str
        """
        self._eps_id = eps_id

    @property
    def name(self):
        r"""Gets the name of this CreateSearchCriteriasBody.

        创建快速查询名称

        :return: The name of this CreateSearchCriteriasBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSearchCriteriasBody.

        创建快速查询名称

        :param name: The name of this CreateSearchCriteriasBody.
        :type name: str
        """
        self._name = name

    @property
    def search_type(self):
        r"""Gets the search_type of this CreateSearchCriteriasBody.

        查询类型 原始日志：ORIGINALLOG 可视化日志: VISUALIZATION

        :return: The search_type of this CreateSearchCriteriasBody.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this CreateSearchCriteriasBody.

        查询类型 原始日志：ORIGINALLOG 可视化日志: VISUALIZATION

        :param search_type: The search_type of this CreateSearchCriteriasBody.
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
        if not isinstance(other, CreateSearchCriteriasBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
