# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotificationRecordInfo:

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
        'type': 'str',
        'user_name': 'str',
        'desktop_name': 'str',
        'desktop_pool_name': 'str',
        'result': 'str',
        'error_message': 'str',
        'operate_time': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'type': 'type',
        'user_name': 'user_name',
        'desktop_name': 'desktop_name',
        'desktop_pool_name': 'desktop_pool_name',
        'result': 'result',
        'error_message': 'error_message',
        'operate_time': 'operate_time'
    }

    def __init__(self, project_id=None, type=None, user_name=None, desktop_name=None, desktop_pool_name=None, result=None, error_message=None, operate_time=None):
        r"""NotificationRecordInfo

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param type: 发送SMN类型:EMAIL-邮件、SMS-短信
        :type type: str
        :param user_name: 用户名
        :type user_name: str
        :param desktop_name: 桌面名
        :type desktop_name: str
        :param desktop_pool_name: 桌面池名称
        :type desktop_pool_name: str
        :param result: 发送结果
        :type result: str
        :param error_message: 报错信息
        :type error_message: str
        :param operate_time: 操作时间
        :type operate_time: str
        """
        
        

        self._project_id = None
        self._type = None
        self._user_name = None
        self._desktop_name = None
        self._desktop_pool_name = None
        self._result = None
        self._error_message = None
        self._operate_time = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if type is not None:
            self.type = type
        if user_name is not None:
            self.user_name = user_name
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_pool_name is not None:
            self.desktop_pool_name = desktop_pool_name
        if result is not None:
            self.result = result
        if error_message is not None:
            self.error_message = error_message
        if operate_time is not None:
            self.operate_time = operate_time

    @property
    def project_id(self):
        r"""Gets the project_id of this NotificationRecordInfo.

        项目id

        :return: The project_id of this NotificationRecordInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this NotificationRecordInfo.

        项目id

        :param project_id: The project_id of this NotificationRecordInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def type(self):
        r"""Gets the type of this NotificationRecordInfo.

        发送SMN类型:EMAIL-邮件、SMS-短信

        :return: The type of this NotificationRecordInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NotificationRecordInfo.

        发送SMN类型:EMAIL-邮件、SMS-短信

        :param type: The type of this NotificationRecordInfo.
        :type type: str
        """
        self._type = type

    @property
    def user_name(self):
        r"""Gets the user_name of this NotificationRecordInfo.

        用户名

        :return: The user_name of this NotificationRecordInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this NotificationRecordInfo.

        用户名

        :param user_name: The user_name of this NotificationRecordInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this NotificationRecordInfo.

        桌面名

        :return: The desktop_name of this NotificationRecordInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this NotificationRecordInfo.

        桌面名

        :param desktop_name: The desktop_name of this NotificationRecordInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_pool_name(self):
        r"""Gets the desktop_pool_name of this NotificationRecordInfo.

        桌面池名称

        :return: The desktop_pool_name of this NotificationRecordInfo.
        :rtype: str
        """
        return self._desktop_pool_name

    @desktop_pool_name.setter
    def desktop_pool_name(self, desktop_pool_name):
        r"""Sets the desktop_pool_name of this NotificationRecordInfo.

        桌面池名称

        :param desktop_pool_name: The desktop_pool_name of this NotificationRecordInfo.
        :type desktop_pool_name: str
        """
        self._desktop_pool_name = desktop_pool_name

    @property
    def result(self):
        r"""Gets the result of this NotificationRecordInfo.

        发送结果

        :return: The result of this NotificationRecordInfo.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this NotificationRecordInfo.

        发送结果

        :param result: The result of this NotificationRecordInfo.
        :type result: str
        """
        self._result = result

    @property
    def error_message(self):
        r"""Gets the error_message of this NotificationRecordInfo.

        报错信息

        :return: The error_message of this NotificationRecordInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this NotificationRecordInfo.

        报错信息

        :param error_message: The error_message of this NotificationRecordInfo.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def operate_time(self):
        r"""Gets the operate_time of this NotificationRecordInfo.

        操作时间

        :return: The operate_time of this NotificationRecordInfo.
        :rtype: str
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        r"""Sets the operate_time of this NotificationRecordInfo.

        操作时间

        :param operate_time: The operate_time of this NotificationRecordInfo.
        :type operate_time: str
        """
        self._operate_time = operate_time

    def to_dict(self):
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
        if not isinstance(other, NotificationRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
