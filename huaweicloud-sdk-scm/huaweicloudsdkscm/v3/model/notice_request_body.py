# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoticeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'notice_type': 'list[str]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'notice_type': 'notice_type'
    }

    def __init__(self, resource_id=None, notice_type=None):
        r"""NoticeRequestBody

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param notice_type: 提醒类型，取值如下： - CERT_EXPIRING(证书到期) - CERT_EXPIRED(证书过期)
        :type notice_type: list[str]
        """
        
        

        self._resource_id = None
        self._notice_type = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if notice_type is not None:
            self.notice_type = notice_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this NoticeRequestBody.

        资源ID。

        :return: The resource_id of this NoticeRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this NoticeRequestBody.

        资源ID。

        :param resource_id: The resource_id of this NoticeRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def notice_type(self):
        r"""Gets the notice_type of this NoticeRequestBody.

        提醒类型，取值如下： - CERT_EXPIRING(证书到期) - CERT_EXPIRED(证书过期)

        :return: The notice_type of this NoticeRequestBody.
        :rtype: list[str]
        """
        return self._notice_type

    @notice_type.setter
    def notice_type(self, notice_type):
        r"""Sets the notice_type of this NoticeRequestBody.

        提醒类型，取值如下： - CERT_EXPIRING(证书到期) - CERT_EXPIRED(证书过期)

        :param notice_type: The notice_type of this NoticeRequestBody.
        :type notice_type: list[str]
        """
        self._notice_type = notice_type

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
        if not isinstance(other, NoticeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
