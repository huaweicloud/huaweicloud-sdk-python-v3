# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteSnapshotsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'code': 'str',
        'total_count': 'int',
        'success_count': 'int',
        'failure_count': 'int',
        'failure_details': 'list[FailureDetail]'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code',
        'total_count': 'total_count',
        'success_count': 'success_count',
        'failure_count': 'failure_count',
        'failure_details': 'failure_details'
    }

    def __init__(self, message=None, code=None, total_count=None, success_count=None, failure_count=None, failure_details=None):
        r"""BatchDeleteSnapshotsResponse

        The model defined in huaweicloud sdk

        :param message: 响应信息。
        :type message: str
        :param code: 响应码。
        :type code: str
        :param total_count: 总数量。
        :type total_count: int
        :param success_count: 成功数量。
        :type success_count: int
        :param failure_count: 失败数量。
        :type failure_count: int
        :param failure_details: 失败详情列表。
        :type failure_details: list[:class:`huaweicloudsdkprojectman.v4.FailureDetail`]
        """
        
        super().__init__()

        self._message = None
        self._code = None
        self._total_count = None
        self._success_count = None
        self._failure_count = None
        self._failure_details = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if total_count is not None:
            self.total_count = total_count
        if success_count is not None:
            self.success_count = success_count
        if failure_count is not None:
            self.failure_count = failure_count
        if failure_details is not None:
            self.failure_details = failure_details

    @property
    def message(self):
        r"""Gets the message of this BatchDeleteSnapshotsResponse.

        响应信息。

        :return: The message of this BatchDeleteSnapshotsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this BatchDeleteSnapshotsResponse.

        响应信息。

        :param message: The message of this BatchDeleteSnapshotsResponse.
        :type message: str
        """
        self._message = message

    @property
    def code(self):
        r"""Gets the code of this BatchDeleteSnapshotsResponse.

        响应码。

        :return: The code of this BatchDeleteSnapshotsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BatchDeleteSnapshotsResponse.

        响应码。

        :param code: The code of this BatchDeleteSnapshotsResponse.
        :type code: str
        """
        self._code = code

    @property
    def total_count(self):
        r"""Gets the total_count of this BatchDeleteSnapshotsResponse.

        总数量。

        :return: The total_count of this BatchDeleteSnapshotsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this BatchDeleteSnapshotsResponse.

        总数量。

        :param total_count: The total_count of this BatchDeleteSnapshotsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def success_count(self):
        r"""Gets the success_count of this BatchDeleteSnapshotsResponse.

        成功数量。

        :return: The success_count of this BatchDeleteSnapshotsResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this BatchDeleteSnapshotsResponse.

        成功数量。

        :param success_count: The success_count of this BatchDeleteSnapshotsResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failure_count(self):
        r"""Gets the failure_count of this BatchDeleteSnapshotsResponse.

        失败数量。

        :return: The failure_count of this BatchDeleteSnapshotsResponse.
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        r"""Sets the failure_count of this BatchDeleteSnapshotsResponse.

        失败数量。

        :param failure_count: The failure_count of this BatchDeleteSnapshotsResponse.
        :type failure_count: int
        """
        self._failure_count = failure_count

    @property
    def failure_details(self):
        r"""Gets the failure_details of this BatchDeleteSnapshotsResponse.

        失败详情列表。

        :return: The failure_details of this BatchDeleteSnapshotsResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FailureDetail`]
        """
        return self._failure_details

    @failure_details.setter
    def failure_details(self, failure_details):
        r"""Sets the failure_details of this BatchDeleteSnapshotsResponse.

        失败详情列表。

        :param failure_details: The failure_details of this BatchDeleteSnapshotsResponse.
        :type failure_details: list[:class:`huaweicloudsdkprojectman.v4.FailureDetail`]
        """
        self._failure_details = failure_details

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteSnapshotsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteSnapshotsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
