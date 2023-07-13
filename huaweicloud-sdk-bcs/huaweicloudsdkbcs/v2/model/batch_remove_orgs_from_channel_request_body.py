# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchRemoveOrgsFromChannelRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_names': 'list[str]'
    }

    attribute_map = {
        'org_names': 'org_names'
    }

    def __init__(self, org_names=None):
        """BatchRemoveOrgsFromChannelRequestBody

        The model defined in huaweicloud sdk

        :param org_names: 组织名称列表
        :type org_names: list[str]
        """
        
        

        self._org_names = None
        self.discriminator = None

        self.org_names = org_names

    @property
    def org_names(self):
        """Gets the org_names of this BatchRemoveOrgsFromChannelRequestBody.

        组织名称列表

        :return: The org_names of this BatchRemoveOrgsFromChannelRequestBody.
        :rtype: list[str]
        """
        return self._org_names

    @org_names.setter
    def org_names(self, org_names):
        """Sets the org_names of this BatchRemoveOrgsFromChannelRequestBody.

        组织名称列表

        :param org_names: The org_names of this BatchRemoveOrgsFromChannelRequestBody.
        :type org_names: list[str]
        """
        self._org_names = org_names

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
        if not isinstance(other, BatchRemoveOrgsFromChannelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
