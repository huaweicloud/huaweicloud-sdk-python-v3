# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRayJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'marker': 'str',
        'limit': 'int',
        'name': 'str',
        'id': 'str',
        'endpoint_name': 'str',
        'federation_name': 'str',
        'create_time_before': 'int',
        'create_time_after': 'int',
        'status': 'list[str]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'marker': 'marker',
        'limit': 'limit',
        'name': 'name',
        'id': 'id',
        'endpoint_name': 'endpoint_name',
        'federation_name': 'federation_name',
        'create_time_before': 'create_time_before',
        'create_time_after': 'create_time_after',
        'status': 'status'
    }

    def __init__(self, workspace_id=None, marker=None, limit=None, name=None, id=None, endpoint_name=None, federation_name=None, create_time_before=None, create_time_after=None, status=None):
        r"""ListRayJobsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param marker: **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type marker: str
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        :param name: **参数解释**：通过名字搜索作业。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、字母、数字、下划线、中划线的组合。 **默认取值**：不涉及。 
        :type name: str
        :param id: **参数解释**：通过作业id检索。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type id: str
        :param endpoint_name: **参数解释**：通过端点名称检索的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 
        :type endpoint_name: str
        :param federation_name: **参数解释**：该参数用于按联邦名称搜索端点。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 
        :type federation_name: str
        :param create_time_before: **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type create_time_before: int
        :param create_time_after: **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type create_time_after: int
        :param status: **参数解释**：状态过滤，支持多种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：可选值有：   - QUEUED：排队中。   - PENDING：待处理。   - RUNNING：运行中。   - CANCELING：取消中。   - CANCELED：已取消。   - FAILED：失败。   - QUEUED_TIMEOUT：排队超时。   - RUNNING_TIMEOUT：运行超时。   - SUCCEEDED：成功。 **默认取值**：不涉及。
        :type status: list[str]
        """
        
        

        self._workspace_id = None
        self._marker = None
        self._limit = None
        self._name = None
        self._id = None
        self._endpoint_name = None
        self._federation_name = None
        self._create_time_before = None
        self._create_time_after = None
        self._status = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if federation_name is not None:
            self.federation_name = federation_name
        if create_time_before is not None:
            self.create_time_before = create_time_before
        if create_time_after is not None:
            self.create_time_after = create_time_after
        if status is not None:
            self.status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListRayJobsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListRayJobsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListRayJobsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListRayJobsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def marker(self):
        r"""Gets the marker of this ListRayJobsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The marker of this ListRayJobsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRayJobsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param marker: The marker of this ListRayJobsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListRayJobsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListRayJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRayJobsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListRayJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListRayJobsRequest.

        **参数解释**：通过名字搜索作业。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、字母、数字、下划线、中划线的组合。 **默认取值**：不涉及。 

        :return: The name of this ListRayJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListRayJobsRequest.

        **参数解释**：通过名字搜索作业。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、字母、数字、下划线、中划线的组合。 **默认取值**：不涉及。 

        :param name: The name of this ListRayJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListRayJobsRequest.

        **参数解释**：通过作业id检索。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The id of this ListRayJobsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListRayJobsRequest.

        **参数解释**：通过作业id检索。 **约束限制**：不涉及。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param id: The id of this ListRayJobsRequest.
        :type id: str
        """
        self._id = id

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ListRayJobsRequest.

        **参数解释**：通过端点名称检索的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 

        :return: The endpoint_name of this ListRayJobsRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ListRayJobsRequest.

        **参数解释**：通过端点名称检索的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 

        :param endpoint_name: The endpoint_name of this ListRayJobsRequest.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def federation_name(self):
        r"""Gets the federation_name of this ListRayJobsRequest.

        **参数解释**：该参数用于按联邦名称搜索端点。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 

        :return: The federation_name of this ListRayJobsRequest.
        :rtype: str
        """
        return self._federation_name

    @federation_name.setter
    def federation_name(self, federation_name):
        r"""Sets the federation_name of this ListRayJobsRequest.

        **参数解释**：该参数用于按联邦名称搜索端点。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 

        :param federation_name: The federation_name of this ListRayJobsRequest.
        :type federation_name: str
        """
        self._federation_name = federation_name

    @property
    def create_time_before(self):
        r"""Gets the create_time_before of this ListRayJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The create_time_before of this ListRayJobsRequest.
        :rtype: int
        """
        return self._create_time_before

    @create_time_before.setter
    def create_time_before(self, create_time_before):
        r"""Sets the create_time_before of this ListRayJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param create_time_before: The create_time_before of this ListRayJobsRequest.
        :type create_time_before: int
        """
        self._create_time_before = create_time_before

    @property
    def create_time_after(self):
        r"""Gets the create_time_after of this ListRayJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The create_time_after of this ListRayJobsRequest.
        :rtype: int
        """
        return self._create_time_after

    @create_time_after.setter
    def create_time_after(self, create_time_after):
        r"""Sets the create_time_after of this ListRayJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param create_time_after: The create_time_after of this ListRayJobsRequest.
        :type create_time_after: int
        """
        self._create_time_after = create_time_after

    @property
    def status(self):
        r"""Gets the status of this ListRayJobsRequest.

        **参数解释**：状态过滤，支持多种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：可选值有：   - QUEUED：排队中。   - PENDING：待处理。   - RUNNING：运行中。   - CANCELING：取消中。   - CANCELED：已取消。   - FAILED：失败。   - QUEUED_TIMEOUT：排队超时。   - RUNNING_TIMEOUT：运行超时。   - SUCCEEDED：成功。 **默认取值**：不涉及。

        :return: The status of this ListRayJobsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListRayJobsRequest.

        **参数解释**：状态过滤，支持多种状态查询，默认查询所有。 **约束限制**：不涉及。 **取值范围**：可选值有：   - QUEUED：排队中。   - PENDING：待处理。   - RUNNING：运行中。   - CANCELING：取消中。   - CANCELED：已取消。   - FAILED：失败。   - QUEUED_TIMEOUT：排队超时。   - RUNNING_TIMEOUT：运行超时。   - SUCCEEDED：成功。 **默认取值**：不涉及。

        :param status: The status of this ListRayJobsRequest.
        :type status: list[str]
        """
        self._status = status

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
        if not isinstance(other, ListRayJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
