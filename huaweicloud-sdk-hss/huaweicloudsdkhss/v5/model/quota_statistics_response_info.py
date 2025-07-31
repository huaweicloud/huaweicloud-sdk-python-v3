# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaStatisticsResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'total_num': 'int'
    }

    attribute_map = {
        'version': 'version',
        'total_num': 'total_num'
    }

    def __init__(self, version=None, total_num=None):
        r"""QuotaStatisticsResponseInfo

        The model defined in huaweicloud sdk

        :param version: **参数解释**： 资源规格编码 **取值范围**： 包含如下6种。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。
        :type version: str
        :param total_num: **参数解释**： 配额总数 **取值范围**： 0到10000000 
        :type total_num: int
        """
        
        

        self._version = None
        self._total_num = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if total_num is not None:
            self.total_num = total_num

    @property
    def version(self):
        r"""Gets the version of this QuotaStatisticsResponseInfo.

        **参数解释**： 资源规格编码 **取值范围**： 包含如下6种。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。

        :return: The version of this QuotaStatisticsResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this QuotaStatisticsResponseInfo.

        **参数解释**： 资源规格编码 **取值范围**： 包含如下6种。 - hss.version.basic ：基础版。 - hss.version.advanced ：专业版。 - hss.version.enterprise ：企业版。 - hss.version.premium ：旗舰版。 - hss.version.wtp ：网页防篡改版。 - hss.version.container.enterprise：容器版。

        :param version: The version of this QuotaStatisticsResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def total_num(self):
        r"""Gets the total_num of this QuotaStatisticsResponseInfo.

        **参数解释**： 配额总数 **取值范围**： 0到10000000 

        :return: The total_num of this QuotaStatisticsResponseInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this QuotaStatisticsResponseInfo.

        **参数解释**： 配额总数 **取值范围**： 0到10000000 

        :param total_num: The total_num of this QuotaStatisticsResponseInfo.
        :type total_num: int
        """
        self._total_num = total_num

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
        if not isinstance(other, QuotaStatisticsResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
