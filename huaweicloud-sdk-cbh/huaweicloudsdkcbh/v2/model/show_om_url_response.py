# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOmUrlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'description': 'str',
        'login_url': 'str'
    }

    attribute_map = {
        'state': 'state',
        'description': 'description',
        'login_url': 'login_url'
    }

    def __init__(self, state=None, description=None, login_url=None):
        r"""ShowOmUrlResponse

        The model defined in huaweicloud sdk

        :param state: 链接获取状态     # SUCCESS(0): 成功；非SUCCESS状态都认为获取失败，需要展示错误代码及description     # IAM_USER_CONFLICT(1016): IAM用户冲突；     # HOST_NOT_MANAGE(1): 查询主机未被纳管；     # HOST_ACCOUNT_NOT_EXIST(553): 主机账户不可用；     # IAM_USER_NO_PERMISSION(901): IAM用户无运维该主机权限；     # CUR_VERSION_NOT_SUPPORT_OPERATION(9001):当前服务版本不支持;     # INS_WHITE_LIST_INITIALIZING(9002):实例白名单正在初始化，请稍后重试;     # UNKNOWN_ERROR(9003):未知错误;
        :type state: str
        :param description: 链接获取异常时说明提示
        :type description: str
        :param login_url: ECS运维登录地址
        :type login_url: str
        """
        
        super(ShowOmUrlResponse, self).__init__()

        self._state = None
        self._description = None
        self._login_url = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if description is not None:
            self.description = description
        if login_url is not None:
            self.login_url = login_url

    @property
    def state(self):
        r"""Gets the state of this ShowOmUrlResponse.

        链接获取状态     # SUCCESS(0): 成功；非SUCCESS状态都认为获取失败，需要展示错误代码及description     # IAM_USER_CONFLICT(1016): IAM用户冲突；     # HOST_NOT_MANAGE(1): 查询主机未被纳管；     # HOST_ACCOUNT_NOT_EXIST(553): 主机账户不可用；     # IAM_USER_NO_PERMISSION(901): IAM用户无运维该主机权限；     # CUR_VERSION_NOT_SUPPORT_OPERATION(9001):当前服务版本不支持;     # INS_WHITE_LIST_INITIALIZING(9002):实例白名单正在初始化，请稍后重试;     # UNKNOWN_ERROR(9003):未知错误;

        :return: The state of this ShowOmUrlResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowOmUrlResponse.

        链接获取状态     # SUCCESS(0): 成功；非SUCCESS状态都认为获取失败，需要展示错误代码及description     # IAM_USER_CONFLICT(1016): IAM用户冲突；     # HOST_NOT_MANAGE(1): 查询主机未被纳管；     # HOST_ACCOUNT_NOT_EXIST(553): 主机账户不可用；     # IAM_USER_NO_PERMISSION(901): IAM用户无运维该主机权限；     # CUR_VERSION_NOT_SUPPORT_OPERATION(9001):当前服务版本不支持;     # INS_WHITE_LIST_INITIALIZING(9002):实例白名单正在初始化，请稍后重试;     # UNKNOWN_ERROR(9003):未知错误;

        :param state: The state of this ShowOmUrlResponse.
        :type state: str
        """
        self._state = state

    @property
    def description(self):
        r"""Gets the description of this ShowOmUrlResponse.

        链接获取异常时说明提示

        :return: The description of this ShowOmUrlResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOmUrlResponse.

        链接获取异常时说明提示

        :param description: The description of this ShowOmUrlResponse.
        :type description: str
        """
        self._description = description

    @property
    def login_url(self):
        r"""Gets the login_url of this ShowOmUrlResponse.

        ECS运维登录地址

        :return: The login_url of this ShowOmUrlResponse.
        :rtype: str
        """
        return self._login_url

    @login_url.setter
    def login_url(self, login_url):
        r"""Sets the login_url of this ShowOmUrlResponse.

        ECS运维登录地址

        :param login_url: The login_url of this ShowOmUrlResponse.
        :type login_url: str
        """
        self._login_url = login_url

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
        if not isinstance(other, ShowOmUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
