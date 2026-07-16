# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvaluatorBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'created_by': 'EvaluationOpsCreatedBy',
        'updated_at': 'str',
        'updated_by': 'EvaluationOpsUpdatedBy'
    }

    attribute_map = {
        'created_at': 'created_at',
        'created_by': 'created_by',
        'updated_at': 'updated_at',
        'updated_by': 'updated_by'
    }

    def __init__(self, created_at=None, created_by=None, updated_at=None, updated_by=None):
        r"""OpsEvaluatorBaseInfo

        The model defined in huaweicloud sdk

        :param created_at: **参数解释：** 评估器的创建时间。 
        :type created_at: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCreatedBy`
        :param updated_at: **参数解释：** 评估器的最近一次更新时间。 
        :type updated_at: str
        :param updated_by: 
        :type updated_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUpdatedBy`
        """
        
        

        self._created_at = None
        self._created_by = None
        self._updated_at = None
        self._updated_by = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def created_at(self):
        r"""Gets the created_at of this OpsEvaluatorBaseInfo.

        **参数解释：** 评估器的创建时间。 

        :return: The created_at of this OpsEvaluatorBaseInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OpsEvaluatorBaseInfo.

        **参数解释：** 评估器的创建时间。 

        :param created_at: The created_at of this OpsEvaluatorBaseInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def created_by(self):
        r"""Gets the created_by of this OpsEvaluatorBaseInfo.

        :return: The created_by of this OpsEvaluatorBaseInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCreatedBy`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this OpsEvaluatorBaseInfo.

        :param created_by: The created_by of this OpsEvaluatorBaseInfo.
        :type created_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCreatedBy`
        """
        self._created_by = created_by

    @property
    def updated_at(self):
        r"""Gets the updated_at of this OpsEvaluatorBaseInfo.

        **参数解释：** 评估器的最近一次更新时间。 

        :return: The updated_at of this OpsEvaluatorBaseInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this OpsEvaluatorBaseInfo.

        **参数解释：** 评估器的最近一次更新时间。 

        :param updated_at: The updated_at of this OpsEvaluatorBaseInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def updated_by(self):
        r"""Gets the updated_by of this OpsEvaluatorBaseInfo.

        :return: The updated_by of this OpsEvaluatorBaseInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUpdatedBy`
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this OpsEvaluatorBaseInfo.

        :param updated_by: The updated_by of this OpsEvaluatorBaseInfo.
        :type updated_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUpdatedBy`
        """
        self._updated_by = updated_by

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
        if not isinstance(other, OpsEvaluatorBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
