# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperateResultResponse:

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
        'server_id': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'status': 'status',
        'server_id': 'server_id',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, status=None, server_id=None, fail_reason=None):
        r"""BatchOperateResultResponse

        The model defined in huaweicloud sdk

        :param status: 
        :type status: str
        :param server_id: 
        :type server_id: str
        :param fail_reason: 
        :type fail_reason: str
        """
        
        

        self._status = None
        self._server_id = None
        self._fail_reason = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if server_id is not None:
            self.server_id = server_id
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def status(self):
        r"""Gets the status of this BatchOperateResultResponse.

        :return: The status of this BatchOperateResultResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchOperateResultResponse.

        :param status: The status of this BatchOperateResultResponse.
        :type status: str
        """
        self._status = status

    @property
    def server_id(self):
        r"""Gets the server_id of this BatchOperateResultResponse.

        :return: The server_id of this BatchOperateResultResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this BatchOperateResultResponse.

        :param server_id: The server_id of this BatchOperateResultResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this BatchOperateResultResponse.

        :return: The fail_reason of this BatchOperateResultResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this BatchOperateResultResponse.

        :param fail_reason: The fail_reason of this BatchOperateResultResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, BatchOperateResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
