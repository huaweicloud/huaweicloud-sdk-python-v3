# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneListenerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'listener_list': 'list[CloneListenerResp]',
        'request_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'listener_list': 'listener_list',
        'request_id': 'request_id',
        'job_id': 'job_id'
    }

    def __init__(self, listener_list=None, request_id=None, job_id=None):
        r"""CloneListenerResponse

        The model defined in huaweicloud sdk

        :param listener_list: **参数解释**：新监听器相关信息。
        :type listener_list: list[:class:`huaweicloudsdkelb.v3.CloneListenerResp`]
        :param request_id: **参数解释**：请求的ID 。 **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        :param job_id: **参数解释**：监听器复制任务的ID，任务详情可通过GET /v3/{project_id}/elb/jobs/{job_id}进行查询。 **取值范围**：标准的UUID格式，长度为36个字符。
        :type job_id: str
        """
        
        super().__init__()

        self._listener_list = None
        self._request_id = None
        self._job_id = None
        self.discriminator = None

        if listener_list is not None:
            self.listener_list = listener_list
        if request_id is not None:
            self.request_id = request_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def listener_list(self):
        r"""Gets the listener_list of this CloneListenerResponse.

        **参数解释**：新监听器相关信息。

        :return: The listener_list of this CloneListenerResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.CloneListenerResp`]
        """
        return self._listener_list

    @listener_list.setter
    def listener_list(self, listener_list):
        r"""Sets the listener_list of this CloneListenerResponse.

        **参数解释**：新监听器相关信息。

        :param listener_list: The listener_list of this CloneListenerResponse.
        :type listener_list: list[:class:`huaweicloudsdkelb.v3.CloneListenerResp`]
        """
        self._listener_list = listener_list

    @property
    def request_id(self):
        r"""Gets the request_id of this CloneListenerResponse.

        **参数解释**：请求的ID 。 **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this CloneListenerResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CloneListenerResponse.

        **参数解释**：请求的ID 。 **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this CloneListenerResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this CloneListenerResponse.

        **参数解释**：监听器复制任务的ID，任务详情可通过GET /v3/{project_id}/elb/jobs/{job_id}进行查询。 **取值范围**：标准的UUID格式，长度为36个字符。

        :return: The job_id of this CloneListenerResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CloneListenerResponse.

        **参数解释**：监听器复制任务的ID，任务详情可通过GET /v3/{project_id}/elb/jobs/{job_id}进行查询。 **取值范围**：标准的UUID格式，长度为36个字符。

        :param job_id: The job_id of this CloneListenerResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("CloneListenerResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CloneListenerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
