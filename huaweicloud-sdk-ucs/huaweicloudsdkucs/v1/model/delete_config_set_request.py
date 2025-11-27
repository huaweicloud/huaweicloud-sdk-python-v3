# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteConfigSetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configsetid': 'str'
    }

    attribute_map = {
        'configsetid': 'configsetid'
    }

    def __init__(self, configsetid=None):
        r"""DeleteConfigSetRequest

        The model defined in huaweicloud sdk

        :param configsetid: 配置集合id
        :type configsetid: str
        """
        
        

        self._configsetid = None
        self.discriminator = None

        self.configsetid = configsetid

    @property
    def configsetid(self):
        r"""Gets the configsetid of this DeleteConfigSetRequest.

        配置集合id

        :return: The configsetid of this DeleteConfigSetRequest.
        :rtype: str
        """
        return self._configsetid

    @configsetid.setter
    def configsetid(self, configsetid):
        r"""Sets the configsetid of this DeleteConfigSetRequest.

        配置集合id

        :param configsetid: The configsetid of this DeleteConfigSetRequest.
        :type configsetid: str
        """
        self._configsetid = configsetid

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
        if not isinstance(other, DeleteConfigSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
