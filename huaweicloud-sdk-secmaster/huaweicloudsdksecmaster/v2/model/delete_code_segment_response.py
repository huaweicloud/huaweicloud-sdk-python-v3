# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCodeSegmentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code_segment_id': 'str',
        'delete_time': 'int'
    }

    attribute_map = {
        'code_segment_id': 'code_segment_id',
        'delete_time': 'delete_time'
    }

    def __init__(self, code_segment_id=None, delete_time=None):
        r"""DeleteCodeSegmentResponse

        The model defined in huaweicloud sdk

        :param code_segment_id: UUID
        :type code_segment_id: str
        :param delete_time: 毫秒时间戳
        :type delete_time: int
        """
        
        super().__init__()

        self._code_segment_id = None
        self._delete_time = None
        self.discriminator = None

        if code_segment_id is not None:
            self.code_segment_id = code_segment_id
        if delete_time is not None:
            self.delete_time = delete_time

    @property
    def code_segment_id(self):
        r"""Gets the code_segment_id of this DeleteCodeSegmentResponse.

        UUID

        :return: The code_segment_id of this DeleteCodeSegmentResponse.
        :rtype: str
        """
        return self._code_segment_id

    @code_segment_id.setter
    def code_segment_id(self, code_segment_id):
        r"""Sets the code_segment_id of this DeleteCodeSegmentResponse.

        UUID

        :param code_segment_id: The code_segment_id of this DeleteCodeSegmentResponse.
        :type code_segment_id: str
        """
        self._code_segment_id = code_segment_id

    @property
    def delete_time(self):
        r"""Gets the delete_time of this DeleteCodeSegmentResponse.

        毫秒时间戳

        :return: The delete_time of this DeleteCodeSegmentResponse.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        r"""Sets the delete_time of this DeleteCodeSegmentResponse.

        毫秒时间戳

        :param delete_time: The delete_time of this DeleteCodeSegmentResponse.
        :type delete_time: int
        """
        self._delete_time = delete_time

    def to_dict(self):
        import warnings
        warnings.warn("DeleteCodeSegmentResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteCodeSegmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
