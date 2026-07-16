# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsEvaluatorVersionsResponseBodyVersions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str',
        'version': 'str',
        'description': 'str',
        'base_info': 'OpsEvaluatorBaseInfo',
        'evaluator_content': 'EvaluatorContent'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'version': 'version',
        'description': 'description',
        'base_info': 'base_info',
        'evaluator_content': 'evaluator_content'
    }

    def __init__(self, evaluator_id=None, version=None, description=None, base_info=None, evaluator_content=None):
        r"""ListOpsEvaluatorVersionsResponseBodyVersions

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释：** 评估器的唯一标识符。 **取值范围：** 不涉及。 
        :type evaluator_id: str
        :param version: **参数解释：** 评估器的具体版本号，用于区分不同的逻辑迭代。 **取值范围：** 不涉及。 
        :type version: str
        :param description: **参数解释：** 该版本的变更详细说明或备注。 **取值范围：** 不涉及。 
        :type description: str
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        :param evaluator_content: 
        :type evaluator_content: :class:`huaweicloudsdkagentarts.v1.EvaluatorContent`
        """
        
        

        self._evaluator_id = None
        self._version = None
        self._description = None
        self._base_info = None
        self._evaluator_content = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if version is not None:
            self.version = version
        if description is not None:
            self.description = description
        if base_info is not None:
            self.base_info = base_info
        if evaluator_content is not None:
            self.evaluator_content = evaluator_content

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this ListOpsEvaluatorVersionsResponseBodyVersions.

        **参数解释：** 评估器的唯一标识符。 **取值范围：** 不涉及。 

        :return: The evaluator_id of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this ListOpsEvaluatorVersionsResponseBodyVersions.

        **参数解释：** 评估器的唯一标识符。 **取值范围：** 不涉及。 

        :param evaluator_id: The evaluator_id of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def version(self):
        r"""Gets the version of this ListOpsEvaluatorVersionsResponseBodyVersions.

        **参数解释：** 评估器的具体版本号，用于区分不同的逻辑迭代。 **取值范围：** 不涉及。 

        :return: The version of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListOpsEvaluatorVersionsResponseBodyVersions.

        **参数解释：** 评估器的具体版本号，用于区分不同的逻辑迭代。 **取值范围：** 不涉及。 

        :param version: The version of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :type version: str
        """
        self._version = version

    @property
    def description(self):
        r"""Gets the description of this ListOpsEvaluatorVersionsResponseBodyVersions.

        **参数解释：** 该版本的变更详细说明或备注。 **取值范围：** 不涉及。 

        :return: The description of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListOpsEvaluatorVersionsResponseBodyVersions.

        **参数解释：** 该版本的变更详细说明或备注。 **取值范围：** 不涉及。 

        :param description: The description of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :type description: str
        """
        self._description = description

    @property
    def base_info(self):
        r"""Gets the base_info of this ListOpsEvaluatorVersionsResponseBodyVersions.

        :return: The base_info of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this ListOpsEvaluatorVersionsResponseBodyVersions.

        :param base_info: The base_info of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        self._base_info = base_info

    @property
    def evaluator_content(self):
        r"""Gets the evaluator_content of this ListOpsEvaluatorVersionsResponseBodyVersions.

        :return: The evaluator_content of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluatorContent`
        """
        return self._evaluator_content

    @evaluator_content.setter
    def evaluator_content(self, evaluator_content):
        r"""Sets the evaluator_content of this ListOpsEvaluatorVersionsResponseBodyVersions.

        :param evaluator_content: The evaluator_content of this ListOpsEvaluatorVersionsResponseBodyVersions.
        :type evaluator_content: :class:`huaweicloudsdkagentarts.v1.EvaluatorContent`
        """
        self._evaluator_content = evaluator_content

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
        if not isinstance(other, ListOpsEvaluatorVersionsResponseBodyVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
