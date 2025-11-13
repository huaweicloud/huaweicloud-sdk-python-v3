# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteServerGroupMemberResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'servers': 'list[BatchOperateResultResponse]'
    }

    attribute_map = {
        'status': 'status',
        'servers': 'servers'
    }

    def __init__(self, status=None, servers=None):
        r"""BatchDeleteServerGroupMemberResponse

        The model defined in huaweicloud sdk

        :param status: 
        :type status: str
        :param servers: 
        :type servers: list[:class:`huaweicloudsdkecs.v2.BatchOperateResultResponse`]
        """
        
        super().__init__()

        self._status = None
        self._servers = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if servers is not None:
            self.servers = servers

    @property
    def status(self):
        r"""Gets the status of this BatchDeleteServerGroupMemberResponse.

        :return: The status of this BatchDeleteServerGroupMemberResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchDeleteServerGroupMemberResponse.

        :param status: The status of this BatchDeleteServerGroupMemberResponse.
        :type status: str
        """
        self._status = status

    @property
    def servers(self):
        r"""Gets the servers of this BatchDeleteServerGroupMemberResponse.

        :return: The servers of this BatchDeleteServerGroupMemberResponse.
        :rtype: list[:class:`huaweicloudsdkecs.v2.BatchOperateResultResponse`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this BatchDeleteServerGroupMemberResponse.

        :param servers: The servers of this BatchDeleteServerGroupMemberResponse.
        :type servers: list[:class:`huaweicloudsdkecs.v2.BatchOperateResultResponse`]
        """
        self._servers = servers

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteServerGroupMemberResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteServerGroupMemberResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
