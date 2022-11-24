# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckWorkflowAuthenticationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'last_modify_time': 'str',
        'agency_id': 'str',
        'agency_name': 'str',
        'agency_duration': 'str',
        'trust_domain_name': 'str',
        'role_id': 'str',
        'role_dependent_by_function': 'str',
        'role_remark_name': 'str',
        'role_remark_type': 'str',
        'x_request_id': 'str',
        'connection': 'str',
        'content_length': 'str',
        'date': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'last_modify_time': 'last_modify_time',
        'agency_id': 'agency_id',
        'agency_name': 'agency_name',
        'agency_duration': 'agency_duration',
        'trust_domain_name': 'trust_domain_name',
        'role_id': 'role_id',
        'role_dependent_by_function': 'role_dependent_by_function',
        'role_remark_name': 'role_remark_name',
        'role_remark_type': 'role_remark_type',
        'x_request_id': 'x-request-id',
        'connection': 'Connection',
        'content_length': 'Content-Length',
        'date': 'Date'
    }

    def __init__(self, create_time=None, last_modify_time=None, agency_id=None, agency_name=None, agency_duration=None, trust_domain_name=None, role_id=None, role_dependent_by_function=None, role_remark_name=None, role_remark_type=None, x_request_id=None, connection=None, content_length=None, date=None):
        """CheckWorkflowAuthenticationResponse

        The model defined in huaweicloud sdk

        :param create_time: 创建时间。
        :type create_time: str
        :param last_modify_time: 最近修改时间。
        :type last_modify_time: str
        :param agency_id: 委托方帐号ID。
        :type agency_id: str
        :param agency_name: 委托名。
        :type agency_name: str
        :param agency_duration: 委托的期限。取值为\&quot;FOREVER\&quot;或“null”表示委托的期限为永久，取值为\&quot;ONEDAY\&quot;表示委托的期限为一天。
        :type agency_duration: str
        :param trust_domain_name: 被委托方帐号名。
        :type trust_domain_name: str
        :param role_id: 权限ID。
        :type role_id: str
        :param role_dependent_by_function: 权限使用的依赖函数。
        :type role_dependent_by_function: str
        :param role_remark_name: 权限备注名。
        :type role_remark_name: str
        :param role_remark_type: 权限的备注模式： AX表示在domain层显示。 XA表示在project层显示。 AA表示在domain和project层均显示。 XX表示在domain和project层均不显示。 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）
        :type role_remark_type: str
        :param x_request_id: 
        :type x_request_id: str
        :param connection: 
        :type connection: str
        :param content_length: 
        :type content_length: str
        :param date: 
        :type date: str
        """
        
        super(CheckWorkflowAuthenticationResponse, self).__init__()

        self._create_time = None
        self._last_modify_time = None
        self._agency_id = None
        self._agency_name = None
        self._agency_duration = None
        self._trust_domain_name = None
        self._role_id = None
        self._role_dependent_by_function = None
        self._role_remark_name = None
        self._role_remark_type = None
        self._x_request_id = None
        self._connection = None
        self._content_length = None
        self._date = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if last_modify_time is not None:
            self.last_modify_time = last_modify_time
        if agency_id is not None:
            self.agency_id = agency_id
        if agency_name is not None:
            self.agency_name = agency_name
        if agency_duration is not None:
            self.agency_duration = agency_duration
        if trust_domain_name is not None:
            self.trust_domain_name = trust_domain_name
        if role_id is not None:
            self.role_id = role_id
        if role_dependent_by_function is not None:
            self.role_dependent_by_function = role_dependent_by_function
        if role_remark_name is not None:
            self.role_remark_name = role_remark_name
        if role_remark_type is not None:
            self.role_remark_type = role_remark_type
        if x_request_id is not None:
            self.x_request_id = x_request_id
        if connection is not None:
            self.connection = connection
        if content_length is not None:
            self.content_length = content_length
        if date is not None:
            self.date = date

    @property
    def create_time(self):
        """Gets the create_time of this CheckWorkflowAuthenticationResponse.

        创建时间。

        :return: The create_time of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CheckWorkflowAuthenticationResponse.

        创建时间。

        :param create_time: The create_time of this CheckWorkflowAuthenticationResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modify_time(self):
        """Gets the last_modify_time of this CheckWorkflowAuthenticationResponse.

        最近修改时间。

        :return: The last_modify_time of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._last_modify_time

    @last_modify_time.setter
    def last_modify_time(self, last_modify_time):
        """Sets the last_modify_time of this CheckWorkflowAuthenticationResponse.

        最近修改时间。

        :param last_modify_time: The last_modify_time of this CheckWorkflowAuthenticationResponse.
        :type last_modify_time: str
        """
        self._last_modify_time = last_modify_time

    @property
    def agency_id(self):
        """Gets the agency_id of this CheckWorkflowAuthenticationResponse.

        委托方帐号ID。

        :return: The agency_id of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._agency_id

    @agency_id.setter
    def agency_id(self, agency_id):
        """Sets the agency_id of this CheckWorkflowAuthenticationResponse.

        委托方帐号ID。

        :param agency_id: The agency_id of this CheckWorkflowAuthenticationResponse.
        :type agency_id: str
        """
        self._agency_id = agency_id

    @property
    def agency_name(self):
        """Gets the agency_name of this CheckWorkflowAuthenticationResponse.

        委托名。

        :return: The agency_name of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this CheckWorkflowAuthenticationResponse.

        委托名。

        :param agency_name: The agency_name of this CheckWorkflowAuthenticationResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def agency_duration(self):
        """Gets the agency_duration of this CheckWorkflowAuthenticationResponse.

        委托的期限。取值为\"FOREVER\"或“null”表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天。

        :return: The agency_duration of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._agency_duration

    @agency_duration.setter
    def agency_duration(self, agency_duration):
        """Sets the agency_duration of this CheckWorkflowAuthenticationResponse.

        委托的期限。取值为\"FOREVER\"或“null”表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天。

        :param agency_duration: The agency_duration of this CheckWorkflowAuthenticationResponse.
        :type agency_duration: str
        """
        self._agency_duration = agency_duration

    @property
    def trust_domain_name(self):
        """Gets the trust_domain_name of this CheckWorkflowAuthenticationResponse.

        被委托方帐号名。

        :return: The trust_domain_name of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._trust_domain_name

    @trust_domain_name.setter
    def trust_domain_name(self, trust_domain_name):
        """Sets the trust_domain_name of this CheckWorkflowAuthenticationResponse.

        被委托方帐号名。

        :param trust_domain_name: The trust_domain_name of this CheckWorkflowAuthenticationResponse.
        :type trust_domain_name: str
        """
        self._trust_domain_name = trust_domain_name

    @property
    def role_id(self):
        """Gets the role_id of this CheckWorkflowAuthenticationResponse.

        权限ID。

        :return: The role_id of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this CheckWorkflowAuthenticationResponse.

        权限ID。

        :param role_id: The role_id of this CheckWorkflowAuthenticationResponse.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_dependent_by_function(self):
        """Gets the role_dependent_by_function of this CheckWorkflowAuthenticationResponse.

        权限使用的依赖函数。

        :return: The role_dependent_by_function of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._role_dependent_by_function

    @role_dependent_by_function.setter
    def role_dependent_by_function(self, role_dependent_by_function):
        """Sets the role_dependent_by_function of this CheckWorkflowAuthenticationResponse.

        权限使用的依赖函数。

        :param role_dependent_by_function: The role_dependent_by_function of this CheckWorkflowAuthenticationResponse.
        :type role_dependent_by_function: str
        """
        self._role_dependent_by_function = role_dependent_by_function

    @property
    def role_remark_name(self):
        """Gets the role_remark_name of this CheckWorkflowAuthenticationResponse.

        权限备注名。

        :return: The role_remark_name of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._role_remark_name

    @role_remark_name.setter
    def role_remark_name(self, role_remark_name):
        """Sets the role_remark_name of this CheckWorkflowAuthenticationResponse.

        权限备注名。

        :param role_remark_name: The role_remark_name of this CheckWorkflowAuthenticationResponse.
        :type role_remark_name: str
        """
        self._role_remark_name = role_remark_name

    @property
    def role_remark_type(self):
        """Gets the role_remark_type of this CheckWorkflowAuthenticationResponse.

        权限的备注模式： AX表示在domain层显示。 XA表示在project层显示。 AA表示在domain和project层均显示。 XX表示在domain和project层均不显示。 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）

        :return: The role_remark_type of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._role_remark_type

    @role_remark_type.setter
    def role_remark_type(self, role_remark_type):
        """Sets the role_remark_type of this CheckWorkflowAuthenticationResponse.

        权限的备注模式： AX表示在domain层显示。 XA表示在project层显示。 AA表示在domain和project层均显示。 XX表示在domain和project层均不显示。 自定义策略的显示模式只能为AX或者XA，不能在domain层和project层都显示（AA），或者在domain层和project层都不显示（XX）

        :param role_remark_type: The role_remark_type of this CheckWorkflowAuthenticationResponse.
        :type role_remark_type: str
        """
        self._role_remark_type = role_remark_type

    @property
    def x_request_id(self):
        """Gets the x_request_id of this CheckWorkflowAuthenticationResponse.

        :return: The x_request_id of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this CheckWorkflowAuthenticationResponse.

        :param x_request_id: The x_request_id of this CheckWorkflowAuthenticationResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    @property
    def connection(self):
        """Gets the connection of this CheckWorkflowAuthenticationResponse.

        :return: The connection of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this CheckWorkflowAuthenticationResponse.

        :param connection: The connection of this CheckWorkflowAuthenticationResponse.
        :type connection: str
        """
        self._connection = connection

    @property
    def content_length(self):
        """Gets the content_length of this CheckWorkflowAuthenticationResponse.

        :return: The content_length of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this CheckWorkflowAuthenticationResponse.

        :param content_length: The content_length of this CheckWorkflowAuthenticationResponse.
        :type content_length: str
        """
        self._content_length = content_length

    @property
    def date(self):
        """Gets the date of this CheckWorkflowAuthenticationResponse.

        :return: The date of this CheckWorkflowAuthenticationResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this CheckWorkflowAuthenticationResponse.

        :param date: The date of this CheckWorkflowAuthenticationResponse.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, CheckWorkflowAuthenticationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
