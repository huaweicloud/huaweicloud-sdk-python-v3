# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_time': 'str',
        'updated_time': 'str',
        'created_by': 'EvaluationOpsUserInfo',
        'updated_by': 'EvaluationOpsUserInfo'
    }

    attribute_map = {
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'created_by': 'created_by',
        'updated_by': 'updated_by'
    }

    def __init__(self, created_time=None, updated_time=None, created_by=None, updated_by=None):
        r"""OpsBaseInfo

        The model defined in huaweicloud sdk

        :param created_time: **参数解释：** 资源的创建时间戳。 **取值范围：** 符合标准时间格式的字符串。
        :type created_time: str
        :param updated_time: **参数解释：** 资源的最后更新时间戳。 **取值范围：** 符合标准时间格式的字符串。
        :type updated_time: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUserInfo`
        :param updated_by: 
        :type updated_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUserInfo`
        """
        
        

        self._created_time = None
        self._updated_time = None
        self._created_by = None
        self._updated_by = None
        self.discriminator = None

        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by

    @property
    def created_time(self):
        r"""Gets the created_time of this OpsBaseInfo.

        **参数解释：** 资源的创建时间戳。 **取值范围：** 符合标准时间格式的字符串。

        :return: The created_time of this OpsBaseInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this OpsBaseInfo.

        **参数解释：** 资源的创建时间戳。 **取值范围：** 符合标准时间格式的字符串。

        :param created_time: The created_time of this OpsBaseInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this OpsBaseInfo.

        **参数解释：** 资源的最后更新时间戳。 **取值范围：** 符合标准时间格式的字符串。

        :return: The updated_time of this OpsBaseInfo.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this OpsBaseInfo.

        **参数解释：** 资源的最后更新时间戳。 **取值范围：** 符合标准时间格式的字符串。

        :param updated_time: The updated_time of this OpsBaseInfo.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def created_by(self):
        r"""Gets the created_by of this OpsBaseInfo.

        :return: The created_by of this OpsBaseInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUserInfo`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this OpsBaseInfo.

        :param created_by: The created_by of this OpsBaseInfo.
        :type created_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUserInfo`
        """
        self._created_by = created_by

    @property
    def updated_by(self):
        r"""Gets the updated_by of this OpsBaseInfo.

        :return: The updated_by of this OpsBaseInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUserInfo`
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this OpsBaseInfo.

        :param updated_by: The updated_by of this OpsBaseInfo.
        :type updated_by: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsUserInfo`
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
        if not isinstance(other, OpsBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
