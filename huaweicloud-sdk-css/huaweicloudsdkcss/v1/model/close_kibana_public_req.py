# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloseKibanaPublicReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_size': 'int',
        'elb_white_list': 'StartKibanaPublicReqElbWhitelist'
    }

    attribute_map = {
        'eip_size': 'eip_size',
        'elb_white_list': 'elb_white_list'
    }

    def __init__(self, eip_size=None, elb_white_list=None):
        r"""CloseKibanaPublicReq

        The model defined in huaweicloud sdk

        :param eip_size: 带宽。单位：Mbit/s
        :type eip_size: int
        :param elb_white_list: 
        :type elb_white_list: :class:`huaweicloudsdkcss.v1.StartKibanaPublicReqElbWhitelist`
        """
        
        

        self._eip_size = None
        self._elb_white_list = None
        self.discriminator = None

        if eip_size is not None:
            self.eip_size = eip_size
        if elb_white_list is not None:
            self.elb_white_list = elb_white_list

    @property
    def eip_size(self):
        r"""Gets the eip_size of this CloseKibanaPublicReq.

        带宽。单位：Mbit/s

        :return: The eip_size of this CloseKibanaPublicReq.
        :rtype: int
        """
        return self._eip_size

    @eip_size.setter
    def eip_size(self, eip_size):
        r"""Sets the eip_size of this CloseKibanaPublicReq.

        带宽。单位：Mbit/s

        :param eip_size: The eip_size of this CloseKibanaPublicReq.
        :type eip_size: int
        """
        self._eip_size = eip_size

    @property
    def elb_white_list(self):
        r"""Gets the elb_white_list of this CloseKibanaPublicReq.

        :return: The elb_white_list of this CloseKibanaPublicReq.
        :rtype: :class:`huaweicloudsdkcss.v1.StartKibanaPublicReqElbWhitelist`
        """
        return self._elb_white_list

    @elb_white_list.setter
    def elb_white_list(self, elb_white_list):
        r"""Sets the elb_white_list of this CloseKibanaPublicReq.

        :param elb_white_list: The elb_white_list of this CloseKibanaPublicReq.
        :type elb_white_list: :class:`huaweicloudsdkcss.v1.StartKibanaPublicReqElbWhitelist`
        """
        self._elb_white_list = elb_white_list

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
        if not isinstance(other, CloseKibanaPublicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
