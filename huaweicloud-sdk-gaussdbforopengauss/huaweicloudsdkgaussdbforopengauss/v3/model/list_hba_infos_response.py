# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHbaInfosResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hba_confs': 'list[HbaConfResult]',
        'total_count': 'int'
    }

    attribute_map = {
        'hba_confs': 'hba_confs',
        'total_count': 'total_count'
    }

    def __init__(self, hba_confs=None, total_count=None):
        r"""ListHbaInfosResponse

        The model defined in huaweicloud sdk

        :param hba_confs: **参数解释**: 客户端接入配置列表。
        :type hba_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        :param total_count: **参数解释**: hba配置总数。 **取值范围**: [0, 2^31-1]，取决于实际查询大小。
        :type total_count: int
        """
        
        super(ListHbaInfosResponse, self).__init__()

        self._hba_confs = None
        self._total_count = None
        self.discriminator = None

        if hba_confs is not None:
            self.hba_confs = hba_confs
        if total_count is not None:
            self.total_count = total_count

    @property
    def hba_confs(self):
        r"""Gets the hba_confs of this ListHbaInfosResponse.

        **参数解释**: 客户端接入配置列表。

        :return: The hba_confs of this ListHbaInfosResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        """
        return self._hba_confs

    @hba_confs.setter
    def hba_confs(self, hba_confs):
        r"""Sets the hba_confs of this ListHbaInfosResponse.

        **参数解释**: 客户端接入配置列表。

        :param hba_confs: The hba_confs of this ListHbaInfosResponse.
        :type hba_confs: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.HbaConfResult`]
        """
        self._hba_confs = hba_confs

    @property
    def total_count(self):
        r"""Gets the total_count of this ListHbaInfosResponse.

        **参数解释**: hba配置总数。 **取值范围**: [0, 2^31-1]，取决于实际查询大小。

        :return: The total_count of this ListHbaInfosResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListHbaInfosResponse.

        **参数解释**: hba配置总数。 **取值范围**: [0, 2^31-1]，取决于实际查询大小。

        :param total_count: The total_count of this ListHbaInfosResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListHbaInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
