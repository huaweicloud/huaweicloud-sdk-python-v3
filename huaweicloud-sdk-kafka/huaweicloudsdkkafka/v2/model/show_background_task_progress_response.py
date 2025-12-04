# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackgroundTaskProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress_percentage': 'int',
        'remain_time': 'int',
        'step_list': 'list[StepDetail]'
    }

    attribute_map = {
        'progress_percentage': 'progress_percentage',
        'remain_time': 'remain_time',
        'step_list': 'step_list'
    }

    def __init__(self, progress_percentage=None, remain_time=None, step_list=None):
        r"""ShowBackgroundTaskProgressResponse

        The model defined in huaweicloud sdk

        :param progress_percentage: **参数解释**： 进度。 **取值范围**： 不涉及。
        :type progress_percentage: int
        :param remain_time: **参数解释**： 剩余时间。 **取值范围**： 不涉及。
        :type remain_time: int
        :param step_list: **参数解释**： 步骤列表。
        :type step_list: list[:class:`huaweicloudsdkkafka.v2.StepDetail`]
        """
        
        super().__init__()

        self._progress_percentage = None
        self._remain_time = None
        self._step_list = None
        self.discriminator = None

        if progress_percentage is not None:
            self.progress_percentage = progress_percentage
        if remain_time is not None:
            self.remain_time = remain_time
        if step_list is not None:
            self.step_list = step_list

    @property
    def progress_percentage(self):
        r"""Gets the progress_percentage of this ShowBackgroundTaskProgressResponse.

        **参数解释**： 进度。 **取值范围**： 不涉及。

        :return: The progress_percentage of this ShowBackgroundTaskProgressResponse.
        :rtype: int
        """
        return self._progress_percentage

    @progress_percentage.setter
    def progress_percentage(self, progress_percentage):
        r"""Sets the progress_percentage of this ShowBackgroundTaskProgressResponse.

        **参数解释**： 进度。 **取值范围**： 不涉及。

        :param progress_percentage: The progress_percentage of this ShowBackgroundTaskProgressResponse.
        :type progress_percentage: int
        """
        self._progress_percentage = progress_percentage

    @property
    def remain_time(self):
        r"""Gets the remain_time of this ShowBackgroundTaskProgressResponse.

        **参数解释**： 剩余时间。 **取值范围**： 不涉及。

        :return: The remain_time of this ShowBackgroundTaskProgressResponse.
        :rtype: int
        """
        return self._remain_time

    @remain_time.setter
    def remain_time(self, remain_time):
        r"""Sets the remain_time of this ShowBackgroundTaskProgressResponse.

        **参数解释**： 剩余时间。 **取值范围**： 不涉及。

        :param remain_time: The remain_time of this ShowBackgroundTaskProgressResponse.
        :type remain_time: int
        """
        self._remain_time = remain_time

    @property
    def step_list(self):
        r"""Gets the step_list of this ShowBackgroundTaskProgressResponse.

        **参数解释**： 步骤列表。

        :return: The step_list of this ShowBackgroundTaskProgressResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.StepDetail`]
        """
        return self._step_list

    @step_list.setter
    def step_list(self, step_list):
        r"""Sets the step_list of this ShowBackgroundTaskProgressResponse.

        **参数解释**： 步骤列表。

        :param step_list: The step_list of this ShowBackgroundTaskProgressResponse.
        :type step_list: list[:class:`huaweicloudsdkkafka.v2.StepDetail`]
        """
        self._step_list = step_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackgroundTaskProgressResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowBackgroundTaskProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
