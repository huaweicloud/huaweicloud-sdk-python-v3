# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudStorageOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_storage_rule': 'str'
    }

    attribute_map = {
        'cloud_storage_rule': 'cloud_storage_rule'
    }

    def __init__(self, cloud_storage_rule=None):
        r"""CloudStorageOptions

        The model defined in huaweicloud sdk

        :param cloud_storage_rule: 配置项内容。
        :type cloud_storage_rule: str
        """
        
        

        self._cloud_storage_rule = None
        self.discriminator = None

        if cloud_storage_rule is not None:
            self.cloud_storage_rule = cloud_storage_rule

    @property
    def cloud_storage_rule(self):
        r"""Gets the cloud_storage_rule of this CloudStorageOptions.

        配置项内容。

        :return: The cloud_storage_rule of this CloudStorageOptions.
        :rtype: str
        """
        return self._cloud_storage_rule

    @cloud_storage_rule.setter
    def cloud_storage_rule(self, cloud_storage_rule):
        r"""Sets the cloud_storage_rule of this CloudStorageOptions.

        配置项内容。

        :param cloud_storage_rule: The cloud_storage_rule of this CloudStorageOptions.
        :type cloud_storage_rule: str
        """
        self._cloud_storage_rule = cloud_storage_rule

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
        if not isinstance(other, CloudStorageOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
