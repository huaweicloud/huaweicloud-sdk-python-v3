# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateJobResponse(SdkResponse):

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
        'version_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_id': 'version_id'
    }

    def __init__(self, id=None, version_id=None):
        r"""UpdateJobResponse

        The model defined in huaweicloud sdk

        :param id: 作业Id
        :type id: str
        :param version_id: 作业版本Id
        :type version_id: str
        """
        
        super().__init__()

        self._id = None
        self._version_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version_id is not None:
            self.version_id = version_id

    @property
    def id(self):
        r"""Gets the id of this UpdateJobResponse.

        作业Id

        :return: The id of this UpdateJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateJobResponse.

        作业Id

        :param id: The id of this UpdateJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def version_id(self):
        r"""Gets the version_id of this UpdateJobResponse.

        作业版本Id

        :return: The version_id of this UpdateJobResponse.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this UpdateJobResponse.

        作业版本Id

        :param version_id: The version_id of this UpdateJobResponse.
        :type version_id: str
        """
        self._version_id = version_id

    def to_dict(self):
        import warnings
        warnings.warn("UpdateJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
