# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityTarget:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_type': 'str',
        'target_ids': 'list[str]'
    }

    attribute_map = {
        'target_type': 'target_type',
        'target_ids': 'target_ids'
    }

    def __init__(self, target_type=None, target_ids=None):
        r"""SecurityTarget

        The model defined in huaweicloud sdk

        :param target_type: 安全态势感知配置绑定的对象，目前仅支持PRODUCT产品级别，仅对设备级别的安全态势感知项生效。
        :type target_type: str
        :param target_ids: 绑定对象id列表，target_type为PRODUCT时，由于产品ID在不同资源空间下可以重复，target_id格式为：资源空间ID:产品ID；资源空间ID与产品ID使用冒号拼接而成。
        :type target_ids: list[str]
        """
        
        

        self._target_type = None
        self._target_ids = None
        self.discriminator = None

        if target_type is not None:
            self.target_type = target_type
        if target_ids is not None:
            self.target_ids = target_ids

    @property
    def target_type(self):
        r"""Gets the target_type of this SecurityTarget.

        安全态势感知配置绑定的对象，目前仅支持PRODUCT产品级别，仅对设备级别的安全态势感知项生效。

        :return: The target_type of this SecurityTarget.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this SecurityTarget.

        安全态势感知配置绑定的对象，目前仅支持PRODUCT产品级别，仅对设备级别的安全态势感知项生效。

        :param target_type: The target_type of this SecurityTarget.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_ids(self):
        r"""Gets the target_ids of this SecurityTarget.

        绑定对象id列表，target_type为PRODUCT时，由于产品ID在不同资源空间下可以重复，target_id格式为：资源空间ID:产品ID；资源空间ID与产品ID使用冒号拼接而成。

        :return: The target_ids of this SecurityTarget.
        :rtype: list[str]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        r"""Sets the target_ids of this SecurityTarget.

        绑定对象id列表，target_type为PRODUCT时，由于产品ID在不同资源空间下可以重复，target_id格式为：资源空间ID:产品ID；资源空间ID与产品ID使用冒号拼接而成。

        :param target_ids: The target_ids of this SecurityTarget.
        :type target_ids: list[str]
        """
        self._target_ids = target_ids

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
        if not isinstance(other, SecurityTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
