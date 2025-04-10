# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpIgnoreRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'status': 'int',
        'page': 'int',
        'pagesize': 'int',
        'rule': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'status': 'status',
        'page': 'page',
        'pagesize': 'pagesize',
        'rule': 'rule'
    }

    def __init__(self, policy_id=None, status=None, page=None, pagesize=None, rule=None):
        r"""ShowHttpIgnoreRulesRequest

        The model defined in huaweicloud sdk

        :param policy_id: 策略id
        :type policy_id: str
        :param status: 规则开关状态
        :type status: int
        :param page: 分页查询参数，第page页
        :type page: int
        :param pagesize: 分页查询参数，每页显示pagesize条记录
        :type pagesize: int
        :param rule: 不检测模块类型
        :type rule: str
        """
        
        

        self._policy_id = None
        self._status = None
        self._page = None
        self._pagesize = None
        self._rule = None
        self.discriminator = None

        self.policy_id = policy_id
        if status is not None:
            self.status = status
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize
        if rule is not None:
            self.rule = rule

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowHttpIgnoreRulesRequest.

        策略id

        :return: The policy_id of this ShowHttpIgnoreRulesRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowHttpIgnoreRulesRequest.

        策略id

        :param policy_id: The policy_id of this ShowHttpIgnoreRulesRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def status(self):
        r"""Gets the status of this ShowHttpIgnoreRulesRequest.

        规则开关状态

        :return: The status of this ShowHttpIgnoreRulesRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowHttpIgnoreRulesRequest.

        规则开关状态

        :param status: The status of this ShowHttpIgnoreRulesRequest.
        :type status: int
        """
        self._status = status

    @property
    def page(self):
        r"""Gets the page of this ShowHttpIgnoreRulesRequest.

        分页查询参数，第page页

        :return: The page of this ShowHttpIgnoreRulesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowHttpIgnoreRulesRequest.

        分页查询参数，第page页

        :param page: The page of this ShowHttpIgnoreRulesRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ShowHttpIgnoreRulesRequest.

        分页查询参数，每页显示pagesize条记录

        :return: The pagesize of this ShowHttpIgnoreRulesRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ShowHttpIgnoreRulesRequest.

        分页查询参数，每页显示pagesize条记录

        :param pagesize: The pagesize of this ShowHttpIgnoreRulesRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

    @property
    def rule(self):
        r"""Gets the rule of this ShowHttpIgnoreRulesRequest.

        不检测模块类型

        :return: The rule of this ShowHttpIgnoreRulesRequest.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this ShowHttpIgnoreRulesRequest.

        不检测模块类型

        :param rule: The rule of this ShowHttpIgnoreRulesRequest.
        :type rule: str
        """
        self._rule = rule

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
        if not isinstance(other, ShowHttpIgnoreRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
