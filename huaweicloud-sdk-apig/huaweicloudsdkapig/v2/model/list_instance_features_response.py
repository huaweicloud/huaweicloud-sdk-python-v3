# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceFeaturesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'total': 'int',
        'features': 'list[str]'
    }

    attribute_map = {
        'size': 'size',
        'total': 'total',
        'features': 'features'
    }

    def __init__(self, size=None, total=None, features=None):
        r"""ListInstanceFeaturesResponse

        The model defined in huaweicloud sdk

        :param size: 本次返回的列表长度
        :type size: int
        :param total: 满足条件的记录数
        :type total: int
        :param features: 实例支持的特性列表： - \&quot;resize_huge_flavor\&quot; - \&quot;health_check_in_instance_etcd\&quot; - \&quot;shubao_support_add_node\&quot; - \&quot;upgrade_uninterrupted\&quot; - \&quot;sm_cipher_type\&quot;  与实例版本有关，列表中不展示的特性为实例不支持的特性
        :type features: list[str]
        """
        
        super(ListInstanceFeaturesResponse, self).__init__()

        self._size = None
        self._total = None
        self._features = None
        self.discriminator = None

        self.size = size
        self.total = total
        if features is not None:
            self.features = features

    @property
    def size(self):
        r"""Gets the size of this ListInstanceFeaturesResponse.

        本次返回的列表长度

        :return: The size of this ListInstanceFeaturesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListInstanceFeaturesResponse.

        本次返回的列表长度

        :param size: The size of this ListInstanceFeaturesResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListInstanceFeaturesResponse.

        满足条件的记录数

        :return: The total of this ListInstanceFeaturesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceFeaturesResponse.

        满足条件的记录数

        :param total: The total of this ListInstanceFeaturesResponse.
        :type total: int
        """
        self._total = total

    @property
    def features(self):
        r"""Gets the features of this ListInstanceFeaturesResponse.

        实例支持的特性列表： - \"resize_huge_flavor\" - \"health_check_in_instance_etcd\" - \"shubao_support_add_node\" - \"upgrade_uninterrupted\" - \"sm_cipher_type\"  与实例版本有关，列表中不展示的特性为实例不支持的特性

        :return: The features of this ListInstanceFeaturesResponse.
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ListInstanceFeaturesResponse.

        实例支持的特性列表： - \"resize_huge_flavor\" - \"health_check_in_instance_etcd\" - \"shubao_support_add_node\" - \"upgrade_uninterrupted\" - \"sm_cipher_type\"  与实例版本有关，列表中不展示的特性为实例不支持的特性

        :param features: The features of this ListInstanceFeaturesResponse.
        :type features: list[str]
        """
        self._features = features

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
        if not isinstance(other, ListInstanceFeaturesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
