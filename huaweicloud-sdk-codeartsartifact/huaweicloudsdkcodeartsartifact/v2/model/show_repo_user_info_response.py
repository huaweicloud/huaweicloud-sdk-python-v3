# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepoUserInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'trace_id': 'str',
        'result': 'RepositoryUserDO'
    }

    attribute_map = {
        'status': 'status',
        'trace_id': 'trace_id',
        'result': 'result'
    }

    def __init__(self, status=None, trace_id=None, result=None):
        r"""ShowRepoUserInfoResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**： 请求成功或失败状态。 **取值范围**： - success：请求成功。 - error：请求失败。
        :type status: str
        :param trace_id: **参数解释**： 请求ID，当前请求唯一标识。 **取值范围**： 数字及中划线（-）组成的字符串。
        :type trace_id: str
        :param result: 
        :type result: :class:`huaweicloudsdkcodeartsartifact.v2.RepositoryUserDO`
        """
        
        super().__init__()

        self._status = None
        self._trace_id = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if trace_id is not None:
            self.trace_id = trace_id
        if result is not None:
            self.result = result

    @property
    def status(self):
        r"""Gets the status of this ShowRepoUserInfoResponse.

        **参数解释**： 请求成功或失败状态。 **取值范围**： - success：请求成功。 - error：请求失败。

        :return: The status of this ShowRepoUserInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowRepoUserInfoResponse.

        **参数解释**： 请求成功或失败状态。 **取值范围**： - success：请求成功。 - error：请求失败。

        :param status: The status of this ShowRepoUserInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ShowRepoUserInfoResponse.

        **参数解释**： 请求ID，当前请求唯一标识。 **取值范围**： 数字及中划线（-）组成的字符串。

        :return: The trace_id of this ShowRepoUserInfoResponse.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ShowRepoUserInfoResponse.

        **参数解释**： 请求ID，当前请求唯一标识。 **取值范围**： 数字及中划线（-）组成的字符串。

        :param trace_id: The trace_id of this ShowRepoUserInfoResponse.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def result(self):
        r"""Gets the result of this ShowRepoUserInfoResponse.

        :return: The result of this ShowRepoUserInfoResponse.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.RepositoryUserDO`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowRepoUserInfoResponse.

        :param result: The result of this ShowRepoUserInfoResponse.
        :type result: :class:`huaweicloudsdkcodeartsartifact.v2.RepositoryUserDO`
        """
        self._result = result

    def to_dict(self):
        import warnings
        warnings.warn("ShowRepoUserInfoResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowRepoUserInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
