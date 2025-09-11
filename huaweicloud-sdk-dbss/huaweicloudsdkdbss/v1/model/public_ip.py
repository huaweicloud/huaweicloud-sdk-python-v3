# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip': 'Eip',
        'id': 'str'
    }

    attribute_map = {
        'eip': 'eip',
        'id': 'id'
    }

    def __init__(self, eip=None, id=None):
        r"""PublicIp

        The model defined in huaweicloud sdk

        :param eip: 
        :type eip: :class:`huaweicloudsdkdbss.v1.Eip`
        :param id: IP地址ID
        :type id: str
        """
        
        

        self._eip = None
        self._id = None
        self.discriminator = None

        if eip is not None:
            self.eip = eip
        if id is not None:
            self.id = id

    @property
    def eip(self):
        r"""Gets the eip of this PublicIp.

        :return: The eip of this PublicIp.
        :rtype: :class:`huaweicloudsdkdbss.v1.Eip`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this PublicIp.

        :param eip: The eip of this PublicIp.
        :type eip: :class:`huaweicloudsdkdbss.v1.Eip`
        """
        self._eip = eip

    @property
    def id(self):
        r"""Gets the id of this PublicIp.

        IP地址ID

        :return: The id of this PublicIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublicIp.

        IP地址ID

        :param id: The id of this PublicIp.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, PublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
