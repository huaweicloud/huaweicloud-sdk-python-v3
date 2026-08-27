# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEvolveTaskMetasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sort_dir': 'str',
        'algorithm_id': 'str',
        'task_name': 'str',
        'status_list': 'list[str]',
        'user_name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'sort_dir': 'sort_dir',
        'algorithm_id': 'algorithm_id',
        'task_name': 'task_name',
        'status_list': 'status_list',
        'user_name': 'user_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, sort_dir=None, algorithm_id=None, task_name=None, status_list=None, user_name=None, limit=None, offset=None):
        r"""ListEvolveTaskMetasRequest

        The model defined in huaweicloud sdk

        :param sort_dir: **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - DESC：降序 - ASC：升序 **默认取值**： DESC 
        :type sort_dir: str
        :param algorithm_id: **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type algorithm_id: str
        :param task_name: **参数解释**： 任务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type task_name: str
        :param status_list: **参数解释**： 任务状态列表。 **约束限制**： 不涉及 **取值范围**： - DRAFT：草稿 - PENDING：初始化 - RUNNING：运行中 - FINISHED：已完成 - STOPPED：已停止 - FAILED：失败 **默认取值**： 不涉及 
        :type status_list: list[str]
        :param user_name: **参数解释**： 用户名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type user_name: str
        :param limit: **参数解释**： 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。 **约束限制**： 不涉及 **取值范围**： [1,1000] **默认取值**： 100 
        :type limit: int
        :param offset: **参数解释**： 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。 **约束限制**： 不涉及 **取值范围**： [0,100000000] **默认取值**： 0 
        :type offset: int
        """
        
        

        self._sort_dir = None
        self._algorithm_id = None
        self._task_name = None
        self._status_list = None
        self._user_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if sort_dir is not None:
            self.sort_dir = sort_dir
        self.algorithm_id = algorithm_id
        if task_name is not None:
            self.task_name = task_name
        if status_list is not None:
            self.status_list = status_list
        if user_name is not None:
            self.user_name = user_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListEvolveTaskMetasRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - DESC：降序 - ASC：升序 **默认取值**： DESC 

        :return: The sort_dir of this ListEvolveTaskMetasRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListEvolveTaskMetasRequest.

        **参数解释**： 排序规则，目前默认创建时间降序。 **约束限制**： 不涉及 **取值范围**： - DESC：降序 - ASC：升序 **默认取值**： DESC 

        :param sort_dir: The sort_dir of this ListEvolveTaskMetasRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def algorithm_id(self):
        r"""Gets the algorithm_id of this ListEvolveTaskMetasRequest.

        **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The algorithm_id of this ListEvolveTaskMetasRequest.
        :rtype: str
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        r"""Sets the algorithm_id of this ListEvolveTaskMetasRequest.

        **参数解释**： 关联的算法设计项目。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param algorithm_id: The algorithm_id of this ListEvolveTaskMetasRequest.
        :type algorithm_id: str
        """
        self._algorithm_id = algorithm_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListEvolveTaskMetasRequest.

        **参数解释**： 任务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The task_name of this ListEvolveTaskMetasRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListEvolveTaskMetasRequest.

        **参数解释**： 任务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param task_name: The task_name of this ListEvolveTaskMetasRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def status_list(self):
        r"""Gets the status_list of this ListEvolveTaskMetasRequest.

        **参数解释**： 任务状态列表。 **约束限制**： 不涉及 **取值范围**： - DRAFT：草稿 - PENDING：初始化 - RUNNING：运行中 - FINISHED：已完成 - STOPPED：已停止 - FAILED：失败 **默认取值**： 不涉及 

        :return: The status_list of this ListEvolveTaskMetasRequest.
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ListEvolveTaskMetasRequest.

        **参数解释**： 任务状态列表。 **约束限制**： 不涉及 **取值范围**： - DRAFT：草稿 - PENDING：初始化 - RUNNING：运行中 - FINISHED：已完成 - STOPPED：已停止 - FAILED：失败 **默认取值**： 不涉及 

        :param status_list: The status_list of this ListEvolveTaskMetasRequest.
        :type status_list: list[str]
        """
        self._status_list = status_list

    @property
    def user_name(self):
        r"""Gets the user_name of this ListEvolveTaskMetasRequest.

        **参数解释**： 用户名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The user_name of this ListEvolveTaskMetasRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListEvolveTaskMetasRequest.

        **参数解释**： 用户名。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param user_name: The user_name of this ListEvolveTaskMetasRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def limit(self):
        r"""Gets the limit of this ListEvolveTaskMetasRequest.

        **参数解释**： 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。 **约束限制**： 不涉及 **取值范围**： [1,1000] **默认取值**： 100 

        :return: The limit of this ListEvolveTaskMetasRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEvolveTaskMetasRequest.

        **参数解释**： 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]。 **约束限制**： 不涉及 **取值范围**： [1,1000] **默认取值**： 100 

        :param limit: The limit of this ListEvolveTaskMetasRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListEvolveTaskMetasRequest.

        **参数解释**： 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。 **约束限制**： 不涉及 **取值范围**： [0,100000000] **默认取值**： 0 

        :return: The offset of this ListEvolveTaskMetasRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEvolveTaskMetasRequest.

        **参数解释**： 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]。 **约束限制**： 不涉及 **取值范围**： [0,100000000] **默认取值**： 0 

        :param offset: The offset of this ListEvolveTaskMetasRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListEvolveTaskMetasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
