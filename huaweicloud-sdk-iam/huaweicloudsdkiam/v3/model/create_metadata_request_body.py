# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMetadataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'xaccount_type': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'xaccount_type': 'xaccount_type',
        'metadata': 'metadata'
    }

    def __init__(self, domain_id=None, xaccount_type=None, metadata=None):
        """CreateMetadataRequestBody

        The model defined in huaweicloud sdk

        :param domain_id: 用户所属账号ID。
        :type domain_id: str
        :param xaccount_type: 该字段为标识租户来源字段，默认为空。
        :type xaccount_type: str
        :param metadata: 该字段为用户IdP服务器的Metadata文件的内容。
        :type metadata: str
        """
        
        

        self._domain_id = None
        self._xaccount_type = None
        self._metadata = None
        self.discriminator = None

        self.domain_id = domain_id
        self.xaccount_type = xaccount_type
        self.metadata = metadata

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateMetadataRequestBody.

        用户所属账号ID。

        :return: The domain_id of this CreateMetadataRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateMetadataRequestBody.

        用户所属账号ID。

        :param domain_id: The domain_id of this CreateMetadataRequestBody.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def xaccount_type(self):
        """Gets the xaccount_type of this CreateMetadataRequestBody.

        该字段为标识租户来源字段，默认为空。

        :return: The xaccount_type of this CreateMetadataRequestBody.
        :rtype: str
        """
        return self._xaccount_type

    @xaccount_type.setter
    def xaccount_type(self, xaccount_type):
        """Sets the xaccount_type of this CreateMetadataRequestBody.

        该字段为标识租户来源字段，默认为空。

        :param xaccount_type: The xaccount_type of this CreateMetadataRequestBody.
        :type xaccount_type: str
        """
        self._xaccount_type = xaccount_type

    @property
    def metadata(self):
        """Gets the metadata of this CreateMetadataRequestBody.

        该字段为用户IdP服务器的Metadata文件的内容。

        :return: The metadata of this CreateMetadataRequestBody.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CreateMetadataRequestBody.

        该字段为用户IdP服务器的Metadata文件的内容。

        :param metadata: The metadata of this CreateMetadataRequestBody.
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
        if not isinstance(other, CreateMetadataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
