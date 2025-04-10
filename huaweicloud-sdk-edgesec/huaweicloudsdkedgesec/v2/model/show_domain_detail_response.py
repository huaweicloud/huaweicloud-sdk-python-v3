# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDomainDetailResponse(SdkResponse):

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
        'domain_name': 'str',
        'enterprise_project_id': 'str',
        'description': 'str',
        'policy_id': 'str',
        'protect_status': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'description': 'description',
        'policy_id': 'policy_id',
        'protect_status': 'protect_status',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, domain_name=None, enterprise_project_id=None, description=None, policy_id=None, protect_status=None, create_time=None, update_time=None):
        r"""ShowDomainDetailResponse

        The model defined in huaweicloud sdk

        :param id: 域名id
        :type id: str
        :param domain_name: 域名
        :type domain_name: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param description: 域名描述
        :type description: str
        :param policy_id: 策略id
        :type policy_id: str
        :param protect_status: - 防护状态: - 防护中：on - 未防护：off
        :type protect_status: str
        :param create_time: 创建域名的时间
        :type create_time: int
        :param update_time: 更新域名的时间
        :type update_time: int
        """
        
        super(ShowDomainDetailResponse, self).__init__()

        self._id = None
        self._domain_name = None
        self._enterprise_project_id = None
        self._description = None
        self._policy_id = None
        self._protect_status = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if description is not None:
            self.description = description
        if policy_id is not None:
            self.policy_id = policy_id
        if protect_status is not None:
            self.protect_status = protect_status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ShowDomainDetailResponse.

        域名id

        :return: The id of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowDomainDetailResponse.

        域名id

        :param id: The id of this ShowDomainDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ShowDomainDetailResponse.

        域名

        :return: The domain_name of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ShowDomainDetailResponse.

        域名

        :param domain_name: The domain_name of this ShowDomainDetailResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowDomainDetailResponse.

        企业项目id

        :return: The enterprise_project_id of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowDomainDetailResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ShowDomainDetailResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def description(self):
        r"""Gets the description of this ShowDomainDetailResponse.

        域名描述

        :return: The description of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowDomainDetailResponse.

        域名描述

        :param description: The description of this ShowDomainDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowDomainDetailResponse.

        策略id

        :return: The policy_id of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowDomainDetailResponse.

        策略id

        :param policy_id: The policy_id of this ShowDomainDetailResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ShowDomainDetailResponse.

        - 防护状态: - 防护中：on - 未防护：off

        :return: The protect_status of this ShowDomainDetailResponse.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ShowDomainDetailResponse.

        - 防护状态: - 防护中：on - 未防护：off

        :param protect_status: The protect_status of this ShowDomainDetailResponse.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowDomainDetailResponse.

        创建域名的时间

        :return: The create_time of this ShowDomainDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowDomainDetailResponse.

        创建域名的时间

        :param create_time: The create_time of this ShowDomainDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowDomainDetailResponse.

        更新域名的时间

        :return: The update_time of this ShowDomainDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowDomainDetailResponse.

        更新域名的时间

        :param update_time: The update_time of this ShowDomainDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowDomainDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
