# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAntileakageRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policyid': 'str',
        'url': 'str',
        'category': 'str',
        'contents': 'list[str]',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'action': 'LeakageListInfoAction'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'url': 'url',
        'category': 'category',
        'contents': 'contents',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'action': 'action'
    }

    def __init__(self, id=None, policyid=None, url=None, category=None, contents=None, timestamp=None, description=None, status=None, action=None):
        r"""CreateAntileakageRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param url: 规则应用的url
        :type url: str
        :param category: 类别（响应码：code，敏感信息：sensitive）
        :type category: str
        :param contents: 内容
        :type contents: list[str]
        :param timestamp: 创建规则时间戳
        :type timestamp: int
        :param description: 描述
        :type description: str
        :param status: **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及
        :type status: int
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.LeakageListInfoAction`
        """
        
        super().__init__()

        self._id = None
        self._policyid = None
        self._url = None
        self._category = None
        self._contents = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._action = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if url is not None:
            self.url = url
        if category is not None:
            self.category = category
        if contents is not None:
            self.contents = contents
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if action is not None:
            self.action = action

    @property
    def id(self):
        r"""Gets the id of this CreateAntileakageRuleResponse.

        规则id

        :return: The id of this CreateAntileakageRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateAntileakageRuleResponse.

        规则id

        :param id: The id of this CreateAntileakageRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this CreateAntileakageRuleResponse.

        策略id

        :return: The policyid of this CreateAntileakageRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this CreateAntileakageRuleResponse.

        策略id

        :param policyid: The policyid of this CreateAntileakageRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def url(self):
        r"""Gets the url of this CreateAntileakageRuleResponse.

        规则应用的url

        :return: The url of this CreateAntileakageRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateAntileakageRuleResponse.

        规则应用的url

        :param url: The url of this CreateAntileakageRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def category(self):
        r"""Gets the category of this CreateAntileakageRuleResponse.

        类别（响应码：code，敏感信息：sensitive）

        :return: The category of this CreateAntileakageRuleResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateAntileakageRuleResponse.

        类别（响应码：code，敏感信息：sensitive）

        :param category: The category of this CreateAntileakageRuleResponse.
        :type category: str
        """
        self._category = category

    @property
    def contents(self):
        r"""Gets the contents of this CreateAntileakageRuleResponse.

        内容

        :return: The contents of this CreateAntileakageRuleResponse.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this CreateAntileakageRuleResponse.

        内容

        :param contents: The contents of this CreateAntileakageRuleResponse.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def timestamp(self):
        r"""Gets the timestamp of this CreateAntileakageRuleResponse.

        创建规则时间戳

        :return: The timestamp of this CreateAntileakageRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this CreateAntileakageRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this CreateAntileakageRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        r"""Gets the description of this CreateAntileakageRuleResponse.

        描述

        :return: The description of this CreateAntileakageRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAntileakageRuleResponse.

        描述

        :param description: The description of this CreateAntileakageRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateAntileakageRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :return: The status of this CreateAntileakageRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateAntileakageRuleResponse.

        **参数解释：** 规则状态标识，用于指定规则的启用或关闭状态 **约束限制：** 不涉及 **取值范围：**  - 0：关闭  - 1：开启 **默认取值：** 不涉及

        :param status: The status of this CreateAntileakageRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def action(self):
        r"""Gets the action of this CreateAntileakageRuleResponse.

        :return: The action of this CreateAntileakageRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.LeakageListInfoAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateAntileakageRuleResponse.

        :param action: The action of this CreateAntileakageRuleResponse.
        :type action: :class:`huaweicloudsdkwaf.v1.LeakageListInfoAction`
        """
        self._action = action

    def to_dict(self):
        import warnings
        warnings.warn("CreateAntileakageRuleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateAntileakageRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
