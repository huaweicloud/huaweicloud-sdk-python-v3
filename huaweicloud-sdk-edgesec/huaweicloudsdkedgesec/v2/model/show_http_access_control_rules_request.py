# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHttpAccessControlRulesRequest:

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
        'name': 'str',
        'page': 'int',
        'pagesize': 'int'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'name': 'name',
        'page': 'page',
        'pagesize': 'pagesize'
    }

    def __init__(self, policy_id=None, name=None, page=None, pagesize=None):
        r"""ShowHttpAccessControlRulesRequest

        The model defined in huaweicloud sdk

        :param policy_id: 策略id
        :type policy_id: str
        :param name: 规则名称
        :type name: str
        :param page: 分页查询参数，第page页
        :type page: int
        :param pagesize: 分页查询参数，每页显示pagesize条记录
        :type pagesize: int
        """
        
        

        self._policy_id = None
        self._name = None
        self._page = None
        self._pagesize = None
        self.discriminator = None

        self.policy_id = policy_id
        if name is not None:
            self.name = name
        if page is not None:
            self.page = page
        if pagesize is not None:
            self.pagesize = pagesize

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowHttpAccessControlRulesRequest.

        策略id

        :return: The policy_id of this ShowHttpAccessControlRulesRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowHttpAccessControlRulesRequest.

        策略id

        :param policy_id: The policy_id of this ShowHttpAccessControlRulesRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def name(self):
        r"""Gets the name of this ShowHttpAccessControlRulesRequest.

        规则名称

        :return: The name of this ShowHttpAccessControlRulesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowHttpAccessControlRulesRequest.

        规则名称

        :param name: The name of this ShowHttpAccessControlRulesRequest.
        :type name: str
        """
        self._name = name

    @property
    def page(self):
        r"""Gets the page of this ShowHttpAccessControlRulesRequest.

        分页查询参数，第page页

        :return: The page of this ShowHttpAccessControlRulesRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowHttpAccessControlRulesRequest.

        分页查询参数，第page页

        :param page: The page of this ShowHttpAccessControlRulesRequest.
        :type page: int
        """
        self._page = page

    @property
    def pagesize(self):
        r"""Gets the pagesize of this ShowHttpAccessControlRulesRequest.

        分页查询参数，每页显示pagesize条记录

        :return: The pagesize of this ShowHttpAccessControlRulesRequest.
        :rtype: int
        """
        return self._pagesize

    @pagesize.setter
    def pagesize(self, pagesize):
        r"""Sets the pagesize of this ShowHttpAccessControlRulesRequest.

        分页查询参数，每页显示pagesize条记录

        :param pagesize: The pagesize of this ShowHttpAccessControlRulesRequest.
        :type pagesize: int
        """
        self._pagesize = pagesize

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
        if not isinstance(other, ShowHttpAccessControlRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
