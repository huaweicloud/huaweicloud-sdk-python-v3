# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnterpriseProjectConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_ep_support': 'str'
    }

    attribute_map = {
        'delete_ep_support': 'delete_ep_support'
    }

    def __init__(self, delete_ep_support=None):
        r"""EnterpriseProjectConfig

        The model defined in huaweicloud sdk

        :param delete_ep_support: 是否支持企业项目删除
        :type delete_ep_support: str
        """
        
        

        self._delete_ep_support = None
        self.discriminator = None

        if delete_ep_support is not None:
            self.delete_ep_support = delete_ep_support

    @property
    def delete_ep_support(self):
        r"""Gets the delete_ep_support of this EnterpriseProjectConfig.

        是否支持企业项目删除

        :return: The delete_ep_support of this EnterpriseProjectConfig.
        :rtype: str
        """
        return self._delete_ep_support

    @delete_ep_support.setter
    def delete_ep_support(self, delete_ep_support):
        r"""Sets the delete_ep_support of this EnterpriseProjectConfig.

        是否支持企业项目删除

        :param delete_ep_support: The delete_ep_support of this EnterpriseProjectConfig.
        :type delete_ep_support: str
        """
        self._delete_ep_support = delete_ep_support

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
        if not isinstance(other, EnterpriseProjectConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
