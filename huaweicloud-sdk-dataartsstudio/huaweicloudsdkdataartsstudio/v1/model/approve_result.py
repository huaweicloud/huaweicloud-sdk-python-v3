# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApproveResult:

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
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, id=None, status=None, message=None):
        r"""ApproveResult

        The model defined in huaweicloud sdk

        :param id: 工单id
        :type id: str
        :param status: 审批结果,SUCCESS,FAIL
        :type status: str
        :param message: 错误信息
        :type message: str
        """
        
        

        self._id = None
        self._status = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this ApproveResult.

        工单id

        :return: The id of this ApproveResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ApproveResult.

        工单id

        :param id: The id of this ApproveResult.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ApproveResult.

        审批结果,SUCCESS,FAIL

        :return: The status of this ApproveResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApproveResult.

        审批结果,SUCCESS,FAIL

        :param status: The status of this ApproveResult.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ApproveResult.

        错误信息

        :return: The message of this ApproveResult.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ApproveResult.

        错误信息

        :param message: The message of this ApproveResult.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ApproveResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
