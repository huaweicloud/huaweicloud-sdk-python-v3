# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPrivacyRuleResponse(SdkResponse):

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
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'url': 'str',
        'category': 'str',
        'index': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'url': 'url',
        'category': 'category',
        'index': 'index'
    }

    def __init__(self, id=None, policyid=None, timestamp=None, description=None, status=None, url=None, category=None, index=None):
        r"""ShowPrivacyRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param timestamp: 创建规则的时间，格式为13位毫秒时间戳
        :type timestamp: int
        :param description: 规则描述，可选参数，设置该规则的备注信息。
        :type description: str
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param url: 隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\&quot;*\&quot;号结尾代表路径前缀
        :type url: str
        :param category: 屏蔽字段   - Params：请求参数   - Cookie：根据Cookie区分的Web访问者   - Header：自定义HTTP首部   - Form：表单参数
        :type category: str
        :param index: 屏蔽字段名
        :type index: str
        """
        
        super(ShowPrivacyRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._url = None
        self._category = None
        self._index = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if category is not None:
            self.category = category
        if index is not None:
            self.index = index

    @property
    def id(self):
        r"""Gets the id of this ShowPrivacyRuleResponse.

        规则id

        :return: The id of this ShowPrivacyRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPrivacyRuleResponse.

        规则id

        :param id: The id of this ShowPrivacyRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this ShowPrivacyRuleResponse.

        策略id

        :return: The policyid of this ShowPrivacyRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this ShowPrivacyRuleResponse.

        策略id

        :param policyid: The policyid of this ShowPrivacyRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ShowPrivacyRuleResponse.

        创建规则的时间，格式为13位毫秒时间戳

        :return: The timestamp of this ShowPrivacyRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ShowPrivacyRuleResponse.

        创建规则的时间，格式为13位毫秒时间戳

        :param timestamp: The timestamp of this ShowPrivacyRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        r"""Gets the description of this ShowPrivacyRuleResponse.

        规则描述，可选参数，设置该规则的备注信息。

        :return: The description of this ShowPrivacyRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPrivacyRuleResponse.

        规则描述，可选参数，设置该规则的备注信息。

        :param description: The description of this ShowPrivacyRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ShowPrivacyRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this ShowPrivacyRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowPrivacyRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this ShowPrivacyRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def url(self):
        r"""Gets the url of this ShowPrivacyRuleResponse.

        隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :return: The url of this ShowPrivacyRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowPrivacyRuleResponse.

        隐私屏蔽规则防护的url，需要填写标准的url格式，例如/admin/xxx或者/admin/*,以\"*\"号结尾代表路径前缀

        :param url: The url of this ShowPrivacyRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def category(self):
        r"""Gets the category of this ShowPrivacyRuleResponse.

        屏蔽字段   - Params：请求参数   - Cookie：根据Cookie区分的Web访问者   - Header：自定义HTTP首部   - Form：表单参数

        :return: The category of this ShowPrivacyRuleResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowPrivacyRuleResponse.

        屏蔽字段   - Params：请求参数   - Cookie：根据Cookie区分的Web访问者   - Header：自定义HTTP首部   - Form：表单参数

        :param category: The category of this ShowPrivacyRuleResponse.
        :type category: str
        """
        self._category = category

    @property
    def index(self):
        r"""Gets the index of this ShowPrivacyRuleResponse.

        屏蔽字段名

        :return: The index of this ShowPrivacyRuleResponse.
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this ShowPrivacyRuleResponse.

        屏蔽字段名

        :param index: The index of this ShowPrivacyRuleResponse.
        :type index: str
        """
        self._index = index

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
        if not isinstance(other, ShowPrivacyRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
