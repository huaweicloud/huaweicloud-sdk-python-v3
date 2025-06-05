# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserNotebookResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'notebooks': 'list[NotebookEntity]'
    }

    attribute_map = {
        'count': 'count',
        'notebooks': 'notebooks'
    }

    def __init__(self, count=None, notebooks=None):
        r"""ListUserNotebookResponse

        The model defined in huaweicloud sdk

        :param count: notebook总数
        :type count: int
        :param notebooks: notebook详情列表
        :type notebooks: list[:class:`huaweicloudsdkeihealth.v1.NotebookEntity`]
        """
        
        super(ListUserNotebookResponse, self).__init__()

        self._count = None
        self._notebooks = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if notebooks is not None:
            self.notebooks = notebooks

    @property
    def count(self):
        r"""Gets the count of this ListUserNotebookResponse.

        notebook总数

        :return: The count of this ListUserNotebookResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListUserNotebookResponse.

        notebook总数

        :param count: The count of this ListUserNotebookResponse.
        :type count: int
        """
        self._count = count

    @property
    def notebooks(self):
        r"""Gets the notebooks of this ListUserNotebookResponse.

        notebook详情列表

        :return: The notebooks of this ListUserNotebookResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NotebookEntity`]
        """
        return self._notebooks

    @notebooks.setter
    def notebooks(self, notebooks):
        r"""Sets the notebooks of this ListUserNotebookResponse.

        notebook详情列表

        :param notebooks: The notebooks of this ListUserNotebookResponse.
        :type notebooks: list[:class:`huaweicloudsdkeihealth.v1.NotebookEntity`]
        """
        self._notebooks = notebooks

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
        if not isinstance(other, ListUserNotebookResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
