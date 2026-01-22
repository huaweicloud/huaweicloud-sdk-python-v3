# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogBackupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_list': 'list[LogList]',
        'type': 'str',
        'completed': 'bool'
    }

    attribute_map = {
        'log_list': 'logList',
        'type': 'type',
        'completed': 'completed'
    }

    def __init__(self, log_list=None, type=None, completed=None):
        r"""ShowLogBackupResponse

        The model defined in huaweicloud sdk

        :param log_list: 
        :type log_list: list[:class:`huaweicloudsdkcss.v1.LogList`]
        :param type: 查询日志的类型。
        :type type: str
        :param completed: **参数解释**： 日志文件是否已经查询完。 **取值范围**： - true： 日志文件已经查询完，没有更多结果了。 - false：日志文件未查询完，因日志条数已达到请求条数或者日志大小达到1MB，查询提前返回结果。
        :type completed: bool
        """
        
        super().__init__()

        self._log_list = None
        self._type = None
        self._completed = None
        self.discriminator = None

        if log_list is not None:
            self.log_list = log_list
        if type is not None:
            self.type = type
        if completed is not None:
            self.completed = completed

    @property
    def log_list(self):
        r"""Gets the log_list of this ShowLogBackupResponse.

        :return: The log_list of this ShowLogBackupResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.LogList`]
        """
        return self._log_list

    @log_list.setter
    def log_list(self, log_list):
        r"""Sets the log_list of this ShowLogBackupResponse.

        :param log_list: The log_list of this ShowLogBackupResponse.
        :type log_list: list[:class:`huaweicloudsdkcss.v1.LogList`]
        """
        self._log_list = log_list

    @property
    def type(self):
        r"""Gets the type of this ShowLogBackupResponse.

        查询日志的类型。

        :return: The type of this ShowLogBackupResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowLogBackupResponse.

        查询日志的类型。

        :param type: The type of this ShowLogBackupResponse.
        :type type: str
        """
        self._type = type

    @property
    def completed(self):
        r"""Gets the completed of this ShowLogBackupResponse.

        **参数解释**： 日志文件是否已经查询完。 **取值范围**： - true： 日志文件已经查询完，没有更多结果了。 - false：日志文件未查询完，因日志条数已达到请求条数或者日志大小达到1MB，查询提前返回结果。

        :return: The completed of this ShowLogBackupResponse.
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        r"""Sets the completed of this ShowLogBackupResponse.

        **参数解释**： 日志文件是否已经查询完。 **取值范围**： - true： 日志文件已经查询完，没有更多结果了。 - false：日志文件未查询完，因日志条数已达到请求条数或者日志大小达到1MB，查询提前返回结果。

        :param completed: The completed of this ShowLogBackupResponse.
        :type completed: bool
        """
        self._completed = completed

    def to_dict(self):
        import warnings
        warnings.warn("ShowLogBackupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLogBackupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
