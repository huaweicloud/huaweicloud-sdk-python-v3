# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDescriptionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description_info': 'str'
    }

    attribute_map = {
        'description_info': 'description_info'
    }

    def __init__(self, description_info=None):
        r"""ClusterDescriptionInfo

        The model defined in huaweicloud sdk

        :param description_info: **参数解释**: 集群描述信息。 **取值范围**: 不涉及。
        :type description_info: str
        """
        
        

        self._description_info = None
        self.discriminator = None

        self.description_info = description_info

    @property
    def description_info(self):
        r"""Gets the description_info of this ClusterDescriptionInfo.

        **参数解释**: 集群描述信息。 **取值范围**: 不涉及。

        :return: The description_info of this ClusterDescriptionInfo.
        :rtype: str
        """
        return self._description_info

    @description_info.setter
    def description_info(self, description_info):
        r"""Sets the description_info of this ClusterDescriptionInfo.

        **参数解释**: 集群描述信息。 **取值范围**: 不涉及。

        :param description_info: The description_info of this ClusterDescriptionInfo.
        :type description_info: str
        """
        self._description_info = description_info

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
        if not isinstance(other, ClusterDescriptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
