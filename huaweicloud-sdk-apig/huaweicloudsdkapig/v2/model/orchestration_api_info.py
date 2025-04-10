# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrchestrationApiInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_id': 'str',
        'api_name': 'str',
        'req_method': 'str',
        'req_uri': 'str',
        'auth_type': 'str',
        'match_mode': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'attached_time': 'datetime'
    }

    attribute_map = {
        'api_id': 'api_id',
        'api_name': 'api_name',
        'req_method': 'req_method',
        'req_uri': 'req_uri',
        'auth_type': 'auth_type',
        'match_mode': 'match_mode',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'attached_time': 'attached_time'
    }

    def __init__(self, api_id=None, api_name=None, req_method=None, req_uri=None, auth_type=None, match_mode=None, group_id=None, group_name=None, attached_time=None):
        r"""OrchestrationApiInfo

        The model defined in huaweicloud sdk

        :param api_id: API编号。
        :type api_id: str
        :param api_name: API名称。 支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。  &gt; 中文字符必须为UTF-8或者unicode编码。
        :type api_name: str
        :param req_method: API的请求方式。
        :type req_method: str
        :param req_uri: 请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  &gt; 需要服从URI规范。
        :type req_uri: str
        :param auth_type: API的认证方式。 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证
        :type auth_type: str
        :param match_mode: API的匹配方式。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL
        :type match_mode: str
        :param group_id: API所属的分组编号。
        :type group_id: str
        :param group_name: API所属分组的名称。
        :type group_name: str
        :param attached_time: 绑定时间。
        :type attached_time: datetime
        """
        
        

        self._api_id = None
        self._api_name = None
        self._req_method = None
        self._req_uri = None
        self._auth_type = None
        self._match_mode = None
        self._group_id = None
        self._group_name = None
        self._attached_time = None
        self.discriminator = None

        if api_id is not None:
            self.api_id = api_id
        if api_name is not None:
            self.api_name = api_name
        if req_method is not None:
            self.req_method = req_method
        if req_uri is not None:
            self.req_uri = req_uri
        if auth_type is not None:
            self.auth_type = auth_type
        if match_mode is not None:
            self.match_mode = match_mode
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if attached_time is not None:
            self.attached_time = attached_time

    @property
    def api_id(self):
        r"""Gets the api_id of this OrchestrationApiInfo.

        API编号。

        :return: The api_id of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        r"""Sets the api_id of this OrchestrationApiInfo.

        API编号。

        :param api_id: The api_id of this OrchestrationApiInfo.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def api_name(self):
        r"""Gets the api_name of this OrchestrationApiInfo.

        API名称。 支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。  > 中文字符必须为UTF-8或者unicode编码。

        :return: The api_name of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._api_name

    @api_name.setter
    def api_name(self, api_name):
        r"""Sets the api_name of this OrchestrationApiInfo.

        API名称。 支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头，3-255个字符。  > 中文字符必须为UTF-8或者unicode编码。

        :param api_name: The api_name of this OrchestrationApiInfo.
        :type api_name: str
        """
        self._api_name = api_name

    @property
    def req_method(self):
        r"""Gets the req_method of this OrchestrationApiInfo.

        API的请求方式。

        :return: The req_method of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._req_method

    @req_method.setter
    def req_method(self, req_method):
        r"""Sets the req_method of this OrchestrationApiInfo.

        API的请求方式。

        :param req_method: The req_method of this OrchestrationApiInfo.
        :type req_method: str
        """
        self._req_method = req_method

    @property
    def req_uri(self):
        r"""Gets the req_uri of this OrchestrationApiInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。

        :return: The req_uri of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._req_uri

    @req_uri.setter
    def req_uri(self, req_uri):
        r"""Sets the req_uri of this OrchestrationApiInfo.

        请求地址。可以包含请求参数，用{}标识，比如/getUserInfo/{userId}，支持 * % - _ .等特殊字符，总长度不超过512，且满足URI规范。 支持环境变量，使用环境变量时，每个变量名的长度为3 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线组成，且只能以英文开头。  > 需要服从URI规范。

        :param req_uri: The req_uri of this OrchestrationApiInfo.
        :type req_uri: str
        """
        self._req_uri = req_uri

    @property
    def auth_type(self):
        r"""Gets the auth_type of this OrchestrationApiInfo.

        API的认证方式。 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :return: The auth_type of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this OrchestrationApiInfo.

        API的认证方式。 - NONE：无认证 - APP：APP认证 - IAM：IAM认证 - AUTHORIZER：自定义认证

        :param auth_type: The auth_type of this OrchestrationApiInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def match_mode(self):
        r"""Gets the match_mode of this OrchestrationApiInfo.

        API的匹配方式。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :return: The match_mode of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        r"""Sets the match_mode of this OrchestrationApiInfo.

        API的匹配方式。 - SWA：前缀匹配 - NORMAL：正常匹配（绝对匹配） 默认：NORMAL

        :param match_mode: The match_mode of this OrchestrationApiInfo.
        :type match_mode: str
        """
        self._match_mode = match_mode

    @property
    def group_id(self):
        r"""Gets the group_id of this OrchestrationApiInfo.

        API所属的分组编号。

        :return: The group_id of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this OrchestrationApiInfo.

        API所属的分组编号。

        :param group_id: The group_id of this OrchestrationApiInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this OrchestrationApiInfo.

        API所属分组的名称。

        :return: The group_name of this OrchestrationApiInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this OrchestrationApiInfo.

        API所属分组的名称。

        :param group_name: The group_name of this OrchestrationApiInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def attached_time(self):
        r"""Gets the attached_time of this OrchestrationApiInfo.

        绑定时间。

        :return: The attached_time of this OrchestrationApiInfo.
        :rtype: datetime
        """
        return self._attached_time

    @attached_time.setter
    def attached_time(self, attached_time):
        r"""Sets the attached_time of this OrchestrationApiInfo.

        绑定时间。

        :param attached_time: The attached_time of this OrchestrationApiInfo.
        :type attached_time: datetime
        """
        self._attached_time = attached_time

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
        if not isinstance(other, OrchestrationApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
