# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionConfigurationResponseItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'code': 'int',
        'error_code': 'str',
        'error_msg': 'str',
        'request_id': 'str',
        'error_stage': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'code': 'code',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'request_id': 'request_id',
        'error_stage': 'error_stage'
    }

    def __init__(self, ids=None, code=None, error_code=None, error_msg=None, request_id=None, error_stage=None):
        r"""ProtectionConfigurationResponseItem

        The model defined in huaweicloud sdk

        :param ids: 资源ID
        :type ids: list[str]
        :param code: 状态码
        :type code: int
        :param error_code: 错误编码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        :param request_id: bcc向其他云服务请求的requestId
        :type request_id: str
        :param error_stage: 发生错误的阶段
        :type error_stage: str
        """
        
        

        self._ids = None
        self._code = None
        self._error_code = None
        self._error_msg = None
        self._request_id = None
        self._error_stage = None
        self.discriminator = None

        self.ids = ids
        self.code = code
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if request_id is not None:
            self.request_id = request_id
        if error_stage is not None:
            self.error_stage = error_stage

    @property
    def ids(self):
        r"""Gets the ids of this ProtectionConfigurationResponseItem.

        资源ID

        :return: The ids of this ProtectionConfigurationResponseItem.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this ProtectionConfigurationResponseItem.

        资源ID

        :param ids: The ids of this ProtectionConfigurationResponseItem.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def code(self):
        r"""Gets the code of this ProtectionConfigurationResponseItem.

        状态码

        :return: The code of this ProtectionConfigurationResponseItem.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ProtectionConfigurationResponseItem.

        状态码

        :param code: The code of this ProtectionConfigurationResponseItem.
        :type code: int
        """
        self._code = code

    @property
    def error_code(self):
        r"""Gets the error_code of this ProtectionConfigurationResponseItem.

        错误编码

        :return: The error_code of this ProtectionConfigurationResponseItem.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ProtectionConfigurationResponseItem.

        错误编码

        :param error_code: The error_code of this ProtectionConfigurationResponseItem.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ProtectionConfigurationResponseItem.

        错误信息

        :return: The error_msg of this ProtectionConfigurationResponseItem.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ProtectionConfigurationResponseItem.

        错误信息

        :param error_msg: The error_msg of this ProtectionConfigurationResponseItem.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def request_id(self):
        r"""Gets the request_id of this ProtectionConfigurationResponseItem.

        bcc向其他云服务请求的requestId

        :return: The request_id of this ProtectionConfigurationResponseItem.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ProtectionConfigurationResponseItem.

        bcc向其他云服务请求的requestId

        :param request_id: The request_id of this ProtectionConfigurationResponseItem.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def error_stage(self):
        r"""Gets the error_stage of this ProtectionConfigurationResponseItem.

        发生错误的阶段

        :return: The error_stage of this ProtectionConfigurationResponseItem.
        :rtype: str
        """
        return self._error_stage

    @error_stage.setter
    def error_stage(self, error_stage):
        r"""Sets the error_stage of this ProtectionConfigurationResponseItem.

        发生错误的阶段

        :param error_stage: The error_stage of this ProtectionConfigurationResponseItem.
        :type error_stage: str
        """
        self._error_stage = error_stage

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
        if not isinstance(other, ProtectionConfigurationResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
