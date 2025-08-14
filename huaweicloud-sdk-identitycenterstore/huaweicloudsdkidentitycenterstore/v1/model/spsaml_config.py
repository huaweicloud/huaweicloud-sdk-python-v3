# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SPSAMLConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'acs_url': 'str',
        'issuer': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'acs_url': 'acs_url',
        'issuer': 'issuer',
        'metadata': 'metadata'
    }

    def __init__(self, acs_url=None, issuer=None, metadata=None):
        r"""SPSAMLConfig

        The model defined in huaweicloud sdk

        :param acs_url: 服务提供商断言响应地址
        :type acs_url: str
        :param issuer: 服务提供商签发者
        :type issuer: str
        :param metadata: 服务提供商元数据
        :type metadata: str
        """
        
        

        self._acs_url = None
        self._issuer = None
        self._metadata = None
        self.discriminator = None

        self.acs_url = acs_url
        self.issuer = issuer
        self.metadata = metadata

    @property
    def acs_url(self):
        r"""Gets the acs_url of this SPSAMLConfig.

        服务提供商断言响应地址

        :return: The acs_url of this SPSAMLConfig.
        :rtype: str
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        r"""Sets the acs_url of this SPSAMLConfig.

        服务提供商断言响应地址

        :param acs_url: The acs_url of this SPSAMLConfig.
        :type acs_url: str
        """
        self._acs_url = acs_url

    @property
    def issuer(self):
        r"""Gets the issuer of this SPSAMLConfig.

        服务提供商签发者

        :return: The issuer of this SPSAMLConfig.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        r"""Sets the issuer of this SPSAMLConfig.

        服务提供商签发者

        :param issuer: The issuer of this SPSAMLConfig.
        :type issuer: str
        """
        self._issuer = issuer

    @property
    def metadata(self):
        r"""Gets the metadata of this SPSAMLConfig.

        服务提供商元数据

        :return: The metadata of this SPSAMLConfig.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this SPSAMLConfig.

        服务提供商元数据

        :param metadata: The metadata of this SPSAMLConfig.
        :type metadata: str
        """
        self._metadata = metadata

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
        if not isinstance(other, SPSAMLConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
