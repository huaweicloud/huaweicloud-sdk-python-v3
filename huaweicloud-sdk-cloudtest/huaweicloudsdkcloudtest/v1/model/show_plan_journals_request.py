# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlanJournalsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'plan_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'plan_id': 'plan_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, plan_id=None, offset=None, limit=None):
        r"""ShowPlanJournalsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id，项目唯一标识，固定长度32位字符
        :type project_id: str
        :param plan_id: 测试计划id，测试计划的唯一标识，长度11-34位字符
        :type plan_id: str
        :param offset: 起始偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量,最大支持200条
        :type limit: int
        """
        
        

        self._project_id = None
        self._plan_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.plan_id = plan_id
        self.offset = offset
        self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPlanJournalsRequest.

        项目id，项目唯一标识，固定长度32位字符

        :return: The project_id of this ShowPlanJournalsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPlanJournalsRequest.

        项目id，项目唯一标识，固定长度32位字符

        :param project_id: The project_id of this ShowPlanJournalsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def plan_id(self):
        r"""Gets the plan_id of this ShowPlanJournalsRequest.

        测试计划id，测试计划的唯一标识，长度11-34位字符

        :return: The plan_id of this ShowPlanJournalsRequest.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this ShowPlanJournalsRequest.

        测试计划id，测试计划的唯一标识，长度11-34位字符

        :param plan_id: The plan_id of this ShowPlanJournalsRequest.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowPlanJournalsRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ShowPlanJournalsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowPlanJournalsRequest.

        起始偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ShowPlanJournalsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowPlanJournalsRequest.

        每页显示的条目数量,最大支持200条

        :return: The limit of this ShowPlanJournalsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowPlanJournalsRequest.

        每页显示的条目数量,最大支持200条

        :param limit: The limit of this ShowPlanJournalsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowPlanJournalsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
