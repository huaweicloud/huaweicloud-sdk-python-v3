# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailureForBatchCreateGroupMembersDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_id': 'str',
        'message': 'list[str]'
    }

    attribute_map = {
        'iam_id': 'iam_id',
        'message': 'message'
    }

    def __init__(self, iam_id=None, message=None):
        r"""FailureForBatchCreateGroupMembersDto

        The model defined in huaweicloud sdk

        :param iam_id: iam_id
        :type iam_id: str
        :param message: 失败原因
        :type message: list[str]
        """
        
        

        self._iam_id = None
        self._message = None
        self.discriminator = None

        if iam_id is not None:
            self.iam_id = iam_id
        if message is not None:
            self.message = message

    @property
    def iam_id(self):
        r"""Gets the iam_id of this FailureForBatchCreateGroupMembersDto.

        iam_id

        :return: The iam_id of this FailureForBatchCreateGroupMembersDto.
        :rtype: str
        """
        return self._iam_id

    @iam_id.setter
    def iam_id(self, iam_id):
        r"""Sets the iam_id of this FailureForBatchCreateGroupMembersDto.

        iam_id

        :param iam_id: The iam_id of this FailureForBatchCreateGroupMembersDto.
        :type iam_id: str
        """
        self._iam_id = iam_id

    @property
    def message(self):
        r"""Gets the message of this FailureForBatchCreateGroupMembersDto.

        失败原因

        :return: The message of this FailureForBatchCreateGroupMembersDto.
        :rtype: list[str]
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this FailureForBatchCreateGroupMembersDto.

        失败原因

        :param message: The message of this FailureForBatchCreateGroupMembersDto.
        :type message: list[str]
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
        if not isinstance(other, FailureForBatchCreateGroupMembersDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
