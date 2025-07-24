# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'irack_num': 'int',
        'id': 'str',
        'region': 'str',
        'deccription': 'str'
    }

    attribute_map = {
        'name': 'name',
        'irack_num': 'irack_num',
        'id': 'id',
        'region': 'region',
        'deccription': 'deccription'
    }

    def __init__(self, name=None, irack_num=None, id=None, region=None, deccription=None):
        r"""IDc

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param irack_num: 
        :type irack_num: int
        :param id: 
        :type id: str
        :param region: 
        :type region: str
        :param deccription: 
        :type deccription: str
        """
        
        

        self._name = None
        self._irack_num = None
        self._id = None
        self._region = None
        self._deccription = None
        self.discriminator = None

        self.name = name
        self.irack_num = irack_num
        self.id = id
        if region is not None:
            self.region = region
        if deccription is not None:
            self.deccription = deccription

    @property
    def name(self):
        r"""Gets the name of this IDc.

        :return: The name of this IDc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IDc.

        :param name: The name of this IDc.
        :type name: str
        """
        self._name = name

    @property
    def irack_num(self):
        r"""Gets the irack_num of this IDc.

        :return: The irack_num of this IDc.
        :rtype: int
        """
        return self._irack_num

    @irack_num.setter
    def irack_num(self, irack_num):
        r"""Sets the irack_num of this IDc.

        :param irack_num: The irack_num of this IDc.
        :type irack_num: int
        """
        self._irack_num = irack_num

    @property
    def id(self):
        r"""Gets the id of this IDc.

        :return: The id of this IDc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IDc.

        :param id: The id of this IDc.
        :type id: str
        """
        self._id = id

    @property
    def region(self):
        r"""Gets the region of this IDc.

        :return: The region of this IDc.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this IDc.

        :param region: The region of this IDc.
        :type region: str
        """
        self._region = region

    @property
    def deccription(self):
        r"""Gets the deccription of this IDc.

        :return: The deccription of this IDc.
        :rtype: str
        """
        return self._deccription

    @deccription.setter
    def deccription(self, deccription):
        r"""Sets the deccription of this IDc.

        :param deccription: The deccription of this IDc.
        :type deccription: str
        """
        self._deccription = deccription

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
        if not isinstance(other, IDc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
