# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckPreliminaryResultsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pre_check_results': 'list[PreCheckResult]',
        'job_id': 'str'
    }

    attribute_map = {
        'pre_check_results': 'pre_check_results',
        'job_id': 'job_id'
    }

    def __init__(self, pre_check_results=None, job_id=None):
        r"""CheckPreliminaryResultsResponse

        The model defined in huaweicloud sdk

        :param pre_check_results: 关联的后端DN信息。
        :type pre_check_results: list[:class:`huaweicloudsdkddm.v1.PreCheckResult`]
        :param job_id: 工作流id。
        :type job_id: str
        """
        
        super().__init__()

        self._pre_check_results = None
        self._job_id = None
        self.discriminator = None

        if pre_check_results is not None:
            self.pre_check_results = pre_check_results
        if job_id is not None:
            self.job_id = job_id

    @property
    def pre_check_results(self):
        r"""Gets the pre_check_results of this CheckPreliminaryResultsResponse.

        关联的后端DN信息。

        :return: The pre_check_results of this CheckPreliminaryResultsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.PreCheckResult`]
        """
        return self._pre_check_results

    @pre_check_results.setter
    def pre_check_results(self, pre_check_results):
        r"""Sets the pre_check_results of this CheckPreliminaryResultsResponse.

        关联的后端DN信息。

        :param pre_check_results: The pre_check_results of this CheckPreliminaryResultsResponse.
        :type pre_check_results: list[:class:`huaweicloudsdkddm.v1.PreCheckResult`]
        """
        self._pre_check_results = pre_check_results

    @property
    def job_id(self):
        r"""Gets the job_id of this CheckPreliminaryResultsResponse.

        工作流id。

        :return: The job_id of this CheckPreliminaryResultsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this CheckPreliminaryResultsResponse.

        工作流id。

        :param job_id: The job_id of this CheckPreliminaryResultsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    def to_dict(self):
        import warnings
        warnings.warn("CheckPreliminaryResultsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CheckPreliminaryResultsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
