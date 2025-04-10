# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptsResponse(SdkResponse):

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
        'scripts': 'list[ScriptSimpleInfo]'
    }

    attribute_map = {
        'count': 'count',
        'scripts': 'scripts'
    }

    def __init__(self, count=None, scripts=None):
        r"""ListScriptsResponse

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param scripts: 脚本列表。
        :type scripts: list[:class:`huaweicloudsdkworkspace.v2.ScriptSimpleInfo`]
        """
        
        super(ListScriptsResponse, self).__init__()

        self._count = None
        self._scripts = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if scripts is not None:
            self.scripts = scripts

    @property
    def count(self):
        r"""Gets the count of this ListScriptsResponse.

        总数。

        :return: The count of this ListScriptsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListScriptsResponse.

        总数。

        :param count: The count of this ListScriptsResponse.
        :type count: int
        """
        self._count = count

    @property
    def scripts(self):
        r"""Gets the scripts of this ListScriptsResponse.

        脚本列表。

        :return: The scripts of this ListScriptsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScriptSimpleInfo`]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        r"""Sets the scripts of this ListScriptsResponse.

        脚本列表。

        :param scripts: The scripts of this ListScriptsResponse.
        :type scripts: list[:class:`huaweicloudsdkworkspace.v2.ScriptSimpleInfo`]
        """
        self._scripts = scripts

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
        if not isinstance(other, ListScriptsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
