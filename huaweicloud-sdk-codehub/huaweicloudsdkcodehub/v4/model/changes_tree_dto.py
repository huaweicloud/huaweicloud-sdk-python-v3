# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangesTreeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_show_my_approval_files': 'bool',
        'tree': 'list[ChangesTreeObjectDto]'
    }

    attribute_map = {
        'can_show_my_approval_files': 'can_show_my_approval_files',
        'tree': 'tree'
    }

    def __init__(self, can_show_my_approval_files=None, tree=None):
        r"""ChangesTreeDto

        The model defined in huaweicloud sdk

        :param can_show_my_approval_files: **参数解释：** 展示审核文件。
        :type can_show_my_approval_files: bool
        :param tree: **参数解释：** 变更树。
        :type tree: list[:class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDto`]
        """
        
        

        self._can_show_my_approval_files = None
        self._tree = None
        self.discriminator = None

        if can_show_my_approval_files is not None:
            self.can_show_my_approval_files = can_show_my_approval_files
        if tree is not None:
            self.tree = tree

    @property
    def can_show_my_approval_files(self):
        r"""Gets the can_show_my_approval_files of this ChangesTreeDto.

        **参数解释：** 展示审核文件。

        :return: The can_show_my_approval_files of this ChangesTreeDto.
        :rtype: bool
        """
        return self._can_show_my_approval_files

    @can_show_my_approval_files.setter
    def can_show_my_approval_files(self, can_show_my_approval_files):
        r"""Sets the can_show_my_approval_files of this ChangesTreeDto.

        **参数解释：** 展示审核文件。

        :param can_show_my_approval_files: The can_show_my_approval_files of this ChangesTreeDto.
        :type can_show_my_approval_files: bool
        """
        self._can_show_my_approval_files = can_show_my_approval_files

    @property
    def tree(self):
        r"""Gets the tree of this ChangesTreeDto.

        **参数解释：** 变更树。

        :return: The tree of this ChangesTreeDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDto`]
        """
        return self._tree

    @tree.setter
    def tree(self, tree):
        r"""Sets the tree of this ChangesTreeDto.

        **参数解释：** 变更树。

        :param tree: The tree of this ChangesTreeDto.
        :type tree: list[:class:`huaweicloudsdkcodehub.v4.ChangesTreeObjectDto`]
        """
        self._tree = tree

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
        if not isinstance(other, ChangesTreeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
