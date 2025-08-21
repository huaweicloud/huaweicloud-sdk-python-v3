# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAverageEvaluationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'merge_request_id': 'int',
        'average_evaluation_level': 'float',
        'evaluations': 'list[MergeRequestBaseEvaluationDto]',
        'custom_evaluations': 'list[MergeRequestCustomAverageEvaluationDto]'
    }

    attribute_map = {
        'merge_request_id': 'merge_request_id',
        'average_evaluation_level': 'average_evaluation_level',
        'evaluations': 'evaluations',
        'custom_evaluations': 'custom_evaluations'
    }

    def __init__(self, merge_request_id=None, average_evaluation_level=None, evaluations=None, custom_evaluations=None):
        r"""ShowAverageEvaluationResponse

        The model defined in huaweicloud sdk

        :param merge_request_id: **参数解释：** 合并请求id。
        :type merge_request_id: int
        :param average_evaluation_level: **参数解释：** 评价平均分。
        :type average_evaluation_level: float
        :param evaluations: **参数解释：** 单人评价详情。
        :type evaluations: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestBaseEvaluationDto`]
        :param custom_evaluations: **参数解释：** 自定义评价维度详情。
        :type custom_evaluations: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestCustomAverageEvaluationDto`]
        """
        
        super(ShowAverageEvaluationResponse, self).__init__()

        self._merge_request_id = None
        self._average_evaluation_level = None
        self._evaluations = None
        self._custom_evaluations = None
        self.discriminator = None

        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if average_evaluation_level is not None:
            self.average_evaluation_level = average_evaluation_level
        if evaluations is not None:
            self.evaluations = evaluations
        if custom_evaluations is not None:
            self.custom_evaluations = custom_evaluations

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this ShowAverageEvaluationResponse.

        **参数解释：** 合并请求id。

        :return: The merge_request_id of this ShowAverageEvaluationResponse.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this ShowAverageEvaluationResponse.

        **参数解释：** 合并请求id。

        :param merge_request_id: The merge_request_id of this ShowAverageEvaluationResponse.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def average_evaluation_level(self):
        r"""Gets the average_evaluation_level of this ShowAverageEvaluationResponse.

        **参数解释：** 评价平均分。

        :return: The average_evaluation_level of this ShowAverageEvaluationResponse.
        :rtype: float
        """
        return self._average_evaluation_level

    @average_evaluation_level.setter
    def average_evaluation_level(self, average_evaluation_level):
        r"""Sets the average_evaluation_level of this ShowAverageEvaluationResponse.

        **参数解释：** 评价平均分。

        :param average_evaluation_level: The average_evaluation_level of this ShowAverageEvaluationResponse.
        :type average_evaluation_level: float
        """
        self._average_evaluation_level = average_evaluation_level

    @property
    def evaluations(self):
        r"""Gets the evaluations of this ShowAverageEvaluationResponse.

        **参数解释：** 单人评价详情。

        :return: The evaluations of this ShowAverageEvaluationResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestBaseEvaluationDto`]
        """
        return self._evaluations

    @evaluations.setter
    def evaluations(self, evaluations):
        r"""Sets the evaluations of this ShowAverageEvaluationResponse.

        **参数解释：** 单人评价详情。

        :param evaluations: The evaluations of this ShowAverageEvaluationResponse.
        :type evaluations: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestBaseEvaluationDto`]
        """
        self._evaluations = evaluations

    @property
    def custom_evaluations(self):
        r"""Gets the custom_evaluations of this ShowAverageEvaluationResponse.

        **参数解释：** 自定义评价维度详情。

        :return: The custom_evaluations of this ShowAverageEvaluationResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestCustomAverageEvaluationDto`]
        """
        return self._custom_evaluations

    @custom_evaluations.setter
    def custom_evaluations(self, custom_evaluations):
        r"""Sets the custom_evaluations of this ShowAverageEvaluationResponse.

        **参数解释：** 自定义评价维度详情。

        :param custom_evaluations: The custom_evaluations of this ShowAverageEvaluationResponse.
        :type custom_evaluations: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestCustomAverageEvaluationDto`]
        """
        self._custom_evaluations = custom_evaluations

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
        if not isinstance(other, ShowAverageEvaluationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
