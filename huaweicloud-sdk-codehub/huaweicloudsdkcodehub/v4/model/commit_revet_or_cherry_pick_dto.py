# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitRevetOrCherryPickDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch': 'str',
        'with_new_merge_request': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'with_new_merge_request': 'with_new_merge_request',
        'message': 'message'
    }

    def __init__(self, branch=None, with_new_merge_request=None, message=None):
        r"""CommitRevetOrCherryPickDto

        The model defined in huaweicloud sdk

        :param branch: revert目标分支
        :type branch: str
        :param with_new_merge_request: 是否使用创建MR的形式Revert
        :type with_new_merge_request: bool
        :param message: 提交信息
        :type message: str
        """
        
        

        self._branch = None
        self._with_new_merge_request = None
        self._message = None
        self.discriminator = None

        self.branch = branch
        if with_new_merge_request is not None:
            self.with_new_merge_request = with_new_merge_request
        if message is not None:
            self.message = message

    @property
    def branch(self):
        r"""Gets the branch of this CommitRevetOrCherryPickDto.

        revert目标分支

        :return: The branch of this CommitRevetOrCherryPickDto.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this CommitRevetOrCherryPickDto.

        revert目标分支

        :param branch: The branch of this CommitRevetOrCherryPickDto.
        :type branch: str
        """
        self._branch = branch

    @property
    def with_new_merge_request(self):
        r"""Gets the with_new_merge_request of this CommitRevetOrCherryPickDto.

        是否使用创建MR的形式Revert

        :return: The with_new_merge_request of this CommitRevetOrCherryPickDto.
        :rtype: bool
        """
        return self._with_new_merge_request

    @with_new_merge_request.setter
    def with_new_merge_request(self, with_new_merge_request):
        r"""Sets the with_new_merge_request of this CommitRevetOrCherryPickDto.

        是否使用创建MR的形式Revert

        :param with_new_merge_request: The with_new_merge_request of this CommitRevetOrCherryPickDto.
        :type with_new_merge_request: bool
        """
        self._with_new_merge_request = with_new_merge_request

    @property
    def message(self):
        r"""Gets the message of this CommitRevetOrCherryPickDto.

        提交信息

        :return: The message of this CommitRevetOrCherryPickDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CommitRevetOrCherryPickDto.

        提交信息

        :param message: The message of this CommitRevetOrCherryPickDto.
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
        if not isinstance(other, CommitRevetOrCherryPickDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
