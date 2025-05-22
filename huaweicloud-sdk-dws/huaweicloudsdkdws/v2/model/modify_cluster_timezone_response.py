# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyClusterTimezoneResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_msg': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'job_id': 'job_id'
    }

    def __init__(self, error_code=None, error_msg=None, job_id=None):
        r"""ModifyClusterTimezoneResponse

        The model defined in huaweicloud sdk

        :param error_code: **参数解释**： 错误码。 **取值范围**： 不涉及。
        :type error_code: str
        :param error_msg: **参数解释**： 错误信息。 **取值范围**： 不涉及。
        :type error_msg: str
        :param job_id: **参数解释**： 任务ID，可用于查询任务进度信息。 **取值范围**： 不涉及。
        :type job_id: str
        """
        
        super(ModifyClusterTimezoneResponse, self).__init__()

        self._error_code = None
        self._error_msg = None
        self._job_id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if job_id is not None:
            self.job_id = job_id

    @property
    def error_code(self):
        r"""Gets the error_code of this ModifyClusterTimezoneResponse.

        **参数解释**： 错误码。 **取值范围**： 不涉及。

        :return: The error_code of this ModifyClusterTimezoneResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ModifyClusterTimezoneResponse.

        **参数解释**： 错误码。 **取值范围**： 不涉及。

        :param error_code: The error_code of this ModifyClusterTimezoneResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ModifyClusterTimezoneResponse.

        **参数解释**： 错误信息。 **取值范围**： 不涉及。

        :return: The error_msg of this ModifyClusterTimezoneResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ModifyClusterTimezoneResponse.

        **参数解释**： 错误信息。 **取值范围**： 不涉及。

        :param error_msg: The error_msg of this ModifyClusterTimezoneResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def job_id(self):
        r"""Gets the job_id of this ModifyClusterTimezoneResponse.

        **参数解释**： 任务ID，可用于查询任务进度信息。 **取值范围**： 不涉及。

        :return: The job_id of this ModifyClusterTimezoneResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ModifyClusterTimezoneResponse.

        **参数解释**： 任务ID，可用于查询任务进度信息。 **取值范围**： 不涉及。

        :param job_id: The job_id of this ModifyClusterTimezoneResponse.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ModifyClusterTimezoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
