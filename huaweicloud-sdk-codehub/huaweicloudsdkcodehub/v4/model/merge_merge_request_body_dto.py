# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeMergeRequestBodyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'squash_commit_message': 'str',
        'squash': 'bool',
        'force_merge': 'bool'
    }

    attribute_map = {
        'squash_commit_message': 'squash_commit_message',
        'squash': 'squash',
        'force_merge': 'force_merge'
    }

    def __init__(self, squash_commit_message=None, squash=None, force_merge=None):
        r"""MergeMergeRequestBodyDto

        The model defined in huaweicloud sdk

        :param squash_commit_message: 压缩合并信息
        :type squash_commit_message: str
        :param squash: 压缩合并
        :type squash: bool
        :param force_merge: 强制合并
        :type force_merge: bool
        """
        
        

        self._squash_commit_message = None
        self._squash = None
        self._force_merge = None
        self.discriminator = None

        if squash_commit_message is not None:
            self.squash_commit_message = squash_commit_message
        if squash is not None:
            self.squash = squash
        if force_merge is not None:
            self.force_merge = force_merge

    @property
    def squash_commit_message(self):
        r"""Gets the squash_commit_message of this MergeMergeRequestBodyDto.

        压缩合并信息

        :return: The squash_commit_message of this MergeMergeRequestBodyDto.
        :rtype: str
        """
        return self._squash_commit_message

    @squash_commit_message.setter
    def squash_commit_message(self, squash_commit_message):
        r"""Sets the squash_commit_message of this MergeMergeRequestBodyDto.

        压缩合并信息

        :param squash_commit_message: The squash_commit_message of this MergeMergeRequestBodyDto.
        :type squash_commit_message: str
        """
        self._squash_commit_message = squash_commit_message

    @property
    def squash(self):
        r"""Gets the squash of this MergeMergeRequestBodyDto.

        压缩合并

        :return: The squash of this MergeMergeRequestBodyDto.
        :rtype: bool
        """
        return self._squash

    @squash.setter
    def squash(self, squash):
        r"""Sets the squash of this MergeMergeRequestBodyDto.

        压缩合并

        :param squash: The squash of this MergeMergeRequestBodyDto.
        :type squash: bool
        """
        self._squash = squash

    @property
    def force_merge(self):
        r"""Gets the force_merge of this MergeMergeRequestBodyDto.

        强制合并

        :return: The force_merge of this MergeMergeRequestBodyDto.
        :rtype: bool
        """
        return self._force_merge

    @force_merge.setter
    def force_merge(self, force_merge):
        r"""Sets the force_merge of this MergeMergeRequestBodyDto.

        强制合并

        :param force_merge: The force_merge of this MergeMergeRequestBodyDto.
        :type force_merge: bool
        """
        self._force_merge = force_merge

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
        if not isinstance(other, MergeMergeRequestBodyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
