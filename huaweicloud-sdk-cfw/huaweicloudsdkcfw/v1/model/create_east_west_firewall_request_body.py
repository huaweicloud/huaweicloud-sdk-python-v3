# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEastWestFirewallRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'inspection_cidr': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'er_id': 'er_id',
        'inspection_cidr': 'inspection_cidr',
        'mode': 'mode'
    }

    def __init__(self, er_id=None, inspection_cidr=None, mode=None):
        """CreateEastWestFirewallRequestBody

        The model defined in huaweicloud sdk

        :param er_id: 出方向关联ER实例id
        :type er_id: str
        :param inspection_cidr: inspection cidr
        :type inspection_cidr: str
        :param mode: 东西向防火墙模式，填写er
        :type mode: str
        """
        
        

        self._er_id = None
        self._inspection_cidr = None
        self._mode = None
        self.discriminator = None

        if er_id is not None:
            self.er_id = er_id
        self.inspection_cidr = inspection_cidr
        self.mode = mode

    @property
    def er_id(self):
        """Gets the er_id of this CreateEastWestFirewallRequestBody.

        出方向关联ER实例id

        :return: The er_id of this CreateEastWestFirewallRequestBody.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this CreateEastWestFirewallRequestBody.

        出方向关联ER实例id

        :param er_id: The er_id of this CreateEastWestFirewallRequestBody.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def inspection_cidr(self):
        """Gets the inspection_cidr of this CreateEastWestFirewallRequestBody.

        inspection cidr

        :return: The inspection_cidr of this CreateEastWestFirewallRequestBody.
        :rtype: str
        """
        return self._inspection_cidr

    @inspection_cidr.setter
    def inspection_cidr(self, inspection_cidr):
        """Sets the inspection_cidr of this CreateEastWestFirewallRequestBody.

        inspection cidr

        :param inspection_cidr: The inspection_cidr of this CreateEastWestFirewallRequestBody.
        :type inspection_cidr: str
        """
        self._inspection_cidr = inspection_cidr

    @property
    def mode(self):
        """Gets the mode of this CreateEastWestFirewallRequestBody.

        东西向防火墙模式，填写er

        :return: The mode of this CreateEastWestFirewallRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateEastWestFirewallRequestBody.

        东西向防火墙模式，填写er

        :param mode: The mode of this CreateEastWestFirewallRequestBody.
        :type mode: str
        """
        self._mode = mode

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
        if not isinstance(other, CreateEastWestFirewallRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
