# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAccountPassword:

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
        'status_code': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'plan_id': 'plan_id',
        'resource_id': 'resource_id',
        'account_name': 'account_name',
        'status_code': 'status_code',
        'detail': 'detail'
    }

    def __init__(self, plan_id=None, resource_id=None, account_name=None, status_code=None, detail=None):
        r"""UpdateAccountPassword

        The model defined in huaweicloud sdk

        :param plan_id: 改密计划唯一UUID
        :type plan_id: str
        :param resource_id: 改密资源id
        :type resource_id: str
        :param account_name: 改密账号名称
        :type account_name: str
        :param status_code: 改密结果状态码
        :type status_code: str
        :param detail: 改密结果详情
        :type detail: str
        """
        
        

        self._plan_id = None
        self._resource_id = None
        self._account_name = None
        self._status_code = None
        self._detail = None
        self.discriminator = None

        self.plan_id = plan_id
        self.resource_id = resource_id
        self.account_name = account_name
        self.status_code = status_code
        self.detail = detail

    @property
    def plan_id(self):
        r"""Gets the plan_id of this UpdateAccountPassword.

        改密计划唯一UUID

        :return: The plan_id of this UpdateAccountPassword.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        r"""Sets the plan_id of this UpdateAccountPassword.

        改密计划唯一UUID

        :param plan_id: The plan_id of this UpdateAccountPassword.
        :type plan_id: str
        """
        self._plan_id = plan_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this UpdateAccountPassword.

        改密资源id

        :return: The resource_id of this UpdateAccountPassword.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this UpdateAccountPassword.

        改密资源id

        :param resource_id: The resource_id of this UpdateAccountPassword.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def account_name(self):
        r"""Gets the account_name of this UpdateAccountPassword.

        改密账号名称

        :return: The account_name of this UpdateAccountPassword.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this UpdateAccountPassword.

        改密账号名称

        :param account_name: The account_name of this UpdateAccountPassword.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def status_code(self):
        r"""Gets the status_code of this UpdateAccountPassword.

        改密结果状态码

        :return: The status_code of this UpdateAccountPassword.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this UpdateAccountPassword.

        改密结果状态码

        :param status_code: The status_code of this UpdateAccountPassword.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def detail(self):
        r"""Gets the detail of this UpdateAccountPassword.

        改密结果详情

        :return: The detail of this UpdateAccountPassword.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this UpdateAccountPassword.

        改密结果详情

        :param detail: The detail of this UpdateAccountPassword.
        :type detail: str
        """
        self._detail = detail

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
        if not isinstance(other, UpdateAccountPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
