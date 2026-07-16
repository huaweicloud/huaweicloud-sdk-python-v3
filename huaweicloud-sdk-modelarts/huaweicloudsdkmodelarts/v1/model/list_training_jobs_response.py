# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrainingJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'count': 'int',
        'limit': 'int',
        'offset': 'int',
        'sort_by': 'str',
        'order': 'str',
        'group_by': 'str',
        'workspace_id': 'str',
        'ai_project': 'str',
        'train_type': 'str',
        'items': 'list[JobResponse]'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'order': 'order',
        'group_by': 'group_by',
        'workspace_id': 'workspace_id',
        'ai_project': 'ai_project',
        'train_type': 'train_type',
        'items': 'items'
    }

    def __init__(self, total=None, count=None, limit=None, offset=None, sort_by=None, order=None, group_by=None, workspace_id=None, ai_project=None, train_type=None, items=None):
        r"""ListTrainingJobsResponse

        The model defined in huaweicloud sdk

        :param total: 查询到当前用户名下的所有作业总数。
        :type total: int
        :param count: 查询到当前用户名下的所有符合查询条件的作业总数。
        :type count: int
        :param limit: 查询作业的每页条目数。最小为1，最大为50。
        :type limit: int
        :param offset: 查询作业的页数，最小为0。例如设置为0，则表示从第一页开始查询。
        :type offset: int
        :param sort_by: 查询作业排列顺序的指标。默认使用create_time排序。
        :type sort_by: str
        :param order: 查询作业排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。
        :type order: str
        :param group_by: 查询作业要搜索的分组条件。
        :type group_by: str
        :param workspace_id: 作业所处的工作空间，默认值为“0”。
        :type workspace_id: str
        :param ai_project: 作业所属的ai项目，默认值为\&quot;default-ai-project\&quot;。
        :type ai_project: str
        :param train_type: **参数解释**：在开启自定义作业和精调作业联合查询时，只显示自定义或精调作业。 **取值范围**：     - job: 只查自定义作业     - ftjob : 只查精调作业
        :type train_type: str
        :param items: 查询到当前用户名下的所有符合查询条件的作业详情。
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.JobResponse`]
        """
        
        super().__init__()

        self._total = None
        self._count = None
        self._limit = None
        self._offset = None
        self._sort_by = None
        self._order = None
        self._group_by = None
        self._workspace_id = None
        self._ai_project = None
        self._train_type = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if group_by is not None:
            self.group_by = group_by
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if ai_project is not None:
            self.ai_project = ai_project
        if train_type is not None:
            self.train_type = train_type
        if items is not None:
            self.items = items

    @property
    def total(self):
        r"""Gets the total of this ListTrainingJobsResponse.

        查询到当前用户名下的所有作业总数。

        :return: The total of this ListTrainingJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTrainingJobsResponse.

        查询到当前用户名下的所有作业总数。

        :param total: The total of this ListTrainingJobsResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        r"""Gets the count of this ListTrainingJobsResponse.

        查询到当前用户名下的所有符合查询条件的作业总数。

        :return: The count of this ListTrainingJobsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListTrainingJobsResponse.

        查询到当前用户名下的所有符合查询条件的作业总数。

        :param count: The count of this ListTrainingJobsResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        r"""Gets the limit of this ListTrainingJobsResponse.

        查询作业的每页条目数。最小为1，最大为50。

        :return: The limit of this ListTrainingJobsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTrainingJobsResponse.

        查询作业的每页条目数。最小为1，最大为50。

        :param limit: The limit of this ListTrainingJobsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTrainingJobsResponse.

        查询作业的页数，最小为0。例如设置为0，则表示从第一页开始查询。

        :return: The offset of this ListTrainingJobsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTrainingJobsResponse.

        查询作业的页数，最小为0。例如设置为0，则表示从第一页开始查询。

        :param offset: The offset of this ListTrainingJobsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListTrainingJobsResponse.

        查询作业排列顺序的指标。默认使用create_time排序。

        :return: The sort_by of this ListTrainingJobsResponse.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListTrainingJobsResponse.

        查询作业排列顺序的指标。默认使用create_time排序。

        :param sort_by: The sort_by of this ListTrainingJobsResponse.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this ListTrainingJobsResponse.

        查询作业排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :return: The order of this ListTrainingJobsResponse.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListTrainingJobsResponse.

        查询作业排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :param order: The order of this ListTrainingJobsResponse.
        :type order: str
        """
        self._order = order

    @property
    def group_by(self):
        r"""Gets the group_by of this ListTrainingJobsResponse.

        查询作业要搜索的分组条件。

        :return: The group_by of this ListTrainingJobsResponse.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this ListTrainingJobsResponse.

        查询作业要搜索的分组条件。

        :param group_by: The group_by of this ListTrainingJobsResponse.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListTrainingJobsResponse.

        作业所处的工作空间，默认值为“0”。

        :return: The workspace_id of this ListTrainingJobsResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListTrainingJobsResponse.

        作业所处的工作空间，默认值为“0”。

        :param workspace_id: The workspace_id of this ListTrainingJobsResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def ai_project(self):
        r"""Gets the ai_project of this ListTrainingJobsResponse.

        作业所属的ai项目，默认值为\"default-ai-project\"。

        :return: The ai_project of this ListTrainingJobsResponse.
        :rtype: str
        """
        return self._ai_project

    @ai_project.setter
    def ai_project(self, ai_project):
        r"""Sets the ai_project of this ListTrainingJobsResponse.

        作业所属的ai项目，默认值为\"default-ai-project\"。

        :param ai_project: The ai_project of this ListTrainingJobsResponse.
        :type ai_project: str
        """
        self._ai_project = ai_project

    @property
    def train_type(self):
        r"""Gets the train_type of this ListTrainingJobsResponse.

        **参数解释**：在开启自定义作业和精调作业联合查询时，只显示自定义或精调作业。 **取值范围**：     - job: 只查自定义作业     - ftjob : 只查精调作业

        :return: The train_type of this ListTrainingJobsResponse.
        :rtype: str
        """
        return self._train_type

    @train_type.setter
    def train_type(self, train_type):
        r"""Sets the train_type of this ListTrainingJobsResponse.

        **参数解释**：在开启自定义作业和精调作业联合查询时，只显示自定义或精调作业。 **取值范围**：     - job: 只查自定义作业     - ftjob : 只查精调作业

        :param train_type: The train_type of this ListTrainingJobsResponse.
        :type train_type: str
        """
        self._train_type = train_type

    @property
    def items(self):
        r"""Gets the items of this ListTrainingJobsResponse.

        查询到当前用户名下的所有符合查询条件的作业详情。

        :return: The items of this ListTrainingJobsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.JobResponse`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListTrainingJobsResponse.

        查询到当前用户名下的所有符合查询条件的作业详情。

        :param items: The items of this ListTrainingJobsResponse.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.JobResponse`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListTrainingJobsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListTrainingJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
