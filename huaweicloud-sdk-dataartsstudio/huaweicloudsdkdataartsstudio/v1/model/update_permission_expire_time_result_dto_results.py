# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePermissionExpireTimeResultDTOResults:

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
        'message': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, id=None, message=None, status=None):
        r"""UpdatePermissionExpireTimeResultDTOResults

        The model defined in huaweicloud sdk

        :param id: 权限id
        :type id: str
        :param message: 更新有效期结果信息
        :type message: str
        :param status: 更新结果状态。1成功 0失败
        :type status: int
        """
        
        

        self._id = None
        self._message = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this UpdatePermissionExpireTimeResultDTOResults.

        权限id

        :return: The id of this UpdatePermissionExpireTimeResultDTOResults.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdatePermissionExpireTimeResultDTOResults.

        权限id

        :param id: The id of this UpdatePermissionExpireTimeResultDTOResults.
        :type id: str
        """
        self._id = id

    @property
    def message(self):
        r"""Gets the message of this UpdatePermissionExpireTimeResultDTOResults.

        更新有效期结果信息

        :return: The message of this UpdatePermissionExpireTimeResultDTOResults.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this UpdatePermissionExpireTimeResultDTOResults.

        更新有效期结果信息

        :param message: The message of this UpdatePermissionExpireTimeResultDTOResults.
        :type message: str
        """
        self._message = message

    @property
    def status(self):
        r"""Gets the status of this UpdatePermissionExpireTimeResultDTOResults.

        更新结果状态。1成功 0失败

        :return: The status of this UpdatePermissionExpireTimeResultDTOResults.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdatePermissionExpireTimeResultDTOResults.

        更新结果状态。1成功 0失败

        :param status: The status of this UpdatePermissionExpireTimeResultDTOResults.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, UpdatePermissionExpireTimeResultDTOResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
