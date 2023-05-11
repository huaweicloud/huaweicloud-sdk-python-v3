# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterEIPResponseSpecSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'eip': 'EipSpec',
        'is_dynamic': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'eip': 'eip',
        'is_dynamic': 'IsDynamic'
    }

    def __init__(self, id=None, eip=None, is_dynamic=None):
        """MasterEIPResponseSpecSpec

        The model defined in huaweicloud sdk

        :param id: 弹性网卡ID
        :type id: str
        :param eip: 
        :type eip: :class:`huaweicloudsdkcce.v3.EipSpec`
        :param is_dynamic: 是否动态创建
        :type is_dynamic: bool
        """
        
        

        self._id = None
        self._eip = None
        self._is_dynamic = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if eip is not None:
            self.eip = eip
        if is_dynamic is not None:
            self.is_dynamic = is_dynamic

    @property
    def id(self):
        """Gets the id of this MasterEIPResponseSpecSpec.

        弹性网卡ID

        :return: The id of this MasterEIPResponseSpecSpec.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MasterEIPResponseSpecSpec.

        弹性网卡ID

        :param id: The id of this MasterEIPResponseSpecSpec.
        :type id: str
        """
        self._id = id

    @property
    def eip(self):
        """Gets the eip of this MasterEIPResponseSpecSpec.

        :return: The eip of this MasterEIPResponseSpecSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.EipSpec`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this MasterEIPResponseSpecSpec.

        :param eip: The eip of this MasterEIPResponseSpecSpec.
        :type eip: :class:`huaweicloudsdkcce.v3.EipSpec`
        """
        self._eip = eip

    @property
    def is_dynamic(self):
        """Gets the is_dynamic of this MasterEIPResponseSpecSpec.

        是否动态创建

        :return: The is_dynamic of this MasterEIPResponseSpecSpec.
        :rtype: bool
        """
        return self._is_dynamic

    @is_dynamic.setter
    def is_dynamic(self, is_dynamic):
        """Sets the is_dynamic of this MasterEIPResponseSpecSpec.

        是否动态创建

        :param is_dynamic: The is_dynamic of this MasterEIPResponseSpecSpec.
        :type is_dynamic: bool
        """
        self._is_dynamic = is_dynamic

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
        if not isinstance(other, MasterEIPResponseSpecSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
