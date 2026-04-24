# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFullSpeedRecordConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_id': 'str',
        'body': 'UpdateScreenRecordsRequestBody'
    }

    attribute_map = {
        'record_id': 'record_id',
        'body': 'body'
    }

    def __init__(self, record_id=None, body=None):
        r"""UpdateFullSpeedRecordConfigRequest

        The model defined in huaweicloud sdk

        :param record_id: 录屏记录UUID。
        :type record_id: str
        :param body: Body of the UpdateFullSpeedRecordConfigRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateScreenRecordsRequestBody`
        """
        
        

        self._record_id = None
        self._body = None
        self.discriminator = None

        self.record_id = record_id
        if body is not None:
            self.body = body

    @property
    def record_id(self):
        r"""Gets the record_id of this UpdateFullSpeedRecordConfigRequest.

        录屏记录UUID。

        :return: The record_id of this UpdateFullSpeedRecordConfigRequest.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this UpdateFullSpeedRecordConfigRequest.

        录屏记录UUID。

        :param record_id: The record_id of this UpdateFullSpeedRecordConfigRequest.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def body(self):
        r"""Gets the body of this UpdateFullSpeedRecordConfigRequest.

        :return: The body of this UpdateFullSpeedRecordConfigRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.UpdateScreenRecordsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateFullSpeedRecordConfigRequest.

        :param body: The body of this UpdateFullSpeedRecordConfigRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.UpdateScreenRecordsRequestBody`
        """
        self._body = body

    def to_dict(self):
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
        if not isinstance(other, UpdateFullSpeedRecordConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
