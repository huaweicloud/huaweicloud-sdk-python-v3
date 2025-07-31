# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountChangePwdPlan:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plan_id': 'str',
        'resource_id': 'str',
        'account_name': 'str',
        'password': 'str',
        'project_id': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'plan_id': 'plan_id',
        'resource_id': 'resource_id',
        'account_name': 'account_name',
        'password': 'password',
        'project_id': 'project_id',
        'create_time': 'create_time'
    }

    def __init__(self, plan_id=None, resource_id=None, account_name=None, password=None, project_id=None, create_time=None):
        r"""AccountChangePwdPlan

        The model defined in huaweicloud sdk

        :param plan_id: 改密计划唯一UUID
        :type plan_id: str
        :param resource_id: 改密资源id
        :type resource_id: str
        :param account_name: 改密账号名称
        :type account_name: str
        :param password: 需要修改的密码
        :type password: str
        :param project_id: 资源所属的项目id
        :type project_id: str
        :param create_time: 改密计划创建时间
        :type create_time: int
        """
        
        

        self._plan_id = None
        self._resource_id = None
        self._account_name = None
        self._password = None
        self._project_id = None
        self._create_time = None
        self.discriminator = None

        self.plan_id = plan_id
        self.resource_id = resource_id
        self.account_name = account_name
        self.password = password
        self.project_id = project_id
        self.create_time = create_time

    @property
    def plan_id(self):
        r"""Gets the plan_id of this AccountChangePwdPlan.

        改密计划唯一UUID

        :return: The plan_id of this AccountChangePwdPlan.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this AccountChangePwdPlan.

        改密计划唯一UUID

        :param plan_id: The plan_id of this AccountChangePwdPlan.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this AccountChangePwdPlan.

        改密资源id

        :return: The resource_id of this AccountChangePwdPlan.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this AccountChangePwdPlan.

        改密资源id

        :param resource_id: The resource_id of this AccountChangePwdPlan.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def account_name(self):
        r"""Gets the account_name of this AccountChangePwdPlan.

        改密账号名称

        :return: The account_name of this AccountChangePwdPlan.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this AccountChangePwdPlan.

        改密账号名称

        :param account_name: The account_name of this AccountChangePwdPlan.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def password(self):
        r"""Gets the password of this AccountChangePwdPlan.

        需要修改的密码

        :return: The password of this AccountChangePwdPlan.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this AccountChangePwdPlan.

        需要修改的密码

        :param password: The password of this AccountChangePwdPlan.
        :type password: str
        """
        self._password = password

    @property
    def project_id(self):
        r"""Gets the project_id of this AccountChangePwdPlan.

        资源所属的项目id

        :return: The project_id of this AccountChangePwdPlan.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AccountChangePwdPlan.

        资源所属的项目id

        :param project_id: The project_id of this AccountChangePwdPlan.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AccountChangePwdPlan.

        改密计划创建时间

        :return: The create_time of this AccountChangePwdPlan.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AccountChangePwdPlan.

        改密计划创建时间

        :param create_time: The create_time of this AccountChangePwdPlan.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, AccountChangePwdPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
