# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CnameStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'domain_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'domain_name': 'domain_name'
    }

    def __init__(self, status=None, domain_name=None):
        r"""CnameStatus

        The model defined in huaweicloud sdk

        :param status: 域名cname状态
        :type status: int
        :param domain_name: 加速域名
        :type domain_name: str
        """
        
        

        self._status = None
        self._domain_name = None
        self.discriminator = None

        self.status = status
        self.domain_name = domain_name

    @property
    def status(self):
        r"""Gets the status of this CnameStatus.

        域名cname状态

        :return: The status of this CnameStatus.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CnameStatus.

        域名cname状态

        :param status: The status of this CnameStatus.
        :type status: int
        """
        self._status = status

    @property
    def domain_name(self):
        r"""Gets the domain_name of this CnameStatus.

        加速域名

        :return: The domain_name of this CnameStatus.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this CnameStatus.

        加速域名

        :param domain_name: The domain_name of this CnameStatus.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, CnameStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
