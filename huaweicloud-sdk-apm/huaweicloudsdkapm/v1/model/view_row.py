# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ViewRow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'view_list': 'list[ViewBase]',
        'title': 'str'
    }

    attribute_map = {
        'view_list': 'view_list',
        'title': 'title'
    }

    def __init__(self, view_list=None, title=None):
        r"""ViewRow

        The model defined in huaweicloud sdk

        :param view_list: 视图行，包含多个视图，展示的时候根据实际的长度适配。
        :type view_list: list[:class:`huaweicloudsdkapm.v1.ViewBase`]
        :param title: 标题。
        :type title: str
        """
        
        

        self._view_list = None
        self._title = None
        self.discriminator = None

        if view_list is not None:
            self.view_list = view_list
        if title is not None:
            self.title = title

    @property
    def view_list(self):
        r"""Gets the view_list of this ViewRow.

        视图行，包含多个视图，展示的时候根据实际的长度适配。

        :return: The view_list of this ViewRow.
        :rtype: list[:class:`huaweicloudsdkapm.v1.ViewBase`]
        """
        return self._view_list

    @view_list.setter
    def view_list(self, view_list):
        r"""Sets the view_list of this ViewRow.

        视图行，包含多个视图，展示的时候根据实际的长度适配。

        :param view_list: The view_list of this ViewRow.
        :type view_list: list[:class:`huaweicloudsdkapm.v1.ViewBase`]
        """
        self._view_list = view_list

    @property
    def title(self):
        r"""Gets the title of this ViewRow.

        标题。

        :return: The title of this ViewRow.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ViewRow.

        标题。

        :param title: The title of this ViewRow.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, ViewRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
