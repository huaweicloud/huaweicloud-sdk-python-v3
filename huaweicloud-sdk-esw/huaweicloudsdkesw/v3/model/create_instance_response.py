# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'instance': 'Instance',
        'job_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'instance': 'instance',
        'job_id': 'job_id'
    }

    def __init__(self, request_id=None, instance=None, job_id=None):
        r"""CreateInstanceResponse

        The model defined in huaweicloud sdk

        :param request_id: - 参数解释：请求的唯一标识。 - 约束限制：UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type request_id: str
        :param instance: 
        :type instance: :class:`huaweicloudsdkesw.v3.Instance`
        :param job_id: - 参数解释：任务的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type job_id: str
        """
        
        super().__init__()

        self._request_id = None
        self._instance = None
        self._job_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if instance is not None:
            self.instance = instance
        if job_id is not None:
            self.job_id = job_id

    @property
    def request_id(self):
        r"""Gets the request_id of this CreateInstanceResponse.

        - 参数解释：请求的唯一标识。 - 约束限制：UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The request_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreateInstanceResponse.

        - 参数解释：请求的唯一标识。 - 约束限制：UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param request_id: The request_id of this CreateInstanceResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def instance(self):
        r"""Gets the instance of this CreateInstanceResponse.

        :return: The instance of this CreateInstanceResponse.
        :rtype: :class:`huaweicloudsdkesw.v3.Instance`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this CreateInstanceResponse.

        :param instance: The instance of this CreateInstanceResponse.
        :type instance: :class:`huaweicloudsdkesw.v3.Instance`
        """
        self._instance = instance

    @property
    def job_id(self):
        r"""Gets the job_id of this CreateInstanceResponse.

        - 参数解释：任务的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The job_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CreateInstanceResponse.

        - 参数解释：任务的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param job_id: The job_id of this CreateInstanceResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateInstanceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
