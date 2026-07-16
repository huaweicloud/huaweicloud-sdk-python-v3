# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkflowsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'labels': 'str',
        'template_id': 'str',
        'limit': 'str',
        'offset': 'str',
        'sort_by': 'str',
        'search_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'labels': 'labels',
        'template_id': 'template_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'search_type': 'search_type'
    }

    def __init__(self, name=None, description=None, status=None, labels=None, template_id=None, limit=None, offset=None, sort_by=None, search_type=None):
        r"""ListWorkflowsRequest

        The model defined in huaweicloud sdk

        :param name: 工作流名称。
        :type name: str
        :param description: 工作流描述信息。
        :type description: str
        :param status: 工作流状态。
        :type status: str
        :param labels: 工作流标签。
        :type labels: str
        :param template_id: 工作流模板ID。
        :type template_id: str
        :param limit: 分页参数limit，表示单次查询的条目数上限。假如要查询20~29条记录，offset为20，limit为10。
        :type limit: str
        :param offset: 分页参数offset，表示单次查询的条目偏移数量。假如要查询20~29条记录，offset为20，limit为10。
        :type offset: str
        :param sort_by: 排序依据字段，例如sort_by&#x3D;create_time，则表示以条目的创建时间进行排序。
        :type sort_by: str
        :param search_type: 过滤方式。可选值如下： - equal表示精确匹配。 - contain表示模糊匹配。  具体过滤的字段，由各个接口额外定义参数。例如Workflow支持按照名称（name）进行过滤，则相应的过滤字段为name。name&#x3D;workflow&amp;search_type&#x3D;contain表示查询名称中含有Workflow字样的所有工作流。
        :type search_type: str
        """
        
        

        self._name = None
        self._description = None
        self._status = None
        self._labels = None
        self._template_id = None
        self._limit = None
        self._offset = None
        self._sort_by = None
        self._search_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if labels is not None:
            self.labels = labels
        if template_id is not None:
            self.template_id = template_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if search_type is not None:
            self.search_type = search_type

    @property
    def name(self):
        r"""Gets the name of this ListWorkflowsRequest.

        工作流名称。

        :return: The name of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListWorkflowsRequest.

        工作流名称。

        :param name: The name of this ListWorkflowsRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListWorkflowsRequest.

        工作流描述信息。

        :return: The description of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListWorkflowsRequest.

        工作流描述信息。

        :param description: The description of this ListWorkflowsRequest.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ListWorkflowsRequest.

        工作流状态。

        :return: The status of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWorkflowsRequest.

        工作流状态。

        :param status: The status of this ListWorkflowsRequest.
        :type status: str
        """
        self._status = status

    @property
    def labels(self):
        r"""Gets the labels of this ListWorkflowsRequest.

        工作流标签。

        :return: The labels of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListWorkflowsRequest.

        工作流标签。

        :param labels: The labels of this ListWorkflowsRequest.
        :type labels: str
        """
        self._labels = labels

    @property
    def template_id(self):
        r"""Gets the template_id of this ListWorkflowsRequest.

        工作流模板ID。

        :return: The template_id of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListWorkflowsRequest.

        工作流模板ID。

        :param template_id: The template_id of this ListWorkflowsRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkflowsRequest.

        分页参数limit，表示单次查询的条目数上限。假如要查询20~29条记录，offset为20，limit为10。

        :return: The limit of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkflowsRequest.

        分页参数limit，表示单次查询的条目数上限。假如要查询20~29条记录，offset为20，limit为10。

        :param limit: The limit of this ListWorkflowsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkflowsRequest.

        分页参数offset，表示单次查询的条目偏移数量。假如要查询20~29条记录，offset为20，limit为10。

        :return: The offset of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkflowsRequest.

        分页参数offset，表示单次查询的条目偏移数量。假如要查询20~29条记录，offset为20，limit为10。

        :param offset: The offset of this ListWorkflowsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListWorkflowsRequest.

        排序依据字段，例如sort_by=create_time，则表示以条目的创建时间进行排序。

        :return: The sort_by of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListWorkflowsRequest.

        排序依据字段，例如sort_by=create_time，则表示以条目的创建时间进行排序。

        :param sort_by: The sort_by of this ListWorkflowsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def search_type(self):
        r"""Gets the search_type of this ListWorkflowsRequest.

        过滤方式。可选值如下： - equal表示精确匹配。 - contain表示模糊匹配。  具体过滤的字段，由各个接口额外定义参数。例如Workflow支持按照名称（name）进行过滤，则相应的过滤字段为name。name=workflow&search_type=contain表示查询名称中含有Workflow字样的所有工作流。

        :return: The search_type of this ListWorkflowsRequest.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this ListWorkflowsRequest.

        过滤方式。可选值如下： - equal表示精确匹配。 - contain表示模糊匹配。  具体过滤的字段，由各个接口额外定义参数。例如Workflow支持按照名称（name）进行过滤，则相应的过滤字段为name。name=workflow&search_type=contain表示查询名称中含有Workflow字样的所有工作流。

        :param search_type: The search_type of this ListWorkflowsRequest.
        :type search_type: str
        """
        self._search_type = search_type

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
        if not isinstance(other, ListWorkflowsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
