# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantNoticeConfigurationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'type': 'type'
    }

    def __init__(self, limit=None, offset=None, type=None):
        r"""ShowTenantNoticeConfigurationRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param type: 通知类型。 * RESOURCE_EXPIRE：资源过期通知 * RESOURCE_LEFT：资源剩余量通知
        :type type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.type = type

    @property
    def limit(self):
        r"""Gets the limit of this ShowTenantNoticeConfigurationRequest.

        每页显示的条目数量。

        :return: The limit of this ShowTenantNoticeConfigurationRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowTenantNoticeConfigurationRequest.

        每页显示的条目数量。

        :param limit: The limit of this ShowTenantNoticeConfigurationRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowTenantNoticeConfigurationRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ShowTenantNoticeConfigurationRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowTenantNoticeConfigurationRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ShowTenantNoticeConfigurationRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def type(self):
        r"""Gets the type of this ShowTenantNoticeConfigurationRequest.

        通知类型。 * RESOURCE_EXPIRE：资源过期通知 * RESOURCE_LEFT：资源剩余量通知

        :return: The type of this ShowTenantNoticeConfigurationRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowTenantNoticeConfigurationRequest.

        通知类型。 * RESOURCE_EXPIRE：资源过期通知 * RESOURCE_LEFT：资源剩余量通知

        :param type: The type of this ShowTenantNoticeConfigurationRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowTenantNoticeConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
