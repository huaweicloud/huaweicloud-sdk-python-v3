# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksBySqlTemplateIdRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str',
        'range_left': 'int',
        'range_right': 'int',
        'sql_template_id': 'str',
        'page_size': 'int',
        'cur_page': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'range_left': 'range_left',
        'range_right': 'range_right',
        'sql_template_id': 'sql_template_id',
        'page_size': 'page_size',
        'cur_page': 'cur_page'
    }

    def __init__(self, instance_id=None, node_id=None, range_left=None, range_right=None, sql_template_id=None, page_size=None, cur_page=None):
        r"""ListTasksBySqlTemplateIdRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param node_id: 节点ID，实例节点的唯一标识
        :type node_id: str
        :param range_left: 起止时间的查询左区间
        :type range_left: int
        :param range_right: 起止时间的查询右区间
        :type range_right: int
        :param sql_template_id: SQL模板ID
        :type sql_template_id: str
        :param page_size: 每页记录数
        :type page_size: int
        :param cur_page: 当前页码
        :type cur_page: int
        """
        
        

        self._instance_id = None
        self._node_id = None
        self._range_left = None
        self._range_right = None
        self._sql_template_id = None
        self._page_size = None
        self._cur_page = None
        self.discriminator = None

        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if range_left is not None:
            self.range_left = range_left
        if range_right is not None:
            self.range_right = range_right
        self.sql_template_id = sql_template_id
        if page_size is not None:
            self.page_size = page_size
        if cur_page is not None:
            self.cur_page = cur_page

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTasksBySqlTemplateIdRequestBody.

        实例ID，实例的唯一标识

        :return: The instance_id of this ListTasksBySqlTemplateIdRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTasksBySqlTemplateIdRequestBody.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this ListTasksBySqlTemplateIdRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ListTasksBySqlTemplateIdRequestBody.

        节点ID，实例节点的唯一标识

        :return: The node_id of this ListTasksBySqlTemplateIdRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListTasksBySqlTemplateIdRequestBody.

        节点ID，实例节点的唯一标识

        :param node_id: The node_id of this ListTasksBySqlTemplateIdRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def range_left(self):
        r"""Gets the range_left of this ListTasksBySqlTemplateIdRequestBody.

        起止时间的查询左区间

        :return: The range_left of this ListTasksBySqlTemplateIdRequestBody.
        :rtype: int
        """
        return self._range_left

    @range_left.setter
    def range_left(self, range_left):
        r"""Sets the range_left of this ListTasksBySqlTemplateIdRequestBody.

        起止时间的查询左区间

        :param range_left: The range_left of this ListTasksBySqlTemplateIdRequestBody.
        :type range_left: int
        """
        self._range_left = range_left

    @property
    def range_right(self):
        r"""Gets the range_right of this ListTasksBySqlTemplateIdRequestBody.

        起止时间的查询右区间

        :return: The range_right of this ListTasksBySqlTemplateIdRequestBody.
        :rtype: int
        """
        return self._range_right

    @range_right.setter
    def range_right(self, range_right):
        r"""Sets the range_right of this ListTasksBySqlTemplateIdRequestBody.

        起止时间的查询右区间

        :param range_right: The range_right of this ListTasksBySqlTemplateIdRequestBody.
        :type range_right: int
        """
        self._range_right = range_right

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this ListTasksBySqlTemplateIdRequestBody.

        SQL模板ID

        :return: The sql_template_id of this ListTasksBySqlTemplateIdRequestBody.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this ListTasksBySqlTemplateIdRequestBody.

        SQL模板ID

        :param sql_template_id: The sql_template_id of this ListTasksBySqlTemplateIdRequestBody.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def page_size(self):
        r"""Gets the page_size of this ListTasksBySqlTemplateIdRequestBody.

        每页记录数

        :return: The page_size of this ListTasksBySqlTemplateIdRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListTasksBySqlTemplateIdRequestBody.

        每页记录数

        :param page_size: The page_size of this ListTasksBySqlTemplateIdRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListTasksBySqlTemplateIdRequestBody.

        当前页码

        :return: The cur_page of this ListTasksBySqlTemplateIdRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListTasksBySqlTemplateIdRequestBody.

        当前页码

        :param cur_page: The cur_page of this ListTasksBySqlTemplateIdRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

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
        if not isinstance(other, ListTasksBySqlTemplateIdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
