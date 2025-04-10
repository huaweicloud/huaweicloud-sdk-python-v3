# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SharedConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shared_type': 'str',
        'shared_state': 'str',
        'expire_time': 'str',
        'allowed_project_ids': 'list[str]'
    }

    attribute_map = {
        'shared_type': 'shared_type',
        'shared_state': 'shared_state',
        'expire_time': 'expire_time',
        'allowed_project_ids': 'allowed_project_ids'
    }

    def __init__(self, shared_type=None, shared_state=None, expire_time=None, allowed_project_ids=None):
        r"""SharedConfig

        The model defined in huaweicloud sdk

        :param shared_type: **参数解释**： 共享类型。 **约束限制**： 该配置仅用于模板 **取值范围**： * PRIVATE：私有，仅本租户可访问。 * PUBLIC：公开，所有租户可访问。当前仅提供系统资产可公开访问。 * SHARED：共享，指定租户可访问。拥有者指定租户可访问。  **默认取值**： 不涉及。
        :type shared_type: str
        :param shared_state: **参数解释**： 共享状态。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 **取值范围**： * PUBLISHED：发布。模板可用。 * DRAFT：草稿。编辑态，仅拥有者可访问。 * REVIEW：审核态。不可编辑，仅拥有者/审核人员可查看。  **默认取值**： 不涉及。
        :type shared_state: str
        :param expire_time: **参数解释**： 共享过期时间。空表示永久不过期。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 格式遵循：RFC 3339，示例“2021*01*10T08:43:17Z”。 **取值范围**： 字符长度0-20位 **默认取值**： 不涉及。
        :type expire_time: str
        :param allowed_project_ids: **参数解释**： 允许访问本资产的租户列表。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 **取值范围**： 最大支持100个租户，重复的记录会被忽略。 租户ID填写project_id，字符长度1-64位。 **默认取值**： 不涉及。
        :type allowed_project_ids: list[str]
        """
        
        

        self._shared_type = None
        self._shared_state = None
        self._expire_time = None
        self._allowed_project_ids = None
        self.discriminator = None

        if shared_type is not None:
            self.shared_type = shared_type
        if shared_state is not None:
            self.shared_state = shared_state
        if expire_time is not None:
            self.expire_time = expire_time
        if allowed_project_ids is not None:
            self.allowed_project_ids = allowed_project_ids

    @property
    def shared_type(self):
        r"""Gets the shared_type of this SharedConfig.

        **参数解释**： 共享类型。 **约束限制**： 该配置仅用于模板 **取值范围**： * PRIVATE：私有，仅本租户可访问。 * PUBLIC：公开，所有租户可访问。当前仅提供系统资产可公开访问。 * SHARED：共享，指定租户可访问。拥有者指定租户可访问。  **默认取值**： 不涉及。

        :return: The shared_type of this SharedConfig.
        :rtype: str
        """
        return self._shared_type

    @shared_type.setter
    def shared_type(self, shared_type):
        r"""Sets the shared_type of this SharedConfig.

        **参数解释**： 共享类型。 **约束限制**： 该配置仅用于模板 **取值范围**： * PRIVATE：私有，仅本租户可访问。 * PUBLIC：公开，所有租户可访问。当前仅提供系统资产可公开访问。 * SHARED：共享，指定租户可访问。拥有者指定租户可访问。  **默认取值**： 不涉及。

        :param shared_type: The shared_type of this SharedConfig.
        :type shared_type: str
        """
        self._shared_type = shared_type

    @property
    def shared_state(self):
        r"""Gets the shared_state of this SharedConfig.

        **参数解释**： 共享状态。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 **取值范围**： * PUBLISHED：发布。模板可用。 * DRAFT：草稿。编辑态，仅拥有者可访问。 * REVIEW：审核态。不可编辑，仅拥有者/审核人员可查看。  **默认取值**： 不涉及。

        :return: The shared_state of this SharedConfig.
        :rtype: str
        """
        return self._shared_state

    @shared_state.setter
    def shared_state(self, shared_state):
        r"""Sets the shared_state of this SharedConfig.

        **参数解释**： 共享状态。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 **取值范围**： * PUBLISHED：发布。模板可用。 * DRAFT：草稿。编辑态，仅拥有者可访问。 * REVIEW：审核态。不可编辑，仅拥有者/审核人员可查看。  **默认取值**： 不涉及。

        :param shared_state: The shared_state of this SharedConfig.
        :type shared_state: str
        """
        self._shared_state = shared_state

    @property
    def expire_time(self):
        r"""Gets the expire_time of this SharedConfig.

        **参数解释**： 共享过期时间。空表示永久不过期。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 格式遵循：RFC 3339，示例“2021*01*10T08:43:17Z”。 **取值范围**： 字符长度0-20位 **默认取值**： 不涉及。

        :return: The expire_time of this SharedConfig.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this SharedConfig.

        **参数解释**： 共享过期时间。空表示永久不过期。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 格式遵循：RFC 3339，示例“2021*01*10T08:43:17Z”。 **取值范围**： 字符长度0-20位 **默认取值**： 不涉及。

        :param expire_time: The expire_time of this SharedConfig.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def allowed_project_ids(self):
        r"""Gets the allowed_project_ids of this SharedConfig.

        **参数解释**： 允许访问本资产的租户列表。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 **取值范围**： 最大支持100个租户，重复的记录会被忽略。 租户ID填写project_id，字符长度1-64位。 **默认取值**： 不涉及。

        :return: The allowed_project_ids of this SharedConfig.
        :rtype: list[str]
        """
        return self._allowed_project_ids

    @allowed_project_ids.setter
    def allowed_project_ids(self, allowed_project_ids):
        r"""Sets the allowed_project_ids of this SharedConfig.

        **参数解释**： 允许访问本资产的租户列表。 **约束限制**： 该配置仅用于shared_type为SHARED的模板。 **取值范围**： 最大支持100个租户，重复的记录会被忽略。 租户ID填写project_id，字符长度1-64位。 **默认取值**： 不涉及。

        :param allowed_project_ids: The allowed_project_ids of this SharedConfig.
        :type allowed_project_ids: list[str]
        """
        self._allowed_project_ids = allowed_project_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SharedConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
