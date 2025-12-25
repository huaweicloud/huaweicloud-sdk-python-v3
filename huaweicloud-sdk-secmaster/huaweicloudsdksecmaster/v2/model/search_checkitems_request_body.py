# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCheckitemsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_uuid': 'str',
        'compliance_package_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort_by': 'str',
        'order': 'str',
        'name': 'str',
        'suggestion': 'str',
        'type': 'int',
        'source_list': 'list[int]',
        'condition': 'SearchCheckitemsRequestBodyCondition',
        'query_mode': 'str',
        'severity': 'str'
    }

    attribute_map = {
        'catalog_uuid': 'catalog_uuid',
        'compliance_package_id': 'compliance_package_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'order': 'order',
        'name': 'name',
        'suggestion': 'suggestion',
        'type': 'type',
        'source_list': 'source_list',
        'condition': 'condition',
        'query_mode': 'query_mode',
        'severity': 'severity'
    }

    def __init__(self, catalog_uuid=None, compliance_package_id=None, limit=None, offset=None, sort_by=None, order=None, name=None, suggestion=None, type=None, source_list=None, condition=None, query_mode=None, severity=None):
        r"""SearchCheckitemsRequestBody

        The model defined in huaweicloud sdk

        :param catalog_uuid: 检查项所属的目录id
        :type catalog_uuid: str
        :param compliance_package_id: 检查项所属的遵从包id
        :type compliance_package_id: str
        :param limit: 分页大小
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录
        :type offset: int
        :param sort_by: 排序关键字
        :type sort_by: str
        :param order: 降序或升序 DESC：降序 ASC: 升序
        :type order: str
        :param name: 按照检查项名称进行筛选
        :type name: str
        :param suggestion: 按照检查项建议进行筛选
        :type suggestion: str
        :param type: 表示该检查项的类型 0：内 1: 自定义
        :type type: int
        :param source_list: 按照检查项对的执行方式进行筛选。0：kotlin; 2：剧本流程；3：手动；4：主机接入
        :type source_list: list[int]
        :param condition: 
        :type condition: :class:`huaweicloudsdksecmaster.v2.SearchCheckitemsRequestBodyCondition`
        :param query_mode: 按照什么维度进行筛选
        :type query_mode: str
        :param severity: 按照检查项严重等级进行筛选 Fatal：致命 High：高危 Medium：中危 Low：低危 Tips：提示
        :type severity: str
        """
        
        

        self._catalog_uuid = None
        self._compliance_package_id = None
        self._limit = None
        self._offset = None
        self._sort_by = None
        self._order = None
        self._name = None
        self._suggestion = None
        self._type = None
        self._source_list = None
        self._condition = None
        self._query_mode = None
        self._severity = None
        self.discriminator = None

        if catalog_uuid is not None:
            self.catalog_uuid = catalog_uuid
        if compliance_package_id is not None:
            self.compliance_package_id = compliance_package_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if name is not None:
            self.name = name
        if suggestion is not None:
            self.suggestion = suggestion
        if type is not None:
            self.type = type
        if source_list is not None:
            self.source_list = source_list
        if condition is not None:
            self.condition = condition
        if query_mode is not None:
            self.query_mode = query_mode
        if severity is not None:
            self.severity = severity

    @property
    def catalog_uuid(self):
        r"""Gets the catalog_uuid of this SearchCheckitemsRequestBody.

        检查项所属的目录id

        :return: The catalog_uuid of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._catalog_uuid

    @catalog_uuid.setter
    def catalog_uuid(self, catalog_uuid):
        r"""Sets the catalog_uuid of this SearchCheckitemsRequestBody.

        检查项所属的目录id

        :param catalog_uuid: The catalog_uuid of this SearchCheckitemsRequestBody.
        :type catalog_uuid: str
        """
        self._catalog_uuid = catalog_uuid

    @property
    def compliance_package_id(self):
        r"""Gets the compliance_package_id of this SearchCheckitemsRequestBody.

        检查项所属的遵从包id

        :return: The compliance_package_id of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._compliance_package_id

    @compliance_package_id.setter
    def compliance_package_id(self, compliance_package_id):
        r"""Sets the compliance_package_id of this SearchCheckitemsRequestBody.

        检查项所属的遵从包id

        :param compliance_package_id: The compliance_package_id of this SearchCheckitemsRequestBody.
        :type compliance_package_id: str
        """
        self._compliance_package_id = compliance_package_id

    @property
    def limit(self):
        r"""Gets the limit of this SearchCheckitemsRequestBody.

        分页大小

        :return: The limit of this SearchCheckitemsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchCheckitemsRequestBody.

        分页大小

        :param limit: The limit of this SearchCheckitemsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this SearchCheckitemsRequestBody.

        偏移量，表示查询该偏移量后面的记录

        :return: The offset of this SearchCheckitemsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchCheckitemsRequestBody.

        偏移量，表示查询该偏移量后面的记录

        :param offset: The offset of this SearchCheckitemsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this SearchCheckitemsRequestBody.

        排序关键字

        :return: The sort_by of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this SearchCheckitemsRequestBody.

        排序关键字

        :param sort_by: The sort_by of this SearchCheckitemsRequestBody.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this SearchCheckitemsRequestBody.

        降序或升序 DESC：降序 ASC: 升序

        :return: The order of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this SearchCheckitemsRequestBody.

        降序或升序 DESC：降序 ASC: 升序

        :param order: The order of this SearchCheckitemsRequestBody.
        :type order: str
        """
        self._order = order

    @property
    def name(self):
        r"""Gets the name of this SearchCheckitemsRequestBody.

        按照检查项名称进行筛选

        :return: The name of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SearchCheckitemsRequestBody.

        按照检查项名称进行筛选

        :param name: The name of this SearchCheckitemsRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def suggestion(self):
        r"""Gets the suggestion of this SearchCheckitemsRequestBody.

        按照检查项建议进行筛选

        :return: The suggestion of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this SearchCheckitemsRequestBody.

        按照检查项建议进行筛选

        :param suggestion: The suggestion of this SearchCheckitemsRequestBody.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def type(self):
        r"""Gets the type of this SearchCheckitemsRequestBody.

        表示该检查项的类型 0：内 1: 自定义

        :return: The type of this SearchCheckitemsRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SearchCheckitemsRequestBody.

        表示该检查项的类型 0：内 1: 自定义

        :param type: The type of this SearchCheckitemsRequestBody.
        :type type: int
        """
        self._type = type

    @property
    def source_list(self):
        r"""Gets the source_list of this SearchCheckitemsRequestBody.

        按照检查项对的执行方式进行筛选。0：kotlin; 2：剧本流程；3：手动；4：主机接入

        :return: The source_list of this SearchCheckitemsRequestBody.
        :rtype: list[int]
        """
        return self._source_list

    @source_list.setter
    def source_list(self, source_list):
        r"""Sets the source_list of this SearchCheckitemsRequestBody.

        按照检查项对的执行方式进行筛选。0：kotlin; 2：剧本流程；3：手动；4：主机接入

        :param source_list: The source_list of this SearchCheckitemsRequestBody.
        :type source_list: list[int]
        """
        self._source_list = source_list

    @property
    def condition(self):
        r"""Gets the condition of this SearchCheckitemsRequestBody.

        :return: The condition of this SearchCheckitemsRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v2.SearchCheckitemsRequestBodyCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this SearchCheckitemsRequestBody.

        :param condition: The condition of this SearchCheckitemsRequestBody.
        :type condition: :class:`huaweicloudsdksecmaster.v2.SearchCheckitemsRequestBodyCondition`
        """
        self._condition = condition

    @property
    def query_mode(self):
        r"""Gets the query_mode of this SearchCheckitemsRequestBody.

        按照什么维度进行筛选

        :return: The query_mode of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._query_mode

    @query_mode.setter
    def query_mode(self, query_mode):
        r"""Sets the query_mode of this SearchCheckitemsRequestBody.

        按照什么维度进行筛选

        :param query_mode: The query_mode of this SearchCheckitemsRequestBody.
        :type query_mode: str
        """
        self._query_mode = query_mode

    @property
    def severity(self):
        r"""Gets the severity of this SearchCheckitemsRequestBody.

        按照检查项严重等级进行筛选 Fatal：致命 High：高危 Medium：中危 Low：低危 Tips：提示

        :return: The severity of this SearchCheckitemsRequestBody.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this SearchCheckitemsRequestBody.

        按照检查项严重等级进行筛选 Fatal：致命 High：高危 Medium：中危 Low：低危 Tips：提示

        :param severity: The severity of this SearchCheckitemsRequestBody.
        :type severity: str
        """
        self._severity = severity

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
        if not isinstance(other, SearchCheckitemsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
