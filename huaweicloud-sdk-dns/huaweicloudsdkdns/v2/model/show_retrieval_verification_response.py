# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRetrievalVerificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, status=None, updated_at=None):
        r"""ShowRetrievalVerificationResponse

        The model defined in huaweicloud sdk

        :param id: 找回请求ID。
        :type id: str
        :param status: 找回状态。  取值范围：  PENDING：处理中 CREATED：已找回
        :type status: str
        :param updated_at: 更新时间。 格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type updated_at: str
        """
        
        super().__init__()

        self._id = None
        self._status = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ShowRetrievalVerificationResponse.

        找回请求ID。

        :return: The id of this ShowRetrievalVerificationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowRetrievalVerificationResponse.

        找回请求ID。

        :param id: The id of this ShowRetrievalVerificationResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ShowRetrievalVerificationResponse.

        找回状态。  取值范围：  PENDING：处理中 CREATED：已找回

        :return: The status of this ShowRetrievalVerificationResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowRetrievalVerificationResponse.

        找回状态。  取值范围：  PENDING：处理中 CREATED：已找回

        :param status: The status of this ShowRetrievalVerificationResponse.
        :type status: str
        """
        self._status = status

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowRetrievalVerificationResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The updated_at of this ShowRetrievalVerificationResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowRetrievalVerificationResponse.

        更新时间。 格式：yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param updated_at: The updated_at of this ShowRetrievalVerificationResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowRetrievalVerificationResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRetrievalVerificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
