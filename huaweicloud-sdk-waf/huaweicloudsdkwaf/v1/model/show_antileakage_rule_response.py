# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAntileakageRuleResponse(SdkResponse):

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
        'status': 'int',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'url': 'url',
        'category': 'category',
        'contents': 'contents',
        'timestamp': 'timestamp',
        'status': 'status',
        'description': 'description'
    }

    def __init__(self, id=None, policyid=None, url=None, category=None, contents=None, timestamp=None, status=None, description=None):
        r"""ShowAntileakageRuleResponse

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
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param description: 规则描述
        :type description: str
        """
        
        super(ShowAntileakageRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._url = None
        self._category = None
        self._contents = None
        self._timestamp = None
        self._status = None
        self._description = None
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
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ShowAntileakageRuleResponse.

        规则id

        :return: The id of this ShowAntileakageRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowAntileakageRuleResponse.

        规则id

        :param id: The id of this ShowAntileakageRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this ShowAntileakageRuleResponse.

        策略id

        :return: The policyid of this ShowAntileakageRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this ShowAntileakageRuleResponse.

        策略id

        :param policyid: The policyid of this ShowAntileakageRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def url(self):
        r"""Gets the url of this ShowAntileakageRuleResponse.

        规则应用的url

        :return: The url of this ShowAntileakageRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowAntileakageRuleResponse.

        规则应用的url

        :param url: The url of this ShowAntileakageRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def category(self):
        r"""Gets the category of this ShowAntileakageRuleResponse.

        类别（响应码：code，敏感信息：sensitive）

        :return: The category of this ShowAntileakageRuleResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowAntileakageRuleResponse.

        类别（响应码：code，敏感信息：sensitive）

        :param category: The category of this ShowAntileakageRuleResponse.
        :type category: str
        """
        self._category = category

    @property
    def contents(self):
        r"""Gets the contents of this ShowAntileakageRuleResponse.

        内容

        :return: The contents of this ShowAntileakageRuleResponse.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this ShowAntileakageRuleResponse.

        内容

        :param contents: The contents of this ShowAntileakageRuleResponse.
        :type contents: list[str]
        """
        self._contents = contents

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ShowAntileakageRuleResponse.

        创建规则时间戳

        :return: The timestamp of this ShowAntileakageRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ShowAntileakageRuleResponse.

        创建规则时间戳

        :param timestamp: The timestamp of this ShowAntileakageRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def status(self):
        r"""Gets the status of this ShowAntileakageRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this ShowAntileakageRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAntileakageRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this ShowAntileakageRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ShowAntileakageRuleResponse.

        规则描述

        :return: The description of this ShowAntileakageRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowAntileakageRuleResponse.

        规则描述

        :param description: The description of this ShowAntileakageRuleResponse.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ShowAntileakageRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
