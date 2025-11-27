# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FederationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'versions_info': 'list[FederationVersionInfo]'
    }

    attribute_map = {
        'versions_info': 'versionsInfo'
    }

    def __init__(self, versions_info=None):
        r"""FederationConfig

        The model defined in huaweicloud sdk

        :param versions_info: 联邦版本信息列表
        :type versions_info: list[:class:`huaweicloudsdkucs.v1.FederationVersionInfo`]
        """
        
        

        self._versions_info = None
        self.discriminator = None

        if versions_info is not None:
            self.versions_info = versions_info

    @property
    def versions_info(self):
        r"""Gets the versions_info of this FederationConfig.

        联邦版本信息列表

        :return: The versions_info of this FederationConfig.
        :rtype: list[:class:`huaweicloudsdkucs.v1.FederationVersionInfo`]
        """
        return self._versions_info

    @versions_info.setter
    def versions_info(self, versions_info):
        r"""Sets the versions_info of this FederationConfig.

        联邦版本信息列表

        :param versions_info: The versions_info of this FederationConfig.
        :type versions_info: list[:class:`huaweicloudsdkucs.v1.FederationVersionInfo`]
        """
        self._versions_info = versions_info

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FederationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
