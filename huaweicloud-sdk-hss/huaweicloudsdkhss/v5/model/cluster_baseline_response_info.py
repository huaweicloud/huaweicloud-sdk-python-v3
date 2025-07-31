# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterBaselineResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline_desc': 'str',
        'baseline_index': 'str',
        'baseline_type': 'str'
    }

    attribute_map = {
        'baseline_desc': 'baseline_desc',
        'baseline_index': 'baseline_index',
        'baseline_type': 'baseline_type'
    }

    def __init__(self, baseline_desc=None, baseline_index=None, baseline_type=None):
        r"""ClusterBaselineResponseInfo

        The model defined in huaweicloud sdk

        :param baseline_desc: 检查项描述
        :type baseline_desc: str
        :param baseline_index: 检查项ID
        :type baseline_index: str
        :param baseline_type: 检查项类型
        :type baseline_type: str
        """
        
        

        self._baseline_desc = None
        self._baseline_index = None
        self._baseline_type = None
        self.discriminator = None

        if baseline_desc is not None:
            self.baseline_desc = baseline_desc
        if baseline_index is not None:
            self.baseline_index = baseline_index
        if baseline_type is not None:
            self.baseline_type = baseline_type

    @property
    def baseline_desc(self):
        r"""Gets the baseline_desc of this ClusterBaselineResponseInfo.

        检查项描述

        :return: The baseline_desc of this ClusterBaselineResponseInfo.
        :rtype: str
        """
        return self._baseline_desc

    @baseline_desc.setter
    def baseline_desc(self, baseline_desc):
        r"""Sets the baseline_desc of this ClusterBaselineResponseInfo.

        检查项描述

        :param baseline_desc: The baseline_desc of this ClusterBaselineResponseInfo.
        :type baseline_desc: str
        """
        self._baseline_desc = baseline_desc

    @property
    def baseline_index(self):
        r"""Gets the baseline_index of this ClusterBaselineResponseInfo.

        检查项ID

        :return: The baseline_index of this ClusterBaselineResponseInfo.
        :rtype: str
        """
        return self._baseline_index

    @baseline_index.setter
    def baseline_index(self, baseline_index):
        r"""Sets the baseline_index of this ClusterBaselineResponseInfo.

        检查项ID

        :param baseline_index: The baseline_index of this ClusterBaselineResponseInfo.
        :type baseline_index: str
        """
        self._baseline_index = baseline_index

    @property
    def baseline_type(self):
        r"""Gets the baseline_type of this ClusterBaselineResponseInfo.

        检查项类型

        :return: The baseline_type of this ClusterBaselineResponseInfo.
        :rtype: str
        """
        return self._baseline_type

    @baseline_type.setter
    def baseline_type(self, baseline_type):
        r"""Sets the baseline_type of this ClusterBaselineResponseInfo.

        检查项类型

        :param baseline_type: The baseline_type of this ClusterBaselineResponseInfo.
        :type baseline_type: str
        """
        self._baseline_type = baseline_type

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
        if not isinstance(other, ClusterBaselineResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
