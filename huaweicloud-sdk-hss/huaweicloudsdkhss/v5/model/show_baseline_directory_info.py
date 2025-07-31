# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineDirectoryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'standard': 'str',
        'data_list': 'list[ShowBaselineDirectoryInfoDataList]'
    }

    attribute_map = {
        'type': 'type',
        'standard': 'standard',
        'data_list': 'data_list'
    }

    def __init__(self, type=None, standard=None, data_list=None):
        r"""ShowBaselineDirectoryInfo

        The model defined in huaweicloud sdk

        :param type: 根据select_type不同的值，得到不同的含义 - 当select_type为check_type，该字段代表check_type（基线的名称） - 当select_type为tag，该字段代表tag（基线检查项的类型）
        :type type: str
        :param standard: 标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准
        :type standard: str
        :param data_list: 基线检查策略三级目录信息
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryInfoDataList`]
        """
        
        

        self._type = None
        self._standard = None
        self._data_list = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if standard is not None:
            self.standard = standard
        if data_list is not None:
            self.data_list = data_list

    @property
    def type(self):
        r"""Gets the type of this ShowBaselineDirectoryInfo.

        根据select_type不同的值，得到不同的含义 - 当select_type为check_type，该字段代表check_type（基线的名称） - 当select_type为tag，该字段代表tag（基线检查项的类型）

        :return: The type of this ShowBaselineDirectoryInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowBaselineDirectoryInfo.

        根据select_type不同的值，得到不同的含义 - 当select_type为check_type，该字段代表check_type（基线的名称） - 当select_type为tag，该字段代表tag（基线检查项的类型）

        :param type: The type of this ShowBaselineDirectoryInfo.
        :type type: str
        """
        self._type = type

    @property
    def standard(self):
        r"""Gets the standard of this ShowBaselineDirectoryInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准

        :return: The standard of this ShowBaselineDirectoryInfo.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ShowBaselineDirectoryInfo.

        标准类型，包含如下:   - cn_standard : 等保合规标准   - hw_standard : 云安全实践标准   - cis_standard : 通用安全标准

        :param standard: The standard of this ShowBaselineDirectoryInfo.
        :type standard: str
        """
        self._standard = standard

    @property
    def data_list(self):
        r"""Gets the data_list of this ShowBaselineDirectoryInfo.

        基线检查策略三级目录信息

        :return: The data_list of this ShowBaselineDirectoryInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryInfoDataList`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ShowBaselineDirectoryInfo.

        基线检查策略三级目录信息

        :param data_list: The data_list of this ShowBaselineDirectoryInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ShowBaselineDirectoryInfoDataList`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ShowBaselineDirectoryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
