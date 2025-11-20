# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[Job]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'jobs': 'jobs',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, jobs=None, page_info=None, request_id=None):
        r"""ListResourceJobsResponse

        The model defined in huaweicloud sdk

        :param jobs: - 参数解释：查询任务列表的响应体。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type jobs: list[:class:`huaweicloudsdkesw.v3.Job`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkesw.v3.PageInfo`
        :param request_id: - 参数解释：请求的唯一标识。 - 约束限制：UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type request_id: str
        """
        
        super().__init__()

        self._jobs = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def jobs(self):
        r"""Gets the jobs of this ListResourceJobsResponse.

        - 参数解释：查询任务列表的响应体。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The jobs of this ListResourceJobsResponse.
        :rtype: list[:class:`huaweicloudsdkesw.v3.Job`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ListResourceJobsResponse.

        - 参数解释：查询任务列表的响应体。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param jobs: The jobs of this ListResourceJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkesw.v3.Job`]
        """
        self._jobs = jobs

    @property
    def page_info(self):
        r"""Gets the page_info of this ListResourceJobsResponse.

        :return: The page_info of this ListResourceJobsResponse.
        :rtype: :class:`huaweicloudsdkesw.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListResourceJobsResponse.

        :param page_info: The page_info of this ListResourceJobsResponse.
        :type page_info: :class:`huaweicloudsdkesw.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListResourceJobsResponse.

        - 参数解释：请求的唯一标识。 - 约束限制：UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The request_id of this ListResourceJobsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListResourceJobsResponse.

        - 参数解释：请求的唯一标识。 - 约束限制：UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param request_id: The request_id of this ListResourceJobsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListResourceJobsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListResourceJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
