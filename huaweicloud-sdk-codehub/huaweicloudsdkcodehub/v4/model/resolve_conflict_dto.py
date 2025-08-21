# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResolveConflictDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'commit_message': 'str',
        'files': 'list[ResolveConflictFileDto]'
    }

    attribute_map = {
        'commit_message': 'commit_message',
        'files': 'files'
    }

    def __init__(self, commit_message=None, files=None):
        r"""ResolveConflictDto

        The model defined in huaweicloud sdk

        :param commit_message: **参数解释：** 提交信息
        :type commit_message: str
        :param files: **参数解释：** 冲突的文件      
        :type files: list[:class:`huaweicloudsdkcodehub.v4.ResolveConflictFileDto`]
        """
        
        

        self._commit_message = None
        self._files = None
        self.discriminator = None

        self.commit_message = commit_message
        self.files = files

    @property
    def commit_message(self):
        r"""Gets the commit_message of this ResolveConflictDto.

        **参数解释：** 提交信息

        :return: The commit_message of this ResolveConflictDto.
        :rtype: str
        """
        return self._commit_message

    @commit_message.setter
    def commit_message(self, commit_message):
        r"""Sets the commit_message of this ResolveConflictDto.

        **参数解释：** 提交信息

        :param commit_message: The commit_message of this ResolveConflictDto.
        :type commit_message: str
        """
        self._commit_message = commit_message

    @property
    def files(self):
        r"""Gets the files of this ResolveConflictDto.

        **参数解释：** 冲突的文件      

        :return: The files of this ResolveConflictDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ResolveConflictFileDto`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this ResolveConflictDto.

        **参数解释：** 冲突的文件      

        :param files: The files of this ResolveConflictDto.
        :type files: list[:class:`huaweicloudsdkcodehub.v4.ResolveConflictFileDto`]
        """
        self._files = files

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
        if not isinstance(other, ResolveConflictDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
