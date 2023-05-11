# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceReqDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'meta_data': 'SvcMetadata',
        'spec': 'SvcSpec'
    }

    attribute_map = {
        'meta_data': 'meta_data',
        'spec': 'spec'
    }

    def __init__(self, meta_data=None, spec=None):
        """ServiceReqDetail

        The model defined in huaweicloud sdk

        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkief.v1.SvcMetadata`
        :param spec: 
        :type spec: :class:`huaweicloudsdkief.v1.SvcSpec`
        """
        
        

        self._meta_data = None
        self._spec = None
        self.discriminator = None

        self.meta_data = meta_data
        self.spec = spec

    @property
    def meta_data(self):
        """Gets the meta_data of this ServiceReqDetail.

        :return: The meta_data of this ServiceReqDetail.
        :rtype: :class:`huaweicloudsdkief.v1.SvcMetadata`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ServiceReqDetail.

        :param meta_data: The meta_data of this ServiceReqDetail.
        :type meta_data: :class:`huaweicloudsdkief.v1.SvcMetadata`
        """
        self._meta_data = meta_data

    @property
    def spec(self):
        """Gets the spec of this ServiceReqDetail.

        :return: The spec of this ServiceReqDetail.
        :rtype: :class:`huaweicloudsdkief.v1.SvcSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ServiceReqDetail.

        :param spec: The spec of this ServiceReqDetail.
        :type spec: :class:`huaweicloudsdkief.v1.SvcSpec`
        """
        self._spec = spec

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
        if not isinstance(other, ServiceReqDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
