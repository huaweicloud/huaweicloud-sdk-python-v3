# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDirectoryByResultCommitIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evolve_task_id': 'str',
        'commit_id': 'str',
        'iteration': 'int'
    }

    attribute_map = {
        'evolve_task_id': 'evolve_task_id',
        'commit_id': 'commit_id',
        'iteration': 'iteration'
    }

    def __init__(self, evolve_task_id=None, commit_id=None, iteration=None):
        r"""ListDirectoryByResultCommitIdRequest

        The model defined in huaweicloud sdk

        :param evolve_task_id: **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type evolve_task_id: str
        :param commit_id: **参数解释**： 演化任务结果的commit_id。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-256]个字符。 **默认取值**： 不涉及 
        :type commit_id: str
        :param iteration: **参数解释**： 从哪个轮次开始查询。 **约束限制**： 不涉及 **取值范围**： [-1-10000]。 **默认取值**： 不涉及 
        :type iteration: int
        """
        
        

        self._evolve_task_id = None
        self._commit_id = None
        self._iteration = None
        self.discriminator = None

        self.evolve_task_id = evolve_task_id
        self.commit_id = commit_id
        self.iteration = iteration

    @property
    def evolve_task_id(self):
        r"""Gets the evolve_task_id of this ListDirectoryByResultCommitIdRequest.

        **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The evolve_task_id of this ListDirectoryByResultCommitIdRequest.
        :rtype: str
        """
        return self._evolve_task_id

    @evolve_task_id.setter
    def evolve_task_id(self, evolve_task_id):
        r"""Sets the evolve_task_id of this ListDirectoryByResultCommitIdRequest.

        **参数解释**： 演化任务标识符。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param evolve_task_id: The evolve_task_id of this ListDirectoryByResultCommitIdRequest.
        :type evolve_task_id: str
        """
        self._evolve_task_id = evolve_task_id

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ListDirectoryByResultCommitIdRequest.

        **参数解释**： 演化任务结果的commit_id。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-256]个字符。 **默认取值**： 不涉及 

        :return: The commit_id of this ListDirectoryByResultCommitIdRequest.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ListDirectoryByResultCommitIdRequest.

        **参数解释**： 演化任务结果的commit_id。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-256]个字符。 **默认取值**： 不涉及 

        :param commit_id: The commit_id of this ListDirectoryByResultCommitIdRequest.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def iteration(self):
        r"""Gets the iteration of this ListDirectoryByResultCommitIdRequest.

        **参数解释**： 从哪个轮次开始查询。 **约束限制**： 不涉及 **取值范围**： [-1-10000]。 **默认取值**： 不涉及 

        :return: The iteration of this ListDirectoryByResultCommitIdRequest.
        :rtype: int
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        r"""Sets the iteration of this ListDirectoryByResultCommitIdRequest.

        **参数解释**： 从哪个轮次开始查询。 **约束限制**： 不涉及 **取值范围**： [-1-10000]。 **默认取值**： 不涉及 

        :param iteration: The iteration of this ListDirectoryByResultCommitIdRequest.
        :type iteration: int
        """
        self._iteration = iteration

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
        if not isinstance(other, ListDirectoryByResultCommitIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
