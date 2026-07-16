# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IntranetConnectionDeleteRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'intranet_connection_ids': 'list[str]'
    }

    attribute_map = {
        'intranet_connection_ids': 'intranet_connection_ids'
    }

    def __init__(self, intranet_connection_ids=None):
        r"""IntranetConnectionDeleteRequest

        The model defined in huaweicloud sdk

        :param intranet_connection_ids: 内网接入的id列表
        :type intranet_connection_ids: list[str]
        """
        
        

        self._intranet_connection_ids = None
        self.discriminator = None

        self.intranet_connection_ids = intranet_connection_ids

    @property
    def intranet_connection_ids(self):
        r"""Gets the intranet_connection_ids of this IntranetConnectionDeleteRequest.

        内网接入的id列表

        :return: The intranet_connection_ids of this IntranetConnectionDeleteRequest.
        :rtype: list[str]
        """
        return self._intranet_connection_ids

    @intranet_connection_ids.setter
    def intranet_connection_ids(self, intranet_connection_ids):
        r"""Sets the intranet_connection_ids of this IntranetConnectionDeleteRequest.

        内网接入的id列表

        :param intranet_connection_ids: The intranet_connection_ids of this IntranetConnectionDeleteRequest.
        :type intranet_connection_ids: list[str]
        """
        self._intranet_connection_ids = intranet_connection_ids

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
        if not isinstance(other, IntranetConnectionDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
