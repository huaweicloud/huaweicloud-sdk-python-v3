# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchPublicipResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status_code': 'int',
        'publicip': 'PublicipResp'
    }

    attribute_map = {
        'status_code': 'statusCode',
        'publicip': 'publicip'
    }

    def __init__(self, status_code=None, publicip=None):
        """BatchPublicipResp

        The model defined in huaweicloud sdk

        :param status_code: 响应码
        :type status_code: int
        :param publicip: 
        :type publicip: :class:`huaweicloudsdkeip.v3.PublicipResp`
        """
        
        

        self._status_code = None
        self._publicip = None
        self.discriminator = None

        self.status_code = status_code
        self.publicip = publicip

    @property
    def status_code(self):
        """Gets the status_code of this BatchPublicipResp.

        响应码

        :return: The status_code of this BatchPublicipResp.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this BatchPublicipResp.

        响应码

        :param status_code: The status_code of this BatchPublicipResp.
        :type status_code: int
        """
        self._status_code = status_code

    @property
    def publicip(self):
        """Gets the publicip of this BatchPublicipResp.

        :return: The publicip of this BatchPublicipResp.
        :rtype: :class:`huaweicloudsdkeip.v3.PublicipResp`
        """
        return self._publicip

    @publicip.setter
    def publicip(self, publicip):
        """Sets the publicip of this BatchPublicipResp.

        :param publicip: The publicip of this BatchPublicipResp.
        :type publicip: :class:`huaweicloudsdkeip.v3.PublicipResp`
        """
        self._publicip = publicip

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
        if not isinstance(other, BatchPublicipResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
