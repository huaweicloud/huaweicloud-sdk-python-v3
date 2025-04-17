# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryScriptsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'scripts': 'list[ScriptInfo]'
    }

    attribute_map = {
        'total': 'total',
        'scripts': 'scripts'
    }

    def __init__(self, total=None, scripts=None):
        r"""ListFactoryScriptsResponse

        The model defined in huaweicloud sdk

        :param total: 总的脚本个数
        :type total: int
        :param scripts: 脚本列表
        :type scripts: list[:class:`huaweicloudsdkdataartsstudio.v1.ScriptInfo`]
        """
        
        super(ListFactoryScriptsResponse, self).__init__()

        self._total = None
        self._scripts = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if scripts is not None:
            self.scripts = scripts

    @property
    def total(self):
        r"""Gets the total of this ListFactoryScriptsResponse.

        总的脚本个数

        :return: The total of this ListFactoryScriptsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFactoryScriptsResponse.

        总的脚本个数

        :param total: The total of this ListFactoryScriptsResponse.
        :type total: int
        """
        self._total = total

    @property
    def scripts(self):
        r"""Gets the scripts of this ListFactoryScriptsResponse.

        脚本列表

        :return: The scripts of this ListFactoryScriptsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ScriptInfo`]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        r"""Sets the scripts of this ListFactoryScriptsResponse.

        脚本列表

        :param scripts: The scripts of this ListFactoryScriptsResponse.
        :type scripts: list[:class:`huaweicloudsdkdataartsstudio.v1.ScriptInfo`]
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
        if not isinstance(other, ListFactoryScriptsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
