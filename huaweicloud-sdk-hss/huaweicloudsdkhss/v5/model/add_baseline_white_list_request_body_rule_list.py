# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddBaselineWhiteListRequestBodyRuleList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index_version': 'str',
        'check_type': 'str',
        'standard': 'str'
    }

    attribute_map = {
        'index_version': 'index_version',
        'check_type': 'check_type',
        'standard': 'standard'
    }

    def __init__(self, index_version=None, check_type=None, standard=None):
        r"""AddBaselineWhiteListRequestBodyRuleList

        The model defined in huaweicloud sdk

        :param index_version: 基线检查的检查项标识
        :type index_version: str
        :param check_type: 基线检查的基线名称
        :type check_type: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准
        :type standard: str
        """
        
        

        self._index_version = None
        self._check_type = None
        self._standard = None
        self.discriminator = None

        if index_version is not None:
            self.index_version = index_version
        if check_type is not None:
            self.check_type = check_type
        if standard is not None:
            self.standard = standard

    @property
    def index_version(self):
        r"""Gets the index_version of this AddBaselineWhiteListRequestBodyRuleList.

        基线检查的检查项标识

        :return: The index_version of this AddBaselineWhiteListRequestBodyRuleList.
        :rtype: str
        """
        return self._index_version

    @index_version.setter
    def index_version(self, index_version):
        r"""Sets the index_version of this AddBaselineWhiteListRequestBodyRuleList.

        基线检查的检查项标识

        :param index_version: The index_version of this AddBaselineWhiteListRequestBodyRuleList.
        :type index_version: str
        """
        self._index_version = index_version

    @property
    def check_type(self):
        r"""Gets the check_type of this AddBaselineWhiteListRequestBodyRuleList.

        基线检查的基线名称

        :return: The check_type of this AddBaselineWhiteListRequestBodyRuleList.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this AddBaselineWhiteListRequestBodyRuleList.

        基线检查的基线名称

        :param check_type: The check_type of this AddBaselineWhiteListRequestBodyRuleList.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this AddBaselineWhiteListRequestBodyRuleList.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准

        :return: The standard of this AddBaselineWhiteListRequestBodyRuleList.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this AddBaselineWhiteListRequestBodyRuleList.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准

        :param standard: The standard of this AddBaselineWhiteListRequestBodyRuleList.
        :type standard: str
        """
        self._standard = standard

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
        if not isinstance(other, AddBaselineWhiteListRequestBodyRuleList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
