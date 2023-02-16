# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageResourceListParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'maker': 'str',
        'limit': 'int',
        'keywords': 'dict(str, str)',
        'ci_relationships': 'bool',
        'ci_type': 'str',
        'ci_region': 'str',
        'ci_ids': 'list[str]',
        'ci_id': 'str'
    }

    attribute_map = {
        'maker': 'maker',
        'limit': 'limit',
        'keywords': 'keywords',
        'ci_relationships': 'ci_relationships',
        'ci_type': 'ci_type',
        'ci_region': 'ci_region',
        'ci_ids': 'ci_ids',
        'ci_id': 'ci_id'
    }

    def __init__(self, maker=None, limit=None, keywords=None, ci_relationships=None, ci_type=None, ci_region=None, ci_ids=None, ci_id=None):
        """PageResourceListParam

        The model defined in huaweicloud sdk

        :param maker: 页面的分页标志位；为分页的最后一条记录的id
        :type maker: str
        :param limit: 查询返回记录的数量限制
        :type limit: int
        :param keywords: 关键字模糊搜索
        :type keywords: dict(str, str)
        :param ci_relationships: 是否需要返回拓扑树,默认是false。需要：true---性能差，不需要false--性能好
        :type ci_relationships: bool
        :param ci_type: 节点类型，取值：application、sub_application、component、environment
        :type ci_type: str
        :param ci_region: 环境的region信息，若没有值，代表全部
        :type ci_region: str
        :param ci_ids: 节点id列表;如果ci_ids和ci_id同时有，则优先ci_ids，但是不能同时为空
        :type ci_ids: list[str]
        :param ci_id: 节点id列表;如果ci_ids和ci_id同时有，则优先ci_ids，但是不能同时为空。但是不支持应用批量查询
        :type ci_id: str
        """
        
        

        self._maker = None
        self._limit = None
        self._keywords = None
        self._ci_relationships = None
        self._ci_type = None
        self._ci_region = None
        self._ci_ids = None
        self._ci_id = None
        self.discriminator = None

        if maker is not None:
            self.maker = maker
        if limit is not None:
            self.limit = limit
        if keywords is not None:
            self.keywords = keywords
        if ci_relationships is not None:
            self.ci_relationships = ci_relationships
        self.ci_type = ci_type
        if ci_region is not None:
            self.ci_region = ci_region
        if ci_ids is not None:
            self.ci_ids = ci_ids
        if ci_id is not None:
            self.ci_id = ci_id

    @property
    def maker(self):
        """Gets the maker of this PageResourceListParam.

        页面的分页标志位；为分页的最后一条记录的id

        :return: The maker of this PageResourceListParam.
        :rtype: str
        """
        return self._maker

    @maker.setter
    def maker(self, maker):
        """Sets the maker of this PageResourceListParam.

        页面的分页标志位；为分页的最后一条记录的id

        :param maker: The maker of this PageResourceListParam.
        :type maker: str
        """
        self._maker = maker

    @property
    def limit(self):
        """Gets the limit of this PageResourceListParam.

        查询返回记录的数量限制

        :return: The limit of this PageResourceListParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageResourceListParam.

        查询返回记录的数量限制

        :param limit: The limit of this PageResourceListParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def keywords(self):
        """Gets the keywords of this PageResourceListParam.

        关键字模糊搜索

        :return: The keywords of this PageResourceListParam.
        :rtype: dict(str, str)
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PageResourceListParam.

        关键字模糊搜索

        :param keywords: The keywords of this PageResourceListParam.
        :type keywords: dict(str, str)
        """
        self._keywords = keywords

    @property
    def ci_relationships(self):
        """Gets the ci_relationships of this PageResourceListParam.

        是否需要返回拓扑树,默认是false。需要：true---性能差，不需要false--性能好

        :return: The ci_relationships of this PageResourceListParam.
        :rtype: bool
        """
        return self._ci_relationships

    @ci_relationships.setter
    def ci_relationships(self, ci_relationships):
        """Sets the ci_relationships of this PageResourceListParam.

        是否需要返回拓扑树,默认是false。需要：true---性能差，不需要false--性能好

        :param ci_relationships: The ci_relationships of this PageResourceListParam.
        :type ci_relationships: bool
        """
        self._ci_relationships = ci_relationships

    @property
    def ci_type(self):
        """Gets the ci_type of this PageResourceListParam.

        节点类型，取值：application、sub_application、component、environment

        :return: The ci_type of this PageResourceListParam.
        :rtype: str
        """
        return self._ci_type

    @ci_type.setter
    def ci_type(self, ci_type):
        """Sets the ci_type of this PageResourceListParam.

        节点类型，取值：application、sub_application、component、environment

        :param ci_type: The ci_type of this PageResourceListParam.
        :type ci_type: str
        """
        self._ci_type = ci_type

    @property
    def ci_region(self):
        """Gets the ci_region of this PageResourceListParam.

        环境的region信息，若没有值，代表全部

        :return: The ci_region of this PageResourceListParam.
        :rtype: str
        """
        return self._ci_region

    @ci_region.setter
    def ci_region(self, ci_region):
        """Sets the ci_region of this PageResourceListParam.

        环境的region信息，若没有值，代表全部

        :param ci_region: The ci_region of this PageResourceListParam.
        :type ci_region: str
        """
        self._ci_region = ci_region

    @property
    def ci_ids(self):
        """Gets the ci_ids of this PageResourceListParam.

        节点id列表;如果ci_ids和ci_id同时有，则优先ci_ids，但是不能同时为空

        :return: The ci_ids of this PageResourceListParam.
        :rtype: list[str]
        """
        return self._ci_ids

    @ci_ids.setter
    def ci_ids(self, ci_ids):
        """Sets the ci_ids of this PageResourceListParam.

        节点id列表;如果ci_ids和ci_id同时有，则优先ci_ids，但是不能同时为空

        :param ci_ids: The ci_ids of this PageResourceListParam.
        :type ci_ids: list[str]
        """
        self._ci_ids = ci_ids

    @property
    def ci_id(self):
        """Gets the ci_id of this PageResourceListParam.

        节点id列表;如果ci_ids和ci_id同时有，则优先ci_ids，但是不能同时为空。但是不支持应用批量查询

        :return: The ci_id of this PageResourceListParam.
        :rtype: str
        """
        return self._ci_id

    @ci_id.setter
    def ci_id(self, ci_id):
        """Sets the ci_id of this PageResourceListParam.

        节点id列表;如果ci_ids和ci_id同时有，则优先ci_ids，但是不能同时为空。但是不支持应用批量查询

        :param ci_id: The ci_id of this PageResourceListParam.
        :type ci_id: str
        """
        self._ci_id = ci_id

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
        if not isinstance(other, PageResourceListParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
