# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePipeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipe_id': 'str'
    }

    attribute_map = {
        'pipe_id': 'pipe_id'
    }

    def __init__(self, pipe_id=None):
        r"""DeletePipeResponse

        The model defined in huaweicloud sdk

        :param pipe_id: 数据管道ID
        :type pipe_id: str
        """
        
        super().__init__()

        self._pipe_id = None
        self.discriminator = None

        if pipe_id is not None:
            self.pipe_id = pipe_id

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this DeletePipeResponse.

        数据管道ID

        :return: The pipe_id of this DeletePipeResponse.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this DeletePipeResponse.

        数据管道ID

        :param pipe_id: The pipe_id of this DeletePipeResponse.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    def to_dict(self):
        import warnings
        warnings.warn("DeletePipeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeletePipeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
