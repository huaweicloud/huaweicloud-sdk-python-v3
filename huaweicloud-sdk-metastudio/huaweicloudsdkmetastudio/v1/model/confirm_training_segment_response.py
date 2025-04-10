# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmTrainingSegmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'confirm_result': 'bool',
        'unmatched_index_hit': 'list[int]'
    }

    attribute_map = {
        'confirm_result': 'confirm_result',
        'unmatched_index_hit': 'unmatched_index_hit'
    }

    def __init__(self, confirm_result=None, unmatched_index_hit=None):
        r"""ConfirmTrainingSegmentResponse

        The model defined in huaweicloud sdk

        :param confirm_result: 是否确认成功。
        :type confirm_result: bool
        :param unmatched_index_hit: 讲解不匹配的文本索引。
        :type unmatched_index_hit: list[int]
        """
        
        super(ConfirmTrainingSegmentResponse, self).__init__()

        self._confirm_result = None
        self._unmatched_index_hit = None
        self.discriminator = None

        if confirm_result is not None:
            self.confirm_result = confirm_result
        if unmatched_index_hit is not None:
            self.unmatched_index_hit = unmatched_index_hit

    @property
    def confirm_result(self):
        r"""Gets the confirm_result of this ConfirmTrainingSegmentResponse.

        是否确认成功。

        :return: The confirm_result of this ConfirmTrainingSegmentResponse.
        :rtype: bool
        """
        return self._confirm_result

    @confirm_result.setter
    def confirm_result(self, confirm_result):
        r"""Sets the confirm_result of this ConfirmTrainingSegmentResponse.

        是否确认成功。

        :param confirm_result: The confirm_result of this ConfirmTrainingSegmentResponse.
        :type confirm_result: bool
        """
        self._confirm_result = confirm_result

    @property
    def unmatched_index_hit(self):
        r"""Gets the unmatched_index_hit of this ConfirmTrainingSegmentResponse.

        讲解不匹配的文本索引。

        :return: The unmatched_index_hit of this ConfirmTrainingSegmentResponse.
        :rtype: list[int]
        """
        return self._unmatched_index_hit

    @unmatched_index_hit.setter
    def unmatched_index_hit(self, unmatched_index_hit):
        r"""Sets the unmatched_index_hit of this ConfirmTrainingSegmentResponse.

        讲解不匹配的文本索引。

        :param unmatched_index_hit: The unmatched_index_hit of this ConfirmTrainingSegmentResponse.
        :type unmatched_index_hit: list[int]
        """
        self._unmatched_index_hit = unmatched_index_hit

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
        if not isinstance(other, ConfirmTrainingSegmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
