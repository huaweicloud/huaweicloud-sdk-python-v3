# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportBatchCreateJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'async_job_id': 'str',
        'import_error_messages': 'list[ImportErrorMessageResp]',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'async_job_id': 'async_job_id',
        'import_error_messages': 'import_error_messages',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, async_job_id=None, import_error_messages=None, error_code=None, error_msg=None):
        """ImportBatchCreateJobsResponse

        The model defined in huaweicloud sdk

        :param async_job_id: 批量导入任务id。
        :type async_job_id: str
        :param import_error_messages: 导入失败的错误信息。
        :type import_error_messages: list[:class:`huaweicloudsdkdrs.v5.ImportErrorMessageResp`]
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误描述。
        :type error_msg: str
        """
        
        super(ImportBatchCreateJobsResponse, self).__init__()

        self._async_job_id = None
        self._import_error_messages = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if async_job_id is not None:
            self.async_job_id = async_job_id
        if import_error_messages is not None:
            self.import_error_messages = import_error_messages
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def async_job_id(self):
        """Gets the async_job_id of this ImportBatchCreateJobsResponse.

        批量导入任务id。

        :return: The async_job_id of this ImportBatchCreateJobsResponse.
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        """Sets the async_job_id of this ImportBatchCreateJobsResponse.

        批量导入任务id。

        :param async_job_id: The async_job_id of this ImportBatchCreateJobsResponse.
        :type async_job_id: str
        """
        self._async_job_id = async_job_id

    @property
    def import_error_messages(self):
        """Gets the import_error_messages of this ImportBatchCreateJobsResponse.

        导入失败的错误信息。

        :return: The import_error_messages of this ImportBatchCreateJobsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ImportErrorMessageResp`]
        """
        return self._import_error_messages

    @import_error_messages.setter
    def import_error_messages(self, import_error_messages):
        """Sets the import_error_messages of this ImportBatchCreateJobsResponse.

        导入失败的错误信息。

        :param import_error_messages: The import_error_messages of this ImportBatchCreateJobsResponse.
        :type import_error_messages: list[:class:`huaweicloudsdkdrs.v5.ImportErrorMessageResp`]
        """
        self._import_error_messages = import_error_messages

    @property
    def error_code(self):
        """Gets the error_code of this ImportBatchCreateJobsResponse.

        错误码。

        :return: The error_code of this ImportBatchCreateJobsResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ImportBatchCreateJobsResponse.

        错误码。

        :param error_code: The error_code of this ImportBatchCreateJobsResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this ImportBatchCreateJobsResponse.

        错误描述。

        :return: The error_msg of this ImportBatchCreateJobsResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this ImportBatchCreateJobsResponse.

        错误描述。

        :param error_msg: The error_msg of this ImportBatchCreateJobsResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ImportBatchCreateJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
