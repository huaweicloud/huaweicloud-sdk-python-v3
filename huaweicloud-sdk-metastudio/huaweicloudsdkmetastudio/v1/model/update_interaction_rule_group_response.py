# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInteractionRuleGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'interaction_rules': 'list[InteractionRuleDetailInfo]',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'interaction_rules': 'interaction_rules',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, group_id=None, group_name=None, interaction_rules=None, create_time=None, update_time=None, x_request_id=None):
        r"""UpdateInteractionRuleGroupResponse

        The model defined in huaweicloud sdk

        :param group_id: 互动规则库ID
        :type group_id: str
        :param group_name: 互动规则库名称
        :type group_name: str
        :param interaction_rules: 互动规则列表。 &gt; 查询互动规则库列表接口不再返回该内容。请使用查询互动规则库详情接口查具体某个库的规则列表。
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleDetailInfo`]
        :param create_time: 创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateInteractionRuleGroupResponse, self).__init__()

        self._group_id = None
        self._group_name = None
        self._interaction_rules = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if interaction_rules is not None:
            self.interaction_rules = interaction_rules
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateInteractionRuleGroupResponse.

        互动规则库ID

        :return: The group_id of this UpdateInteractionRuleGroupResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateInteractionRuleGroupResponse.

        互动规则库ID

        :param group_id: The group_id of this UpdateInteractionRuleGroupResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this UpdateInteractionRuleGroupResponse.

        互动规则库名称

        :return: The group_name of this UpdateInteractionRuleGroupResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this UpdateInteractionRuleGroupResponse.

        互动规则库名称

        :param group_name: The group_name of this UpdateInteractionRuleGroupResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def interaction_rules(self):
        r"""Gets the interaction_rules of this UpdateInteractionRuleGroupResponse.

        互动规则列表。 > 查询互动规则库列表接口不再返回该内容。请使用查询互动规则库详情接口查具体某个库的规则列表。

        :return: The interaction_rules of this UpdateInteractionRuleGroupResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleDetailInfo`]
        """
        return self._interaction_rules

    @interaction_rules.setter
    def interaction_rules(self, interaction_rules):
        r"""Sets the interaction_rules of this UpdateInteractionRuleGroupResponse.

        互动规则列表。 > 查询互动规则库列表接口不再返回该内容。请使用查询互动规则库详情接口查具体某个库的规则列表。

        :param interaction_rules: The interaction_rules of this UpdateInteractionRuleGroupResponse.
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleDetailInfo`]
        """
        self._interaction_rules = interaction_rules

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateInteractionRuleGroupResponse.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The create_time of this UpdateInteractionRuleGroupResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateInteractionRuleGroupResponse.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param create_time: The create_time of this UpdateInteractionRuleGroupResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateInteractionRuleGroupResponse.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The update_time of this UpdateInteractionRuleGroupResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateInteractionRuleGroupResponse.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param update_time: The update_time of this UpdateInteractionRuleGroupResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateInteractionRuleGroupResponse.

        :return: The x_request_id of this UpdateInteractionRuleGroupResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateInteractionRuleGroupResponse.

        :param x_request_id: The x_request_id of this UpdateInteractionRuleGroupResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, UpdateInteractionRuleGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
