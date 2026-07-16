# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreSpaceJobsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[CoreSpaceJobSummary]',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'jobs': 'jobs',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, jobs=None, size=None, total=None):
        r"""ListCoreSpaceJobsResponse

        The model defined in huaweicloud sdk

        :param jobs: **参数解释：** 异步任务列表。 **取值范围：** 不涉及。 
        :type jobs: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceJobSummary`]
        :param size: **参数解释：** 当前页返回的任务数量（条）。 **取值范围：** 不涉及。 
        :type size: int
        :param total: **参数解释：** 任务总数（条）。 **取值范围：** 不涉及。 
        :type total: int
        """
        
        super().__init__()

        self._jobs = None
        self._size = None
        self._total = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def jobs(self):
        r"""Gets the jobs of this ListCoreSpaceJobsResponse.

        **参数解释：** 异步任务列表。 **取值范围：** 不涉及。 

        :return: The jobs of this ListCoreSpaceJobsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceJobSummary`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        r"""Sets the jobs of this ListCoreSpaceJobsResponse.

        **参数解释：** 异步任务列表。 **取值范围：** 不涉及。 

        :param jobs: The jobs of this ListCoreSpaceJobsResponse.
        :type jobs: list[:class:`huaweicloudsdkagentarts.v1.CoreSpaceJobSummary`]
        """
        self._jobs = jobs

    @property
    def size(self):
        r"""Gets the size of this ListCoreSpaceJobsResponse.

        **参数解释：** 当前页返回的任务数量（条）。 **取值范围：** 不涉及。 

        :return: The size of this ListCoreSpaceJobsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListCoreSpaceJobsResponse.

        **参数解释：** 当前页返回的任务数量（条）。 **取值范围：** 不涉及。 

        :param size: The size of this ListCoreSpaceJobsResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListCoreSpaceJobsResponse.

        **参数解释：** 任务总数（条）。 **取值范围：** 不涉及。 

        :return: The total of this ListCoreSpaceJobsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCoreSpaceJobsResponse.

        **参数解释：** 任务总数（条）。 **取值范围：** 不涉及。 

        :param total: The total of this ListCoreSpaceJobsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreSpaceJobsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCoreSpaceJobsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
