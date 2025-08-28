# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job': 'MainJob',
        'request_id': 'str'
    }

    attribute_map = {
        'job': 'job',
        'request_id': 'request_id'
    }

    def __init__(self, job=None, request_id=None):
        r"""ShowJobResponse

        The model defined in huaweicloud sdk

        :param job: 
        :type job: :class:`huaweicloudsdkelb.v3.MainJob`
        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        """
        
        super(ShowJobResponse, self).__init__()

        self._job = None
        self._request_id = None
        self.discriminator = None

        if job is not None:
            self.job = job
        if request_id is not None:
            self.request_id = request_id

    @property
    def job(self):
        r"""Gets the job of this ShowJobResponse.

        :return: The job of this ShowJobResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.MainJob`
        """
        return self._job

    @job.setter
    def job(self, job):
        r"""Sets the job of this ShowJobResponse.

        :param job: The job of this ShowJobResponse.
        :type job: :class:`huaweicloudsdkelb.v3.MainJob`
        """
        self._job = job

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowJobResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this ShowJobResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowJobResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this ShowJobResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ShowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
